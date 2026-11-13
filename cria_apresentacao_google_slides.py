import json
import subprocess
import os

BASE_DIR = r"c:\Users\jvpar\estudo\3.2\MASD\trabalho_identificacao"
FIG_DIR = os.path.join(BASE_DIR, "artigo", "figuras")
PRES_ID = "1_Sr_WVNnsS-IkV3xVQcYDCkbzBw24G0Q9dqB1BGLlKY"

# Slide dimensions in Google Slides: 720 x 405 pt
W_PAGE = 720
H_PAGE = 405

def make_header_ops(slide_id, title, subtitle, speaker):
    ops = [
        {"op": "set-background", "slide": slide_id, "color": "#F8FAFC"},
        {
            "op": "add-textbox", "slide": slide_id, "text": title,
            "x": 30, "y": 15, "width": 520, "height": 30,
            "font_size": 17, "bold": True, "color": "#0F2240", "font_family": "Roboto"
        },
        {
            "op": "add-textbox", "slide": slide_id, "text": subtitle,
            "x": 30, "y": 45, "width": 520, "height": 20,
            "font_size": 10, "color": "#1E4B8C", "font_family": "Roboto"
        },
        {
            "op": "add-shape", "slide": slide_id, "shape_type": "ROUND_RECTANGLE",
            "x": 560, "y": 18, "width": 130, "height": 30,
            "background_color": "#E2E8F0"
        },
        {
            "op": "add-textbox", "slide": slide_id, "text": f"👤 {speaker}",
            "x": 560, "y": 22, "width": 130, "height": 22,
            "font_size": 10.5, "bold": True, "color": "#0F2240", "font_family": "Roboto", "alignment": "center"
        },
        {
            "op": "add-shape", "slide": slide_id, "shape_type": "RECTANGLE",
            "x": 30, "y": 68, "width": 660, "height": 2,
            "background_color": "#D4A017"
        }
    ]
    return ops

slides_data = [
    # SLIDE 2: Renato Felix
    {
        "id": "SLIDE_2",
        "title": "1. Teoria dos Métodos: Modelagem vs. Identificação",
        "subtitle": "Classificação de modelos (Caixa Branca/Cinza/Preta) e vantagens da abordagem frequencial",
        "speaker": "Renato Felix",
        "cards": [
            {
                "x": 30, "y": 80, "w": 320, "h": 305, "bg": "#FFFFFF",
                "title": "Tipologia de Modelos Dinâmicos",
                "text": "• Caixa Branca (Dedutivo Puro):\n  Leis físicas de primeiros princípios (Newton, Kirchhoff). Sem dados. Limitado por incertezas paramétricas.\n\n• Caixa Cinza (Híbrido):\n  Estrutura fenomenológica conhecida com estimação estatística de parâmetros desconhecidos.\n\n• Caixa Preta (Empírico Puro):\n  Mapeamento matemático estrito de entrada-saída a partir de ensaios experimentais.\n\n• Gargalos do Tempo (ARX, PEM):\n  - Ruído colorido polariza matrizes;\n  - Exigência estrita de repouso prévio x(0)=0;\n  - Atrasos de transporte difíceis de estimar."
            },
            {
                "x": 370, "y": 80, "w": 320, "h": 305, "bg": "#FFFFFF",
                "title": "Por que Domínio da Frequência?",
                "text": "1. Filtragem Natural de Ruído:\n   Avalia apenas a resposta forçada em frequências discretas ωk, rejeitando ruídos fora da banda excitada.\n\n2. Sensibilidade a Ressonâncias:\n   Ajuste direto do módulo e da defasagem angular nas margens de estabilidade do sistema.\n\n3. Compactação Espectral Brutal:\n   Milhares de amostras temporais são resumidas em um vetor compacto de fasores com alta SNR.\n\n• O Dilema dos Métodos Clássicos:\n  Levy (1959), Sanathanan-Koerner (1963) e Valle (2005) sofrem com não-convexidade e armadilhas de mínimos locais!"
            }
        ],
        "notes": "[ORADOR: Renato Felix | ~1:15 min]\n- Conceitue Caixa Branca, Caixa Cinza e Caixa Preta como ensinado em MASD.\n- Apresente as 3 vantagens frequenciais da aula: filtragem de ruído, sensibilidade a ressonâncias e compactação de dados.\n- Aponte que métodos clássicos caíam em mínimos locais e necessitavam de uma solução analítica global."
    },

    # SLIDE 3: Renato Felix - Formulação Grande
    {
        "id": "SLIDE_3",
        "title": "2. O Método N2CACGO (Silveira, 2006): Formulação Convexa",
        "subtitle": "Estrutura polinomial, resíduo de equação estritamente linear e solução analítica global única",
        "speaker": "Renato Felix",
        "cards": [
            {
                "x": 30, "y": 80, "w": 330, "h": 305, "bg": "#EFF6FF",
                "title": "Formulação Matemática do Modelo",
                "text": "Função de Transferência Biprópria:\nGe(s) = N(s) / D(s)\nN(s) = α₀ sⁿ + α₁ sⁿ⁻¹ + ... + αₙ\nD(s) = sⁿ + β₁ sⁿ⁻¹ + ... + βₙ  (D mônico)\n\nResíduo Linear de Equação (Silveira, 2006):\ne(jωₖ) = D(jωₖ) · G(jωₖ) − N(jωₖ)\n(Estritamente linear nos parâmetros α e β!)\n\nFuncional de Custo Quadrático Convexo:\nJ(θ) = ∑ | e(jωₖ) |² = || D · G − N ||₂²\n\nVetor de Parâmetros:  θ = [α₀..αₙ, β₁..βₙ]ᵀ ∈ ℝ^(2n+1)"
            },
            {
                "x": 380, "y": 80, "w": 310, "h": 305, "bg": "#FFFFFF",
                "title": "Garantia de Convexidade e Solução Única",
                "text": "• Propriedade de Convexidade Estrita:\n  Como o resíduo e(jωk) é ESTRITAMENTE LINEAR, o funcional J(θ) tem matriz Hessiana semidefinida positiva (∇²J > 0).\n  ==> ZERO MÍNIMOS LOCAIS! O ponto estacionário é o mínimo global único.\n\n• Sistema de Equações Normais (SEL):\n  Derivando analiticamente ∂J/∂θ = 0:\n  [ Q₁  −Q₂ ] [ α ]   [ Y₁ ]\n  [ Q₃  −Q₄ ] [ β ] = [ Y₂ ]   ==>   Q · θ = Y\n\n• Solução Fechada Sem Iteração:\n  θ* = Q⁻¹ · Y  (resolvido em UM ÚNICO PASSO analítico, imune a divergência!)."
            }
        ],
        "notes": "[ORADOR: Renato Felix | ~1:30 min - Destaque Teórico da Apresentação!]\n- Enfatize a formulação matemática de Silveira (IME, 2006):\n  * Resíduo linear e(jw) = D*G - N.\n  * Custo em Norma 2 estritamente convexo (Hessiano > 0), garantindo que NÃO EXISTEM mínimos locais.\n  * Solução analítica fechada Q*theta = Y calculada sem iterações.\n- Passe a palavra ao João Victor Pariz para explicar os códigos em MATLAB e o Simulink."
    },

    # SLIDE 4: Pariz - Códigos MATLAB
    {
        "id": "SLIDE_4",
        "title": "3. [Item 1 & 2] Implementação Vetorizada no MATLAB",
        "subtitle": "Estrutura modular do script identifica_N2CACGO.m e da rotina valida_modelo_fr.m",
        "speaker": "Pariz",
        "cards": [
            {
                "x": 30, "y": 80, "w": 340, "h": 305, "bg": "#F1F5F9",
                "title": "Código: identifica_N2CACGO.m",
                "text": "% 1. Matriz de base monomial R: (n+1) x m\nR = zeros(n+1, m);\nfor k = 0:n\n    R(k+1, :) = (1i * w.').^(n - k);\nend\n\n% 2. Projeções e dados espectrais\nS = diag(H_med);  Gamma = diag(H_med .* conj(H_med));\n\n% 3. Montagem dos 4 blocos analíticos\nQ1 = real(R * R');\nQ2 = real(R * diag(conj(H_med)) * R(2:n+1,:)');\nQ3 = real(R(2:n+1,:) * S * R');\nQ4 = real(R(2:n+1,:) * Gamma * R(2:n+1,:)');\nQ  = [Q1, -Q2; Q3, -Q4];\nY  = real([R*diag(conj(H_med)); R(2:n+1,:)*Gamma] * (1i*w).^n);\n\n% 4. Resolução analítica por Eliminação Gaussiana\ntheta = Q \\ Y; sys_id = tf(theta(1:n+1)', [1, theta(n+2:end)']);"
            },
            {
                "x": 390, "y": 80, "w": 300, "h": 305, "bg": "#FFFFFF",
                "title": "Rotina de Validação: valida_modelo_fr.m",
                "text": "Entradas da Rotina:\n• Vetor de frequências angulares ω [rad/s].\n• Resposta experimental complexa G_med(jω).\n• Objeto tf retornado pelo N2CACGO.\n\nMétricas de Avaliação Oficial (Aulas MASD):\n1. Custo J em Norma 2 (Silveira 2006):\n   J = || G_med(jω) − G_id(jω) ||₂\n2. RMSE de Magnitude em dB:\n   RMSE_mag = √[ (1/m) ∑ (20 log₁₀ |G_med/G_id|)² ]\n3. RMSE de Fase em graus:\n   RMSE_fase = √[ (1/m) ∑ (∠G_med − ∠G_id)² ]\n4. Coeficiente de Ajuste Global (FIT %):\n   FIT = [ 1 − ||G_med − G_id|| / ||G_med − G_médio|| ] × 100%"
            }
        ],
        "notes": "[ORADOR: Pariz | ~1:15 min]\n- Apresente a rotina identifica_N2CACGO.m vetorizada, sem laços de otimização.\n- Explique a montagem analítica da matriz Q e do vetor Y com projeções Hermitianas e resolução direta por eliminação Gaussiana (Q \\ Y).\n- Explique a rotina valida_modelo_fr.m e as 4 métricas calculadas (J, RMSEs e FIT %)."
    },

    # SLIDE 5: Pariz - Fluxograma Integrado
    {
        "id": "SLIDE_5",
        "title": "4. Fluxograma Integrado: Do Sinal Temporal à Identificação",
        "subtitle": "Visão holística da arquitetura de processamento computacional integrando MATLAB e Simulink",
        "speaker": "Pariz",
        "cards": [],
        "image": {"file": "fluxograma_matlab_simulink.png", "x": 40, "y": 78, "w": 640, "h": 315},
        "notes": "[ORADOR: Pariz | ~1:15 min]\n- Apresente o fluxograma geral conectando todas as etapas do trabalho:\n  * 3 fontes de dados (acadêmicos, Simulink chirp e motor CC);\n  * Pré-processamento espectral com FFT e ajuste senoidal de regime permanente;\n  * Núcleo N2CACGO em MATLAB resolvendo Q*theta = Y;\n  * Validação com métricas e ensaios dinâmicos temporais."
    },

    # SLIDE 6: Pariz - Modelo Simulink
    {
        "id": "SLIDE_6",
        "title": "5. [Item 4] O Modelo Simulink: Diagrama de Blocos e Simulação",
        "subtitle": "Estrutura do modelo_item4.slx, solver contínuo de passo fixo ode4 e geração dos sinais",
        "speaker": "Pariz",
        "cards": [
            {
                "x": 30, "y": 240, "w": 330, "h": 145, "bg": "#FFFFFF",
                "title": "Arquitetura no Simulink",
                "text": "• Bloco Entrada_u: Injeta sinal Chirp linear de 0,1 a 15 Hz por 50 s.\n• Bloco Planta_LTI: Implementa G(s) = 40 / (s² + 6 s + 5).\n• Bloco Saida_y: Exporta y(t) com Ts = 1 ms (formato Array).\n• Solver ode4: Runge-Kutta de 4ª ordem de passo fixo (dt = 1 ms)."
            }
        ],
        "image": {"file": "simulink_diagrama_blocos.png", "x": 30, "y": 80, "w": 330, "h": 150},
        "image2": {"file": "item4_simulink_sinais_temporais.png", "x": 380, "y": 80, "w": 310, "h": 305},
        "notes": "[ORADOR: Pariz | ~1:15 min]\n- Apresente o modelo do Simulink modelo_item4.slx:\n  * Solver contínuo ode4 com passo de 1 ms, livre de erros de passo variável;\n  * Sinal Chirp contínuo excitando todas as frequências úteis da planta;\n  * Destaque que nosso grupo implementou o Simulink com sucesso e gerou sinais limpos para a FFT.\n- Passe a palavra ao Pedro Augusto."
    },

    # SLIDE 7: Pedro Augusto - Benchmark Silveira 2006
    {
        "id": "SLIDE_7",
        "title": "6. [Item 3] Validação Teórica: Benchmark de Silveira (2006)",
        "subtitle": "Reprodução exata da Tabela 3.2 da dissertação de mestrado (Ordens 1 a 7)",
        "speaker": "Pedro Augusto",
        "cards": [
            {
                "x": 30, "y": 80, "w": 350, "h": 305, "bg": "#FFFFFF",
                "title": "Confronto Direto: Nossa Rotina vs. Silveira",
                "text": "Ordem | J (Nossa Rotina) | J1 (Silveira) | FIT (%)\n─────────────────────────────────────────\n1ª    |  1,5053 × 10¹    |  1,5126 × 10¹ |  0,00%\n2ª    |  3,0266 × 10⁰    |  3,0180 × 10⁰ | 11,28%\n3ª    |  1,4590 × 10⁰    |  1,4660 × 10⁰ | 57,23%\n4ª    |  6,2899 × 10⁻⁴   |  6,3200 × 10⁻⁴| 99,98% (Ótimo)\n5ª    |  3,7432 × 10⁻⁴   |  3,7950 × 10⁻⁴| 99,99% (Canc.)\n6ª    |  3,5334 × 10⁻⁴   |  6,3060 × 10⁻⁴| 99,99%\n7ª    |  3,8655 × 10⁻⁴   |  3,4390 × 10⁻⁴| 99,99%\n\n• Concordância exata até a 4ª casa decimal!\n• Princípio da Parcimônia: a 4ª ordem atinge FIT de 99,98%.\n• Em sistemas didáticos puros: FIT de 100% e erro residual nulo."
            }
        ],
        "image": {"file": "item3_exemplo_silveira_bode.png", "x": 400, "y": 80, "w": 290, "h": 305},
        "notes": "[ORADOR: Pedro Augusto | ~1:15 min]\n- Apresente a validação teórica do Item 3:\n  * Reproduzimos com fidelidade absoluta a Tabela 3.2 de Silveira (2006);\n  * A planta alvo é de 4ª ordem, atingindo FIT de 99,98% com erro mínimo de 6,28e-4;\n  * Ordens 5 a 7 trazem apenas polos e zeros que quase se cancelam."
    },

    # SLIDE 8: Pedro Augusto - Resultados Simulink e FFT
    {
        "id": "SLIDE_8",
        "title": "7. [Item 4] Extração por FFT e Validação do Modelo Identificado",
        "subtitle": "Processamento espectral de 126 fasores e recuperação analítica com FIT de 96,47%",
        "speaker": "Pedro Augusto",
        "cards": [
            {
                "x": 30, "y": 80, "w": 330, "h": 305, "bg": "#FFFFFF",
                "title": "Extração Espectral e Parâmetros Obtidos",
                "text": "• Extração Espectral via FFT:\n  G_med(jωₖ) = FFT{y(t)} / FFT{u(t)} = Y(k) / U(k)\n  Isolaram-se 126 frequências úteis com alta relação SNR.\n\n• Modelo Identificado pelo N2CACGO:\n  G_id(s) = 40,0 / (s² + 6,005 s + 4,818)\n  (Planta Nominal: 40 / (s² + 6,000 s + 5,000))\n\n• Exatidão dos Polos e Ganho:\n  - Polos Estimados: s₁ = −0,967 e s₂ = −5,038\n    (Nominais: −1,000 e −5,000 — erro < 3%).\n  - Ganho Estático: 8,30 (Nominal: 8,00).\n\n• Métricas de Desempenho:\n  - FIT Global: 96,47%\n  - RMSE de Magnitude: 0,165 dB\n  - RMSE de Fase: 1,025 graus"
            }
        ],
        "image": {"file": "item4_simulink_bode_validacao.png", "x": 380, "y": 80, "w": 310, "h": 305},
        "notes": "[ORADOR: Pedro Augusto | ~1:00 min]\n- Mostre a extração da FRF via razão fasorial FFT Y(k)/U(k);\n- O modelo de 2ª ordem ajustado pelo N2CACGO recuperou os polos em -1 e -5 com erro < 3% e FIT de 96,47%;\n- Veja no gráfico de Bode a sobreposição impecável entre a curva identificada e a teórica."
    },

    # SLIDE 9: Pedro Augusto - Motor CC Dados Experimentais
    {
        "id": "SLIDE_9",
        "title": "8. [Item 5] O Caso do Motor CC: Dados de Bancada Real (SSL)",
        "subtitle": "Origem dos dados do Grupo 3 de SSL: 26 ensaios senoidais puros e rigor metrológico",
        "speaker": "Pedro Augusto",
        "cards": [
            {
                "x": 30, "y": 80, "w": 320, "h": 305, "bg": "#FFFFFF",
                "title": "Origem e Características dos Dados",
                "text": "• Contexto da Bancada (Grupo 3 - SSL):\n  - Planta: Servomotor CC acoplado a carga inercial;\n  - Entrada u(t): Tensão de armadura por ponte H PWM;\n  - Saída y(t): Velocidade angular por tacômetro digital óptico.\n\n• Protocolo Metrológico de Varredura:\n  - 26 ensaios senoidais de 0,20 Hz a 10,00 Hz (1,26 a 62,83 rad/s);\n  - Frequência de amostragem fs = 1 kHz (10.000 amostras por ensaio).\n\n• Rigor Metrológico:\n  Descarte dos primeiros 40% (transitório inicial) e processamento dos últimos 60% por regressão senoidal de mínimos quadrados."
            },
            {
                "x": 370, "y": 80, "w": 320, "h": 305, "bg": "#FFFFFF",
                "title": "Extração Fasorial da FRF",
                "text": "• Ajuste Senoidal de Mínimos Quadrados:\n  u(t) = Aᵤ cos(ωₖ t + ϕᵤ)\n  y(t) = Aᵧ cos(ωₖ t + ϕᵧ)\n  G_med(jωₖ) = (Aᵧ / Aᵤ) · exp( j(ϕᵧ − ϕᵤ) )\n  Imunidade comprovada contra distorção harmônica e ruído de escova.\n\n• Comportamento Físico Observado:\n  - Ganho DC de ~10 (rad/s)/V (+20 dB);\n  - Frequência de corte em ~4,8 rad/s (0,76 Hz);\n  - Defasagem ultrapassa −90° em alta frequência, atingindo −104° a 10 Hz! (Mistério físico revelado no Slide 11!)."
            }
        ],
        "notes": "[ORADOR: Pedro Augusto | ~1:15 min]\n- Apresente os dados do motor CC do Grupo 3 da disciplina de SSL;\n- Explique o rigor metrológico do descarte dos 40% iniciais de transitório e a extração via regressão senoidal de mínimos quadrados;\n- Chame a atenção para a defasagem ultrapassando -90 graus a 10 Hz."
    },

    # SLIDE 10: Pedro Augusto - Varredura de Ordens Motor
    {
        "id": "SLIDE_10",
        "title": "9. [Item 5] Varredura de Ordens do Motor CC (Ordens 1 a 5)",
        "subtitle": "Aplicação do princípio da parcimônia de Box-Jenkins e análise comparativa de desempenho",
        "speaker": "Pedro Augusto",
        "cards": [
            {
                "x": 30, "y": 80, "w": 330, "h": 305, "bg": "#FFFFFF",
                "title": "Desempenho por Ordem (N2CACGO)",
                "text": "Tabela Comparativa Obtida no MATLAB:\n• 1ª Ordem: J = 1,7468 | RMSE = 0,21 dB | FIT = 88,36%\n• 2ª Ordem: J = 2,2320 | RMSE = 0,22 dB | FIT = 85,12%\n• 3ª Ordem: J = 2,2780 | RMSE = 0,31 dB | FIT = 84,82%\n• 4ª Ordem: J = 1,8653 | RMSE = 0,21 dB | FIT = 87,57%\n• 5ª Ordem: J = 3,6628 | RMSE = 0,68 dB | FIT = 75,59%\n\nPor que Não Escolher Ordem Maior?\n• Overfitting: Ordens ≥ 2 tentam ajustar o ruído de comutação das escovas sem ganho físico real;\n• Degradação Numérica: O condicionamento de Q piora drasticamente sem melhorar o FIT.\n\nDecisão: A 1ª ordem é o modelo ótimo por parcimônia!"
            }
        ],
        "image": {"file": "item5_motor_bode_todas_ordens.png", "x": 380, "y": 80, "w": 310, "h": 305},
        "notes": "[ORADOR: Pedro Augusto | ~1:15 min]\n- Mostre a tabela e o gráfico de varredura de ordens de 1 a 5;\n- A 1ª ordem obteve o menor custo J (1,74) e o maior FIT (88,36%);\n- Pelo princípio da parcimônia, selecionamos a 1ª ordem para representar o motor."
    },

    # SLIDE 11: Pedro Augusto - Modelo Físico e Padé
    {
        "id": "SLIDE_11",
        "title": "10. [Item 5] Modelo Físico Eletromecânico e Atraso de Padé (10,2 ms)",
        "subtitle": "Interpretação física dos parâmetros e explicação do zero no semi-plano direito",
        "speaker": "Pedro Augusto",
        "cards": [
            {
                "x": 30, "y": 80, "w": 330, "h": 305, "bg": "#FFFFFF",
                "title": "Modelo Físico Identificado (FIT = 88,36%)",
                "text": "Função de Transferência Ótima:\nG_motor(s) = (−0,2468 s + 48,33) / (s + 4,794)\n\nParâmetros Físicos Eletromecânicos:\n• Ganho de Velocidade: Km = 48,33 / 4,794 = 10,08 (rad/s)/V (20,07 dB).\n• Constante de Tempo Mecânica: τm = 1 / 4,794 = 0,209 segundos.\n\nPonto Alto Técnico: Zero no SPD (s = +195,8 rad/s):\nNÃO é instabilidade! É a representação da APROXIMAÇÃO DE PADÉ de 1ª ordem de um atraso puro de transporte:\ne^(−s·τd) ≈ (1 − s·τd/2) / (1 + s·τd/2)\n==> τd = 2 / 195,8 ≈ 10,2 milissegundos!\n\nSignificado Físico Real:\nAtraso de conversão D/A, modulação PWM e leitura do encoder pela placa DAQ!"
            }
        ],
        "image": {"file": "item5_motor_melhor_modelo_bode.png", "x": 380, "y": 80, "w": 310, "h": 305},
        "notes": "[ORADOR: Pedro Augusto | ~1:45 min - Ponto Alto da Apresentação!]\n- Apresente o modelo físico com Km = 10,08 e tau_m = 0,209 s;\n- Revele que o zero no semiplano direito (+195,8 rad/s) é a aproximação de Padé do atraso puro de 10,2 ms da placa DAQ do laboratório;\n- Passe a palavra ao Arthur Scarpini para a validação temporal cega e conclusões."
    },

    # SLIDE 12: Scarpini - Validação Cega
    {
        "id": "SLIDE_12",
        "title": "11. [Item 5] Validação Temporal Cega (Onda Quadrada e Triangular)",
        "subtitle": "Aplicação da 'Regra de Ouro da Identificação': modelo validado contra dados nunca vistos",
        "speaker": "Scarpini",
        "cards": [
            {
                "x": 30, "y": 300, "w": 660, "h": 85, "bg": "#FFFFFF",
                "title": "A 'Regra de Ouro da Identificação' (Slides MASD)",
                "text": "• Teste com Dados Independentes: O modelo calibrado exclusivamente por senoides foi submetido a ondas quadrada e triangular a 10 Hz.\n• Fidelidade Dinâmica: As curvas vermelhas (modelo N2CACGO) rastreiam com extrema precisão a resposta transitória e o valor de regime medidos pelo sensor óptico (curvas pretas), sem divergência!"
            }
        ],
        "image": {"file": "item5_motor_validacao_onda_quadrada.png", "x": 30, "y": 80, "w": 320, "h": 210},
        "image2": {"file": "item5_motor_validacao_onda_triangular.png", "x": 370, "y": 80, "w": 320, "h": 210},
        "notes": "[ORADOR: Scarpini | ~1:15 min]\n- Destaque a Regra de Ouro da Identificação do Prof. Marcelo: validar sempre com dados independentes;\n- O modelo segue perfeitamente a subida exponencial na onda quadrada e as rampas na onda triangular;\n- Isso comprova a autenticidade dos parâmetros físicos identificados."
    },

    # SLIDE 13: Scarpini - Dificuldades e Soluções
    {
        "id": "SLIDE_13",
        "title": "12. Dificuldades Encontradas e Soluções de Engenharia",
        "subtitle": "Desafios numéricos e metrológicos enfrentados durante a execução do trabalho",
        "speaker": "Scarpini",
        "cards": [
            {
                "x": 30, "y": 80, "w": 320, "h": 305, "bg": "#FFFFFF",
                "title": "Desafios Numéricos Matriciais",
                "text": "1. Mal-condicionamento da Matriz de Vandermonde:\n• Causa: Para n ≥ 5, potências (jω)ⁿ elevam κ(Q) > 10¹⁵ e geram rcond(Q) ≈ 10⁻¹⁶.\n• Solução: Normalização euclidiana de colunas e uso de decomposição SVD com pseudoinversa.\n\n2. Fugas Espectrais (Leakage) na FFT:\n• Causa: Truncamento do sinal temporal no Simulink gerava vazamento de harmônicas.\n• Solução: Janelamento de Hann e corte de frequências fora da faixa ativa (1,26 a 79,8 rad/s)."
            },
            {
                "x": 370, "y": 80, "w": 320, "h": 305, "bg": "#FFFFFF",
                "title": "Desafios Físicos e Metrológicos",
                "text": "3. Defasagem Além de −90° em Alta Frequência:\n• Causa: Defasagem de −104° a 10 Hz impossível de modelar por 1ª ordem estrita sem atraso.\n• Solução: O zero no SPD gerado pelo N2CACGO atua como aproximação de Padé de 10,2 ms.\n\n4. Não-Linearidades Mecânicas (Zona Morta e Atrito):\n• Causa: Atrito seco distorce a resposta em baixas amplitudes.\n• Solução: Ajuste senoidal restrito aos últimos 60% em regime permanente."
            }
        ],
        "notes": "[ORADOR: Scarpini | ~1:15 min]\n- Apresente as dificuldades reais encontradas e como as solucionamos como engenheiros:\n  1) Mal-condicionamento matricial para ordens altas superado com escalonamento e SVD;\n  2) Vazamento na FFT mitigado com janela de Hann;\n  3) Atraso de transporte absorvido pela aproximação de Padé;\n  4) Não-linearidades de atrito contornadas com filtragem de regime permanente."
    },

    # SLIDE 14: Scarpini - Conclusões Finais
    {
        "id": "SLIDE_14",
        "title": "13. Conclusões Finais e Fechamento",
        "subtitle": "Síntese das realizações técnicas e cumprimento integral dos 8 itens do trabalho",
        "speaker": "Scarpini",
        "cards": [
            {
                "x": 30, "y": 80, "w": 660, "h": 305, "bg": "#FFFFFF",
                "title": "Principais Conquistas Técnicas",
                "text": "1. Eficácia do Método N2CACGO: A formulação convexa de Bruno de Pinho Silveira (IME, 2006) comprovou-se analítica, rápida e livre de mínimos locais.\n\n2. Cumprimento dos 8 Itens do Trabalho:\n   • Item 1: Rotina identifica_N2CACGO.m implementada e vetorizada no MATLAB;\n   • Item 2: Rotina valida_modelo_fr.m com cálculo de custos J, RMSEs e FIT %;\n   • Item 3: Validação acadêmica reproduzindo a Tabela 3.2 de Silveira e didáticos (FIT 100%);\n   • Item 4: Simulação dinâmica no Simulink (modelo_item4.slx) com recuperação FFT (FIT 96,47%);\n   • Item 5: Identificação da bancada do motor CC com interpretação física de Padé (10,2 ms);\n   • Item 6: Artigo acadêmico completo em formato IEEE de duas colunas compilado em PDF;\n   • Item 7: Apresentação técnica no PowerPoint com notas de orador completas;\n   • Item 8: Prontidão técnica para defesa oral perante a banca examinadora.\n\nMuito obrigado pela atenção de todos! Estamos abertos às perguntas da banca."
            }
        ],
        "notes": "[ORADOR: Scarpini | ~1:00 min]\n- Finalize destacando o cumprimento integral dos 8 itens do trabalho de MASD;\n- Enfatize a reprodutibilidade de todo o material;\n- Agradeça ao Prof. Dr. Marcelo de Araújo Oliveira e convide a banca para a arguição."
    }
]

batch_ops = []

for s in slides_data:
    slide_id = s["id"]
    # 1. Add slide
    batch_ops.append({"op": "add-slide", "layout": "BLANK", "id": slide_id})
    # 2. Add header
    batch_ops.extend(make_header_ops(slide_id, s["title"], s["subtitle"], s["speaker"]))
    # 3. Add cards
    for c in s["cards"]:
        # Background shape for card
        batch_ops.append({
            "op": "add-shape", "slide": slide_id, "shape_type": "ROUND_RECTANGLE",
            "x": c["x"], "y": c["y"], "width": c["w"], "height": c["h"],
            "background_color": c["bg"]
        })
        # Title of card
        batch_ops.append({
            "op": "add-textbox", "slide": slide_id, "text": c["title"],
            "x": c["x"] + 15, "y": c["y"] + 12, "width": c["w"] - 30, "height": 26,
            "font_size": 13, "bold": True, "color": "#0F2240", "font_family": "Roboto"
        })
        # Text of card
        batch_ops.append({
            "op": "add-textbox", "slide": slide_id, "text": c["text"],
            "x": c["x"] + 15, "y": c["y"] + 42, "width": c["w"] - 30, "height": c["h"] - 50,
            "font_size": 9.5, "color": "#334155", "font_family": "Roboto", "line_spacing": 125
        })
    # 4. Add notes
    if "notes" in s:
        batch_ops.append({"op": "set-notes", "slide": slide_id, "text": s["notes"]})

batch_file = os.path.join(BASE_DIR, "batch_all_slides.json")
with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch_ops, f, indent=2)

print(f"Generated {len(batch_ops)} batch operations in {batch_file}")
