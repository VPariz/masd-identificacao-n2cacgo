# 📋 ROTEIRO OFICIAL DE APRESENTAÇÃO (POWERPOINT 14 SLIDES)
## Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO
**Instituição:** Instituto Militar de Engenharia (IME) — DE/3 • Engenharia Elétrica  
**Disciplina:** Modelagem e Análise de Sistemas Dinâmicos (MASD)  
**Docente / Orientador:** Prof. Dr. Marcelo de Araújo Oliveira  
**Equipe de Autores (Nomes de Guerra em Destaque):**  
- **Renato Felix** (Renato Costa Félix)  
- **Pariz** (João Victor Tavares Pariz)  
- **Pedro Augusto / Peu** (Pedro Augusto dos Santos Barbosa)  
- **Scarpini** (Wagner Scarpini Miranda)  

**Tempo Total de Apresentação:** ~15 a 17 minutos (faixa ideal da banca) + arguição.  
**Arquivo Oficial da Apresentação:** [`apresentacao_MASD_N2CACGO_IME.pptx`](file:///c:/Users/jvpar/estudo/3.2/MASD/trabalho_identificacao/apresentacao/apresentacao_MASD_N2CACGO_IME.pptx)  
**Artigo Acadêmico IEEE (PDF):** [`artigo_identificacao.pdf`](file:///c:/Users/jvpar/estudo/3.2/MASD/trabalho_identificacao/artigo/artigo_identificacao.pdf)

---

### ⏱️ Tabela de Distribuição do Tempo e Funções por Integrante

| Bloco | Orador | Slides | Foco Técnico Principal | Tempo Estimado |
|:---:|---|:---:|---|:---:|
| **1** | **Renato Felix** | 1 a 3 | Abertura oficial, Modelagem vs. Identificação (Caixa Branca/Cinza/Preta), Domínio da Frequência vs. Tempo, Teoria de Silveira (2006) e Formulação Matemática Convexa | **~3:45 min** |
| **2** | **Pariz** | 4 a 6 | Implementação Vetorizada no MATLAB (`identifica_N2CACGO.m` e `valida_modelo_fr.m`), Fluxograma Geral Integrado e Arquitetura do Modelo Simulink (`modelo_item4.slx`) | **~3:45 min** |
| **3** | **Pedro Augusto (Peu)** | 7 a 11 | Validação Teórica de Silveira (Tabela 3.2), Reconstrução Espectral por FFT ($FIT = 96,47\%$), Metrologia da Bancada Experimental do Motor CC (SSL Grupo 3), Varredura de Ordens e Modelo Físico com Padé (10,2 ms) | **~5:00 min** |
| **4** | **Scarpini** | 12 a 14 | Regra de Ouro da Identificação (Validação Temporal Cega com Ondas Quadrada e Triangular), Desafios Numéricos de Engenharia e Conclusões Finais (Cumprimento dos 8 Itens) | **~3:30 min** |
| **TOTAL** | **Toda a Equipe** | **1 a 14** | **Apresentação Completa, Equilibrada, Visual e com Rigor Militar** | **~16:00 min** |

---

# 🎙️ GUIA DE FALA SLIDE A SLIDE (O QUE CADA UM DEVE FALAR)

---

## 👤 BLOCO 1: RENATO FELIX (Slides 1 a 3 — ~3:45 min)

### 🟢 Slide 1: Capa & Apresentação da Equipe (Tempo: ~1:00 min)
* **O que falar:**
  > *"Bom dia / boa tarde a todos. Cumprimento o nosso orientador, Prof. Dr. Marcelo de Araújo Oliveira, e os colegas presentes.*  
  > *Nossa equipe é formada por mim, Renato Felix, pelo João Victor Pariz, Pedro Augusto e Wagner Scarpini.*  
  > *Hoje apresentamos o trabalho final da disciplina de Modelagem e Análise de Sistemas Dinâmicos, com o tema: **'Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO'**.*  
  > *Estruturamos a nossa apresentação em 4 blocos técnicos equilibrados, cobrindo com rigor absoluto todos os 8 itens propostos na disciplina:*  
  > 1. *Eu (Renato) abrirei a apresentação com a contextualização física, os métodos de identificação e a teoria matemática de Silveira (2006);*  
  > 2. *O Pariz explicará a estrutura dos códigos em MATLAB, o fluxograma do pipeline e a arquitetura do modelo no Simulink;*  
  > 3. *O Pedro Augusto apresentará os resultados acadêmicos, a extração por FFT e toda a caracterização experimental da bancada do motor CC;*  
  > 4. *E o Scarpini conduzirá a validação temporal cega, os desafios numéricos superados e as conclusões finais.*  
  > *Passo agora ao contexto da identificação de sistemas."*

### 🟢 Slide 2: 1. Teoria dos Métodos: Modelagem vs. Identificação (Tempo: ~1:15 min)
* **O que falar:**
  > *"Como vimos ao longo das aulas de MASD, os modelos matemáticos dividem-se em três grandes famílias:*  
  > - * **Caixa Branca:** Conhecimento dedutivo puro, baseado estritamente em leis físicas de primeiros princípios (Newton, Kirchhoff, conservação de energia), sem dados experimentais. Apresenta limitações sérias quando não conhecemos com precisão os atritos ou parâmetros térmicos.*  
  > - * **Caixa Cinza:** Abordagem híbrida onde a estrutura fenomenológica é conhecida e utilizamos dados para estimar os parâmetros físicos desconhecidos.*  
  > - * **Caixa Preta:** Mapeamento puramente baseado em dados medidos de entrada e saída.*  
  > *Na identificação de sistemas, surge a decisão fundamental: **Domínio do Tempo ou Domínio da Frequência?***  
  > *Os métodos no tempo (como ARX e PEM) sofrem com três problemas críticos: sensibilidade a ruídos estocásticos coloridos, exigência estrita de condições iniciais nulas ($x(0)=0$) e dificuldade na estimação de atrasos puros.*  
  > *Por outro lado, no domínio da frequência, colhemos as **três grandes vantagens clássicas** destacadas pelo professor em sala:*  
  > 1. * **Filtragem natural de ruído**, pois analisamos apenas a resposta forçada nas frequências excitadas, descartando ruídos fora da banda;*  
  > 2. * **Sensibilidade direta a picos de ressonância e margens de estabilidade**, cruciais para controle robusto;*  
  > 3. * **Compactação brutal de dados**, comprimindo milhares de amostras temporais em poucos fasores de resposta em frequência (FRF).*  
  > *Porém, métodos frequenciais anteriores — como Levy (1959), Sanathanan-Koerner (1963) e Valle (2005) — sofrem com não-convexidade e mínimos locais. Para resolver isso em definitivo, adotamos o método de Silveira (2006)."*

### 🟢 Slide 3: 2. O Método N2CACGO (Silveira, 2006): Formulação Convexa (Tempo: ~1:30 min)
* **O que falar:**
  > *"O método que implementamos foi desenvolvido na dissertação de mestrado de **Bruno de Pinho Silveira (IME, 2006)**, denominado **N2CACGO** — sigla para Norma 2 Convexo Analítico Conjunto Gerador Ótimo.*  
  > *Como podemos ver em destaque na fórmula matemática do slide:*  
  > *Buscamos uma Função de Transferência biprópria de ordem $n$, onde o numerador é $N(s)$ e o denominador é $D(s)$, sendo $D(s)$ mônico.*  
  > *A genialidade de Silveira foi formular o resíduo de equação ponderado:*  
  > $$e(j\omega_k) = D(j\omega_k) \cdot G(j\omega_k) - N(j\omega_k)$$  
  > *Observem com atenção: esse resíduo é **estritamente linear** em relação a todos os parâmetros desconhecidos $\alpha$ e $\beta$!*  
  > *Ao definirmos a função custo em Norma 2 como a soma dos quadrados desses resíduos, $J(\theta) = \sum |e(j\omega_k)|^2$, temos uma forma quadrática com matriz Hessiana estritamente positiva definida.*  
  > *A consequência matemática direta é extraordinária: **NÃO EXISTEM MÍNIMOS LOCAIS!** O problema é estritamente convexo.*  
  > *Diferenciando analiticamente a função custo em relação aos parâmetros e igualando a zero, obtemos o sistema de equações normais particionado:*  
  > $$Q \cdot \theta = Y \implies \theta^* = Q^{-1} Y$$  
  > *Ou seja: a solução ótima global é obtida **em um único passo analítico**, sem nenhuma iteração, sem chutes iniciais e sem risco de divergência numérica.*  
  > *Para explicar como vetorizamos esse algoritmo e as métricas no MATLAB, passo a palavra ao João Victor Pariz."*

---

## 👤 BLOCO 2: JOÃO VICTOR PARIZ (Slides 4 a 6 — ~3:45 min)

### 🟢 Slide 4: 3. [Item 1 & 2] Implementação Vetorizada no MATLAB (Tempo: ~1:15 min)
* **O que falar:**
  > *"Obrigado, Renato. Cumprimento o professor Marcelo e a banca.*  
  > *No Bloco 2, apresento a implementação computacional que desenvolvemos.*  
  > *Para cumprir o **Item 1 do enunciado**, implementamos a rotina `identifica_N2CACGO.m` de forma totalmente vetorizada:*  
  > 1. *Montamos a matriz monomial $R$, cujas linhas são as potências $(j\omega)^k$ avaliadas em todas as frequências de medição;*  
  > 2. *Calculamos analiticamente os 4 blocos da matriz $Q$ e o vetor $Y$ através de projeções Hermitianas (usando `real(R * R_H)` e a resposta complexa $G$);*  
  > 3. *Resolvemos o sistema matricial pelo operador backslash (`Q \ Y`), que executa eliminação Gaussiana com pivoteamento ótimo.*  
  > *Para o **Item 2 do enunciado**, criamos a rotina `valida_modelo_fr.m`, responsável por calcular as 4 métricas oficiais ensinadas em aula:*  
  > - *O Custo $J$ em Norma 2 de Silveira;*  
  > - *O RMSE de Magnitude em dB e o RMSE de Fase em graus;*  
  > - *E o coeficiente de ajuste global **FIT %**, que quantifica a aderência percentual da curva estimada.*  
  > *A rotina plota automaticamente o diagrama de Bode comparativo com as curvas sobrepostas."*

### 🟢 Slide 5: 4. Fluxograma Integrado: Do Sinal Temporal à Identificação (Tempo: ~1:15 min)
* **O que falar:**
  > *"No Slide 5, apresentamos o fluxograma completo de engenharia que elaboramos para integrar todos os códigos do trabalho.*  
  > *Vejam como o pipeline se organiza de forma modular:*  
  > - *À esquerda, temos as três fontes de dados: os modelos acadêmicos do Item 3, o modelo contínuo no Simulink do Item 4, e os dados brutos da bancada do motor CC do Item 5.*  
  > - *Para os sinais temporais, aplicamos o processamento espectral: no Simulink, calculamos a FRF fasorial via FFT com janelamento de Hann; no caso do motor CC, extraímos os fasores via regressão senoidal de regime permanente.*  
  > - *Todos esses dados convergem para o coração do algoritmo: a função `identifica_N2CACGO.m`, que constrói as matrizes $Q$ e $Y$ e calcula o vetor de coeficientes $\theta^*$.*  
  > - *Por fim, a rotina `valida_modelo_fr.m` avalia as métricas numéricas e envia o modelo identificado para a validação temporal cega no domínio do tempo.*  
  > *Vamos ver agora como o modelo dinâmico do Simulink foi construído."*

### 🟢 Slide 6: 5. [Item 4] O Modelo Simulink: Diagrama de Blocos e Simulação (Tempo: ~1:15 min)
* **O que falar:**
  > *"Para atender ao **Item 4 do trabalho**, criamos o arquivo `modelo_item4.slx` no Simulink, cujo diagrama de blocos está exibido na imagem superior à esquerda.*  
  > *Diferente de outros grupos que relataram dificuldades em integrar o Simulink, nossa modelagem foi desenvolvida com rigor técnico:*  
  > 1. *O bloco `Entrada_u` (From Workspace) injeta um sinal Chirp contínuo varrendo de 0,1 Hz a 15 Hz por 50 segundos, garantindo uma excitação espectral rica em todas as frequências de interesse;*  
  > 2. *O bloco `Planta_LTI` (Transfer Fcn) simula a função de transferência contínua com polos reais em $-1$ e $-5$ e ganho estático igual a 8;*  
  > 3. *O bloco `Saida_y` (To Workspace) exporta a resposta temporal $y(t)$ em formato de Array, com passo fixo de amostragem $T_s = 1$ ms ($20.001$ amostras);*  
  > 4. *Configuramos o solver numérico contínuo **ode4 (Runge-Kutta de 4ª ordem)**, assegurando alta fidelidade e ausência total de truncamento.*  
  > *À direita, observamos os sinais temporais gerados: à medida que a frequência da entrada aumenta, a saída sofre a atenuação e a defasagem características da planta.*  
  > *Para apresentar os resultados desse modelo, o benchmark de Silveira e a bancada do motor, passo a palavra ao Pedro Augusto."*

---

## 👤 BLOCO 3: PEDRO AUGUSTO / PEU (Slides 7 a 11 — ~5:00 min)

### 🟢 Slide 7: 6. [Item 3] Validação Teórica: Benchmark de Silveira (2006) (Tempo: ~1:15 min)
* **O que falar:**
  > *"Obrigado, Pariz. Cumprimento o professor Marcelo e a banca.*  
  > *No Bloco 3, apresento a validação dos resultados e a análise física experimental.*  
  > *Iniciando pelo **Item 3**, nosso primeiro objetivo foi reproduzir o Exemplo 3.4.1 da dissertação de Bruno de Pinho Silveira (IME, 2006).*  
  > *A tabela no slide mostra a comparação direta entre os custos $J$ obtidos pela nossa rotina em MATLAB e os valores teóricos de Silveira:*  
  > - *Para ordens 1, 2 e 3, os erros são elevados (custo de 15, 3 e 1,46);*  
  > - *Na **4ª ordem**, que é a ordem real da planta alvo, o custo despenca para $6,28 \times 10^{-4}$ e o FIT atinge **99,98%**!*  
  > - *Os valores da nossa rotina batem com precisão de 4 casas decimais com o gabarito de Silveira.*  
  > - *Ao testarmos ordens superiores (5 a 7), o FIT estabiliza em 99,99% e surgem polos e zeros que quase se cancelam, confirmando o **Princípio da Parcimônia** ensinado em aula: a 4ª ordem é o modelo ótimo.*  
  > *Em funções didáticas puras de 1ª a 3ª ordem, nossa rotina alcançou FIT de 100,00% com erro de máquina."*

### 🟢 Slide 8: 7. [Item 4] Extração por FFT e Validação do Modelo Identificado (Tempo: ~1:00 min)
* **O que falar:**
  > *"No Slide 8, fechamos o Item 4 apresentando a extração espectral a partir dos sinais do Simulink.*  
  > *Aplicamos a Transformada Rápida de Fourier (FFT) aos sinais $u(t)$ e $y(t)$, obtendo a FRF empírica pela razão fasorial $\hat{H}(j\omega_k) = Y(k) / U(k)$ em 126 frequências com alta relação sinal-ruído.*  
  > *Alimentamos esses fasores na rotina N2CACGO para ordem 2. Vejam o resultado extraordinário:*  
  > - *A planta nominal é $40 / (s^2 + 6s + 5)$, com polos em $-1$ e $-5$ e ganho 8;*  
  > - *O modelo identificado foi $40,0 / (s^2 + 6,005s + 4,818)$, estimando os polos em $-0,967$ e $-5,038$ — erro inferior a 3%!*  
  > - *O índice de ajuste global **FIT foi de 96,47%**, com RMSE de magnitude de apenas $0,16$ dB e RMSE de fase de $1,02$ grau!*  
  > *O gráfico de Bode à direita comprova que a curva identificada em vermelho sobrepõe com perfeição a curva teórica em azul."*

### 🟢 Slide 9: 8. [Item 5] O Caso do Motor CC: Dados de Bancada Real (SSL) (Tempo: ~1:15 min)
* **O que falar:**
  > *"Passamos agora ao **Item 5**, que é a identificação de um sistema físico real de laboratório: o motor de corrente contínua da disciplina de Sinais e Sistemas Lineares (dados do Grupo 3).*  
  > *Explico o arranjo experimental e o que são os dados que utilizamos:*  
  > - *O sistema físico é um servomotor CC acoplado a uma carga inercial;*  
  > - *A entrada $u(t)$ é a tensão de armadura gerada por ponte H PWM;*  
  > - *A saída $y(t)$ é a velocidade angular em rad/s, medida por um encoder digital óptico;*  
  > - *O ensaio é composto por 26 arquivos de dados, cobrindo senoides puras de 0,20 Hz até 10,00 Hz (1,26 a 62,83 rad/s), amostrados a 1 kHz.*  
  > *Para garantir rigor metrológico:*  
  > - *Descartamos os primeiros 40% de cada ensaio para eliminar o transitório de partida do motor;*  
  > - *Ajustamos os últimos 60% por regressão senoidal de mínimos quadrados, obtendo ganho e fase purificados contra ruído de escova.*  
  > *Um comportamento experimental chamou a atenção: a defasagem angular ultrapassa $-90^\circ$ e chega a $-104^\circ$ a 10 Hz! Vamos ver o porquê."*

### 🟢 Slide 10: 9. [Item 5] Varredura de Ordens do Motor CC (Ordens 1 a 5) (Tempo: ~1:00 min)
* **O que falar:**
  > *"No Slide 10, executamos a varredura de ordens de 1 a 5 no N2CACGO para determinar o modelo ótimo do motor CC.*  
  > *A tabela e o gráfico de Bode mostram os resultados:*  
  > - * **1ª Ordem:** Menor custo $J = 1,7468$, RMSE de magnitude de $0,21$ dB e o **maior FIT: 88,36%**;*  
  > - *2ª Ordem: FIT cai para 85,12%;*  
  > - *3ª e 4ª Ordens: Mantêm FIT em torno de 85 a 87%;*  
  > - *5ª Ordem: O FIT despenca para 75,59% e o erro dispara.*  
  > *Por que ordens maiores não melhoram o modelo?*  
  > *Porque ordens altas sofrem de **overfitting**, tentando modelar o ruído elétrico de comutação das escovas e as vibrações mecânicas de alta frequência, além de piorar severamente o condicionamento numérico da matriz.*  
  > *Aplicando o Princípio da Parcimônia de Box-Jenkins, escolhemos a **1ª ordem** como o modelo ótimo de engenharia."*

### 🟢 Slide 11: 10. [Item 5] Modelo Físico Eletromecânico e Atraso de Padé (10,2 ms) (Tempo: ~1:30 min)
* **O que falar:**
  > *"Este é o ponto alto da interpretação física do trabalho.*  
  > *A função de transferência de 1ª ordem identificada pelo N2CACGO foi:*  
  > $$G(s) = \frac{-0,2468 s + 48,33}{s + 4,794}$$  
  > *Extraindo os parâmetros físicos fundamentais:*  
  > - *Ganho estático de velocidade: $K_m = 48,33 / 4,794 = 10,08$ (rad/s)/V ($20,07$ dB);*  
  > - *Constante de tempo mecânica dominante: $\tau_m = 1 / 4,794 = 0,209$ segundos.*  
  > *Agora reparem no numerador: temos um zero real no semiplano direito em $s = +48,33 / 0,2468 \approx +195,8$ rad/s!*  
  > *Isso é um sistema de **fase não-mínima**! Mas por que um motor CC apresenta esse zero?*  
  > *Isso NÃO é erro de cálculo. É a manifestação exata da **Aproximação de Padé de 1ª ordem** de um atraso puro de transporte:*  
  > $$e^{-s \tau_d} \approx \frac{1 - s \tau_d / 2}{1 + s \tau_d / 2} \implies \tau_d = \frac{2}{195,8} \approx 10,2 \text{ milissegundos!}$$  
  > *E o que são esses 10,2 ms? É exatamente o atraso combinado de conversão D/A, modulação PWM e latência de contagem do tacômetro óptico da placa DAQ!*  
  > *O algoritmo N2CACGO capturou esse atraso puro autonomamente sem precisarmos adicionar polos extras.*  
  > *Para apresentar a validação cega no tempo, as dificuldades e conclusões, passo a palavra ao Arthur Scarpini."*

---

## 👤 BLOCO 4: SCARPINI (Slides 12 a 14 — ~3:30 min)

### 🟢 Slide 12: 11. [Item 5] Validação Temporal Cega (Onda Quadrada e Triangular) (Tempo: ~1:15 min)
* **O que falar:**
  > *"Obrigado, Pedro. Cumprimento o professor Marcelo e a banca examinadora.*  
  > *No Bloco 4, trago o fechamento do trabalho com a validação definitiva do modelo.*  
  > *Aplicamos aqui a chamada **'Regra de Ouro da Identificação'**, ensinada nas aulas de MASD: um modelo jamais deve ser validado usando os mesmos dados usados na sua estimação.*  
  > *O nosso modelo de motor CC foi estimado exclusivamente com dados senoidais.*  
  > *Para testá-lo de verdade, submetemos a função identificada a sinais temporais dinâmicos nunca antes vistos: ensaios com **Onda Quadrada** e **Onda Triangular** a 10 Hz.*  
  > *Vejam os dois gráficos no slide:*  
  > - *Na onda quadrada (à esquerda), a curva vermelha do modelo N2CACGO rastreia perfeitamente a subida exponencial e o patamar de regime medido pelo tacômetro (curva preta);*  
  > - *Na onda triangular (à direita), o modelo segue fielmente as rampas de aceleração e desaceleração.*  
  > *Essa concordância cega no domínio do tempo prova que o ganho de 10,08 e a constante de tempo de 0,21 s são a representação física autêntica da bancada real!"*

### 🟢 Slide 13: 12. Dificuldades Encontradas e Soluções de Engenharia (Tempo: ~1:15 min)
* **O que falar:**
  > *"Ao longo do desenvolvimento, enfrentamos quatro dificuldades técnicas reais de engenharia e adotamos soluções concretas:*  
  > 1. * **Mal-condicionamento da Matriz de Vandermonde:** Para ordens altas ($n \ge 5$), as potências $(j\omega)^n$ geram colunas com ordens de grandeza díspares, fazendo a razão de condicionamento cair para $rcond(Q) < 10^{-16}$. Solucionamos aplicando normalização euclidiana de colunas e uso de decomposição SVD com pseudoinversa no MATLAB.*  
  > 2. * **Vazamento Espectral (Spectral Leakage) na FFT:** No Item 4, o truncamento finito das janelas temporais gerava dispersão de energia nas frequências vizinhas. Superamos isso aplicando janela de Hann e selecionando a banda de alta coerência espectral (1,26 a 79,8 rad/s).*  
  > 3. * **Defasagem Além de $-90^\circ$ em Alta Frequência:** O motor real apresentava $-104^\circ$ a 10 Hz. Identificamos que a síntese de um zero no semiplano direito pelo N2CACGO atua como a aproximação de Padé do atraso puro de transporte de 10,2 ms da DAQ.*  
  > 4. * **Não-Linearidades Mecânicas de Zona Morta e Atrito:** Em baixas velocidades, o atrito seco distorce o comportamento linear. Solucionamos descartando o transitório de partida e utilizando ajuste senoidal restrito ao regime forçado permanente.*"

### 🟢 Slide 14: 13. Conclusões Finais e Fechamento (Tempo: ~1:00 min)
* **O que falar:**
  > *"Para concluir nossa apresentação, destacamos as três grandes conquistas do trabalho:*  
  > 1. * **Eficácia e Robustez do N2CACGO:** O método proposto por Bruno de Pinho Silveira no IME (2006) comprovou ser extremamente eficiente, analítico e livre dos mínimos locais que afetam métodos clássicos;*  
  > 2. * **Cumprimento Integral dos 8 Itens:** Atendemos 100% das exigências da disciplina de MASD:*  
  >    - *Item 1: Algoritmo N2CACGO implementado e vetorizado;*  
  >    - *Item 2: Rotina de cálculo de erro de FRF e métricas de validação;*  
  >    - *Item 3: Validação acadêmica com gabarito exato de Silveira e didáticos (FIT 100%);*  
  >    - *Item 4: Modelo dinâmico no Simulink com reconstrução espectral FFT (FIT 96,47%);*  
  >    - *Item 5: Identificação da bancada do motor CC com interpretação física e atraso de Padé;*  
  >    - *Item 6: Artigo completo de 6 páginas no padrão IEEE compilado em PDF;*  
  >    - *Item 7: Apresentação em PowerPoint estruturada e cronometrada;*  
  >    - *Item 8: Nossa apresentação técnica perante o professor e a banca.*  
  > 3. * **Organização e Reprodutibilidade:** Todo o código, modelos e artigo estão organizados e prontos para entrega no Classroom.*  
  > *Agradecemos a atenção do Prof. Dr. Marcelo e da banca, e estamos à disposição para as perguntas."*

---

# 🎯 PERGUNTAS PROVÁVEIS DA BANCA (E COMO RESPONDER)

### ❓ Pergunta 1: *"Por que o método N2CACGO é garantido de não ter mínimos locais?"*
* **Quem responde:** Renato Felix.
* **Resposta ideal:**  
  > *"Porque a função objetivo $J(\theta)$ é formulada a partir do resíduo de equação $e(j\omega) = D(j\omega)G(j\omega) - N(j\omega)$, que é estritamente linear em relação aos parâmetros a estimar. Isso transforma $J(\theta)$ em uma forma quadrática cuja matriz Hessiana $\nabla^2 J$ é constante e estritamente positiva definida em todo o espaço de parâmetros. Em cálculo e otimização convexa, qualquer forma quadrática com Hessiano positivo definido possui um único ponto estacionário que é, por definição matemática, o mínimo global absoluto."*

### ❓ Pergunta 2: *"Como foi montado o modelo no Simulink e por que usar o solver ode4?"*
* **Quem responde:** Pariz.
* **Resposta ideal:**  
  > *"O modelo `modelo_item4.slx` foi construído com três blocos principais: `From Workspace` para injetar o sinal Chirp contínuo varrendo de 0,1 a 15 Hz por 50 s; `Transfer Fcn` contendo a dinâmica contínua $40/(s^2+6s+5)$; e `To Workspace` exportando em formato de Array. Adotamos o solver contínuo de passo fixo `ode4` (Runge-Kutta de 4ª ordem) com passo de amostragem de 1 ms ($T_s = 0,001$ s) para evitar erros de truncamento e artefatos de solver de passo variável na aplicação posterior da FFT."*

### ❓ Pergunta 3: *"Por que vocês escolheram o modelo de 1ª ordem para o motor se a 4ª ordem tinha FIT parecido?"*
* **Quem responde:** Pedro Augusto (Peu).
* **Resposta ideal:**  
  > *"Pelo Princípio da Parcimônia e pela física do sistema. A teoria clássica de máquinas elétricas CC mostra que a velocidade angular é dominada pelo polo mecânico $\tau_m$, pois o polo elétrico $\tau_e = L/R$ é ordens de grandeza mais rápido e inobservável na faixa de até 10 Hz. A 1ª ordem obteve o menor custo em norma 2 ($J=1,74$) e o maior FIT ($88,36\%$). Modelos de ordem superior começam a ajustar ruído de comutação das escovas e vibrações mecânicas (overfitting), degradando o condicionamento da matriz sem trazer ganho fenomenológico real."*

### ❓ Pergunta 4: *"O que significa fisicamente o zero no semiplano direito ($s = +195,8$ rad/s) no modelo do motor?"*
* **Quem responde:** Pedro Augusto ou Scarpini.
* **Resposta ideal:**  
  > *"Esse zero no SPD indica um sistema de fase não-mínima gerado pela aproximação racional de Padé de 1ª ordem de um atraso puro de transporte $e^{-s\tau_d} \approx (1 - s\tau_d/2)/(1 + s\tau_d/2)$. Fazendo $\tau_d = 2 / 195,8$, encontramos um atraso puro de aproximadamente 10,2 milissegundos. Esse atraso é a latência física combinada de conversão digital-analógica, modulação PWM e leitura do encoder pela placa DAQ do laboratório, o que explica perfeitamente por que a defasagem medida na bancada ultrapassa $-90^\circ$ e chega a $-104^\circ$ a 10 Hz."*

### ❓ Pergunta 5: *"Quais foram os maiores desafios numéricos que vocês enfrentaram na implementação?"*
* **Quem responde:** Scarpini.
* **Resposta ideal:**  
  > *"O maior desafio numérico foi o mal-condicionamento da matriz de Vandermonde $Q$ quando subimos a ordem para $n \ge 5$, onde as potências $(j\omega)^n$ em frequências altas levam o número de condição a ultrapassar $10^{15}$, gerando $rcond \approx 10^{-16}$. Superamos isso através do escalonamento euclidiano das colunas da matriz de regressão e uso de decomposição SVD/pseudoinversa. Outro desafio foi o vazamento espectral na FFT dos dados do Simulink, mitigado com janelamento de Hann e corte de bordas."*
