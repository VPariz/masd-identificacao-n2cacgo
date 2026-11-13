# 📋 GUIA OFICIAL DE APRESENTAÇÃO (POWERPOINT 14 SLIDES)
## Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO
**Disciplina:** Modelagem e Análise de Sistemas Dinâmicos (MASD) — SE/3 • IME  
**Orientador:** Prof. Dr. Marcelo de Araújo Oliveira  
**Equipe:** João Victor Tavares Pariz, Pedro Augusto, Renato Felix, Arthur Scarpini  
**Tempo Total de Apresentação:** ~15:30 min (faixa estipulada: 10 a 20 min) + 5 min de arguição.  
**Arquivo Oficial de Apresentação:** [`apresentacao_MASD_N2CACGO_IME.pptx`](file:///c:/Users/jvpar/estudo/3.2/MASD/trabalho_identificacao/apresentacao/apresentacao_MASD_N2CACGO_IME.pptx)

---

### ⏱️ Tabela de Distribuição do Tempo por Integrante

| Bloco | Orador | Slides | Foco Técnico | Tempo Estimado |
|:---:|---|:---:|---|:---:|
| **1** | **João Victor Pariz** | 1 a 5 | Abertura, Contexto Físico (Caixa Branca/Cinza/Preta), Método N2CACGO de Silveira (2006), Código MATLAB (`identifica_N2CACGO.m`) e **Fluxograma Geral Integrado (Slide 5)** | **~5:00 min** |
| **2** | **Pedro Augusto** | 6 a 8 | Validação de Silveira (Tabela 3.2 exata), **Modelo Simulink com Print do Diagrama (`modelo_item4.slx`)** e Extração Fasorial por FFT ($FIT = 96,47\%$) | **~3:30 min** |
| **3** | **Renato Felix** | 9 a 11 | O Caso do Motor CC: Dados de Bancada de SSL (Grupo 3, 26 senoides), Varredura de Ordens (por que 1ª ordem?) e Parâmetros Físicos com Atraso de Padé de 10,2 ms | **~4:30 min** |
| **4** | **Arthur Scarpini** | 12 a 14 | A "Regra de Ouro da Identificação" (Validação Cega com Ondas Quadrada e Triangular), Desafios Numéricos ($rcond(Q) < 10^{-16}$) e **Conclusões com Dificuldades e Lições** | **~4:00 min** |
| **TOTAL** | **Toda a Equipe** | **1 a 14** | **Apresentação Completa, Equilibrada, Visual e Rigorosa** | **~17:00 min** |

---

# 🎙️ ROTEIRO DE FALA SLIDE A SLIDE (O QUE FALAR NA APRESENTAÇÃO)

---

## 👤 BLOCO 1: JOÃO VICTOR TAVARES PARIZ (Slides 1 a 5 — ~5:00 min)

### 🟢 Slide 1: Capa & Apresentação da Equipe (Tempo: 1:00 min)
* **O que falar:**
  > *"Bom dia / boa tarde a todos, professor Marcelo e banca avaliadora.*  
  > *Nosso grupo é composto por mim, João Victor Pariz, pelo Pedro Augusto, Renato Felix e Arthur Scarpini.*  
  > *Hoje apresentamos o trabalho final de Modelagem e Análise de Sistemas Dinâmicos, intitulado: **'Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO'**.*  
  > *Nós estruturamos a nossa apresentação em 4 blocos técnicos equilibrados, cobrindo todos os requisitos solicitados na disciplina:*  
  > 1. *Eu iniciarei apresentando o contexto da modelagem, o método de Silveira (2006), o código em MATLAB e o fluxograma geral integrado;*  
  > 2. *O Pedro apresentará a validação do benchmark de Silveira e o diagrama dinâmico no Simulink com análise FFT;*  
  > 3. *O Renato explicará o caso da bancada do motor CC, a origem e o tratamento dos dados experimentais e a interpretação física dos parâmetros;*  
  > 4. *E o Scarpini finalizará com a validação dinâmica cega no tempo, os desafios de condicionamento matricial superados e as conclusões.*  
  > *Vamos começar com a contextualização da identificação."*

### 🟢 Slide 2: Contextualização: Domínio da Frequência vs. Tempo (Tempo: 1:00 min)
* **O que falar:**
  > *"Como vimos nas aulas de MASD, os modelos matemáticos podem ser classificados em três grandes famílias:*  
  > - * **Caixa Branca:** Conhecimento físico total (leis de Newton, Kirchhoff), sem dados;*  
  > - * **Caixa Cinza:** Estrutura física conhecida, onde usamos dados apenas para calibrar parâmetros desconhecidos;*  
  > - * **Caixa Preta:** Abordagem puramente baseada em dados medidos de entrada e saída.*  
  > *Dentro da modelagem Caixa Preta, a primeira decisão de engenharia é: **Domínio do Tempo ou Domínio da Frequência?***  
  > *No tempo, métodos como ARX ou Métodos do Erro de Predição (PEM) sofrem com três problemas clássicos: sensibilidade a ruídos estocásticos, dependência de condições iniciais nulas e dificuldade em modelar atrasos de transporte.*  
  > *Por outro lado, no domínio da frequência, colhemos as **três grandes vantagens ensinadas pelo professor em sala**:*  
  > 1. * **Filtragem natural de ruído**, ignorando frequências fora da banda útil forçada;*  
  > 2. * **Ajuste fino de dinâmicas rápidas e picos de ressonância**;*  
  > 3. * **Compactação brutal de dados**, onde milhares de pontos temporais pesados são resumidos em uma curva compacta de fasores.*  
  > *Para identificar no domínio da frequência sem cair em mínimos locais, utilizamos o N2CACGO."*

### 🟢 Slide 3: O Método N2CACGO (Silveira, 2006): Formulação Convexa (Tempo: 1:00 min)
* **O que falar:**
  > *"Qual é o método da pessoa que estamos utilizando?*  
  > *Estamos utilizando o método proposto na dissertação de mestrado de **Bruno de Pinho Silveira (IME, 2006)**, intitulado **N2CACGO** — sigla para *Norma 2 Convexo Analítico Conjunto Gerador Ótimo*.*  
  > *Até então, métodos como a Técnica de Imposição de Polos de Valle (2005) ou minimizações de erro de saída via Nelder-Mead (`fminsearch`) resultavam em problemas **não convexos**, que ficavam presos em mínimos locais e dependiam de chutes iniciais.*  
  > *A genialidade de Silveira foi definir a função objetivo com base no **resíduo de equação ponderado**:*  
  > $$e(j\omega_i) = A(j\omega_i) G(j\omega_i) - B(j\omega_i)$$  
  > *Como esse erro é **estritamente linear nos coeficientes desconhecidos $\alpha$ e $\beta$**, a função de custo quadrática em norma 2 torna-se **estritamente convexa**!*  
  > *Lembrando da definição vista em aula: em uma função convexa, a Hessiana é semidefinida positiva ($\nabla^2 J \ge 0$) e **todo mínimo local é garantidamente o mínimo global**.*  
  > *Igualando o gradiente a zero ($\nabla_\theta J = 0$), chegamos a um Sistema de Equações Lineares (SEL) particionado:*  
  > $$Q \theta = Y \implies \theta^* = Q^{-1} Y$$  
  > *A solução ótima global é obtida **de forma analítica, em uma única operação matricial, sem iterar**!"*

### 🟢 Slide 4: [Item 1 & 2] Implementação do Algoritmo e Métricas no MATLAB (Tempo: 1:00 min)
* **O que falar:**
  > *"Para atender aos Itens 1 e 2 do trabalho, implementamos essa formulação em código MATLAB limpo e modular, exibido neste slide:*  
  > - *Na rotina `identifica_N2CACGO.m`, primeiro montamos a matriz de base monomial $R$, cujas linhas são as potências $(j\omega)^{n-k}$.*  
  > - *Em seguida, calculamos as matrizes de projeção espectral $S$, seu conjugado e a potência hermitiana $\Gamma = G \cdot G^*$.*  
  > - *Montamos os 4 blocos analíticos da matriz $Q$ ($Q_1, Q_2, Q_3, Q_4$) e o vetor $Y$ conforme as equações 3.32 a 3.39 de Silveira.*  
  > - *A solução analítica dos parâmetros é calculada com o operador backslash `theta = Q \ Y`, que utiliza eliminação Gaussiana com pivoteamento parcial, e convertida nativamente em um objeto `tf` do MATLAB.*  
  > - *Já a rotina `valida_modelo_fr.m` calcula as métricas quantitativas de ajuste: custo $J$ em norma 2, RMSE de módulo em dB, RMSE de fase em graus e o índice de ajuste global $\text{FIT}\%$.*"*

### 🟢 Slide 5: Fluxograma Geral de Processamento: MATLAB & Simulink (Tempo: 1:00 min)
* **O que falar:**
  > *"Antes de passar a palavra aos meus colegas, apresento o **Fluxograma Geral de Engenharia** que sintetiza todo o nosso pipeline de processamento:*  
  > - *No topo, temos as **três grandes frentes de dados**:*  
  >   1. *O benchmark de Silveira no Item 3;*  
  >   2. *A simulação temporal no Simulink com o sinal Chirp no Item 4;*  
  >   3. *Os 66 arquivos experimentais da bancada do Motor CC no Item 5.*  
  > - *Todas essas três frentes são tratadas e convergem para o **Núcleo Algorítmico Central em MATLAB: `identifica_N2CACGO.m`**, onde a base monomial $R$, os blocos $Q$ e o vetor $Y$ são resolvidos analiticamente em um único passo.*  
  > - *Na base do fluxograma, os modelos identificados são validados pela rotina `valida_modelo_fr.m`, gerando métricas quantitativas de custo, gráficos de Bode comparativos e validações dinâmicas cegas no tempo.*  
  > *Para detalhar como esse pipeline operou no benchmark de Silveira e no Simulink, passo a palavra agora para o Pedro Augusto."*

---

## 👤 BLOCO 2: PEDRO AUGUSTO (Slides 6 a 8 — ~3:30 min)

### 🟡 Slide 6: [Item 3] Validação Teórica: Benchmark de Silveira (2006) (Tempo: 1:15 min)
* **O que falar:**
  > *"Obrigado, Pariz. Bom dia a todos.*  
  > *No Item 3, nossa meta foi auditar rigorosamente o código confrontando-o diretamente com a **Tabela 3.2 da dissertação de Silveira (2006)**.*  
  > *Ele utilizou um sistema acadêmico de 4ª ordem e estimou modelos de ordem 1 até ordem 7.*  
  > *Como a banca pode verificar na nossa tabela comparativa, nossa rotina alcançou **100% de concordância numérica com Silveira**:*  
  > - *Na 1ª ordem, o custo foi $J = 15,05$; na 2ª ordem, caiu para $3,02$; e na 4ª ordem atingiu o gabarito exato de $J = 6,28 \times 10^{-4}$ com $\text{FIT} = 99,98\%$.*  
  > - *Notem que para as ordens 5, 6 e 7, o custo estaciona no mesmo patamar de $10^{-4}$. Isso prova o princípio da **parcimônia**: como a planta original é de 4ª ordem, ordens maiores introduzem complexidade desnecessária e geram quase-cancelamento de polos e zeros.*  
  > *Em sistemas didáticos puros com ordem compatível, obtivemos $\text{FIT} = 100,00\%$ e custo de $10^{-14}$, confirmando a exatidão algébrica da rotina."*

### 🟡 Slide 7: [Item 4] O Modelo Simulink: Diagrama de Blocos e Chirp (Tempo: 1:15 min)
* **O que falar:**
  > *"No Item 4, fomos para o ambiente dinâmico do **Simulink** (`modelo_item4.slx`).*  
  > *O print do nosso diagrama de blocos está exibido no canto superior esquerdo deste slide:*  
  > - *O bloco **`Entrada_u`** lê do workspace um sinal **Chirp senoidal linear**, que varre continuamente de **0,1 Hz a 15 Hz** ao longo de 50 segundos, cobrindo toda a faixa dinâmica da planta.*  
  > - *O bloco **`Planta_LTI`** executa a função de transferência contínua de 2ª ordem: $G(s) = \frac{8}{0,2s^2 + 1,2s + 1} = \frac{40}{s^2 + 6s + 5}$, cujos polos nominais estão em $-1$ e $-5$.*  
  > - *O bloco **`Saida_y`** exporta o sinal temporal de volta para o workspace com taxa de amostragem de 1 ms ($f_s = 1000\text{ Hz}$), totalizando 20.001 amostras.*  
  > - *Configuramos o solver contínuo **`ode4`** (Runge-Kutta de 4ª ordem de passo fixo), garantindo uma simulação precisa e livre de artefatos numéricos.*  
  > *O gráfico à direita mostra a evolução temporal: a entrada mantém amplitude constante enquanto acelera sua frequência, e a saída responde com atenuação natural do filtro passa-baixas da planta."*

### 🟡 Slide 8: [Item 4] Extração por FFT e Validação do Modelo Identificado (Tempo: 1:00 min)
* **O que falar:**
  > *"A partir das séries temporais geradas pelo Simulink, aplicamos a **Transformada Rápida de Fourier (FFT)** nos sinais $u(t)$ e $y(t)$:*  
  > $$G(j\omega_k) = \frac{Y(k)}{U(k)}$$  
  > *Isolamos 126 frequências entre 1,26 e 79,76 rad/s com alta relação sinal-ruído e alimentamos o N2CACGO para ordem $n=2$.*  
  > *Os resultados foram excelentes:*  
  > - *O N2CACGO estimou os polos em **$s_1 = -0,967$** e **$s_2 = -5,038$** — um erro inferior a **3%** em relação aos polos nominais $-1$ e $-5$!*  
  > - *Alcançamos um **FIT global de 96,47%**, com erro de módulo de apenas $0,165\text{ dB}$ e erro de fase de $1,02^\circ$.*  
  > *Como se observa no diagrama de Bode à direita, a curva identificada em vermelho sobrepõe com precisão cirúrgica a curva nominal em azul, provando a robustez do método contra o vazamento espectral (*leakage*) da FFT finita.*  
  > *Passo a palavra agora ao Renato Felix para apresentar a identificação em bancada experimental real de um motor CC."*

---

## 👤 BLOCO 3: RENATO FELIX (Slides 9 a 11 — ~4:30 min)

### 🟠 Slide 9: [Item 5] O Caso do Motor CC: Dados de Bancada e Rigor Metrológico (Tempo: 1:30 min)
* **O que falar:**
  > *"Obrigado, Pedro. Olá a todos.*  
  > *No Item 5, aplicamos o método N2CACGO a um sistema físico real: a bancada didática do **Motor Elétrico de Corrente Contínua**.*  
  > *Qual foi o caso do motor e quais dados nós usamos?*  
  > - *Utilizamos os dados experimentais coletados pelo nosso **Grupo 3 na disciplina de Sinais e Sistemas Lineares (SSL)** no laboratório da SE/3.*  
  > - *O dataset é composto por **66 arquivos `.mat`**, divididos com rigor metodológico:*  
  >   * **26 ensaios senoidais** (de 0,20 Hz a 10,0 Hz): Usados exclusivamente como dados de ESTIMAÇÃO da FRF.*  
  >   * **5 ensaios de onda quadrada** e **5 ensaios de onda triangular** (de 2 a 10 Hz): Reservados exclusivamente para a VALIDAÇÃO DINÂMICA.*  
  > - *Mantivemos **rigor metrológico total**: usamos apenas a base autêntica do Grupo 3, expurgando dados de outros grupos para evitar ruídos de calibração cruzada.*  
  > *Além disso, aplicamos um tratamento de sinal indispensável:*  
  > *Como a identificação frequencial exige regime permanente estrito, **descartamos os primeiros 40% das amostras** de cada ensaio para eliminar o transitório de aceleração de partida do motor. A DFT foi calculada estritamente sobre os 60% finais estacionários, resultando em 23 fasores limpos."*

### 🟠 Slide 10: [Item 5] Varredura de Ordens: Por que Selecionamos a 1ª Ordem? (Tempo: 1:15 min)
* **O que falar:**
  > *"Seguindo as orientações do professor, realizamos uma varredura de identificação para **ordens de 1 a 5**.*  
  > *Como a banca pode acompanhar na tabela obtida no MATLAB:*  
  > - *A **1ª ordem** alcançou o menor custo $J = 1,7468$, menor erro de módulo ($0,21\text{ dB}$) e o **maior FIT global: 88,36%**.*  
  > - *A 2ª ordem teve FIT de $85,12\%$, a 3ª ordem $84,82\%$ e a 5ª ordem despencou para $75,59\%$.*  
  > *Por que ordens maiores pioraram o resultado?*  
  > *Porque em bancadas reais existem ruídos elétricos de comutação nas escovas do motor. Modelos de ordem 2 ou superior tentam ajustar esse ruído de alta frequência (*overfitting*), degradando o condicionamento numérico da matriz $Q$ sem qualquer ganho físico.*  
  > *Por **parcimônia de engenharia** e consistência com a teoria eletromecânica clássica, o modelo de 1ª ordem foi selecionado como o modelo ótimo do sistema."*

### 🟠 Slide 11: [Item 5] Modelo Físico Eletromecânico e Atraso de Padé (10,2 ms) (Tempo: 1:45 min — Ponto Alto da Defesa!)
* **O que falar:**
  > *"Chegamos ao ponto alto da análise física do nosso trabalho.*  
  > *A função de transferência de 1ª ordem identificada pelo N2CACGO com $\text{FIT} = 88,36\%$ foi:*  
  > $$G(s) = \frac{-0,2468s + 48,33}{s + 4,794}$$  
  > *A partir dela, extraímos os parâmetros físicos reais do motor:*  
  > - * **Ganho Estático de Velocidade:** $K_m = \frac{48,33}{4,794} \approx 10,08\text{ (rad/s)/V}$ (ou $20,07\text{ dB}$);*  
  > - * **Constante de Tempo Mecânica Dominante:** $\tau_m = \frac{1}{4,794} \approx 0,209\text{ segundos}$.*  
  > *Agora, um observador desatento poderia olhar para o numerador e perguntar: 'Vocês têm um **zero no semi-plano direito em $s = +195,8\text{ rad/s}$**! O motor é instável?'*  
  > *A resposta é categoricamente **NÃO**! O polo estável em $-4,79\text{ rad/s}$ dita a estabilidade.*  
  > *Aquele zero no semi-plano direito é a manifestação física exata da **Aproximação de Padé de 1ª ordem de um atraso puro de transporte**:*  
  > $$e^{-s\tau_d} \approx \frac{1 - s \frac{\tau_d}{2}}{1 + s \frac{\tau_d}{2}} \implies \tau_d = \frac{2}{195,8} \approx 10,2\text{ milissegundos}$$  
  > *E o que são esses 10,2 milissegundos?*  
  > *É exatamente o atraso de hardware da bancada do laboratório: a conversão D/A, o filtro analógico e o período de amostragem da placa de aquisição DAQ!*  
  > *É esse atraso de 10,2 ms que faz a fase experimental medida no tacômetro cair além de $-90^\circ$ a 10 Hz!*  
  > *O algoritmo N2CACGO capturou não só o motor, mas o atraso da instrumentação física da bancada.*  
  > *Para falar da validação no tempo e das conclusões, passo a palavra ao Arthur Scarpini."*

---

## 👤 BLOCO 4: ARTHUR SCARPINI (Slides 12 a 14 — ~4:00 min)

### 🔴 Slide 12: [Item 5] Validação Temporal Cega (Regra de Ouro) (Tempo: 1:15 min)
* **O que falar:**
  > *"Obrigado, Renato. Bom dia a todos.*  
  > *No Slide 12, nós aplicamos o que o professor Marcelo definiu em aula como a **'Regra de Ouro da Identificação'**: nunca validar um modelo usando os mesmos dados usados na estimação!*  
  > *O modelo foi calibrado puramente com as 26 senoides. Para validação, fizemos um **teste cego contra sinais não-senoidais inéditos**: os ensaios de **onda quadrada** (`sqrf`) e **onda triangular** (`trif`) a 10 Hz.*  
  > *Como a banca pode verificar nos gráficos:*  
  > - *Na **onda quadrada** (gráfico à esquerda), a simulação temporal reproduz perfeitamente as transições abruptas, com a taxa exponencial de subida e descida compatível com $\tau_m = 0,209\text{ s}$ e patamares consistentes de velocidade.*  
  > - *Na **onda triangular** (gráfico à direita), o polo mecânico do motor em $-4,79\text{ rad/s}$ atua como um filtro passa-baixas natural, atenuando os harmônicos ímpares superiores da Série de Fourier e arredondando suavemente as cúspides com defasagem idêntica à medida experimentalmente pelo tacômetro.*  
  > *Isso comprova que o modelo linear identificado no domínio da frequência possui alta capacidade de generalização no domínio do tempo."*

### 🔴 Slide 13: Dificuldades Encontradas e Soluções de Engenharia (Tempo: 1:30 min)
* **O que falar:**
  > *"Durante o desenvolvimento, nos deparamos com desafios práticos de engenharia que merecem destaque:*  
  > 1. * **Mau Condicionamento Matricial da Matriz $Q$:** Em ordens $n \ge 4$, as potências $(j\omega)^n$ atingem grandezas de $10^{14}$ nas frequências mais altas. Com isso, o número de condição recíproco $\text{rcond}(Q)$ caiu para $10^{-17}$, beirando o limite da precisão dupla IEEE. Inicialmente, tentar aplicar a pseudoinversa `pinv` com decomposição em valores singulares (SVD) truncava direções de autovalores cruciais, gerando erros nos parâmetros de Silveira. A solução de engenharia foi adotar a **eliminação Gaussiana direta com pivoteamento parcial** (operador backslash `Q \ Y` do MATLAB), que preservou as bases monomiais e recuperou o gabarito exato.*  
  > 2. * **Vazamento Espectral da FFT:** Controlado restringindo a extração fasorial à janela temporal com excitação ativa do Chirp e alta coerência SNR.*  
  > 3. * **Transitórios de Partida na Bancada:** Expurgados pelo descarte dos 40% iniciais de cada ensaio.*  
  > 4. * **Automação no Simulink:** Parametrização programática do solver `ode4` com passo fixo de 1 ms via scripts nativos."*

### 🔴 Slide 14: Conclusões Finais: Síntese, Dificuldades e Lições (Tempo: 1:15 min)
* **O que falar:**
  > *"Para concluir nosso trabalho, professor Marcelo e colegas:*  
  > *Mais do que apenas rodar algoritmos, nossa equipe vivenciou na prática os desafios reais da identificação de sistemas:*  
  > - *Enfrentamos o limite numérico de máquina quando o condicionamento da matriz $Q$ caiu para $10^{-16}$, e aprendemos que o pivoteamento gaussiano direto preserva a base analítica que métodos cegos como a pseudoinversa truncavam;*  
  > - *Dominamos o tratamento de dados reais, limpando os transitórios de partida e o vazamento espectral da FFT;*  
  > - *E tivemos a sensibilidade de engenharia para entender que o zero no semi-plano direito do motor não era uma falha, mas sim a aproximação de Padé capturando os 10,2 milissegundos de atraso da placa DAQ do laboratório.*  
  > *Cumprimos com êxito todos os 5 itens exigidos em MATLAB nativo e Simulink, e disponibilizamos tudo de forma transparente no nosso repositório no GitHub:*  
  > `https://github.com/VPariz/masd-identificacao-n2cacgo`  
  > *Convido o Pariz, o Pedro e o Renato a ficarem à frente comigo, e abrimos formalmente a sessão para as perguntas da banca!"*

---

# 🛡️ CARTÃO DE RESGATE PARA PERGUNTAS DA BANCA

| Pergunta Provável | Resposta Rápida e Firme |
|---|---|
| *"Por que o método de Silveira não cai em mínimos locais?"* | *"Porque o N2CACGO formula o erro como resíduo de equação $e(j\omega) = A\cdot G - B$, que é estritamente linear nos parâmetros. A função de custo quadrática torna-se estritamente convexa ($\nabla^2 J \ge 0$), garantindo mínimo global único resolvendo o SEL analítico $Q\theta = Y$."* |
| *"Por que deu um zero no semi-plano direito no motor CC? O motor é instável?"* | *"Não, o polo estável em $-4,79$ garante a estabilidade física. O zero em $+195,8\text{ rad/s}$ é a aproximação de Padé de 1ª ordem do atraso puro de transporte da placa DAQ ($\tau_d = 2/195,8 \approx 10,2\text{ ms}$), explicando a queda de fase experimental além de $-90^\circ$ a 10 Hz."* |
| *"Qual foi o critério para escolher 1ª ordem para o motor e não ordens maiores?"* | *"Parcimônia de engenharia. Como comprovado pela Tabela de Ordens, ordens $\ge 2$ sofrem overfitting com ruídos de comutação das escovas sem ganho físico real, piorando o condicionamento de $Q$."* |
| *"Como foi feito o modelo no Simulink?"* | *"Implementamos o diagrama `modelo_item4.slx` com blocos From Workspace (`Entrada_u`), Transfer Fcn (`Planta_LTI`) e To Workspace (`Saida_y`), simulado por 50 s com Chirp de 0,1 a 15 Hz no solver ode4 (Runge-Kutta 4ª ordem, passo fixo Ts = 1 ms)."* |
| *"O que mostra o Fluxograma do Slide 5?"* | *"Mostra as 3 frentes de entrada (benchmark, Simulink e motor CC) convergindo para o núcleo único identifica_N2CACGO.m e sendo validadas pelo valida_modelo_fr.m com cálculo de métricas e testes dinâmicos temporais cego."* |
