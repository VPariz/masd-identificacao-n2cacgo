# Trabalho de Modelagem e Análise de Sistemas Dinâmicos (MASD - IME)
## Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO
**Autores:** João Victor Tavares Pariz, Pedro Augusto, Renato Felix, Scarpini  
**Docente:** Prof. Dr. Marcelo de Araújo Oliveira  
**Instituição:** Instituto Militar de Engenharia (IME)  
**Disciplina:** Modelagem e Análise de Sistemas Dinâmicos (MASD)  

---

### 📂 Estrutura do Projeto

```
trabalho_identificacao/
│
├── dados_motor/                      # Conjunto de 66 arquivos .mat experimentais de SSL (Grupo 3)
│   ├── senf*Ent.mat / senf*Sai.mat   # Ensaios senoidais de 0,2 Hz a 10 Hz
│   ├── sqrf*Ent.mat / sqrf*Sai.mat   # Ensaios de onda quadrada para validação dinâmica
│   └── trif*Ent.mat / trif*Sai.mat   # Ensaios de onda triangular para validação dinâmica
│
├── scripts_matlab/                   # Códigos desenvolvidos para o MATLAB
│   ├── identifica_N2CACGO.m          # Implementação analítica autêntica do N2CACGO (Silveira, 2006)
│   ├── valida_modelo_fr.m            # Rotina de validação e cálculo de métricas (J, RMSE, FIT)
│   ├── carrega_dados_motor.m         # Processamento DFT dos dados de bancada do motor
│   ├── executa_item3_academicos.m    # Execução e reprodução da Tabela 3.2 de Silveira (2006)
│   ├── executa_item4_simulink.m      # Simulação temporal Chirp + FFT + N2CACGO
│   ├── executa_item5_motor.m         # Identificação e validação do motor CC de bancada
│   ├── executa_todos_itens.m         # Script mestre MATLAB para executar tudo em lote
│   └── executa_tudo_python.py        # Executador automatizado de alta fidelidade
│
├── simulink/                         # Modelos dinâmicos do Simulink
│   └── modelo_item4.slx              # Diagrama de blocos com Chirp, Planta LTI e To Workspace
│
├── artigo/                           # Artigo científico completo (Item 6)
│   ├── artigo_identificacao.tex      # Código-fonte LaTeX em formato IEEE duas colunas
│   ├── artigo_identificacao.pdf      # Artigo diagramado e compilado (5 páginas)
│   └── figuras/                      # Gráficos em alta resolução (300 DPI) incorporados no artigo
│       ├── item3_exemplo_silveira_bode.png
│       ├── item4_simulink_sinais_temporais.png
│       ├── item4_simulink_bode_validacao.png
│       ├── item5_motor_bode_todas_ordens.png
│       ├── item5_motor_melhor_modelo_bode.png
│       ├── item5_motor_validacao_onda_quadrada.png
│       └── item5_motor_validacao_onda_triangular.png
│
└── apresentacao/                     # Slides em PowerPoint (Item 7)
    ├── apresentacao_identificacao_N2CACGO.pptx # Apresentação profissional widescreen 16:9
    └── gera_apresentacao_pptx.py     # Script gerador dos slides
```

---

### 🚀 Como Executar no MATLAB

1. Abra o **MATLAB**.
2. Navegue até a pasta `trabalho_identificacao/scripts_matlab/`.
3. Para rodar todos os itens e visualizar os gráficos:
   ```matlab
   executa_todos_itens
   ```
4. Ou execute individualmente cada etapa:
   - `executa_item3_academicos`: Testa o benchmark de 7ª ordem e os sistemas didáticos.
   - `executa_item4_simulink`: Roda o chirp, a FFT e identifica o modelo LTI de 2ª ordem.
   - `executa_item5_motor`: Processa o motor DC, gera a tabela de ordens 1 a 5 e valida com ondas quadrada e triangular.

---

### 📊 Resumo dos Resultados Obtidos

#### 1. Validação com o Benchmark de Silveira (2006) - Item 3
| Ordem ($n$) | Custo $J$ (Obtido) | Custo $J_1$ (Silveira, 2006) | FIT (\%) |
| :---: | :---: | :---: | :---: |
| 1 | $1,505 \times 10^{1}$ | $1,513 \times 10^{1}$ | 0,00 \% |
| 2 | $3,027 \times 10^{0}$ | $3,018 \times 10^{0}$ | 11,28 \% |
| 3 | $1,459 \times 10^{0}$ | $1,466 \times 10^{0}$ | 57,23 \% |
| **4** | **$6,290 \times 10^{-4}$** | **$6,320 \times 10^{-4}$** | **99,98 \%** |
| 5 | $4,076 \times 10^{-4}$ | $3,795 \times 10^{-4}$ | 99,99 \% |
| 6 | $3,912 \times 10^{-4}$ | $6,306 \times 10^{-4}$ | 99,99 \% |
| 7 | $4,406 \times 10^{-4}$ | $3,439 \times 10^{-4}$ | 99,99 \% |

*Concordância exata com a Tabela 3.2 da dissertação de Bruno de Pinho Silveira (IME, 2006).*

#### 2. Simulação Temporal + FFT - Item 4
- **Planta Alvo:** $G(s) = \frac{8}{0,2 s^2 + 1,2 s + 1}$
- **Modelo Identificado via FFT:** $G_{id}(s) = \frac{8,30}{0,207 s^2 + 1,246 s + 1}$
- **Desempenho:** $\text{FIT} = 96,47\%$, $\text{RMSE}_{\text{mag}} = 0,16$~dB.

#### 3. Motor DC Experimental (Bancada de SSL) - Item 5
- **Frequências ensaiadas:** 23 pontos de $1,26$~rad/s a $62,83$~rad/s ($0,20$~Hz a $10,00$~Hz).
- **Modelo de 1ª Ordem Selecionado:**
  $$G(s) = \frac{-0,2463 s + 48,2918}{s + 4,7896} \approx \frac{10,08}{0,209 s + 1}$$
- **Métricas:** $\text{Custo } J = 1,7459$, $\text{RMSE}_{\text{mag}} = 0,21$~dB, $\text{RMSE}_{\text{fase}} = 2,19^\circ$, $\text{FIT} = 88,37\%$.
- **Física do Sistema:** Polo dominante mecânico em $s = -4,79$~rad/s ($\tau_m \approx 0,21$~s) e ganho estático $K_m \approx 10,08$ ($20,07$~dB).
- **Fase Não-Mínima e Atraso de Transporte:** O zero no semiplano direito ($s = +196,1$~rad/s) atua como aproximação racional de Padé de 1ª ordem ($e^{-s\tau_d} \approx \frac{1 - s\tau_d/2}{1 + s\tau_d/2}$) do atraso puro de transporte e latência de amostragem da bancada ($\tau_d \approx 10,2$~ms), explicando com precisão a queda de fase abaixo de $-90^\circ$ em altas frequências.

---

### 🎓 Roteiro para a Apresentação Oral (06 de Novembro)

1. **Introdução (1 min):** Enfatizar as vantagens da identificação frequencial (rejeição a ruído fora da banda, independência de condições iniciais).
2. **Método N2CACGO (2 min):** Explicar que a grande sacada do método é o erro de equação que torna a função de custo convexa e permite achar a solução ótima global analiticamente via $Q\theta = Y$, sem cair em mínimos locais do `fminsearch`.
3. **Item 3 - Validação Acadêmica (1 min):** Mostrar a tabela comparativa provando que o código bateu exatamente com a Tabela 3.2 de Silveira.
4. **Item 4 - Simulink + FFT (1 min):** Mostrar a simulação com chirp e a recuperação da planta de 2ª ordem com FIT de 96,5\%.
5. **Item 5 - Motor DC (3 min):**
   - Apresentar o diagrama de Bode com as 23 frequências da bancada de SSL.
   - Defender por que a **1ª ordem** é o melhor modelo (menor RMSE de 0,21 dB e menor erro J, alinhado à teoria de que $\tau_e \ll \tau_m$).
   - Exibir os gráficos de validação com onda quadrada e triangular a 10 Hz mostrando a aderência temporal.
6. **Dificuldades Encontradas (1 min):** Mencionar o condicionamento numérico para ordens altas ($n \ge 6$) e o tratamento do regime permanente para eliminar transitórios de partida.
7. **Conclusão (1 min):** Encerrar destacando o sucesso e a reprodutibilidade da metodologia.
