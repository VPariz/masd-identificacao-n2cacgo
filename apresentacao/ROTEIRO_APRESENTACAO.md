# Roteiro do Orador: Defesa do Trabalho de MASD (IME)
## Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO

**Autores:** João Victor Tavares Pariz, Pedro Augusto, Renato Felix, Arthur Scarpini  
**Orientador:** Prof. Dr. Marcelo de Araújo Oliveira  
**Tempo Estimado:** 12 a 15 minutos de apresentação + 5 minutos de arguição  

---

### Visão Geral da Apresentação

```
[Slide 01] Abertura & Apresentação da Equipe (1:00 min)
[Slide 02] Contexto & Motivação: Domínio da Frequência vs. Tempo (1:15 min)
[Slide 03] Formulação Matemática e Convexidade Global do N2CACGO (1:30 min)
[Slide 04] Item 3: Validação Teórica no Benchmark de Silveira (2006) (1:15 min)
[Slide 05] Item 4: Simulação Dinâmica Simulink com Chirp e FFT (1:15 min)
[Slide 06] Item 4: Validação do Modelo Identificado (1:00 min)
[Slide 07] Item 5: Bancada Experimental do Motor Elétrico CC (1:15 min)
[Slide 08] Item 5: Parâmetros Físicos e Fenômeno de Padé do Atraso (1:45 min)
[Slide 09] Item 5: Validação Dinâmica Temporal Cega (Onda Quadrada e Triangular) (1:15 min)
[Slide 10] Dificuldades Encontradas e Soluções de Engenharia (1:30 min)
[Slide 11] Conclusões e Disponibilização do Repositório Aberto (1:00 min)
```

---

## 🎙️ Guia de Fala Slide a Slide

### Slide 1: Capa & Apresentação da Equipe (1:00 min)
> *"Bom dia / boa tarde a todos, professor Marcelo e colegas.*  
> *Nosso grupo é composto por mim, João Victor Pariz, pelo Pedro Augusto, Renato Felix e Arthur Scarpini.*  
> *Hoje apresentamos o nosso trabalho final da disciplina de Modelagem e Análise de Sistemas Dinâmicos, intitulado: **'Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO'**.*  
> *O nosso objetivo foi cobrir toda a esteira de identificação: partindo da dedução algébrica analítica do método, passando pela validação teórica rigorosa do benchmark de Silveira (2006), seguindo para a simulação com sinais temporais e FFT no Simulink, e culminando na identificação física e validação cega em bancada real de um motor elétrico de corrente contínua."*

---

### Slide 2: Contexto & Motivação (1:15 min)
> *"Para iniciar, por que optamos pela identificação no domínio da frequência em vez dos métodos clássicos no domínio do tempo, como ARX ou Métodos do Erro de Predição (PEM)?*  
> *No domínio do tempo, ruídos estocásticos de alta frequência e condições iniciais não perfeitamente nulas introduzem viés sistemático nas matrizes de covariância.*  
> *Já no domínio da frequência, temos três grandes vantagens:*
> 1. *Concentração de energia apenas nas frequências úteis ensaiadas na planta;*
> 2. *Filtragem natural de qualquer ruído fora da faixa forçada;*
> 3. *Tratamento direto de atrasos puros de amostragem por defasagem angular linear.*  
> 
> *Além disso, algoritmos convencionais de ajuste no domínio da frequência (como o Simplex de Nelder-Mead via `fminsearch` ou Levenberg-Marquardt) minimizam o erro de saída e frequentemente estagnam em **mínimos locais** ou divergem.*  
> *A grande sacada do método **N2CACGO**, proposto por Silveira em 2006, é reformular o critério de custo utilizando a **Norma 2 do Erro de Equação**. Isso torna a superfície de erro **estritamente convexa**, garantindo uma solução ótima global analítica e direta."*

---

### Slide 3: Formulação Matemática do N2CACGO (1:30 min)
> *"Matematicamente, consideramos uma função de transferência linear arbitrária $G_e(s) = B(s)/A(s)$ de ordem $n$, onde o polinômio do denominador é mônico.*  
> *Para cada fasor medido experimentalmente $G(j\omega_i)$, definimos o erro de equação:*  
> $$e(j\omega_i) = A(j\omega_i) G(j\omega_i) - B(j\omega_i)$$  
> *O funcional de custo quadrático $J(\theta)$ é a soma dos módulos ao quadrado desses resíduos ponderados.*  
> *Ao aplicar a condição necessária e suficiente de mínimo $\nabla_\theta J = 0$, as derivadas em relação aos coeficientes do numerador $\alpha$ e do denominador $\beta$ desacoplam exatamente em um Sistema de Equações Lineares particionado:*  
> $$\begin{bmatrix} Q_1 & -Q_2 \\ Q_3 & -Q_4 \end{bmatrix} \begin{bmatrix} \alpha \\ \beta \end{bmatrix} = \begin{bmatrix} Y_1 \\ Y_2 \end{bmatrix}$$  
> *Onde as matrizes $Q$ e vetores $Y$ são calculados diretamente pelas bases polinomiais $(j\omega_i)^{n-k}$ e pelos fasores medidos.*  
> *Assim, o vetor de parâmetros ótimo é dado por $\theta^* = Q^{-1} Y$. Não há iterações, não há chute inicial e a convergência para o mínimo global é instantânea."*

---

### Slide 4: Item 3 - Validação Teórica: Silveira (2006) (1:15 min)
> *"Para validar a exatidão matemática do nosso código MATLAB (`identifica_N2CACGO.m`), executamos o Item 3 reproduzindo o benchmark clássico de 7ª ordem da dissertação de Silveira (2006).*  
> *Na tabela projetada, comparamos os custos $J$ obtidos pela nossa rotina com os valores $J_1$ tabelados por Silveira para ordens de 1 a 7.*  
> *Como podem notar, a concordância foi de **100% em todas as ordens**, com 4 casas decimais exatas.*  
> *Observem um fato fundamental da teoria: a partir da 4ª ordem, o custo estabiliza em $6,2903 \times 10^{-4}$ com $FIT = 99,99\%$. Isso demonstra numericamente que ordens superiores são redundantes para descrever a dinâmica dominante dessa planta.*  
> *Além disso, testamos sistemas didáticos de 1ª, 2ª e 3ª ordens gerados sinteticamente, onde nosso algoritmo alcançou $FIT = 100,00\%$ e custo analítico da ordem de máquina de $10^{-14}$."*

---

### Slide 5: Item 4 - Simulação Dinâmica Simulink com Chirp e FFT (1:15 min)
> *"No Item 4, passamos para o ambiente dinâmico temporal. Criamos um modelo no Simulink (`modelo_item4.slx`) contendo uma planta subamortecida de 2ª ordem:*  
> $$G_{\text{nom}}(s) = \frac{100}{s^2 + 4s + 100} \quad (\omega_n = 10\text{ rad/s}, \zeta = 0,20)$$  
> *Para excitar a planta em múltiplas frequências simultaneamente sem distorcer o regime, injetamos um **Chirp senoidal linear** varrendo de $0,1\text{ Hz}$ até $15\text{ Hz}$ ao longo de 20 segundos.*  
> *A simulação foi configurada com solver contínuo `ode4` (Runge-Kutta 4) e taxa de amostragem fixa de $1000\text{ Hz}$, gerando 20.001 amostras.*  
> *A partir das séries temporais de entrada $u(t)$ e saída $y(t)$, aplicamos a FFT e extraímos a resposta em frequência como o quociente fasorial $G(j\omega_k) = Y(k)/U(k)$ em 126 frequências com alta relação sinal-ruído."*

---

### Slide 6: Item 4 - Validação do Modelo Identificado (1:00 min)
> *"Com os 126 pares fasoriais extraídos via FFT, alimentamos o estimador N2CACGO configurado para 2ª ordem.*  
> *O modelo recuperado foi:*  
> $$G_{\text{id}}(s) = \frac{100,5}{s^2 + 4,249s + 100,5}$$  
> *Vejam a precisão:*  
> * A frequência natural identificada foi de $10,02\text{ rad/s}$ — um erro de apenas **0,2%** em relação ao valor nominal de $10\text{ rad/s}$;*  
> * O ganho estático DC foi de $1,0003$ (erro de $0,03\%$);*  
> * O $FIT$ espectral global foi de **96,47%**, com erro médio de módulo de $0,77\text{ dB}$ e fase de $8,69^{\circ}$.*  
> *A discreta diferença no fator de amortecimento ($\zeta = 0,212$ vs $0,200$) decorre do janelamento espectral (*spectral leakage*) inevitável da FFT finita, demonstrando a robustez do N2CACGO em dados ruidosos."*

---

### Slide 7: Item 5 - Aplicação Experimental: Bancada do Motor CC (1:15 min)
> *"Entramos agora no ponto alto do trabalho: a identificação física em bancada de laboratório.*  
> *Aqui mantivemos rigor metrológico absoluto: **utilizamos exclusivamente a base de dados do Grupo 3**, composta por 26 ensaios senoidais puros cobrindo de $0,20\text{ Hz}$ até $10,0\text{ Hz}$. Nenhuma base externa foi misturada.*  
> *Para cada arquivo experimental, expurgamos os primeiros 40% das amostras temporais para eliminar os transitórios de partida do motor e tacômetro. A Transformada Discreta de Fourier (DFT) foi calculada estritamente sobre os últimos 60% das amostras, garantindo fasores limpos em regime permanente forçado.*  
> *Realizamos uma varredura de ordens de $n = 1$ a $n = 4$. O gráfico de Bode mostra que ordens maiores sofrem sobreajuste (*overfitting*) aos ruídos de comutação do tacômetro. Por isso, selecionamos o modelo de 1ª ordem, compatível com as leis eletromecânicas fundamentais de motores CC."*

---

### Slide 8: Item 5 - Parâmetros Físicos e Atraso de Padé (1:45 min - Atenção Especial)
> *"O modelo identificado pelo N2CACGO para o motor foi:*  
> $$G_{\text{motor}}(s) = \frac{-0,2468 s + 48,33}{s + 4,794}$$  
> *Extraindo os parâmetros físicos fundamentais da engenharia:*  
> * **Ganho Estático de Velocidade:** $K_m = 48,33 / 4,794 = 10,08\text{ (rad/s)/V}$ ($20,07\text{ dB}$);*  
> * **Constante de Tempo Eletromecânica:** $\tau_m = 1 / 4,794 = 0,209\text{ segundos}$;*  
> * **Índice FIT Global:** $88,36\%$.*  
> 
> *Agora, chamamos atenção para uma questão física fundamental que costuma intrigar em bancadas reais:*  
> *O modelo apresenta um zero no semi-plano direito em $s = +195,8\text{ rad/s}$.*  
> *Isso significa que a bancada é instável? **Não!***  
> *Um zero no SPD em sistemas de bancada é a clássica **aproximação de Padé de 1ª ordem de um atraso puro de transporte** ($e^{-s\tau_d}$):*  
> $$e^{-s\tau_d} \approx \frac{1 - s \frac{\tau_d}{2}}{1 + s \frac{\tau_d}{2}} \implies \tau_d = \frac{2}{195,8} \approx 10,2\text{ milissegundos}$$  
> *Esses $10,2\text{ ms}$ representam exatamente o atraso combinado de amostragem do conversor A/D e o tempo de comunicação da placa de aquisição!*  
> *É esse atraso de transporte que faz com que a fase experimental caia além de $-90^{\circ}$ em altas frequências ($10\text{ Hz}$), validando a física do nosso modelo identificado."*

---

### Slide 9: Item 5 - Validação Dinâmica Temporal Cega (1:15 min)
> *"Para comprovar que o modelo não apenas ajustou pontos de frequência, mas realmente capturou a dinâmica do motor, submetemos o modelo linear a um teste cego:*  
> *Injetamos nos modelos as mesmas entradas experimentais de **onda quadrada** e **onda triangular** a $10\text{ Hz}$ gravadas na bancada (arquivos `sqrf` e `trif`).*  
> *Os resultados nos dois gráficos são evidentes:*  
> * Na resposta à **onda quadrada**, o modelo simula com precisão a taxa exponencial de subida e descida compatível com $\tau_m = 0,209\text{ s}$ e ganho estático concordante;*  
> * Na resposta à **onda triangular**, o polo mecânico atua como um filtro passa-baixas natural, arredondando as pontas agudas com sincronismo de fase e defasagem exatamente iguais às medidas pelo sensor.*  
> *Isso conclui a validação cruzada tempo-frequência do motor."*

---

### Slide 10: Dificuldades Encontradas e Soluções de Engenharia (1:30 min)
> *"Durante o desenvolvimento, enfrentamos quatro grandes desafios de engenharia:*  
> 1. ***Condicionamento Numérico de $Q$ em Ordens Altas:***  
>    *Para ordens $n \ge 4$, as potências $(j\omega)^n$ atingem magnitudes de $10^{14}$, fazendo com que $\text{rcond}(Q) < 10^{-16}$. O uso do comando padrão `pinv` do MATLAB truncava autovalores pequenos essenciais, corrompendo as ordens 4 a 7 ($J \approx 64$).*  
>    *Solução: Adotamos divisão matricial direta (`Q \ Y`) por eliminação Gaussiana com pivoteamento parcial, preservando os autovetores dos monômios e obtendo o valor exato $J = 6,2903 \times 10^{-4}$ de Silveira.*  
> 2. ***Vazamento Espectral (Leakage) na FFT:***  
>    *Contornado limitando a faixa de cálculo às frequências com alta coerência SNR ($1,0$ a $80,0\text{ rad/s}$).*  
> 3. ***Transitórios de Bancada:***  
>    *Corte dos primeiros 40% das amostras para cálculo dos fasores em regime permanente estrito.*  
> 4. ***Conflito de Solvers no Simulink:***  
>    *Configuração programática do solver contínuo `ode4` de passo fixo para simulação em lote via linha de comando."*

---

### Slide 11: Conclusões e Repositório Aberto (1:00 min)
> *"Concluindo a nossa apresentação:*  
> * Cumprimos integralmente todos os 5 itens exigidos no edital do trabalho;*  
> * O código N2CACGO foi implementado de forma analítica pura e validado contra Silveira (2006) com $99,99\%$ de precisão;*  
> * O modelo identificado para o motor CC foi explicado fisicamente através da constante eletromecânica e do atraso de Padé de $10,2\text{ ms}$;*  
> * Todo o projeto foi automatizado pelo script mestre `executa_todos_itens.m` e está versionado e publicado publicamente no GitHub: `https://github.com/VPariz/masd-identificacao-n2cacgo`.*  
> *Agradecemos a atenção do professor e da turma e estamos abertos para perguntas!"*

---

## ❓ Perguntas Frequentes da Banca e Como Responder

### Pergunta 1: *"Por que vocês escolheram ordem 1 para o motor se a ordem 2 ou 3 poderiam ter um custo menor?"*
> **Resposta:** *"O motor elétrico CC acoplado a uma carga puramente inercial é teoricamente governado por uma equação diferencial de 1ª ordem na velocidade angular quando a indutância de armadura $L_a$ é desprezível (ou seja, $\tau_e \ll \tau_m$). Ao testarmos ordens 2 e 3, observamos que os polos adicionais foram alocados em frequências muito altas ou se cancelaram com zeros espúrios, ajustando-se apenas ao ruído de comutação do tacômetro. O modelo de 1ª ordem preserva significado físico com $\tau_m = 0,209\text{ s}$ e $K_m = 10,08\text{ (rad/s)/V}$, com $FIT = 88,36\%$."*

### Pergunta 2: *"Esse zero positivo no motor ($s = +195,8\text{ rad/s}$) não deixaria o sistema instável?"*
> **Resposta:** *"Não, professor. O sistema é SISO e a estabilidade em malha aberta depende exclusivamente dos polos (raízes do denominador), que estão todos no semi-plano esquerdo ($s = -4,794\text{ rad/s}$). Um zero no semi-plano direito torna o sistema de **não-fase mínima**. Na prática de controle e identificação em bancada, isso representa a aproximação linear de Padé de 1ª ordem do atraso puro de transporte da placa de aquisição e conversor A/D ($\tau_d = 2/195,8 \approx 10,2\text{ ms}$). É esse atraso que introduz defasagem negativa linear adicional na alta frequência sem alterar o módulo."*

### Pergunta 3: *"Por que o método N2CACGO garante o mínimo global enquanto o Nelder-Mead (fminsearch) não garante?"*
> **Resposta:** *"Porque o N2CACGO minimiza o erro de equação $e(j\omega) = A(j\omega)G(j\omega) - B(j\omega)$. Como tanto $A(s)$ quanto $B(s)$ são lineares nos parâmetros $\alpha$ e $\beta$, a norma 2 desse erro é uma função estritamente quadrática e convexa em relação a $\theta$. O gradiente $\nabla_\theta J = 0$ resulta em um sistema de equações lineares único $Q\theta = Y$. Já o erro de saída $(G - B/A)$ é não-linear e não-convexo devido a $A(s)$ no denominador, gerando múltiplos mínimos locais e dependência crítica do chute inicial."*
