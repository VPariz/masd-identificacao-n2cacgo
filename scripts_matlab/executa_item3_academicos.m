function executa_item3_academicos()
% EXECUTA_ITEM3_ACADEMICOS Executa os testes de identificação N2CACGO
% em funções de transferência acadêmicas de ordens distintas.
%
% Inclui:
%   1. Exemplo 3.4.1 da dissertação de Bruno de Pinho Silveira (IME, 2006):
%      FT biprópria de 7ª ordem e fase mínima, testando ordens n = 1 a 7
%      e confrontando os custos de erro J com a Tabela 3.2 da dissertação.
%   2. Sistemas acadêmicos de 1ª, 2ª e 3ª ordens (com zeros).

    clc;
    fprintf('=================================================================\n');
    fprintf(' [ITEM 3] IDENTIFICAÇÃO DE SISTEMAS ACADÊMICOS (N2CACGO)\n');
    fprintf('=================================================================\n\n');

    diretorio_figuras = fullfile(pwd, '..', 'artigo', 'figuras');
    if ~exist(diretorio_figuras, 'dir')
        diretorio_figuras = fullfile(pwd, 'artigo', 'figuras');
    end

    %% PARTE A: EXEMPLO 3.4.1 DE SILVEIRA (2006) - 7ª ORDEM BIPRÓPRIA
    fprintf('--- PARTE A: Exemplo 3.4.1 da Dissertação de Silveira (2006) ---\n');

    num_7 = [0.100000000, 4.753000000, 90.01275000, 863.2453825, ...
             4417.863626, 11761.82161, 14942.80380, 6958.320022];
    den_7 = [1.000000000, 16.82000000, 252.6691000, 2476.872788, ...
             13659.19997, 59044.40987, 131354.0179, 87580.35014];

    G_silveira = tf(num_7, den_7);

    % 100 pontos logaritmicamente espaçados entre 0.01 e 100 rad/s
    w_silv = logspace(-2, 2, 100)';
    [mag_s, fase_s] = bode(G_silveira, w_silv);
    H_silv = squeeze(mag_s) .* exp(1i * deg2rad(squeeze(fase_s)));

    % Valores de referência da Tabela 3.2 da dissertação de Silveira (2006)
    J_ref_silveira = [15.126, 3.018, 1.466, 6.320e-4, 3.795e-4, 6.306e-4, 3.439e-4];

    fprintf('\nComparação com a Tabela 3.2 da Dissertação:\n');
    fprintf('-----------------------------------------------------------------\n');
    fprintf(' Ordem (n) | Custo J (Obtido) | Custo J1 (Silveira, 2006) | FIT (%%)\n');
    fprintf('-----------------------------------------------------------------\n');

    G_identificados_silv = cell(1, 7);
    erros_silv = cell(1, 7);

    for n = 1:7
        [G_identificados_silv{n}, ~, J_obtido] = identifica_N2CACGO(w_silv, H_silv, n);
        erros_silv{n} = valida_modelo_fr(w_silv, H_silv, G_identificados_silv{n}, false, sprintf('Silveira Ordem %d', n));
        fprintf('    %2d     |    %12.4e    |        %12.4e       |  %6.2f %%\n', ...
                n, J_obtido, J_ref_silveira(n), erros_silv{n}.FIT_pct);
    end
    fprintf('-----------------------------------------------------------------\n\n');

    % Gráfico comparativo de Bode para ordens 1, 2, 4 e 7
    fig_silv = figure('Name', 'Item 3 - Exemplo Acadêmico Silveira (2006)', ...
                      'Color', 'w', 'Position', [100, 100, 800, 650]);
    
    ordens_plot = [1, 2, 4, 7];
    estilos = {'b--', 'm-.', 'g--', 'r-'};
    
    subplot(2, 1, 1);
    semilogx(w_silv, 20*log10(abs(H_silv)), 'k-', 'LineWidth', 2.2, 'DisplayName', 'G(s) Original (7ª Ordem)');
    hold on;
    for idx = 1:length(ordens_plot)
        n = ordens_plot(idx);
        [m_id, ~] = bode(G_identificados_silv{n}, w_silv);
        semilogx(w_silv, 20*log10(squeeze(m_id)), estilos{idx}, 'LineWidth', 1.4, ...
                 'DisplayName', sprintf('N2CACGO n = %d (J = %.2e)', n, erros_silv{n}.Custo_J));
    end
    grid on; ylabel('Magnitude (dB)', 'FontSize', 11);
    title('Exemplo Acadêmico 3.4.1 (Silveira, 2006) - Diagrama de Bode', 'FontSize', 12, 'FontWeight', 'bold');
    legend('Location', 'best', 'FontSize', 10);

    subplot(2, 1, 2);
    semilogx(w_silv, rad2deg(angle(H_silv)), 'k-', 'LineWidth', 2.2, 'DisplayName', 'G(s) Original (7ª Ordem)');
    hold on;
    for idx = 1:length(ordens_plot)
        n = ordens_plot(idx);
        [~, f_id] = bode(G_identificados_silv{n}, w_silv);
        semilogx(w_silv, squeeze(f_id), estilos{idx}, 'LineWidth', 1.4, ...
                 'DisplayName', sprintf('N2CACGO n = %d', n));
    end
    grid on; ylabel('Fase (graus)', 'FontSize', 11);
    xlabel('Frequência Angular \omega (rad/s)', 'FontSize', 11);
    legend('Location', 'best', 'FontSize', 10);

    caminho_fig_silv = fullfile(diretorio_figuras, 'item3_exemplo_silveira_bode.png');
    exportgraphics(fig_silv, caminho_fig_silv, 'Resolution', 300);
    fprintf('Figura salva em: %s\n', caminho_fig_silv);

    %% PARTE B: SISTEMAS DE 1ª, 2ª E 3ª ORDENS
    fprintf('\n--- PARTE B: Sistemas Acadêmicos Didáticos (Ordens 1, 2 e 3) ---\n');

    w_didat = logspace(-1, 2, 60)';
    sistemas = {
        tf(5, [2, 1]),                                      '1ª Ordem',          1;
        tf(10, conv([0.5, 1], [0.1, 1])),                   '2ª Ordem',          2;
        tf([2, 5], conv([1, 1], conv([0.2, 1], [0.05, 1]))), '3ª Ordem com Zero', 3
    };

    fig_didat = figure('Name', 'Item 3 - Sistemas Didáticos 1ª, 2ª e 3ª Ordens', ...
                       'Color', 'w', 'Position', [150, 150, 900, 650]);

    for k = 1:size(sistemas, 1)
        G_k = sistemas{k, 1};
        nome_k = sistemas{k, 2};
        ord_k = sistemas{k, 3};

        [m_k, f_k] = bode(G_k, w_didat);
        H_k = squeeze(m_k) .* exp(1i * deg2rad(squeeze(f_k)));

        [G_k_id, ~, J_k] = identifica_N2CACGO(w_didat, H_k, ord_k);
        err_k = valida_modelo_fr(w_didat, H_k, G_k_id, false, nome_k);

        fprintf('Sistema %s -> Custo J = %.4e | FIT = %.2f %%\n', nome_k, J_k, err_k.FIT_pct);

        % Subplot da magnitude
        subplot(2, 3, k);
        semilogx(w_didat, 20*log10(abs(H_k)), 'k-', 'LineWidth', 2, 'DisplayName', 'Original');
        hold on;
        [m_id, ~] = bode(G_k_id, w_didat);
        semilogx(w_didat, 20*log10(squeeze(m_id)), 'r--', 'LineWidth', 1.5, 'DisplayName', 'N2CACGO');
        grid on; ylabel('Magnitude (dB)'); title(sprintf('%s (J=%.1e)', nome_k, J_k));
        legend('Location', 'best');

        % Subplot da fase
        subplot(2, 3, k + 3);
        semilogx(w_didat, rad2deg(angle(H_k)), 'k-', 'LineWidth', 2, 'DisplayName', 'Original');
        hold on;
        [~, f_id] = bode(G_k_id, w_didat);
        semilogx(w_didat, squeeze(f_id), 'r--', 'LineWidth', 1.5, 'DisplayName', 'N2CACGO');
        grid on; ylabel('Fase (graus)'); xlabel('\omega (rad/s)');
        legend('Location', 'best');
    end

    caminho_fig_didat = fullfile(diretorio_figuras, 'item3_sistemas_didaticos_bode.png');
    exportgraphics(fig_didat, caminho_fig_didat, 'Resolution', 300);
    fprintf('Figura salva em: %s\n\n', caminho_fig_didat);
end
