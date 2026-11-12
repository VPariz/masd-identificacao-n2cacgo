function erros = valida_modelo_fr(w, H_orig, sys_id, exibe_grafico, nome_modelo, salvar_figura, caminho_figura)
% VALIDA_MODELO_FR Validação da resposta em frequência do modelo identificado
% Calcula métricas de desempenho:
%   - Custo J (Norma 2 do erro complexo) - Critério de Silveira (2006)
%   - RMSE da Magnitude em dB
%   - RMSE da Fase em graus
%   - FIT Percentual (%) clássico de identificação
%
% Entradas:
%   w              - Vetor de frequências (rad/s)
%   H_orig         - Resposta complexa original ou medida
%   sys_id         - Função de transferência identificada
%   exibe_grafico  - Booleano para plotar os diagramas de Bode
%   nome_modelo    - String com o título identificador
%   salvar_figura  - Booleano para salvar figura em disco
%   caminho_figura - Caminho do arquivo de saída (ex: 'figura.png')

    if nargin < 4, exibe_grafico = false; end
    if nargin < 5, nome_modelo = 'Modelo Identificado'; end
    if nargin < 6, salvar_figura = false; end
    if nargin < 7, caminho_figura = ''; end

    w = w(:);
    H_orig = H_orig(:);

    % Resposta em frequência do modelo estimado
    [mag_id, fase_id] = bode(sys_id, w);
    mag_id  = squeeze(mag_id);
    fase_id = squeeze(fase_id);
    H_id    = mag_id .* exp(1i * deg2rad(fase_id));

    % Cálculos de Erro
    mag_orig_db   = 20 * log10(abs(H_orig));
    mag_id_db     = 20 * log10(mag_id);
    fase_orig_deg = rad2deg(angle(H_orig));

    % Norma 2 (Critério Clássico de Custo J de Silveira 2006)
    erros.Custo_J       = norm(H_orig - H_id);
    
    % RMSE Magnitude (dB) e Fase (graus)
    erros.RMSE_Mag_dB   = sqrt(mean((mag_orig_db - mag_id_db).^2));
    erro_fase           = wrapTo180(fase_orig_deg - fase_id);
    erros.RMSE_Fase_deg = sqrt(mean(erro_fase.^2));
    
    % FIT Percentual clássico
    erros.FIT_pct = max(0, 100 * (1 - norm(H_orig - H_id) / norm(H_orig - mean(H_orig))));

    % Exibição no console
    fprintf('=== Validação: %s ===\n', nome_modelo);
    fprintf('  Custo J (Norma 2):  %.4e\n', erros.Custo_J);
    fprintf('  RMSE Magnitude:     %.4f dB\n', erros.RMSE_Mag_dB);
    fprintf('  RMSE Fase:          %.4f graus\n', erros.RMSE_Fase_deg);
    fprintf('  FIT:                %.2f %%\n\n', erros.FIT_pct);

    % Plotagem
    if exibe_grafico
        fig = figure('Name', sprintf('Validação - %s', nome_modelo), ...
                     'Color', 'w', 'Position', [100, 100, 750, 600]);

        subplot(2, 1, 1);
        semilogx(w, mag_orig_db, 'k-o', 'LineWidth', 1.5, 'MarkerSize', 5, 'DisplayName', 'Original / Medido');
        hold on;
        semilogx(w, mag_id_db, 'r--s', 'LineWidth', 1.5, 'MarkerSize', 5, 'DisplayName', sprintf('Identificado (%s)', nome_modelo));
        grid on;
        ylabel('Magnitude (dB)', 'FontSize', 11);
        title(sprintf('Validação em Frequência - %s (J = %.4e | FIT = %.1f%%)', nome_modelo, erros.Custo_J, erros.FIT_pct), ...
              'FontSize', 12, 'FontWeight', 'bold');
        legend('Location', 'best', 'FontSize', 10);

        subplot(2, 1, 2);
        semilogx(w, fase_orig_deg, 'k-o', 'LineWidth', 1.5, 'MarkerSize', 5, 'DisplayName', 'Original / Medido');
        hold on;
        semilogx(w, fase_id, 'r--s', 'LineWidth', 1.5, 'MarkerSize', 5, 'DisplayName', sprintf('Identificado (%s)', nome_modelo));
        grid on;
        ylabel('Fase (graus)', 'FontSize', 11);
        xlabel('Frequência Angular \omega (rad/s)', 'FontSize', 11);
        legend('Location', 'best', 'FontSize', 10);

        if salvar_figura && ~isempty(caminho_figura)
            exportgraphics(fig, caminho_figura, 'Resolution', 300);
        end
    end
end
