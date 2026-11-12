function [w_motor, H_motor, dados_brutos] = carrega_dados_motor(caminho_dados)
% CARREGA_DADOS_MOTOR Carrega e processa os ensaios do motor elétrico DC
% de bancada da disciplina Sinais e Sistemas Lineares (SSL).
%
% Extrai a resposta em frequência complexa H(j*w) = Y(j*w) / U(j*w)
% aplicando a transformada discreta de Fourier na frequência fundamental
% após atingido o regime permanente (últimos 60% das amostras).
%
% Entrada:
%   caminho_dados - Diretório onde estão os arquivos .mat (opcional)
%
% Saídas:
%   w_motor      - Vetor de frequências angulares (rad/s) ordenadas
%   H_motor      - Vetor complexo de resposta em frequência G(j*w)
%   dados_brutos - Estrutura com os sinais temporais para validação

    if nargin < 1 || isempty(caminho_dados)
        % Procura na pasta local de dados ou na pasta original de SSL
        if exist(fullfile(pwd, 'dados_motor'), 'dir')
            caminho_dados = fullfile(pwd, 'dados_motor');
        elseif exist(fullfile(pwd, '..', 'dados_motor'), 'dir')
            caminho_dados = fullfile(pwd, '..', 'dados_motor');
        else
            caminho_dados = 'c:\Users\jvpar\estudo\3.1\Sinais_e_Sistemas\SSL - IME 25\LinearSystemsAndSignals\trabalhoRespostaEmFrequencia\Gp3';
        end
    end

    arquivos_ent = dir(fullfile(caminho_dados, 'sen*Ent.mat'));
    if isempty(arquivos_ent)
        % Tenta padrão genérico
        arquivos_ent = dir(fullfile(caminho_dados, '*Ent.mat'));
    end

    if isempty(arquivos_ent)
        error('Nenhum arquivo de entrada (*Ent.mat) encontrado em: %s', caminho_dados);
    end

    frequencias = [];
    H_medido    = [];
    dados_brutos = struct();

    for k = 1:length(arquivos_ent)
        nome_ent = arquivos_ent(k).name;
        nome_sai = strrep(nome_ent, 'Ent.mat', 'Sai.mat');
        caminho_sai = fullfile(caminho_dados, nome_sai);

        if ~exist(caminho_sai, 'file')
            continue;
        end

        % Extração da frequência nominal: senfXXXa... -> XXX em centésimos de Hz
        tok = regexp(nome_ent, 'senf(\d+)a(\d+)Ent', 'tokens');
        if isempty(tok)
            continue;
        end
        f_num = str2double(tok{1}{1});
        f_hz  = f_num / 100.0; % Ex: 020 -> 0.20 Hz, 1000 -> 10.00 Hz
        w_val = 2 * pi * f_hz;

        % Carregamento dos dados
        d_in  = load(fullfile(caminho_dados, nome_ent));
        d_out = load(caminho_sai);

        campos_in  = fieldnames(d_in);
        campos_out = fieldnames(d_out);

        u = d_in.(campos_in{~contains(campos_in, 'Time')})(:, 1);
        t = d_in.(campos_in{contains(campos_in, 'Time')})(:, 1);
        
        y_raw = d_out.(campos_out{~contains(campos_out, 'Time')});
        % No motor de bancada, a coluna 2 é a saída medida real do tacômetro/sensor
        if size(y_raw, 2) >= 2
            y = y_raw(:, 2);
        else
            y = y_raw(:, 1);
        end

        n_pts = min([length(u), length(t), length(y)]);
        u = u(1:n_pts);
        t = t(1:n_pts);
        y = y(1:n_pts);

        % Seleciona regime permanente (últimos 60% do ensaio)
        idx_ini = round(0.4 * n_pts);
        t_reg = t(idx_ini:end);
        u_reg = u(idx_ini:end);
        y_reg = y(idx_ini:end);

        % Estimativa espectral via DFT na frequência da senoide
        sen_ref = exp(-1i * w_val * t_reg);
        U_w = sum(u_reg .* sen_ref);
        Y_w = sum(y_reg .* sen_ref);

        if abs(U_w) > 1e-4
            H_val = Y_w / U_w;
            frequencias(end+1) = w_val; %#ok<AGROW>
            H_medido(end+1)    = H_val; %#ok<AGROW>
            
            % Armazena amostra para validação temporal se necessário
            id_tag = sprintf('f_%04d', f_num);
            dados_brutos.(id_tag).t = t;
            dados_brutos.(id_tag).u = u;
            dados_brutos.(id_tag).y = y;
            dados_brutos.(id_tag).w = w_val;
        end
    end

    % Ordenação por frequência crescente e média para frequências repetidas
    [w_unicos, ~, idx_map] = unique(frequencias);
    H_unicos = zeros(size(w_unicos));
    for j = 1:length(w_unicos)
        H_unicos(j) = mean(H_medido(idx_map == j));
    end

    w_motor = w_unicos(:);
    H_motor = H_unicos(:);

    fprintf('Carregados com sucesso %d pontos de frequência do motor (%.2f rad/s a %.2f rad/s).\n', ...
            length(w_motor), min(w_motor), max(w_motor));
end
