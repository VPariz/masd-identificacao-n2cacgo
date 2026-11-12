function [sys_id, theta, J] = identifica_N2CACGO(w, H_med, n)
% IDENTIFICA_N2CACGO Identificação de Sistemas SISO no Domínio da Frequência
% Método: N2CACGO (Norma 2 Convexo Analítico Conjunto Gerador Ótimo)
% Referência: SILVEIRA, Bruno de Pinho. "Identificação de Sistemas no Domínio
%             da Frequência aplicada a Veículos Aéreos Não Tripulados",
%             Dissertação de Mestrado, Instituto Militar de Engenharia (IME), 2006.
%
% Entradas:
%   w     - Vetor de frequências angulares (rad/s), tamanho [m x 1]
%   H_med - Resposta em frequência complexa G(j*w), tamanho [m x 1]
%   n     - Ordem arbitrada para o modelo a ser estimado
%
% Saídas:
%   sys_id - Objeto tf contendo a função de transferência identificada
%   theta  - Vetor de parâmetros ótimos [alpha; beta]
%   J      - Custo ótimo em norma 2 (erro de validação)

    % Força vetores coluna
    w = w(:);
    H_med = H_med(:);
    m = length(w);

    if m < n + 1
        error('Número de pontos de frequência (%d) insuficiente para ordem %d.', m, n);
    end

    % 1. Montagem da matriz de base polinomial R: tamanho (n+1) x m
    % R(k+1, i) = (j * w(i))^(n - k), para k = 0, 1, ..., n
    % Linha 1 = (jw)^n, Linha 2 = (jw)^(n-1), ..., Linha n+1 = (jw)^0 = 1
    R = zeros(n + 1, m);
    for k = 0:n
        R(k + 1, :) = (1i * w.').^(n - k);
    end

    % 2. Matrizes diagonais de dados espectrais
    S_diag  = diag(H_med);                % S(jw)
    S_conj  = diag(conj(H_med));          % S(-jw) = S(jw)*
    S_gamma = diag(H_med .* conj(H_med)); % Gamma = G * G*

    % R_H é o conjugado transposto de R (Hermitiano): tamanho m x (n+1)
    R_H = R';

    % 3. Montagem analítica dos blocos da matriz Q e do vetor Y
    % Conforme Equações 3.32 a 3.39 da dissertação de Silveira (2006)
    
    % Bloco Q1: tamanho (n+1) x (n+1)
    Q1 = real(R * R_H);

    % Bloco Q2: tamanho (n+1) x n
    % Utiliza colunas de 2 a n+1 de R_H (correspondentes aos coeficientes beta_1 a beta_n)
    Q2 = real(R * S_conj * R_H(:, 2:n+1));

    % Bloco Q3: tamanho n x (n+1)
    % Utiliza linhas de 2 a n+1 de R
    Q3 = real(R(2:n+1, :) * S_diag * R_H);

    % Bloco Q4: tamanho n x n
    Q4 = real(R(2:n+1, :) * S_gamma * R_H(:, 2:n+1));

    % Vetor Y1: tamanho (n+1) x 1
    % R_H(:, 1) corresponde ao termo independente com beta_0 = 1, i.e., (jw)^n
    Y1 = real(R * S_conj * R_H(:, 1));

    % Vetor Y2: tamanho n x 1
    Y2 = real(R(2:n+1, :) * S_gamma * R_H(:, 1));

    % Matriz completa do SEL e Vetor Independente
    Q = [Q1, -Q2; ...
         Q3, -Q4];
    Y = [Y1; Y2];

    % 4. Resolução Analítica do Sistema Linear (Mínimo Global Convexo)
    % Utiliza divisão matricial (\) por eliminação Gaussiana com pivoteamento
    warn_state = warning('off', 'MATLAB:nearlySingularMatrix');
    try
        theta = Q \ Y;
    catch
        theta = pinv(Q, 1e-30) * Y;
    end
    warning(warn_state);

    % 5. Extração dos Polinômios Numerador e Denominador
    num = theta(1:n+1).';
    den = [1, theta(n+2:end).'];

    % Criação da Função de Transferência Contínua
    sys_id = tf(num, den);

    % Cálculo do custo de validação J = || G(jw) - Ge(jw) ||_2
    [mag_id, fase_id] = bode(sys_id, w);
    H_id = squeeze(mag_id) .* exp(1i * deg2rad(squeeze(fase_id)));
    J = norm(H_med - H_id(:));
end
