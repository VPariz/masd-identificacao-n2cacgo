%% SCRIPT PRINCIPAL: EXECUÇÃO INTEGRADA DO TRABALHO DE IDENTIFICAÇÃO (MASD - IME)
% Método: N2CACGO (Norma 2 Convexo Analítico Conjunto Gerador Ótimo - Silveira, 2006)
% Autores: João Victor Tavares Pariz, Pedro Augusto, Renato Felix, Scarpini
% Professor: Prof. Dr. Marcelo de Araújo Oliveira
% Data de Apresentação: 06 de Novembro

clc; clear; close all;

fprintf('========================================================================\n');
fprintf('  INSTITUTO MILITAR DE ENGENHARIA - IME\n');
fprintf('  Modelagem e Análise de Sistemas Dinâmicos (MASD)\n');
fprintf('  Trabalho de Identificação no Domínio da Frequência - Método N2CACGO\n');
fprintf('========================================================================\n\n');

% Adiciona pastas ao path do MATLAB
pasta_scripts = fileparts(mfilename('fullpath'));
addpath(pasta_scripts);
addpath(fullfile(pasta_scripts, '..', 'dados_motor'));
addpath(fullfile(pasta_scripts, '..', 'simulink'));

%% 1. EXECUÇÃO DO ITEM 3: EXEMPLOS ACADÊMICOS
fprintf('\n>>> INICIANDO ITEM 3: EXEMPLOS ACADÊMICOS <<<\n');
executa_item3_academicos();

%% 2. EXECUÇÃO DO ITEM 4: SIMULAÇÃO TEMPORAL SIMULINK + FFT
fprintf('\n>>> INICIANDO ITEM 4: SIMULINK + FFT <<<\n');
executa_item4_simulink();

%% 3. EXECUÇÃO DO ITEM 5: IDENTIFICAÇÃO DO MOTOR DC REAL
fprintf('\n>>> INICIANDO ITEM 5: IDENTIFICAÇÃO DO MOTOR DC (DADOS DE SSL) <<<\n');
executa_item5_motor();

fprintf('\n========================================================================\n');
fprintf('  TODAS AS ETAPAS COMPUTACIONAIS FORAM EXECUTADAS COM SUCESSO!\n');
fprintf('  Figuras de alta resolução salvas em: trabalho_identificacao/artigo/figuras/\n');
fprintf('========================================================================\n');
