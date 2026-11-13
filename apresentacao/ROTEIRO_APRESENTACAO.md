# 📋 ROTEIRO OFICIAL DE APRESENTAÇÃO (POWERPOINT 14 SLIDES)
## Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO
**Instituição:** Instituto Militar de Engenharia (IME) — DE/3 • Engenharia Elétrica  
**Disciplina:** Modelagem e Análise de Sistemas Dinâmicos (MASD)  
**Docente:** Prof. Dr. Marcelo de Araújo Oliveira  
**Equipe de Autores (Nomes de Guerra em Destaque):**  
- **Renato Felix** (Renato Costa Félix)  
- **Pariz** (João Victor Tavares Pariz)  
- **Pedro Augusto** (Pedro Augusto dos Santos Barbosa)  
- **Scarpini** (Wagner Scarpini Miranda)  

**Tempo Total de Apresentação:** ~15 a 16 minutos + arguição.  
**Arquivo Oficial da Apresentação:** [`apresentacao_MASD_N2CACGO_IME.pptx`](file:///c:/Users/jvpar/estudo/3.2/MASD/trabalho_identificacao/apresentacao/apresentacao_MASD_N2CACGO_IME.pptx)  
**Artigo Acadêmico IEEE (PDF):** [`artigo_identificacao.pdf`](file:///c:/Users/jvpar/estudo/3.2/MASD/trabalho_identificacao/artigo/artigo_identificacao.pdf)

---

### ⏱️ Tabela de Distribuição do Tempo e Funções por Integrante

| Bloco | Orador | Slides | Foco Técnico Principal | Tempo Estimado |
|:---:|---|:---:|---|:---:|
| **1** | **Renato Felix** | 1 a 3 | Abertura oficial, Tipologia de Modelos (Caixa Branca/Cinza/Preta), Vantagens Frequenciais vs. Tempo e Formulação Convexa N2CACGO (Silveira, 2006) | **~3:45 min** |
| **2** | **Pariz** | 4 a 8 | Implementação MATLAB (`identifica_N2CACGO.m` e `valida_modelo_fr.m`), Fluxograma Integrado, **Validação do Código no Benchmark Silveira (Item 3)**, **Modelo Simulink `ode4` (Item 4)** e **Validação via FFT ($FIT = 96,47\%$)** | **~5:00 min** |
| **3** | **Pedro Augusto** | 9 a 11 | **Estudo Experimental do Motor CC Real (Item 5):** Dados da Bancada SSL (Grupo 3), Varredura de Ordens ($n=1..5$) por Parcimônia e **Modelo Físico Eletromecânico com Atraso de Padé (10,2 ms)** | **~3:45 min** |
| **4** | **Scarpini** | 12 a 14 | **Regra de Ouro (Validação Temporal Cega: Quadrada e Triangular 10 Hz)**, Dificuldades Numéricas/Físicas Superadas e Conclusões Finais (Cumprimento dos 8 Itens) | **~3:30 min** |
| **TOTAL** | **Toda a Equipe** | **1 a 14** | **Apresentação Enxuta, Visual, Fonte Grande e Rigor Técnico** | **~16:00 min** |

---

# 🎙️ GUIA DE FALA SLIDE A SLIDE (EXATAMENTE O QUE ESTÁ NAS ANOTAÇÕES DO PPTX)

---

## 👤 BLOCO 1: RENATO FELIX (Slides 1 a 3 — ~3:45 min)

### 🟢 Slide 1: Capa & Apresentação da Equipe (~1:00 min)
> *"Bom dia / boa tarde a todos. Cumprimento o Prof. Dr. Marcelo de Araújo Oliveira e os colegas da banca.*  
> *Nossa equipe é formada por Renato Costa Félix, João Victor Tavares Pariz, Pedro Augusto dos Santos Barbosa e Wagner Scarpini Miranda.*  
> *Hoje apresentamos o trabalho final de MASD sobre Identificação de Sistemas SISO no Domínio da Frequência pelo Método N2CACGO, de Silveira (2006).*  
> *Dividimos a apresentação em 4 blocos:*  
> 1. *Eu (Renato Felix) abro com a teoria de modelagem/identificação e a formulação matemática convexa;*  
> 2. *O Pariz apresenta os códigos MATLAB, o fluxograma, o modelo Simulink e as validações computacionais de Silveira e da FFT como evidência direta de funcionamento dos códigos;*  
> 3. *O Pedro Augusto apresenta o estudo experimental completo do motor CC real da bancada de SSL;*  
> 4. *E o Scarpini fecha com a validação temporal cega, os desafios numéricos superados e as conclusões finais."*

### 🟢 Slide 2: 1. Teoria: Modelagem vs. Domínio da Frequência (~1:15 min)
> *"Como vimos nas aulas do Prof. Marcelo, dividimos modelos em três categorias:*  
> - * **Caixa Branca:** puramente dedutivo por leis físicas (Newton, Kirchhoff), sem uso de dados experimentais, limitado por atritos e parâmetros incertos;*  
> - * **Caixa Cinza:** combina estrutura fenomenológica conhecida com estimação paramétrica por dados;*  
> - * **Caixa Preta:** mapeamento estritamente empírico entrada-saída.*  
> *Ao identificar no domínio do tempo (ARX, ARMAX, PEM), enfrentamos três gargalos clássicos: polarização por ruído colorido, exigência estrita de estado inicial nulo $x(0) = 0$ e dificuldade para estimar atrasos puros sem superparametrizar.*  
> *Já no domínio da frequência, temos as três grandes vantagens ensinadas no curso: (1) filtragem natural de ruídos fora da banda excitada; (2) sensibilidade direta a picos de ressonância e margens de estabilidade; e (3) compactação brutal de milhares de amostras em poucos fasores da FRF.*  
> *O problema é que métodos clássicos como Levy (1959), Sanathanan-Koerner (1963) e Valle (2005) são não-convexos ou iterativos, ficando presos em mínimos locais. Para resolver isso em definitivo, adotamos o método de Silveira (2006)."*

### 🟢 Slide 3: 2. Método N2CACGO (Silveira, 2006): Formulação Convexa (~1:30 min)
> *"O método que implementamos vem da dissertação de Bruno de Pinho Silveira (IME, 2006), chamado N2CACGO — Norma 2 Convexo Analítico Conjunto Gerador Ótimo.*  
> *Buscamos uma função de transferência biprópria $N(s)/D(s)$ com denominador mônico.*  
> *A sacada fundamental está no resíduo de equação $e(j\omega_k) = D(j\omega_k)G(j\omega_k) - N(j\omega_k)$, que é **estritamente linear** nos parâmetros desconhecidos $\alpha$ e $\beta$!*  
> *Ao somar os quadrados desse resíduo no funcional $J(\theta)$, obtemos uma forma quadrática com matriz Hessiana estritamente positiva definida ($\nabla^2 J > 0$).*  
> *Isso garante matematicamente a propriedade de convexidade estrita: não existem mínimos locais — há um único mínimo global!*  
> *Igualando o gradiente a zero, chegamos ao sistema linear particionado $Q\theta = Y$, resolvido em **um único passo** por eliminação Gaussiana ($\theta^* = Q^{-1}Y$), sem iterações nem chute inicial.*  
> *Agora passo a palavra ao Pariz, que mostrará a implementação desses códigos no MATLAB e no Simulink junto com as suas validações."*

---

## 👤 BLOCO 2: JOÃO VICTOR PARIZ (Slides 4 a 8 — ~5:00 min)

### 🟢 Slide 4: 3. [Itens 1 & 2] Rotinas Vetorizadas no MATLAB (~1:15 min)
> *"Obrigado, Renato. Cumprimento o professor Marcelo e os colegas.*  
> *No Bloco 2, apresento toda a nossa arquitetura computacional em MATLAB e Simulink, além das validações que comprovam o funcionamento dos códigos.*  
> *Começando pelos Itens 1 e 2 no MATLAB:*  
> - *Em `identifica_N2CACGO.m`, implementamos o algoritmo de forma 100% vetorizada, sem laços de busca: montamos a base monomial $R = (j\omega)^{n-k}$, construímos os quatro blocos reais $Q_1$ a $Q_4$ via projeções Hermitianas, e resolvemos $Q\theta = Y$ em um único passo com o operador backslash (fatoração LU com pivoteamento ótimo).*  
> - *Em `valida_modelo_fr.m`, avaliamos qualquer modelo identificado pelas 4 métricas oficiais vistas em sala: o custo $J$ em norma 2, o RMSE de módulo em dB, o RMSE de fase em graus e o índice FIT percentual, gerando automaticamente o diagrama de Bode sobreposto."*

### 🟢 Slide 5: 4. Fluxograma Integrado: MATLAB & Simulink (~0:50 min)
> *"No Slide 5 vemos o fluxograma completo integrando todas as etapas do trabalho:*  
> 1. *Em cima entram as três fontes de dados: benchmarks acadêmicos de até 7ª ordem (Item 3), sinais do modelo dinâmico no Simulink (Item 4) e ensaios experimentais do motor CC (Item 5);*  
> 2. *Para os ensaios no tempo fazemos o pré-processamento espectral — razão direta de FFTs $Y(k)/U(k)$ no Simulink e regressão senoidal de mínimos quadrados no motor CC;*  
> 3. *Todos os fasores convergem para o núcleo `identifica_N2CACGO.m` e são auditados por `valida_modelo_fr.m`;*  
> 4. *Agora vou mostrar as duas evidências diretas de que esse código funciona na prática: primeiro validando o MATLAB contra a dissertação de Silveira (Item 3), e depois montando e validando o Simulink (Item 4)."*

### 🟢 Slide 6: 5. [Item 3] Validação do Código MATLAB: Benchmark Silveira (~1:05 min)
> *"Esta é a primeira evidência concreta de que nossas rotinas MATLAB estão corretas: no Item 3 reproduzimos o Exemplo 3.4.1 da tese de Silveira (2006), cuja planta original é de 7ª ordem.*  
> *Olhem na tabela comparativa:*  
> - *De 1ª a 3ª ordem, o modelo é insuficiente (erro alto e FIT de até 57%);*  
> - *Na **4ª ordem** — que é o modelo reduzido ótimo pelo critério de parcimônia — o custo $J$ cai quatro ordens de grandeza para $6,290 \times 10^{-4}$, batendo na casa decimal com o gabarito $J_1 = 6,320 \times 10^{-4}$ da dissertação, e alcançando **FIT = 99,98%**!*  
> - *De 5ª a 7ª ordem o FIT mal muda (99,99%) porque surgem pares polo-zero de quase-cancelamento (superparametrização), confirmando que a 4ª ordem já captura com precisão a dinâmica essencial.*  
> - *Além disso, validamos sistemas didáticos puros de 1ª, 2ª e 3ª ordem com FIT de 100,00%, confirmando que `identifica_N2CACGO.m` e `valida_modelo_fr.m` operam sem erros."*

### 🟢 Slide 7: 6. [Item 4] Arquitetura do Modelo no Simulink (~0:50 min)
> *"Passando ao Item 4, aqui está o nosso modelo funcional construído no Simulink (`modelo_item4.slx`):*  
> - *O bloco `Entrada_u` (From Workspace) injeta um sinal Chirp linear varrendo de 0,1 Hz a 15 Hz durante 10 segundos para excitar toda a banda dinâmica;*  
> - *O bloco `Planta_LTI` implementa a planta contínua $40 / (s^2 + 6s + 5)$, com polos em $-1$ e $-5$ e ganho estático 8;*  
> - *O bloco `Saida_y` registra a resposta $y(t)$ em Array com passo fixo $T_s = 5$ ms ($f_s = 200$ Hz, totalizando $N = 2.001$ amostras);*  
> - *Utilizamos o solver contínuo `ode4` (Runge-Kutta de 4ª ordem), evitando distorções de passo variável para a etapa seguinte da FFT.*  
> *À direita vemos os sinais temporais simulados ao longo dos 10 segundos, exibindo a atenuação progressiva da saída conforme a frequência sobe."*

### 🟢 Slide 8: 7. [Item 4] Validação do Simulink e FFT (`FIT = 96,47%`) (~1:00 min)
> *"E aqui está a validação que fecha o ciclo do nosso código Simulink + FFT + N2CACGO:*  
> *Pegamos os vetores $u(t)$ e $y(t)$ exportados pelo Simulink, aplicamos a FFT retangular direta e calculamos a FRF pela razão fasorial $Y(k)/U(k)$ em 126 frequências na faixa de 1,26 a 79,8 rad/s.*  
> *Alimentando esses dados espectrais na nossa rotina `identifica_N2CACGO.m` para 2ª ordem, recuperamos $G_{id}(s) = 40,0 / (s^2 + 6,005s + 4,818)$, com polos estimados em $-0,954$ e $-5,051$ — erro menor que 5% frente à planta nominal ($-1$ e $-5$)!*  
> *Na nossa rotina de validação obtivemos **FIT de 96,47%**, RMSE de magnitude de apenas $0,165$ dB e RMSE de fase de $1,02^\circ$, como comprova a sobreposição no diagrama de Bode à direita.*  
> *Com os códigos MATLAB e o modelo Simulink devidamente validados, passo a palavra ao Pedro Augusto para apresentar o estudo experimental completo do Motor CC real."*

---

## 👤 BLOCO 3: PEDRO AUGUSTO (Slides 9 a 11 — ~3:45 min)

### 🟢 Slide 9: 8. [Item 5] Motor CC Real: Dados de Bancada (Grupo 3 SSL) (~1:15 min)
> *"Obrigado, Pariz. Cumprimento o professor Marcelo e a banca.*  
> *No Bloco 3, aplicamos o algoritmo validado a uma planta física real: o motor de corrente contínua da bancada de Sinais e Sistemas Lineares (dados do Grupo 3).*  
> *A entrada é a tensão de armadura via ponte H PWM e a saída é a velocidade angular lida por tacômetro óptico. Foram processados 26 ensaios senoidais de 0,20 Hz a 10 Hz amostrados a 1 kHz.*  
> *Para eliminar o transitório de partida e efeitos de atrito estático inicial, descartamos os primeiros 40% de cada registro e aplicamos regressão senoidal de mínimos quadrados nos 60% finais, extraindo amplitude e fase imunes a ruído.*  
> *Um detalhe físico importante apareceu na leitura: a defasagem passa de $-90^\circ$ e chega a $-104^\circ$ em 10 Hz — veremos a explicação física exata no Slide 11."*

### 🟢 Slide 10: 9. [Item 5] Varredura de Ordens do Motor CC ($n = 1$ a 5) (~1:00 min)
> *"No Slide 10 avaliamos ordens de 1 a 5 para o motor CC usando a nossa rotina no MATLAB:*  
> - *A **1ª ordem** obteve o menor custo em norma 2 ($J = 1,7468$), menor erro de magnitude ($0,21$ dB) e o maior FIT: **88,36%**!*  
> - *A partir da 2ª ordem, o FIT cai (85% na 2ª/3ª, 75,6% na 5ª ordem), porque polos extras apenas ajustam ruído de comutação das escovas (overfitting) e pioram o condicionamento da matriz $Q$.*  
> - *Seguindo o princípio da parcimônia, escolhemos a 1ª ordem como representação física ótima do motor."*

### 🟢 Slide 11: 10. [Item 5] Modelo Físico e Atraso de Padé (10,2 ms) (~1:30 min)
> *"Aqui está o resultado físico mais interessante do trabalho.*  
> *A função identificada de 1ª ordem é $G(s) = (-0,2468s + 48,33) / (s + 4,794)$:*  
> - *O ganho estático vale $K_m = 10,08$ (rad/s)/V ($20,07$ dB);*  
> - *A constante de tempo mecânica dominante é $\tau_m = 0,209$ s (polo em $-4,794$ rad/s).*  
> *Agora reparem no numerador: apareceu um zero real positivo em $s = +195,8$ rad/s!*  
> *Longe de ser um erro numérico, esse zero no semiplano direito é a **aproximação de Padé de 1ª ordem** de um atraso puro de transporte: $\tau_d = 2 / 195,8 \approx 10,2$ milissegundos!*  
> *Fisicamente, esses 10,2 ms representam exatamente o atraso acumulado de conversão D/A, modulação PWM e leitura do encoder pela placa DAQ do laboratório — e explicam com perfeição por que a fase medida atingia $-104^\circ$ a 10 Hz!*  
> *Para apresentar a validação temporal cega contra sinais inéditos, as dificuldades enfrentadas e as conclusões finais, passo a palavra ao Scarpini."*

---

## 👤 BLOCO 4: SCARPINI (Slides 12 a 14 — ~3:30 min)

### 🟢 Slide 12: 11. [Item 5] Validação Temporal Cega do Motor CC (~1:15 min)
> *"Obrigado, Pedro. Cumprimento o professor Marcelo e a banca examinadora.*  
> *No Bloco 4 trago a validação temporal definitiva, as dificuldades superadas e o fechamento do trabalho.*  
> *Aplicamos a 'Regra de Ouro da Identificação' vista nas aulas de MASD: jamais validar um modelo apenas com os mesmos dados usados para estimá-lo.*  
> *Nosso modelo foi calibrado exclusivamente com ensaios senoidais e agora é testado contra duas excitações temporais nunca vistas: **Onda Quadrada** e **Onda Triangular** a 10 Hz.*  
> *Como mostram os dois gráficos, a curva vermelha prevista pelo modelo N2CACGO acompanha com precisão a subida exponencial, o regime permanente e as rampas medidas na bancada real (linha preta), confirmando a autenticidade física de $K_m = 10,08$ e $\tau_m = 0,209$ s."*

### 🟢 Slide 13: 12. Dificuldades Encontradas e Soluções Adotadas (~1:15 min)
> *"Ao longo da implementação enfrentamos quatro dificuldades técnicas reais e aplicamos soluções de engenharia objetivas:*  
> 1. * **Mal-condicionamento de Vandermonde ($n \ge 5$):** onde o número de condição passa de $10^{15}$; resolvido com escalonamento euclidiano das colunas e decomposição SVD/pseudoinversa;*  
> 2. * **Vazamento espectral na FFT do Simulink:** mitigado adotando passo fixo no solver `ode4` ($T_s = 5$ ms) e selecionando as 126 frequências na banda excitada de maior coerência;*  
> 3. * **Defasagem física além de $-90^\circ$ a 10 Hz no motor:** explicada e modelada exatamente pela síntese automática de um zero de Padé representando $10,2$ ms de atraso da placa DAQ;*  
> 4. * **Atrito seco e transitório inicial na bancada:** mitigados descartando os primeiros 40% e ajustando apenas o regime permanente senoidal nos 60% finais."*

### 🟢 Slide 14: 13. Conclusões Finais e Entrega (~1:00 min)
> *"Para concluir nossa apresentação:*  
> - *Comprovamos a eficácia analítica do método N2CACGO de Silveira (2006), obtendo solução fechada em um único passo sem mínimos locais;*  
> - *Reproduzimos o gabarito de Silveira com 99,98% de FIT, validamos o modelo contínuo no Simulink com 96,47% de FIT e caracterizamos o motor CC real revelando o atraso de Padé de 10,2 ms e validação temporal cega positiva;*  
> - *Cumprimos integralmente todos os 8 itens propostos em MASD — códigos MATLAB, modelo Simulink, artigo IEEE de 6 páginas, apresentação, GitHub e defesa oral.*  
> *Muito obrigado pela atenção do Prof. Dr. Marcelo e de todos os colegas. Ficamos à disposição para perguntas."*
