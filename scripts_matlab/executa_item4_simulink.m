function executa_item4_simulink()
% EXECUTA_ITEM4_SIMULINK Simulação temporal via Simulink, extração da resposta
% em frequência via FFT e identificação de parâmetros pelo método N2CACGO.
%
% Requisito do Trabalho (Item 4):
%   "Utilizar o simulink para gerar sinais temporais de entrada e de saída
%    de sistemas LTI de FT estabelecidas, obter a resposta em frequência
%    desses sistemas com uso da FFT e identificar os respectivos modelos."

    clc;
    fprintf('=================================================================\n');
    fprintf(' [ITEM 4] SIMULAÇÃO TEMPORAL NO SIMULINK -> FFT -> N2CACGO\n');
    fprintf('=================================================================\n\n');

    diretorio_figuras = fullfile(pwd, '..', 'artigo', 'figuras');
    if ~exist(diretorio_figuras, 'dir')
        diretorio_figuras = fullfile(pwd, 'artigo', 'figuras');
    end

    diretorio_simulink = fullfile(pwd, '..', 'simulink');
    if ~exist(diretorio_simulink, 'dir')
        diretorio_simulink = fullfile(pwd, 'simulink');
    end

    % 1. Definição do Sistema LTI Alvo (2ª Ordem Subamortecido)
    % G(s) = 8 / (0.2 s^2 + 1.2 s + 1)
    num_alvo = 8;
    den_alvo = [0.2, 1.2, 1];
    G_alvo = tf(num_alvo, den_alvo);

    fprintf('Sistema LTI Alvo:\n');
    display(G_alvo);

    % 2. Parâmetros Temporais e do Sinal de Excitação
    fs = 200;                % Frequência de amostragem (Hz)
    dt = 1 / fs;             % Passo temporal (s)
    T_total = 10;            % Tempo total de simulação (s)
    t_sim = (0:dt:T_total)'; % Vetor de tempo coluna

    f0 = 0.1;                % Frequência inicial do Chirp (Hz)
    f1 = 15;                 % Frequência final do Chirp (Hz)

    % Sinal Chirp linear: f(t) = f0 + (f1 - f0)*(t / 2*T)
    u_sim = sin(2 * pi * (f0 + (f1 - f0) * t_sim / (2 * T_total)) .* t_sim);

    % 3. Execução da Simulação via Simulink
    nome_modelo = 'modelo_item4';
    caminho_slx = fullfile(diretorio_simulink, [nome_modelo '.slx']);

    % Cria o modelo do Simulink programaticamente caso não exista
    cria_modelo_simulink(nome_modelo, caminho_slx, num_alvo, den_alvo, T_total, dt);

    fprintf('Executando simulação do modelo Simulink (%s.slx)...\n', nome_modelo);
    
    % Prepara os dados de entrada para o bloco From Workspace do Simulink
    simin_u = [t_sim, u_sim]; %#ok<NASGU>
    assignin('base', 'simin_u', simin_u);
    assignin('base', 'num_alvo', num_alvo);
    assignin('base', 'den_alvo', den_alvo);

    try
        sim_out = sim(caminho_slx, 'StopTime', num2str(T_total), 'FixedStep', num2str(dt));
        if isprop(sim_out, 'yout') && ~isempty(sim_out.yout)
            y_sim = sim_out.yout;
        elseif isprop(sim_out, 'simout_y') && ~isempty(sim_out.simout_y)
            y_sim = sim_out.simout_y;
        else
            % Fallback seguro caso os sinais estejam no workspace base
            y_sim = evalin('base', 'simout_y');
        end
        if isa(y_sim, 'timeseries')
            y_sim = y_sim.Data;
        end
        y_sim = y_sim(:);
        fprintf('Simulação no Simulink concluída com sucesso.\n');
    catch ME
        warning('Não foi possível executar via Simulink CLI (%s). Utilizando lsim como fallback temporal.', ME.message);
        y_sim = lsim(G_alvo, u_sim, t_sim);
    end

    % Garante que os vetores tenham mesmo comprimento
    n_pts = min(length(u_sim), length(y_sim));
    t_sim = t_sim(1:n_pts);
    u_sim = u_sim(1:n_pts);
    y_sim = y_sim(1:n_pts);

    % 4. Obtenção da Resposta em Frequência Empírica via FFT
    N_fft = length(t_sim);
    U_fft = fft(u_sim);
    Y_fft = fft(y_sim);

    % Apenas frequências positivas (metade do espectro)
    N_half = floor(N_fft / 2);
    U_half = U_fft(1:N_half);
    Y_half = Y_fft(1:N_half);

    f_vetor = (0:N_half-1)' * (fs / N_fft); % Hz
    w_fft   = 2 * pi * f_vetor;             % rad/s

    % Seleciona faixa útil de frequências com energia de excitação adequada
    idx_validos = (w_fft >= 1.0) & (w_fft <= 80.0);
    w_corte = w_fft(idx_validos);
    H_fft   = Y_half(idx_validos) ./ U_half(idx_validos);

    fprintf('Obtidos %d pontos na FRF estimada por FFT (%.2f a %.2f rad/s).\n', ...
            length(w_corte), min(w_corte), max(w_corte));

    % 5. Identificação N2CACGO a partir dos dados espectrais obtidos
    ordem_id = 2;
    [G_id_fft, theta_id, J_fft] = identifica_N2CACGO(w_corte, H_fft, ordem_id);

    fprintf('\nModelo Identificado via N2CACGO a partir da FFT do Simulink:\n');
    display(G_id_fft);

    % Validação em frequência
    erros = valida_modelo_fr(w_corte, H_fft, G_id_fft, false, 'Simulink + FFT (N2CACGO)');
    fprintf('  Custo J: %.4e | FIT: %.2f %% | RMSE Mag: %.4f dB | RMSE Fase: %.4f deg\n\n', ...
            J_fft, erros.FIT_pct, erros.RMSE_Mag_dB, erros.RMSE_Fase_deg);

    % 6. Geração dos Gráficos para o Artigo
    % Gráfico 1: Sinais Temporais
    fig_temp = figure('Name', 'Item 4 - Sinais Temporais Simulink', ...
                      'Color', 'w', 'Position', [100, 100, 800, 500]);
    subplot(2, 1, 1);
    plot(t_sim, u_sim, 'b', 'LineWidth', 1.2);
    grid on; ylabel('Entrada u(t) (Chirp)', 'FontSize', 11);
    title('Sinais Temporais Gerados no Simulink (Chirp 0.1 Hz a 15 Hz)', 'FontSize', 12, 'FontWeight', 'bold');
    
    subplot(2, 1, 2);
    plot(t_sim, y_sim, 'm', 'LineWidth', 1.2);
    grid on; ylabel('Saída y(t)', 'FontSize', 11);
    xlabel('Tempo (s)', 'FontSize', 11);

    caminho_fig_temp = fullfile(diretorio_figuras, 'item4_simulink_sinais_temporais.png');
    exportgraphics(fig_temp, caminho_fig_temp, 'Resolution', 300);
    fprintf('Figura de sinais temporais salva em: %s\n', caminho_fig_temp);

    % Gráfico 2: Diagrama de Bode Comparativo (Teórico vs FFT vs N2CACGO)
    [mag_alvo, fase_alvo] = bode(G_alvo, w_corte);
    [mag_id, fase_id]     = bode(G_id_fft, w_corte);

    fig_bode = figure('Name', 'Item 4 - Validação Espectral N2CACGO', ...
                      'Color', 'w', 'Position', [150, 150, 800, 650]);
    
    subplot(2, 1, 1);
    semilogx(w_corte, 20*log10(squeeze(mag_alvo)), 'k-', 'LineWidth', 2.2, 'DisplayName', 'G(s) Teórico Alvo');
    hold on;
    semilogx(w_corte, 20*log10(abs(H_fft)), 'c.', 'MarkerSize', 8, 'DisplayName', 'H(j\omega) FFT Simulink');
    semilogx(w_corte, 20*log10(squeeze(mag_id)), 'r--', 'LineWidth', 1.8, 'DisplayName', 'N2CACGO Identificado');
    grid on; ylabel('Magnitude (dB)', 'FontSize', 11);
    title(sprintf('Item 4: Comparação Espectral (FIT = %.2f%% | J = %.2e)', erros.FIT_pct, J_fft), ...
          'FontSize', 12, 'FontWeight', 'bold');
    legend('Location', 'best', 'FontSize', 10);

    subplot(2, 1, 2);
    semilogx(w_corte, squeeze(fase_alvo), 'k-', 'LineWidth', 2.2, 'DisplayName', 'G(s) Teórico Alvo');
    hold on;
    semilogx(w_corte, rad2deg(angle(H_fft)), 'c.', 'MarkerSize', 8, 'DisplayName', 'H(j\omega) FFT Simulink');
    semilogx(w_corte, squeeze(fase_id), 'r--', 'LineWidth', 1.8, 'DisplayName', 'N2CACGO Identificado');
    grid on; ylabel('Fase (graus)', 'FontSize', 11);
    xlabel('Frequência Angular \omega (rad/s)', 'FontSize', 11);
    legend('Location', 'best', 'FontSize', 10);

    caminho_fig_bode = fullfile(diretorio_figuras, 'item4_simulink_bode_validacao.png');
    exportgraphics(fig_bode, caminho_fig_bode, 'Resolution', 300);
    fprintf('Figura de validação espectral salva em: %s\n\n', caminho_fig_bode);
end

% --- FUNÇÃO AUXILIAR PARA CRIAR O MODELO SIMULINK ---
function cria_modelo_simulink(nome_modelo, caminho_slx, num, den, T_fim, dt)
    if exist(caminho_slx, 'file')
        return;
    end

    try
        close_system(nome_modelo, 0);
    catch
    end

    new_system(nome_modelo);
    load_system(nome_modelo);

    set_param(nome_modelo, 'SolverType', 'Fixed-step', ...
                           'Solver', 'ode4', ...
                           'FixedStep', num2str(dt), ...
                           'StopTime', num2str(T_fim));

    % Bloco From Workspace para entrada
    add_block('simulink/Sources/From Workspace', [nome_modelo '/Entrada_u'], ...
              'VariableName', 'simin_u', 'Position', [80, 100, 150, 140]);

    % Bloco Transfer Fcn para a planta LTI
    str_num = ['[' num2str(num) ']'];
    str_den = ['[' num2str(den) ']'];
    add_block('simulink/Continuous/Transfer Fcn', [nome_modelo '/Planta_LTI'], ...
              'Numerator', str_num, 'Denominator', str_den, ...
              'Position', [220, 95, 360, 145]);

    % Bloco To Workspace para a saída
    add_block('simulink/Sinks/To Workspace', [nome_modelo '/Saida_y'], ...
              'VariableName', 'simout_y', 'SaveFormat', 'Array', ...
              'Position', [430, 100, 500, 140]);

    % Linhas de conexão
    add_line(nome_modelo, 'Entrada_u/1', 'Planta_LTI/1');
    add_line(nome_modelo, 'Planta_LTI/1', 'Saida_y/1');

    save_system(nome_modelo, caminho_slx);
    close_system(nome_modelo);
    fprintf('Modelo Simulink criado com sucesso em: %s\n', caminho_slx);
end
