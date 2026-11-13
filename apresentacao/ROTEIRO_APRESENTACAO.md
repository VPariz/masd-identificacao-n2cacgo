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

## 👤 BLOCO 2: PARIZ (Slides 4 a 8 — ~5:00 min)

### 🟢 Slide 4: 3. [Itens 1 & 2] Rotinas Vetorizadas no MATLAB (~1:15 min)
> *"Obrigado, Renato. Cumprimento o professor Marcelo e os colegas. Eu sou o Pariz e vou detalhar como saímos das equações matemáticas do N2CACGO para as rotinas funcionais no MATLAB e no Simulink, trazendo duas comprovações objetivas de validação.*  
> *À esquerda está o núcleo vetorizado `identifica_N2CACGO.m` em três passos:*  
> 1. *Montamos a base monomial $R = (j\omega)^{n-k}$ e as matrizes diagonais $S$, $\Gamma$ e $R_H = R^H$;*  
> 2. *Calculamos os blocos reais $Q_1$ a $Q_4$ e o vetor independente $Y = [Y_1; Y_2]$ decorrente do denominador mônico ($\beta_0 = 1$);*  
> 3. *Como o erro de equação linearizado $J_S(\theta) = \|D\cdot G - N\|_2^2$ é convexo e quadrático nos parâmetros, $Q\theta = Y$ resolve o mínimo global em passo único via eliminação LU (`theta = Q \ Y`), sem chute inicial nem iterações.*  
> *À direita está `valida_modelo_fr.m`, nossa auditoria oficial em quatro métricas sobre o erro direto de transferência ($G_{\text{med}} - G_{\text{id}}$): Custo $J$ (Norma 2), RMSE de Magnitude (dB), RMSE de Fase (graus) e o índice global FIT percentual."*

### 🟢 Slide 5: 4. Fluxograma Integrado: MATLAB & Simulink (~0:50 min)
> *"No Slide 5 vemos o pipeline completo integrando todas as etapas do trabalho em três estágios numerados:*  
> - *Etapa 1 (Fontes de Dados): no Item 3 entram as FRFs analíticas da planta de 7ª ordem de Silveira e sistemas didáticos; no Item 4 simulamos o modelo no Simulink com chirp de 0,1 a 15 Hz e obtemos a FRF via FFT $Y(k)/U(k)$; e no Item 5 o colega Pedro Augusto carrega os 26 ensaios senoidais do motor CC via projeção fasorial (DFT fundamental) nos 60% estacionários;*  
> - *Etapa 2 (Núcleo Analítico): todos os espectros convergem exatamente para a mesma rotina `identifica_N2CACGO.m`;*  
> - *Etapa 3 (Auditoria): `valida_modelo_fr.m` calcula $J$, RMSEs, FIT, gera os diagramas de Bode e alimenta a validação temporal cega.*  
> *A seguir apresento as duas evidências diretas de que esse código opera com precisão."*

### 🟢 Slide 6: 5. [Item 3] Validação do Código MATLAB: Benchmark Silveira (~1:05 min)
> *"Esta é a primeira evidência concreta de validação das rotinas MATLAB: no Item 3 reproduzimos o Exemplo 3.4.1 de Silveira (2006), uma planta original de 7ª ordem avaliada em 100 pontos de 0,01 a 100 rad/s.*  
> *Olhem na tabela:*  
> - *De 1ª a 3ª ordem há subajuste (FIT máximo de 57,2%);*  
> - *Na **4ª ordem** — modelo reduzido ótimo pelo princípio da parcimônia — o custo $J$ despenca quatro ordens de grandeza para $6,290 \times 10^{-4}$, batendo na casa decimal com $J_1 = 6,320 \times 10^{-4}$ da tese e atingindo **FIT = 99,98%**;*  
> - *De 5ª a 7ª ordem ocorre sobreajuste/quase-cancelamento polo-zero ($99,99\%$, com pequenas variações numéricas em $n=6,7$ pelo condicionamento das potências de $\omega^n$);*  
> - *Além disso, validamos sistemas didáticos puros de 1ª, 2ª e 3ª ordens com FIT = 100,00% (erro nulo), confirmando que nossas rotinas operam sem falhas."*

### 🟢 Slide 7: 6. [Item 4] Arquitetura do Modelo no Simulink (~0:50 min)
> *"Passando ao Item 4, aqui está o modelo funcional construído no Simulink (`modelo_item4.slx`):*  
> - *`Entrada_u` (From Workspace) injeta um chirp linear varrendo de 0,1 Hz a 15 Hz em $T = 10$ s para excitar toda a banda dinâmica;*  
> - *`Planta_LTI` implementa o sistema contínuo sobreamortecido $40 / [(s+1)(s+5)]$, com ganho estático $K_0 = 8$ e $\omega_n \approx 2,24$ rad/s;*  
> - *`Saida_y` grava $y(t)$ com passo fixo $T_s = 5$ ms ($f_s = 200$ Hz, $N = 2.001$ amostras) usando o solver contínuo `ode4` (Runge-Kutta de 4ª ordem) — passo fixo é essencial para gerar grade temporal uniforme antes da FFT.*  
> *À direita observamos os sinais temporais $u(t)$ e $y(t)$, evidenciando a atenuação progressiva da planta conforme a frequência sobe."*

### 🟢 Slide 8: 7. [Item 4] Validação do Simulink e FFT (`FIT = 96,47%`) (~1:00 min)
> *"Por fim, fechando a minha parte no Slide 8, validamos o encadeamento completo Simulink → FFT → N2CACGO:*  
> *Extraímos a FRF empírica pela razão fasorial $Y(k)/U(k)$ via FFT retangular direta sobre 126 frequências válidas entre 1,26 e 79,8 rad/s.*  
> *Aplicando `identifica_N2CACGO` para ordem $n = 2$, recuperamos $G_{id}(s) = 40,00 / (s^2 + 6,005s + 4,818)$, com polos em $-0,954$ e $-5,051$ (erro abaixo de 5% frente aos nominais $-1$ e $-5$) e $K_0 = 8,30$ (nominal 8,00).*  
> *Na rotina `valida_modelo_fr` alcançamos **FIT de 96,47%**, $J = 2,49 \times 10^{-1}$, RMSE de $0,165$ dB em magnitude e $1,02^\circ$ em fase — sendo o desvio residual (~3,5%) explicado pelo vazamento espectral típico da janela retangular aplicada a um chirp finito.*  
> *Com código MATLAB e Simulink validados, passo a palavra ao Pedro Augusto para apresentar o estudo experimental no motor CC real."*

---

## 👤 BLOCO 3: PEDRO AUGUSTO (Slides 9 a 11 — ~3:45 min)

### 🟢 Slide 9: 8. [Item 5] Motor CC Real: Dados de Bancada (Grupo 3 SSL) (~1:15 min)
> *"Obrigado, Pariz. Cumprimento o professor Marcelo e a banca.*  
> *No Bloco 3, aplicamos o algoritmo validado a uma planta física real: o motor de corrente contínua da bancada de Sinais e Sistemas Lineares (dados do Grupo 3).*  
> *A entrada é a tensão de armadura via ponte H PWM e a saída é a velocidade angular lida por tacômetro óptico. Foram processados 26 ensaios senoidais de 0,20 Hz a 10 Hz amostrados a $f_s = 100$ Hz ($352$ a $1.000$ amostras por ensaio).*  
> *Para eliminar o transitório de partida e efeitos de atrito estático inicial, descartamos os primeiros 40% de cada registro e aplicamos projeção fasorial (DFT na frequência fundamental) nos 60% finais, extraindo amplitude e fase imunes a ruído.*  
> *Um detalhe físico importante apareceu na leitura: a defasagem passa de $-90^\circ$ e chega a $-104^\circ$ em 10 Hz — veremos a explicação física exata no Slide 11."*

### 🟢 Slide 10: 9. [Item 5] Varredura de Ordens do Motor CC ($n = 1$ a 5) (~1:00 min)
> *"No Slide 10 avaliamos ordens de 1 a 5 para o motor CC usando a nossa rotina no MATLAB:*  
> - *A **1ª ordem** obteve o menor custo em norma 2 ($J = 1,7468$), erro de magnitude de $0,22$ dB ($0,2166$ dB), menor erro de fase ($2,19^\circ$) e o maior FIT: **88,36%**!*  
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
> 1. * **Mal-condicionamento de Vandermonde ($n \ge 5$):** onde o número de condição passa de $10^{15}$; mitigado com fatoração LU (`Q \ Y`), fallback por decomposição SVD/pseudoinversa (`pinv`) e critério de parcimônia ($n \le 4$);*  
> 2. * **Vazamento espectral na FFT do Simulink:** mitigado adotando passo fixo no solver `ode4` ($T_s = 5$ ms) e selecionando as 126 frequências na banda excitada de maior coerência;*  
> 3. * **Defasagem física além de $-90^\circ$ a 10 Hz no motor:** explicada e modelada exatamente pela síntese automática de um zero de Padé representando $10,2$ ms de atraso da placa DAQ;*  
> 4. * **Atrito seco e transitório inicial na bancada:** mitigados descartando os primeiros 40% e aplicando projeção fasorial na frequência fundamental nos 60% finais."*

### 🟢 Slide 14: 13. Conclusões Finais e Entrega (~1:00 min)
> *"Para concluir nossa apresentação:*  
> - *Comprovamos a eficácia analítica do método N2CACGO de Silveira (2006), obtendo solução fechada em um único passo sem mínimos locais;*  
> - *Reproduzimos o gabarito de Silveira com 99,98% de FIT, validamos o modelo contínuo no Simulink com 96,47% de FIT e caracterizamos o motor CC real revelando o atraso de Padé de 10,2 ms e validação temporal cega positiva;*  
> - *Cumprimos integralmente todos os 8 itens propostos em MASD — códigos MATLAB, modelo Simulink, artigo IEEE de 6 páginas, apresentação, GitHub e defesa oral.*  
> *Muito obrigado pela atenção do Prof. Dr. Marcelo e de todos os colegas. Ficamos à disposição para perguntas."*
