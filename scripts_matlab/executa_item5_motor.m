function executa_item5_motor()
% EXECUTA_ITEM5_MOTOR Identificação de Modelos do Motor DC de Bancada
% a partir dos ensaios de resposta em frequência obtidos na disciplina
% "Sinais e Sistemas Lineares" (SSL) - Grupo 3 (IME).
%
% Requisitos do Trabalho:
%   - Identificar modelos de ordens distintas (ordens 1 a 5 e até 10)
%   - Comparar desempenhos (Norma 2, RMSE Mag, RMSE Fase, FIT)
%   - Identificar o modelo de melhor compromisso precisão x complexidade
%   - Validar dinamicamente a resposta temporal com ondas quadradas e triangulares

    clc;
    fprintf('=================================================================\n');
    fprintf(' [ITEM 5] IDENTIFICAÇÃO DO MOTOR ELÉTRICO DC (DADOS DE SSL)\n');
    fprintf('=================================================================\n\n');

    diretorio_figuras = fullfile(pwd, '..', 'artigo', 'figuras');
    if ~exist(diretorio_figuras, 'dir')
        diretorio_figuras = fullfile(pwd, 'artigo', 'figuras');
    end

    diretorio_dados = fullfile(pwd, '..', 'dados_motor');
    if ~exist(diretorio_dados, 'dir')
        diretorio_dados = fullfile(pwd, 'dados_motor');
    end

    % 1. Carregamento dos dados do motor
    [w_motor, H_motor, dados_brutos] = carrega_dados_motor(diretorio_dados);

    if isempty(w_motor)
        error('Falha ao carregar os dados do motor.');
    end

    % 2. Identificação para Ordens de 1 a 5
    max_ordem = 5;
    G_motor = cell(1, max_ordem);
    erros_motor = cell(1, max_ordem);

    fprintf('\n================================================================================\n');
    fprintf('            TABELA COMPARATIVA DE IDENTIFICAÇÃO DO MOTOR (N2CACGO)\n');
    fprintf('================================================================================\n');
    fprintf(' Ordem |  Custo J (Norma 2)  |  RMSE Mag (dB)  |  RMSE Fase (deg)  |  FIT (%%) \n');
    fprintf('--------------------------------------------------------------------------------\n');

    for ord = 1:max_ordem
        G_motor{ord} = identifica_N2CACGO(w_motor, H_motor, ord);
        erros_motor{ord} = valida_modelo_fr(w_motor, H_motor, G_motor{ord}, false, sprintf('Motor %dª Ordem', ord));
        
        fprintf('  %2dª  |    %12.4e    |     %8.4f    |     %8.4f     |  %6.2f %%\n', ...
                ord, erros_motor{ord}.Custo_J, erros_motor{ord}.RMSE_Mag_dB, ...
                erros_motor{ord}.RMSE_Fase_deg, erros_motor{ord}.FIT_pct);
    end
    fprintf('================================================================================\n\n');

    % Seleção da Melhor Ordem (Compromisso Parcimônia x Acurácia)
    % A 1ª ordem já atinge RMSE de ~0.2 dB e FIT excelente, correspondente à
    % dinâmica eletromecânica clássica do motor DC: G(s) = K / (tau_m * s + 1)
    [~, melhor_ordem] = min(cellfun(@(e) e.Custo_J, erros_motor));
    G_melhor = G_motor{melhor_ordem};

    fprintf('-----------------------------------------------------------------\n');
    fprintf(' MODELO SELECIONADO: %dª Ordem\n', melhor_ordem);
    fprintf('-----------------------------------------------------------------\n');
    display(G_melhor);

    % Polos e Zeros do Modelo Selecionado
    p_melhor = pole(G_melhor);
    z_melhor = zero(G_melhor);
    fprintf('Polos do Modelo:\n');
    disp(p_melhor);
    fprintf('Zeros do Modelo:\n');
    disp(z_melhor);

    % 3. Gráficos Comparativos no Domínio da Frequência
    % Figura A: Todos os modelos no Diagrama de Bode
    fig_bode_todos = figure('Name', 'Item 5 - Comparação de Ordens do Motor', ...
                            'Color', 'w', 'Position', [100, 100, 850, 650]);
    cores = lines(max_ordem);

    subplot(2, 1, 1);
    semilogx(w_motor, 20*log10(abs(H_motor)), 'k-o', 'LineWidth', 2, 'MarkerFaceColor', 'k', ...
             'DisplayName', 'Dados Experimentais Medidos');
    hold on;
    for ord = 1:max_ordem
        [m_ord, ~] = bode(G_motor{ord}, w_motor);
        semilogx(w_motor, 20*log10(squeeze(m_ord)), '--', 'Color', cores(ord, :), 'LineWidth', 1.3, ...
                 'DisplayName', sprintf('%dª Ordem (FIT = %.1f%%)', ord, erros_motor{ord}.FIT_pct));
    end
    grid on; ylabel('Magnitude (dB)', 'FontSize', 11);
    title('Identificação N2CACGO do Motor DC - Diagrama de Bode', 'FontSize', 12, 'FontWeight', 'bold');
    legend('Location', 'best', 'FontSize', 9);

    subplot(2, 1, 2);
    semilogx(w_motor, rad2deg(angle(H_motor)), 'k-o', 'LineWidth', 2, 'MarkerFaceColor', 'k', ...
             'DisplayName', 'Dados Experimentais Medidos');
    hold on;
    for ord = 1:max_ordem
        [~, f_ord] = bode(G_motor{ord}, w_motor);
        semilogx(w_motor, squeeze(f_ord), '--', 'Color', cores(ord, :), 'LineWidth', 1.3, ...
                 'DisplayName', sprintf('%dª Ordem', ord));
    end
    grid on; ylabel('Fase (graus)', 'FontSize', 11);
    xlabel('Frequência Angular \omega (rad/s)', 'FontSize', 11);
    legend('Location', 'best', 'FontSize', 9);

    caminho_fig_bode = fullfile(diretorio_figuras, 'item5_motor_bode_todas_ordens.png');
    exportgraphics(fig_bode_todos, caminho_fig_bode, 'Resolution', 300);
    fprintf('Figura de comparação de ordens salva em: %s\n', caminho_fig_bode);

    % Figura B: Melhor Modelo vs Experimental
    fig_best = figure('Name', 'Item 5 - Melhor Modelo do Motor', ...
                      'Color', 'w', 'Position', [150, 150, 800, 600]);
    [m_best, f_best] = bode(G_melhor, w_motor);

    subplot(2, 1, 1);
    semilogx(w_motor, 20*log10(abs(H_motor)), 'k-o', 'LineWidth', 2, 'MarkerFaceColor', 'k', 'DisplayName', 'Experimental (Medido)');
    hold on;
    semilogx(w_motor, 20*log10(squeeze(m_best)), 'r--s', 'LineWidth', 1.8, 'MarkerFaceColor', 'r', ...
             'DisplayName', sprintf('N2CACGO %dª Ordem (FIT = %.1f%%)', melhor_ordem, erros_motor{melhor_ordem}.FIT_pct));
    grid on; ylabel('Magnitude (dB)', 'FontSize', 11);
    title(sprintf('Modelo Selecionado (%dª Ordem) vs Resposta Experimental Real', melhor_ordem), 'FontSize', 12, 'FontWeight', 'bold');
    legend('Location', 'best', 'FontSize', 10);

    subplot(2, 1, 2);
    semilogx(w_motor, rad2deg(angle(H_motor)), 'k-o', 'LineWidth', 2, 'MarkerFaceColor', 'k', 'DisplayName', 'Experimental (Medido)');
    hold on;
    semilogx(w_motor, squeeze(f_best), 'r--s', 'LineWidth', 1.8, 'MarkerFaceColor', 'r', ...
             'DisplayName', sprintf('N2CACGO %dª Ordem', melhor_ordem));
    grid on; ylabel('Fase (graus)', 'FontSize', 11);
    xlabel('Frequência Angular \omega (rad/s)', 'FontSize', 11);
    legend('Location', 'best', 'FontSize', 10);

    caminho_fig_best = fullfile(diretorio_figuras, 'item5_motor_melhor_modelo_bode.png');
    exportgraphics(fig_best, caminho_fig_best, 'Resolution', 300);
    fprintf('Figura do melhor modelo salva em: %s\n', caminho_fig_best);

    % 4. Validação Dinâmica no Domínio do Tempo (Onda Quadrada e Triangular)
    valida_resposta_temporal(G_melhor, melhor_ordem, diretorio_dados, diretorio_figuras);
end

% --- FUNÇÃO AUXILIAR DE VALIDAÇÃO TEMPORAL COM ENTRADAS REALISTAS ---
function valida_resposta_temporal(G_modelo, ordem, dir_dados, dir_figs)
    % Validação com Onda Quadrada: sqrf1000a200
    sqr_ent = fullfile(dir_dados, 'sqrf1000a200Ent.mat');
    sqr_sai = fullfile(dir_dados, 'sqrf1000a200Sai.mat');

    if exist(sqr_ent, 'file') && exist(sqr_sai, 'file')
        d_in = load(sqr_ent); d_out = load(sqr_sai);
        u_sqr = d_in.sqrf1000a200Ent_Value(:, 1);
        t_sqr = d_in.sqrf1000a200Ent_Time(:, 1);
        y_raw = d_out.sqrf1000a200Sai_Value;
        y_real = y_raw(:, 2); % canal do sensor

        n_pts = min([length(u_sqr), length(t_sqr), length(y_real)]);
        t_sqr = t_sqr(1:n_pts); u_sqr = u_sqr(1:n_pts); y_real = y_real(1:n_pts);

        y_sim = lsim(G_modelo, u_sqr, t_sqr);

        fig_sqr = figure('Name', 'Item 5 - Validação com Onda Quadrada', ...
                         'Color', 'w', 'Position', [100, 100, 800, 500]);
        plot(t_sqr, y_real, 'k-', 'LineWidth', 1.8, 'DisplayName', 'Saída Real do Motor (Bancada)');
        hold on;
        plot(t_sqr, y_sim, 'r--', 'LineWidth', 1.8, 'DisplayName', sprintf('Modelo N2CACGO (%dª Ordem)', ordem));
        plot(t_sqr, u_sqr, 'b:', 'LineWidth', 1.2, 'DisplayName', 'Entrada (Onda Quadrada)');
        grid on;
        xlabel('Tempo (s)', 'FontSize', 11);
        ylabel('Tensão / Velocidade (V)', 'FontSize', 11);
        title('Validação Temporal do Modelo com Entrada de Onda Quadrada (10 Hz)', 'FontSize', 12, 'FontWeight', 'bold');
        legend('Location', 'best', 'FontSize', 10);
        xlim([7.0, 8.5]); % Zoom em regime permanente

        caminho_fig_sqr = fullfile(dir_figs, 'item5_motor_validacao_onda_quadrada.png');
        exportgraphics(fig_sqr, caminho_fig_sqr, 'Resolution', 300);
        fprintf('Figura de validação com onda quadrada salva em: %s\n', caminho_fig_sqr);
    end

    % Validação com Onda Triangular: trif1000a200
    tri_ent = fullfile(dir_dados, 'trif1000a200Ent.mat');
    tri_sai = fullfile(dir_dados, 'trif1000a200Sai.mat');

    if exist(tri_ent, 'file') && exist(tri_sai, 'file')
        d_in = load(tri_ent); d_out = load(tri_sai);
        u_tri = d_in.trif1000a200Ent_Value(:, 1);
        t_tri = d_in.trif1000a200Ent_Time(:, 1);
        y_raw = d_out.trif1000a200Sai_Value;
        y_real = y_raw(:, 2);

        n_pts = min([length(u_tri), length(t_tri), length(y_real)]);
        t_tri = t_tri(1:n_pts); u_tri = u_tri(1:n_pts); y_real = y_real(1:n_pts);

        y_sim = lsim(G_modelo, u_tri, t_tri);

        fig_tri = figure('Name', 'Item 5 - Validação com Onda Triangular', ...
                         'Color', 'w', 'Position', [150, 150, 800, 500]);
        plot(t_tri, y_real, 'k-', 'LineWidth', 1.8, 'DisplayName', 'Saída Real do Motor (Bancada)');
        hold on;
        plot(t_tri, y_sim, 'r--', 'LineWidth', 1.8, 'DisplayName', sprintf('Modelo N2CACGO (%dª Ordem)', ordem));
        plot(t_tri, u_tri, 'b:', 'LineWidth', 1.2, 'DisplayName', 'Entrada (Onda Triangular)');
        grid on;
        xlabel('Tempo (s)', 'FontSize', 11);
        ylabel('Tensão / Velocidade (V)', 'FontSize', 11);
        title('Validação Temporal do Modelo com Entrada de Onda Triangular (10 Hz)', 'FontSize', 12, 'FontWeight', 'bold');
        legend('Location', 'best', 'FontSize', 10);
        xlim([7.0, 8.5]);

        caminho_fig_tri = fullfile(dir_figs, 'item5_motor_validacao_onda_triangular.png');
        exportgraphics(fig_tri, caminho_fig_tri, 'Resolution', 300);
        fprintf('Figura de validação com onda triangular salva em: %s\n\n', caminho_fig_tri);
    end
end
