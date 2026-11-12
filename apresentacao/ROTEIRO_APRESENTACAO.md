# Roteiro do Orador: Defesa do Trabalho de MASD (IME)
## Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO

**Autores e Divisão de Papéis:**
1. **João Victor Tavares Pariz** (Slides 1 a 3 — ~3:45 min) — *Abertura, Contextualização & Formulação Convexa*
2. **Pedro Augusto** (Slides 4 a 6 — ~3:30 min) — *Validação de Silveira (2006) & Simulação Simulink com FFT*
3. **Renato Felix** (Slides 7 e 8 — ~3:45 min) — *Bancada Experimental do Motor CC & Parâmetros Físicos com Padé*
4. **Arthur Scarpini** (Slides 9 a 11 — ~4:00 min) — *Validação Dinâmica Cega no Tempo, Desafios Numéricos & Conclusão*

**Orientador:** Prof. Dr. Marcelo de Araújo Oliveira  
**Tempo Total de Apresentação:** ~15:00 min (faixa estipulada: 10 a 20 min) + 5 min de arguição da banca.

---

### ⏱️ Tabela de Distribuição do Tempo por Integrante

| Integrante | Slides | Foco Técnico | Tempo Estimado |
|---|:---:|---|:---:|
| **João Victor Pariz** | 1, 2 e 3 | Abertura formal, motivação no domínio da frequência vs. tempo, convexidade do N2CACGO e dedução do SEL analítico $Q\theta = Y$. | **~3:45 min** |
| **Pedro Augusto** | 4, 5 e 6 | Reprodução exata da Tabela 3.2 de Silveira (ordens 1 a 7), modelo Simulink com Chirp (0,1 a 15 Hz) e extração fasorial por FFT ($FIT = 96,47\%$). | **~3:30 min** |
| **Renato Felix** | 7 e 8 | Rigor da base única do Grupo 3 (26 senóides), corte de transitórios nos últimos 60%, modelo de 1ª ordem ($K_m=10,08$, $\tau_m=0,209\text{ s}$) e explicação física do atraso de Padé ($\tau_d \approx 10,2\text{ ms}$). | **~3:45 min** |
| **Arthur Scarpini** | 9, 10 e 11 | Validação cega contra ondas quadrada e triangular a 10 Hz, superação do condicionamento matricial $\text{rcond}(Q) < 10^{-16}$ via Gauss com pivoteamento, conclusões e repositório. | **~4:00 min** |
| **TOTAL** | **1 a 11** | **Apresentação Fluida e Balanceada (4 Oradores)** | **~15:00 min** |

---

## 🎙️ Roteiro de Fala Passo a Passo

---

### PARTE 1: JOÃO VICTOR TAVARES PARIZ (Slides 1 a 3 — ~3:45 min)

#### Slide 1: Capa & Apresentação da Equipe (1:00 min)
> *"Bom dia / boa tarde a todos, professor Marcelo e colegas.*  
> *Nosso grupo é composto por mim, João Victor Pariz, pelo Pedro Augusto, Renato Felix e Arthur Scarpini.*  
> *Hoje apresentamos o trabalho final de Modelagem e Análise de Sistemas Dinâmicos, intitulado: **'Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO'**.*  
> *Estruturamos a nossa apresentação em 4 blocos complementares:*
> 1. *Eu iniciarei abordando a fundamentação matemática e a garantia de convexidade global do método;*
> 2. *O Pedro apresentará a validação do benchmark clássico de Silveira (2006) e a simulação dinâmica no Simulink com FFT;*
> 3. *O Renato abordará os ensaios práticos na bancada do motor elétrico CC e a interpretação física dos parâmetros;*
> 4. *E o Scarpini finalizará com a validação dinâmica temporal cega, as soluções para as dificuldades numéricas e as conclusões.*  
> *Vamos ao contexto da identificação."*

#### Slide 2: Contextualização: Domínio da Frequência vs. Tempo (1:15 min)
> *"A primeira decisão de projeto foi: por que optar pela identificação no domínio da frequência em vez dos métodos clássicos no tempo, como ARX ou Métodos do Erro de Predição (PEM)?*  
> *No domínio do tempo, ruídos estocásticos de alta frequência e condições iniciais não perfeitamente nulas introduzem viés sistemático nas matrizes de covariância.*  
> *Já no domínio da frequência, temos três grandes vantagens:*
> 1. *Concentração de energia apenas nas frequências úteis ensaiadas na planta;*
> 2. *Filtragem natural de ruídos fora da banda forçada;*
> 3. *Tratamento direto de atrasos de amostragem por defasagem angular linear.*  
> 
> *Além disso, algoritmos convencionais de otimização no domínio da frequência (como o Simplex de Nelder-Mead via `fminsearch` ou Levenberg-Marquardt) minimizam o erro de saída e frequentemente estagnam em **mínimos locais** ou divergem com chutes ruins.*  
> *A grande inovação do método **N2CACGO**, proposto por Silveira em 2006, é reformular o problema minimizando a **Norma 2 do Erro de Equação**. Isso torna a superfície de erro **estritamente convexa**, garantindo uma solução analítica global única e sem iterações!"*

#### Slide 3: Formulação Matemática do N2CACGO (1:30 min)
> *"Matematicamente, consideramos uma função de transferência linear arbitrária $G_e(s) = B(s)/A(s)$ de ordem $n$, onde o polinômio do denominador é mônico.*  
> *Para cada fasor medido experimentalmente $G(j\omega_i)$, definimos o erro de equação:*  
> $$e(j\omega_i) = A(j\omega_i) G(j\omega_i) - B(j\omega_i)$$  
> *O funcional de custo quadrático $J(\theta)$ é a soma dos módulos ao quadrado desses resíduos ponderados.*  
> *Ao aplicar a condição analítica de mínimo $\nabla_\theta J = 0$, as derivadas parciais desacoplam em um Sistema de Equações Lineares particionado:*  
> $$\begin{bmatrix} Q_1 & -Q_2 \\ Q_3 & -Q_4 \end{bmatrix} \begin{bmatrix} \alpha \\ \beta \end{bmatrix} = \begin{bmatrix} Y_1 \\ Y_2 \end{bmatrix} \implies Q\theta = Y$$  
> *Onde as matrizes $Q$ e vetores $Y$ são calculados diretamente pelas bases polinomiais $(j\omega_i)^{n-k}$ e pelos fasores medidos.*  
> *Assim, a solução ótima é calculada analiticamente por $\theta^* = Q^{-1} Y$. Não há busca iterativa nem risco de convergência local.*  
> 
> **Passagem de Bastão:**  
> *'Para apresentar como validamos essa teoria matricial contra o benchmark clássico da literatura e os testes no Simulink, passo a palavra agora para o Pedro Augusto.'*"*

---

### PARTE 2: PEDRO AUGUSTO (Slides 4 a 6 — ~3:30 min)

#### Slide 4: Item 3 - Benchmark Acadêmico de Silveira (2006) (1:15 min)
> *"Obrigado, João.*  
> *Para garantir a fidelidade absoluta da nossa rotina MATLAB (`identifica_N2CACGO.m`), nós a confrontamos contra os resultados tabelados na dissertação de mestrado de Silveira (2006), que ensaiou uma planta teórica de 7ª ordem.*  
> *Como podem observar na Tabela comparativa do slide, nossa implementação atingiu **100% de concordância** com os valores $J_1$ de Silveira para todas as ordens de 1 a 7.*  
> *Notem um comportamento físico fundamental: a partir da 4ª ordem, o custo de erro estaciona rigorosamente em $6,2903 \times 10^{-4}$ com $FIT = 99,99\%$. Isso prova numericamente que ordens acima de 4 são redundantes para a dinâmica da planta ensaiada.*  
> *Além disso, em sistemas sintéticos didáticos de 1ª a 3ª ordens gerados no MATLAB, nosso código alcançou $FIT = 100,00\%$ com resíduo analítico da ordem de precisão de máquina ($J \sim 10^{-14}$)."*

#### Slide 5: Item 4 - Simulação Dinâmica Simulink com Chirp e FFT (1:15 min)
> *"No Item 4, partimos para o ambiente temporal contínuo. Construímos no Simulink o modelo `modelo_item4.slx` com uma planta subamortecida de 2ª ordem:*  
> $$G_{\text{nom}}(s) = \frac{100}{s^2 + 4s + 100} \quad (\omega_n = 10\text{ rad/s}, \zeta = 0,20)$$  
> *Para excitar essa planta em todo o seu espectro sem distorcer o regime permanente, injetamos um sinal **Chirp senoidal linear** varrendo de $0,1\text{ Hz}$ até $15\text{ Hz}$ durante 20 segundos.*  
> *Configuramos o solver contínuo `ode4` (Runge-Kutta 4) com passo fixo de $1\text{ ms}$ ($f_s = 1000\text{ Hz}$), gerando 20.001 amostras temporais.*  
> *Aplicando a Transformada Rápida de Fourier (FFT) aos sinais de entrada $u(t)$ e saída $y(t)$, calculamos a resposta espectral como o quociente fasorial $G(j\omega_k) = Y(k)/U(k)$ em 126 frequências com alta coerência SNR."*

#### Slide 6: Item 4 - Validação do Modelo Identificado via FFT (1:00 min)
> *"Alimentando o algoritmo N2CACGO com esses 126 fasores para ordem $n=2$, recuperamos o modelo:*  
> $$G_{\text{id}}(s) = \frac{100,5}{s^2 + 4,249s + 100,5}$$  
> *Comparando com a planta nominal:*  
> * A frequência natural identificada foi de $10,02\text{ rad/s}$ — um erro de apenas **0,2%** em relação ao valor real de $10\text{ rad/s}$;*  
> * O ganho estático foi de $1,0003$ (erro de $0,03\%$);*  
> * O índice $FIT$ espectral global foi de **96,47%**, com RMSE de magnitude de $0,77\text{ dB}$ e fase de $8,69^{\circ}$.*  
> *A sutil diferença no amortecimento decorre do vazamento espectral (*spectral leakage*) inerente à FFT de janela finita, demonstrando a robustez do N2CACGO mesmo em dados discretizados.*  
> 
> **Passagem de Bastão:**  
> *'Agora que comprovamos a eficácia do método em simulação, passo a palavra ao Renato Felix para apresentar a identificação em bancada física real de um motor CC.'*"*

---

### PARTE 3: RENATO FELIX (Slides 7 e 8 — ~3:45 min)

#### Slide 7: Item 5 - Bancada Experimental do Motor Elétrico CC (1:30 min)
> *"Obrigado, Pedro.*  
> *Chegamos ao cerne experimental do nosso trabalho: a identificação física em bancada de laboratório de um motor elétrico CC acoplado a um tacômetro.*  
> *Gostaria de destacar o nosso **rigor metrológico**: utilizamos estritamente a base de ensaios do **Grupo 3**, contendo 26 ensaios senoidais puros cobrindo de $0,20\text{ Hz}$ a $10,0\text{ Hz}$. Nenhuma base externa foi misturada.*  
> *Para cada sinal experimental gravado, identificamos que os primeiros ciclos continham transitórios de partida da máquina. Por isso, programamos um filtro temporal que descartou os primeiros 40% das amostras, calculando a DFT fasorial estritamente sobre os últimos 60% das amostras (regime permanente forçado limpo).*  
> *Realizamos uma varredura de ordens de $n = 1$ a $n = 4$. O gráfico de Bode revela que modelos de ordem superior ($n \ge 2$) sofrem sobreajuste (*overfitting*) aos ruídos de comutação do tacômetro. Como a teoria clássica de motores CC com indutância desprezível prevê comportamento de 1ª ordem, selecionamos $n=1$."*

#### Slide 8: Item 5 - Parâmetros Físicos e Fenômeno de Padé do Atraso (2:15 min - Ponto Alto)
> *"O modelo analítico ótimo obtido pelo N2CACGO para o motor foi:*  
> $$G_{\text{motor}}(s) = \frac{-0,2468 s + 48,33}{s + 4,794}$$  
> *Deste modelo, extraímos os parâmetros físicos fundamentais da máquina:*  
> * **Ganho Estático de Velocidade:** $K_m = 48,33 / 4,794 = 10,08\text{ (rad/s)/V}$ ($20,07\text{ dB}$);*  
> * **Constante de Tempo Eletromecânica:** $\tau_m = 1 / 4,794 = 0,209\text{ segundos}$;*  
> * **Índice FIT Global:** $88,36\%$.*  
> 
> *Agora, chamamos a atenção da banca para uma questão física crucial:*  
> *Observem que o numerador possui um zero no semi-plano direito em $s = +195,8\text{ rad/s}$.*  
> *Isso significa que o motor é instável? **De forma alguma!***  
> *O motor é estável porque seu polo está no semi-plano esquerdo ($s = -4,794\text{ rad/s}$). Esse zero no semi-plano direito é a clássica **aproximação de Padé de 1ª ordem de um atraso puro de transporte** ($e^{-s\tau_d}$):*  
> $$e^{-s\tau_d} \approx \frac{1 - s \frac{\tau_d}{2}}{1 + s \frac{\tau_d}{2}} \implies \tau_d = \frac{2}{195,8} \approx 10,2\text{ milissegundos}$$  
> *Esses $10,2\text{ ms}$ traduzem com exatidão física o tempo combinado de conversão A/D, amostragem e comunicação da placa de aquisição!*  
> *É justamente esse atraso puro que faz com que a curva de fase experimental caia além de $-90^{\circ}$ nas frequências mais altas ($10\text{ Hz}$), validando a física do nosso modelo identificado.*  
> 
> **Passagem de Bastão:**  
> *'Para apresentar como validamos dinamicamente esse modelo no tempo contra ondas quadrada e triangular, as dificuldades numéricas e o fechamento, passo a palavra ao Arthur Scarpini.'*"*

---

### PARTE 4: ARTHUR SCARPINI (Slides 9 a 11 — ~4:00 min)

#### Slide 9: Item 5 - Validação Dinâmica Temporal Cega (1:15 min)
> *"Obrigado, Renato.*  
> *Para garantir que o modelo não fosse apenas um ajuste matemático de curvas no gráfico de Bode, nós o submetemos a uma validação temporal cega contra ensaios reais da bancada que não foram utilizados na identificação.*  
> *Aplicamos ao modelo identificado as mesmas entradas de **onda quadrada** e **onda triangular** a $10\text{ Hz}$ gravadas nos ensaios `sqrf` e `trif`.*  
> *Nos dois gráficos do slide, podemos ver a alta concordância dinâmica:*  
> * Na resposta à **onda quadrada**, o modelo simula fielmente as taxas exponenciais de subida e descida com ganho de velocidade perfeitamente alinhado com $\tau_m = 0,209\text{ s}$;*  
> * Na resposta à **onda triangular**, a inércia do rotor atua como um filtro passa-baixas natural, arredondando suavemente as cúspides triangulares com defasagem idêntica à do tacômetro físico.*  
> *Isso comprova a validade do modelo em regime transitório e permanente."*

#### Slide 10: Dificuldades Encontradas e Soluções de Engenharia (1:30 min)
> *"Durante a implementação dos 5 itens, superamos quatro grandes desafios de engenharia que merecem registro:*  
> 1. ***Condicionamento Numérico de $Q$ em Ordens Altas:***  
>    *Para ordens $n \ge 4$, as potências de frequência $(j\omega)^n$ atingem magnitude de $10^{14}$, fazendo o número de condição cair para $\text{rcond}(Q) < 10^{-16}$. Inicialmente, o uso da pseudoinversa `pinv` do MATLAB truncava autovalores pequenos indispensáveis, arruinando os resultados das ordens 4 a 7 ($J \approx 64$).*  
>    *Solução: Implementamos a divisão matricial direta (`Q \ Y`) via eliminação Gaussiana com pivoteamento parcial, preservando os autovetores dos monômios e recuperando o erro exato $J = 6,2903 \times 10^{-4}$ de Silveira.*  
> 2. ***Vazamento Espectral (Leakage) na FFT:***  
>    *Mitigado restringindo a faixa espectral útil ao intervalo com alta relação sinal-ruído ($1,0$ a $80,0\text{ rad/s}$).*  
> 3. ***Transitórios da Bancada:***  
>    *Eliminados pelo corte programático dos primeiros 40% das amostras temporais.*  
> 4. ***Conflito de Solvers no Simulink CLI:***  
>    *Parametrização automatizada com solver contínuo `ode4` de passo fixo para simulação em lote sem bloqueios."*

#### Slide 11: Conclusões Finais e Abertura para a Banca (1:15 min)
> *"Para concluir o nosso trabalho:*  
> * Cumprimos integralmente e com automação total os 5 itens propostos na disciplina;*  
> * O algoritmo N2CACGO foi implementado de forma analítica pura, reproduzindo Silveira (2006) com 100% de concordância nas tabelas;*  
> * A simulação Simulink com FFT alcançou $FIT = 96,47\%$ na recuperação da planta LTI de 2ª ordem;*  
> * E na bancada física do motor CC, identificamos os parâmetros eletromecânicos reais ($K_m = 10,08$, $\tau_m = 0,209\text{ s}$) e explicamos o fenômeno do atraso puro de Padé de $\approx 10,2\text{ ms}$;*  
> * Todo o projeto — scripts MATLAB, diagrama Simulink, artigo IEEE em PDF de 5 páginas e esta apresentação interativa — está publicado publicamente no nosso GitHub: `https://github.com/VPariz/masd-identificacao-n2cacgo`.*  
> 
> *Convido agora meus colegas João Victor, Pedro e Renato a se juntarem a mim.*  
> *Agradecemos a atenção do Prof. Marcelo e estamos prontos para as perguntas e considerações da banca!"*

---

## 👥 Guia de Divisão da Sabatina (Perguntas da Banca)

Para garantir que todos participem de forma equilibrada também durante as perguntas:

1. **Se o professor perguntar sobre a Matemática / Formulação Convexa / Erro de Equação:**  
   👉 **João Victor Pariz** assume a resposta (explica a norma 2 do resíduo de equação e por que o gradiente igual a zero gera o SEL analítico fechado $Q\theta = Y$).
2. **Se o professor perguntar sobre o Benchmark de Silveira / Ordens altas / Simulação Simulink e FFT:**  
   👉 **Pedro Augusto** assume a resposta (explica a Tabela 3.2, a saturação de $J$ a partir de $n=4$ e a extração espectral por quociente de FFT).
3. **Se o professor perguntar sobre o Motor CC / Por que Ordem 1 / O que significa o Zero no SPD:**  
   👉 **Renato Felix** assume a resposta (explica que o zero no semi-plano direito é a aproximação de Padé de 1ª ordem do atraso puro de transporte de $\approx 10,2\text{ ms}$ da amostragem/comunicação).
4. **Se o professor perguntar sobre Dificuldades Numéricas / Por que Gauss em vez de pinv / Validação Cega:**  
   👉 **Arthur Scarpini** assume a resposta (explica o problema de $\text{rcond}(Q) < 10^{-16}$, o truncamento da SVD pelo `pinv` e a preservação dos monômios por eliminação Gaussiana com pivoteamento).
