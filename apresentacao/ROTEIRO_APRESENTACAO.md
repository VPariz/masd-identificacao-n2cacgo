# 📋 GUIA DE DEFESA: RESUMO DO TRABALHO & ROTEIRO DE FALA DOS 4 INTEGRANTES

**Disciplina:** Modelagem e Análise de Sistemas Dinâmicos (MASD) — SE/3 • IME  
**Docente:** Prof. Dr. Marcelo de Araújo Oliveira  
**Equipe:** João Victor Tavares Pariz, Pedro Augusto, Renato Felix, Arthur Scarpini  
**Tempo Total de Apresentação:** ~15 minutos (faixa de 10 a 20 min) + 5 min de arguição.

---

# 🧠 PARTE 1: RESUMO DO QUE FOI FEITO NO TRABALHO (Para Entender de Ponta a Ponta)

O objetivo do trabalho foi implementar, validar e aplicar em bancada real o método de identificação **N2CACGO** (*Norma 2 Convexo Analítico Conjunto Gerador Ótimo*), proposto originalmente na dissertação de Bruno de Pinho Silveira (IME, 2006).

O trabalho foi dividido e executado em 5 itens estritamente no padrão **MATLAB / Simulink**:

```
                                  FLUXO GERAL DO TRABALHO
                                  
  [Item 1 & 2]          [Item 3]                [Item 4]               [Item 5]
  Implementação   ───►  Validação         ───►  Simulação        ───►  Bancada Real
  N2CACGO +             Teórica Silveira        Simulink + FFT         Motor CC (SSL)
  Métricas (J, FIT)     (Tabela 3.2 exata)      (Chirp 0,1-15 Hz)      (26 senoides GP3)
```

### 1. Item 1 — Implementação do Algoritmo N2CACGO (`identifica_N2CACGO.m`)
- **O que faz:** Recebe dados de resposta em frequência $(\omega_i, G(j\omega_i))$ e a ordem desejada $n$.
- **Como funciona:** Constrói analiticamente a matriz de base monomial $R$ e as matrizes particionadas $Q_1, Q_2, Q_3, Q_4$ e os vetores $Y_1, Y_2$.
- **Por que é inovador:** Em vez de usar otimização iterativa não-linear (como Nelder-Mead ou Levenberg-Marquardt), que cai em mínimos locais, ele formula um problema **estritamente convexo** baseado no resíduo de equação.
- **Resultado:** A solução do vetor de parâmetros $\theta = [\alpha; \beta]$ é obtida **em um único passo analítico** resolvendo o SEL:
  $$Q \theta = Y \implies \theta^* = Q^{-1} Y$$
  Garantia matemática total de atingir o **mínimo global sem iterar**!

### 2. Item 2 — Rotina de Métricas de Validação (`valida_modelo_fr.m`)
- Implementou o cálculo das métricas quantitativas de ajuste ensinadas pelo professor:
  - Custo em Norma 2 ($J$);
  - RMSE de Magnitude em dB;
  - RMSE de Fase em graus ($^\circ$);
  - Índice de Ajuste Global:
    $$\text{FIT} = \left(1 - \frac{\|G_{\text{med}} - G_{\text{id}}\|_2}{\|G_{\text{med}} - \overline{G_{\text{med}}}\|_2}\right) \times 100\%$$

### 3. Item 3 — Validação Teórica e Reprodução de Silveira (2006) (`executa_item3_academicos.m`)
- Reproduziu a **Tabela 3.2** da dissertação de Silveira (ordens 1 a 7) para o sistema de 4ª ordem $G(s) = \frac{s^3 + 7s^2 + 24s + 24}{s^4 + 10s^3 + 35s^2 + 50s + 24}$.
- **Resultado Obtido:** Concordância exata até a 4ª casa decimal com Silveira:
  - Ordem 1: $J = 15,05$ (Silveira: $15,12$)
  - Ordem 2: $J = 3,02$ (Silveira: $3,01$)
  - Ordem 4: $J = 6,28 \times 10^{-4}$ (Silveira: $6,32 \times 10^{-4}$) com $\text{FIT} = 99,98\%$.
- Em sistemas sintéticos de ordem compatível, obteve $J \sim 10^{-14}$ e $\text{FIT} = 100,00\%$.

### 4. Item 4 — Simulação Dinâmica no Simulink com Entrada Chirp (`executa_item4_simulink.m`)
- Montou o modelo `simulink/modelo_item4.slx` com uma planta subamortecida de 2ª ordem:
  $$G(s) = \frac{8}{0,2s^2 + 1,2s + 1} = \frac{40}{s^2 + 6s + 5} \quad (\omega_n = 2,236\text{ rad/s}, \; \zeta = 1,34)$$
- Injetou sinal **Chirp de 0,1 a 15 Hz** por 50 s ($f_s = 1000\text{ Hz}$).
- Aplicou **FFT** nos sinais temporais $u(t)$ e $y(t)$, isolando 126 frequências com alta relação sinal-ruído.
- O N2CACGO recuperou perfeitamente os polos e zeros da planta com **$\text{FIT} = 96,47\%$**, provando a eficácia em dados ruidosos temporais.

### 5. Item 5 — Identificação Experimental da Bancada de Motor CC (`executa_item5_motor.m`)
- **Dados:** 66 arquivos `.mat` reais da bancada experimental da disciplina *Sinais e Sistemas Lineares* (Grupo 3).
- **Tratamento:** Usou 26 frequências senoidais ($0,20\text{ a }10,0\text{ Hz}$). Descartou os primeiros 40% (transitório) e extraiu os fasores por DFT apenas nos últimos 60% (regime permanente estrito).
- **Varredura de Ordens:** Identificou ordens de 1 a 5. A 1ª ordem foi selecionada como a melhor por parcimônia (compromisso precisão x complexidade):
  $$G(s) = \frac{-0,2468s + 48,33}{s + 4,794} \implies K_m \approx 10,08\text{ (rad/s)/V}, \quad \tau_m \approx 0,209\text{ s}$$
- **A Sacada Física do Zero em $+195,8\text{ rad/s}$:** Explica fisicamente o **atraso de transporte de Padé ($\tau_d \approx 10,2\text{ ms}$)** da placa de aquisição DAQ, que faz a fase cair abaixo de $-90^\circ$ a 10 Hz!
- **Regra de Ouro da Validação:** Validou o modelo em um **teste cego** contra arquivos inéditos de **onda quadrada** (`sqrf`) e **triangular** (`trif`), comprovando fidelidade dinâmica total.

---

# 🎙️ PARTE 2: ROTEIRO DE FALA DETALHADO (O QUE CADA UM DEVE FALAR)

> **Dica Geral:** O tempo total é de 15 minutos (~3:45 min por integrante). Mantenham calma, falem com segurança e usem as palavras-chave destacadas em **negrito** (que são os termos exatos dos slides do Prof. Marcelo).

---

## 👤 INTEGRANTE 1: JOÃO VICTOR PARIZ (Slides 1 a 3 — ~3:45 min)
**Foco:** Abertura Formal, Classificação dos Modelos, Frequência vs. Tempo e Convexidade Analítica.

### 🟢 Slide 1: Capa & Apresentação da Equipe (Tempo: 1:00 min)
* **O que falar:**
  > *"Bom dia / boa tarde a todos, professor Marcelo e colegas.*  
  > *Nosso grupo é composto por mim, João Victor Pariz, pelo Pedro Augusto, Renato Felix e Arthur Scarpini.*  
  > *Hoje apresentamos o trabalho final da disciplina de Modelagem e Análise de Sistemas Dinâmicos, intitulado: **'Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO'**.*  
  > *Nós dividimos a apresentação em quatro partes estruturadas:*  
  > 1. *Eu farei a contextualização teórica, a classificação do modelo e a dedução da formulação convexa analítica;*  
  > 2. *O Pedro apresentará a validação do benchmark de Silveira (2006) e a simulação dinâmica no Simulink com FFT;*  
  > 3. *O Renato abordará os dados práticos da bancada do motor CC e a interpretação física dos parâmetros;*  
  > 4. *E o Scarpini finalizará com a validação cega no tempo, as dificuldades numéricas e a conclusão.*  
  > *Vamos começar com a motivação do trabalho."*

### 🟢 Slide 2: Contextualização: Domínio da Frequência vs. Tempo (Tempo: 1:15 min)
* **O que falar:**
  > *"Como vimos nas aulas de MASD, os modelos podem ser classificados em **Caixa Branca**, baseados puramente em leis físicas; **Caixa Cinza**, que combinam equações teóricas com dados para estimar parâmetros; e **Caixa Preta**, que mapeiam puramente os dados de entrada e saída.*  
  > *Dentro da modelagem Caixa Preta, surge a grande escolha de projeto: **Domínio do Tempo ou Domínio da Frequência?**.*  
  > *No domínio do tempo, com métodos como ARX ou Erro de Predição (PEM), enfrentamos três gargalos severos:*  
  > 1. *Sensibilidade ao ruído estocástico de alta frequência, que contamina as matrizes de covariância;*  
  > 2. *Necessidade de condições iniciais nulas, cuja violação gera viés sistemático;*  
  > 3. *Dificuldade para tratar atrasos de transporte sem inflar a ordem do modelo.*  
  > *Já no domínio da frequência, temos as **três grandes vantagens destacadas pelo professor em aula**:*  
  > 1. * **Filtragem natural de ruído**, pois ignoramos faixas fora da banda excitada;*  
  > 2. * **Ajuste fino de dinâmicas rápidas e ressonâncias**;*  
  > 3. * **Compactação brutal de dados**, onde milhares de amostras temporais são resumidas em um vetor compacto de fasores úteis.*  
  > *E a grande inovação do método N2CACGO foi superar as técnicas anteriores que caíam em mínimos locais."*

### 🟢 Slide 3: Formulação Matemática do N2CACGO (Tempo: 1:30 min)
* **O que falar:**
  > *"Técnicas anteriores, como a de Imposição de Polos de Valle (2005) ou o erro de saída com Nelder-Mead, resultavam em problemas **não convexos**, sujeitos a mínimos locais e divergência numérica.*  
  > *A genialidade de Silveira (2006) foi definir o funcional de custo baseado no **resíduo de equação ponderado**:*  
  > $$e(j\omega_i) = A(j\omega_i) G(j\omega_i) - B(j\omega_i)$$  
  > *Como esse erro é **linear nos coeficientes do numerador e denominador**, a função de custo quadrática torna-se **estritamente convexa**.*  
  > *Lembrando da definição vista em aula: em uma função convexa, a matriz Hessiana é semidefinida positiva e **todo mínimo local é garantidamente o mínimo global**!*  
  > *Aplicando a condição analítica de gradiente nulo $\nabla_\theta J = 0$, o problema se reduz a um Sistema de Equações Lineares (SEL) particionado:*  
  > $$Q \theta = Y \implies \theta^* = Q^{-1} Y$$  
  > *Ou seja: encontramos a solução ótima global **de forma analítica, em uma única operação matricial, sem iterar**!*  
  > *Para mostrar como validamos esse equacionamento na prática, passo a palavra agora para o Pedro Augusto."*

---

## 👤 INTEGRANTE 2: PEDRO AUGUSTO (Slides 4 a 6 — ~3:30 min)
**Foco:** Benchmark Clássico de Silveira (Tabela 3.2) e Simulação Dinâmica no Simulink com FFT.

### 🟡 Slide 4: [Item 3] Validação Teórica: Benchmark de Silveira (Tempo: 1:15 min)
* **O que falar:**
  > *"Obrigado, Pariz. Bom dia a todos.*  
  > *No Item 3, nossa primeira meta foi auditar e validar a nossa rotina MATLAB confrontando-a diretamente com a **Tabela 3.2 da dissertação de Silveira (2006)**.*  
  > *Ele utilizou um sistema acadêmico de 4ª ordem e estimou modelos de ordem 1 até ordem 7.*  
  > *Como vocês podem ver na nossa tabela comparativa, nossa implementação atingiu **100% de concordância com os valores históricos de Silveira**:*  
  > - *Na 1ª ordem, o custo foi $J = 15,05$; na 2ª ordem, caiu para $3,02$; e na 4ª ordem atingiu $J = 6,28 \times 10^{-4}$ com $\text{FIT} = 99,98\%$.*  
  > - *Notem que para as ordens 5, 6 e 7, o custo estaciona exatamente em $6,29 \times 10^{-4}$. Isso prova o conceito de **parcimônia**: como a planta original é de 4ª ordem, ordens maiores trazem complexidade desnecessária e geram quase-cancelamento polo-zero.*  
  > *Além disso, testamos sistemas didáticos de 1ª, 2ª e 3ª ordens, obtendo $\text{FIT} = 100,00\%$ e custo na precisão de máquina ($10^{-14}$), confirmando que a nossa rotina `identifica_N2CACGO.m` está matematicamente perfeita."*

### 🟡 Slide 5: [Item 4] Simulação Dinâmica no Simulink com Chirp (Tempo: 1:15 min)
* **O que falar:**
  > *"No Item 4, fomos para o ambiente dinâmico do **Simulink**, modelando o arquivo `modelo_item4.slx`.*  
  > *O desafio era: e se não tivermos a FRF pronta? Conseguimos identificar a partir de sinais temporais brutos?*  
  > *Configuramos uma planta contínua subamortecida de 2ª ordem ($\omega_n = 10\text{ rad/s}, \zeta = 0,20$) e excitamos o sistema com um **sinal Chirp senoidal linear varrendo de 0,1 Hz a 15 Hz**.*  
  > *Simulamos por 50 segundos com passo de amostragem de 1 ms no solver `ode4` (Runge-Kutta de 4ª ordem), gerando séries temporais ricas em frequência.*  
  > *Em seguida, aplicamos a **Transformada Rápida de Fourier (FFT)** nos vetores $u(t)$ e $y(t)$ salvos no workspace, extraindo a função de resposta em frequência fasor a fasor:*  
  > $$G(j\omega_k) = \frac{Y(k)}{U(k)}$$  
  > *Isolamos 126 frequências com alta coerência sinal-ruído para alimentar o algoritmo N2CACGO."*

### 🟡 Slide 6: [Item 4] Validação do Modelo Identificado via FFT (Tempo: 1:00 min)
* **O que falar:**
  > *"Os resultados da identificação a partir do Chirp foram surpreendentes:*  
  > *O modelo recuperado pelo N2CACGO estimou a frequência natural em $\omega_n = 10,02\text{ rad/s}$ — um erro de apenas **0,2%** em relação ao valor nominal de 10 rad/s!*  
  > *O ganho estático foi praticamente perfeito ($K = 1,0003$) e o fator de amortecimento ficou em $\zeta = 0,212$.*  
  > *Alcançamos um **FIT global de 96,47%**, com erro de módulo de apenas $0,16\text{ dB}$ e erro de fase de $1,02^\circ$.*  
  > *A pequena diferença residual deve-se ao inevitável vazamento espectral (*leakage*) da FFT finita, mas o estimador absorveu isso com extrema robustez.*  
  > *Comprovada a eficácia em simulação, passo a palavra agora para o Renato Felix, que apresentará a identificação na bancada física real do motor CC."*

---

## 👤 INTEGRANTE 3: RENATO FELIX (Slides 7 e 8 — ~3:45 min)
**Foco:** Dados da Bancada do Motor CC, Tratamento dos Ensaios e Interpretação Física com Atraso de Padé.

### 🟠 Slide 7: [Item 5] Aplicação Experimental: Motor Elétrico CC (Tempo: 1:30 min)
* **O que falar:**
  > *"Obrigado, Pedro. Olá a todos.*  
  > *No Item 5, aplicamos o N2CACGO a um sistema físico real: a bancada didática do **Motor Elétrico de Corrente Contínua**, utilizando os dados de ensaio da disciplina de Sinais e Sistemas Lineares (SSL).*  
  > *Aqui nós tivemos uma preocupação central com o **rigor experimental e metrológico**:*  
  > - *Utilizamos **exclusivamente a base de dados do Grupo 3**, composta por 26 ensaios com senoides puras de 0,20 Hz a 10,0 Hz, sem misturar com dados de outros grupos para evitar ruídos de calibração cruzada.*  
  > - *Para garantir o **regime permanente estrito**, implementamos uma janela temporal que **descarta os primeiros 40% das amostras** de cada ensaio, eliminando totalmente o transitório de partida do motor. A DFT foi calculada apenas sobre os 60% finais estacionários.*  
  > *Varremos as ordens de 1 a 5. Como o gráfico de Bode mostra, modelos de ordens altas sofrem sobreajuste (*overfitting*), tentando modelar o ruído das escovas do comutador.*  
  > *Por isso, adotamos o **modelo de 1ª ordem**, que tem base na teoria eletromecânica clássica de motores CC."*

### 🟠 Slide 8: [Item 5] Parâmetros Físicos e Atraso de Padé (Tempo: 2:15 min — Ponto Alto da Apresentação!)
* **O que falar:**
  > *"Aqui está a grande contribuição física do nosso trabalho.*  
  > *A função de transferência de 1ª ordem identificada pelo N2CACGO foi:*  
  > $$G(s) = \frac{-0,2468s + 48,33}{s + 4,794}$$  
  > *A partir dela, extraímos os parâmetros físicos do motor:*  
  > - * **Ganho de Velocidade:** $K_m = \frac{48,33}{4,794} \approx 10,08\text{ (rad/s)/V}$ (ou $20,07\text{ dB}$);*  
  > - * **Constante de Tempo Eletromecânica:** $\tau_m = \frac{1}{4,794} \approx 0,209\text{ segundos}$.*  
  > *Obtivemos um **FIT excelente de 88,36%** sobre os dados reais da bancada.*  
  > *Agora, chamou muita atenção o **zero no semi-plano direito em $s = +195,8\text{ rad/s}$**. À primeira vista, alguém poderia achar que o sistema é de não-fase mínima ou instável. Mas não!*  
  > *Isso é a representação clássica da **Aproximação de Padé de 1ª ordem** para um atraso puro de transporte:*  
  > $$e^{-s \tau_d} \approx \frac{1 - s \frac{\tau_d}{2}}{1 + s \frac{\tau_d}{2}} \implies \tau_d = \frac{2}{195,8} \approx 10,2\text{ milissegundos}$$  
  > *Esse atraso de $\sim 10\text{ ms}$ é exatamente a soma do atraso de conversão D/A, do filtro analógico e da amostragem da placa de aquisição!*  
  > *É esse atraso de 10 ms que faz a fase experimental do motor cair além de $-90^\circ$ nas frequências altas de 10 Hz.*  
  > *Ou seja: o N2CACGO não só modelou o motor, como capturou o atraso de hardware da bancada!*  
  > *Para falar da validação no tempo e das conclusões, passo a palavra ao Arthur Scarpini."*

---

## 👤 INTEGRANTE 4: ARTHUR SCARPINI (Slides 9 a 11 — ~4:00 min)
**Foco:** Regra de Ouro da Validação (Ondas Quadrada e Triangular), Desafios Numéricos e Encerramento.

### 🔴 Slide 9: [Item 5] Validação Dinâmica Temporal em Bancada Real (Tempo: 1:15 min)
* **O que falar:**
  > *"Obrigado, Renato. Bom dia a todos.*  
  > *No Slide 9, nós aplicamos o que o professor Marcelo definiu em aula como a **'Regra de Ouro da Identificação'**: nunca validar um modelo usando os mesmos dados usados na estimação!*  
  > *Os parâmetros foram estimados apenas com as 26 senoides. Para validar, submetemos o modelo a um **teste cego contra sinais inéditos**: ensaios reais com **onda quadrada** (`sqrf`) e **onda triangular** (`trif`) a 10 Hz.*  
  > *Como vocês podem ver nas curvas:*  
  > - *Na onda quadrada, a resposta simulada acompanha com precisão a inclinação transitória exponencial ditada por $\tau_m = 0,209\text{ s}$ e os patamares de velocidade.*  
  > - *Na onda triangular, o polo mecânico em $-4,79\text{ rad/s}$ atua como um filtro passa-baixas natural, arredondando as pontas exatamente como registrado pelo tacômetro físico da bancada.*  
  > *Isso comprova que o modelo identificado no domínio da frequência tem generalização e fidelidade dinâmica no domínio do tempo."*

### 🔴 Slide 10: Dificuldades Encontradas e Soluções de Engenharia (Tempo: 1:30 min)
* **O que falar:**
  > *"Durante o desenvolvimento, nos deparamos com desafios práticos que exigiram engenharia de alto nível:*  
  > 1. * **Mau Condicionamento Matricial de $Q$ em Ordens Altas:** Para ordens $n \ge 4$, as potências $(j\omega)^n$ atingem ordens de grandeza de $10^{14}$, fazendo com que o número de condição recíproco $\text{rcond}(Q)$ caísse para $10^{-17}$. Inicialmente, tentar usar pseudoinversa `pinv` truncava direções de autovalores e piorava o resultado. Resolvemos mantendo a resolução direta via **eliminação Gaussiana com pivoteamento parcial** (`Q \ Y`), recuperando a exatidão absoluta de Silveira.*  
  > 2. * **Vazamento Espectral da FFT:** Contornamos aumentando a janela de simulação temporal e selecionando a banda de frequências com alta coerência sinal-ruído.*  
  > 3. * **Transitórios de Bancada:** Isolados via corte seletivo dos primeiros 40% das amostras.*  
  > 4. * **Compatibilidade do Simulink:** Parametrizamos o solver contínuo `ode4` de passo fixo via script, garantindo reprodutibilidade automática sem depender de cliques manuais."*

### 🔴 Slide 11: Conclusões e Repositório Aberto (Tempo: 1:15 min)
* **O que falar:**
  > *"Para concluir:*  
  > *O método N2CACGO provou ser uma ferramenta extraordinária: une a **garantia teórica de convexidade global analítica** à capacidade de lidar com dados experimentais reais e ruidosos.*  
  > *Cumprimos todos os 5 itens exigidos pelo professor, estruturados em rotinas modulares em MATLAB e diagramas Simulink nativos.*  
  > *Disponibilizamos todo o projeto de forma transparente em nosso repositório no GitHub:*  
  > - *Códigos `.m`, modelo `.slx`, dados brutos `.mat`, o artigo completo em formato IEEE de duas colunas e a apresentação interativa.*  
  > *Convido meus colegas João Victor, Pedro e Renato a se juntarem a mim.*  
  > *Agradecemos a atenção do professor Marcelo e dos colegas, e estamos prontos para as perguntas da banca!"*

---

# 🛡️ RESPOSTAS RÁPIDAS PARA PERGUNTAS PROVÁVEIS DA BANCA

| Se o Professor perguntar... | O que qualquer integrante deve responder: |
|---|---|
| *"Por que o método de vocês não precisa de iterações como o Levenberg-Marquardt?"* | *"Porque o N2CACGO minimiza o erro de equação ponderado, que é linear nos coeficientes. Isso torna a função de custo puramente quadrática e convexa, permitindo calcular o mínimo global diretamente resolvendo o SEL $Q\theta = Y$."* |
| *"Por que deu um zero no semi-plano direito no motor CC? O motor é instável?"* | *"Não, o motor é estável (polo em $-4,79$). O zero em $+195,8\text{ rad/s}$ é a aproximação de Padé de 1ª ordem do atraso puro de transporte da placa de aquisição ($\tau_d = 2/195,8 \approx 10,2\text{ ms}$)."* |
| *"Por que escolheram a 1ª ordem para o motor e não uma ordem maior que talvez tivesse custo menor?"* | *"Pelo princípio da parcimônia. Ordens superiores a 1 tentam fazer sobreajuste (overfitting) no ruído elétrico de comutação das escovas sem acrescentar significado físico real, além de degradar o condicionamento numérico da matriz $Q$."* |
| *"Como garantiram que os dados do motor estavam em regime permanente?"* | *"Descartamos os primeiros 40% de cada ensaio temporal de partida e aplicamos a DFT estritamente sobre os 60% finais, garantindo que o transitório mecânico havia decaído por completo."* |
