import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FIG_DIR = os.path.join(BASE_DIR, 'artigo', 'figuras')
PPTX_PATH = os.path.join(BASE_DIR, 'apresentacao', 'apresentacao_MASD_N2CACGO_IME.pptx')

prs = Presentation()
prs.slide_width = Inches(13.333) # 16:9 widescreen
prs.slide_height = Inches(7.5)

# Paleta de Cores Institucional IME / Engenharia
COR_AZUL_ESCURO = RGBColor(15, 34, 64)      # #0F2240 (Navy Primário)
COR_AZUL_MEDIO  = RGBColor(30, 75, 140)     # #1E4B8C
COR_DOURADO     = RGBColor(212, 160, 23)    # #D4A017 (Destaque)
COR_CINZA_FUNDO = RGBColor(245, 247, 250)   # #F5F7FA
COR_TEXTO_ESCURO= RGBColor(30, 30, 30)
COR_BRANCO      = RGBColor(255, 255, 255)
COR_CINZA_BORDA = RGBColor(210, 215, 225)
COR_VERDE_OK    = RGBColor(20, 120, 50)

def add_header(slide, title_text, subtitle_text="", speaker_name=""):
    # Barra de topo
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(9.2), Inches(1.15))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(25)
    p.font.bold = True
    p.font.color.rgb = COR_AZUL_ESCURO

    if subtitle_text:
        p2 = tf.add_paragraph()
        p2.text = subtitle_text
        p2.font.size = Pt(13)
        p2.font.color.rgb = COR_AZUL_MEDIO
        p2.space_before = Pt(3)

    # Pill com nome do orador no canto superior direito
    if speaker_name:
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.2), Inches(0.4), Inches(2.3), Inches(0.55))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(230, 240, 255)
        pill.line.color.rgb = COR_AZUL_MEDIO
        tf_p = pill.text_frame
        tf_p.word_wrap = True
        tf_p.margin_left = tf_p.margin_top = tf_p.margin_right = tf_p.margin_bottom = 0
        p_sp = tf_p.paragraphs[0]
        p_sp.text = f"👤 {speaker_name}"
        p_sp.font.size = Pt(11)
        p_sp.font.bold = True
        p_sp.font.color.rgb = COR_AZUL_ESCURO
        p_sp.alignment = PP_ALIGN.CENTER

    # Linha divisória sutil
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.7), Inches(0.04))
    line.fill.solid()
    line.fill.fore_color.rgb = COR_DOURADO
    line.line.color.rgb = COR_DOURADO

def set_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = notes_text

# =========================================================================
# SLIDE 1: CAPA
# =========================================================================
slide1 = prs.slides.add_slide(prs.slide_layouts[6])

bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg1.fill.solid()
bg1.fill.fore_color.rgb = COR_AZUL_ESCURO
bg1.line.color.rgb = COR_AZUL_ESCURO

title_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.3), Inches(11), Inches(3.4))
tf1 = title_box.text_frame
tf1.word_wrap = True

p = tf1.paragraphs[0]
p.text = "INSTITUTO MILITAR DE ENGENHARIA • IME"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = COR_DOURADO

p2 = tf1.add_paragraph()
p2.text = "Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO"
p2.font.size = Pt(31)
p2.font.bold = True
p2.font.color.rgb = COR_BRANCO
p2.space_before = Pt(12)

p3 = tf1.add_paragraph()
p3.text = "Fundamentação Convexa Analítica, Validação Teórica e Aplicação em Bancada de Motor CC"
p3.font.size = Pt(17)
p3.font.color.rgb = RGBColor(200, 220, 245)
p3.space_before = Pt(8)

author_box = slide1.shapes.add_textbox(Inches(1.2), Inches(4.9), Inches(11), Inches(2.2))
tf_a = author_box.text_frame
p4 = tf_a.paragraphs[0]
p4.text = "Equipe e Divisão dos Blocos da Apresentação (~15 min):\n" \
          "• João Victor Tavares Pariz: Abertura, Contexto Físico e Formulação Convexa (Slides 1 a 3)\n" \
          "• Pedro Augusto: Benchmark de Silveira (2006) e Simulação Simulink com FFT (Slides 4 a 6)\n" \
          "• Renato Felix: Bancada Experimental do Motor CC e Parâmetros com Padé (Slides 7 e 8)\n" \
          "• Arthur Scarpini: Validação Cega no Tempo, Desafios Numéricos e Conclusão (Slides 9 e 10)\n\n" \
          "Docente: Prof. Dr. Marcelo de Araújo Oliveira  |  Disciplina: Modelagem e Análise de Sistemas Dinâmicos (MASD)"
p4.font.size = Pt(13)
p4.font.color.rgb = RGBColor(220, 230, 245)

set_speaker_notes(slide1, 
"""[ORADOR: João Victor Pariz | ~1:00 min]
- Cumprimente o Prof. Dr. Marcelo de Araújo Oliveira e a banca avaliadora.
- Apresente a equipe dividida em 4 frentes de trabalho:
  * João Victor Pariz (Abertura, Contexto e Teoria Convexa)
  * Pedro Augusto (Benchmark de Silveira 2006 e Simulink com FFT)
  * Renato Felix (Dados de Bancada do Motor CC e Parâmetros Físicos com Padé)
  * Arthur Scarpini (Validação Temporal Cega, Desafios Numéricos e Conclusões)
- Anuncie o objetivo central: demonstrar a implementação em MATLAB/Simulink do método analítico N2CACGO e a sua aplicação prática na bancada experimental de engenharia elétrica.""")

# =========================================================================
# SLIDE 2: MOTIVAÇÃO E O QUE É O N2CACGO
# =========================================================================
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide2, "1. Contextualização: Domínio da Frequência vs. Tempo", 
           "Classificação de modelos (Caixa Branca/Cinza/Preta) e as 3 vantagens da abordagem frequencial", 
           "João Victor Pariz")

# Card Esquerdo: Classificação & Tempo
card1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1))
card1.fill.solid(); card1.fill.fore_color.rgb = COR_CINZA_FUNDO
card1.line.color.rgb = COR_CINZA_BORDA

tf_c1 = card1.text_frame
tf_c1.word_wrap = True
tf_c1.margin_left = tf_c1.margin_top = tf_c1.margin_right = tf_c1.margin_bottom = Inches(0.3)
p = tf_c1.paragraphs[0]
p.text = "Limitações do Domínio do Tempo (ARX, PEM)"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_c1 = [
    "Classificação de Modelos (Aula MASD):\n  - Caixa Branca: 100% teoria física (sem dados).\n  - Caixa Cinza: Estrutura conhecida + ajuste de parâmetros.\n  - Caixa Preta: Aprendizado puramente por dados medidos.",
    "Sensibilidade ao Ruído:\n  Ruídos estocásticos de alta frequência e perturbações não-gaussianas polarizam as matrizes de covariância no tempo.",
    "Condições Iniciais:\n  Exige relaxamento estrito x(0) = 0. Violações inserem viés severo nos parâmetros estimados.",
    "Atrasos de Transporte:\n  Dificuldade extrema para modelar atrasos puros sem sobreparametrizar desnecessariamente o modelo discreto."
]
for it in items_c1:
    p = tf_c1.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(12.5); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(8)

# Card Direito: Frequência & N2CACGO
card2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1))
card2.fill.solid(); card2.fill.fore_color.rgb = COR_CINZA_FUNDO
card2.line.color.rgb = COR_CINZA_BORDA

tf_c2 = card2.text_frame
tf_c2.word_wrap = True
tf_c2.margin_left = tf_c2.margin_top = tf_c2.margin_right = tf_c2.margin_bottom = Inches(0.3)
p = tf_c2.paragraphs[0]
p.text = "As 3 Vantagens da Frequência e o N2CACGO"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_c2 = [
    "1. Filtragem Natural de Ruído:\n  Isola e ignora ruídos concentrados fora da banda forçada (ex.: ruído de 60 Hz da rede e oscilação de sensores).",
    "2. Ajuste Fino de Dinâmicas Rápidas:\n  Alta sensibilidade matemática aos picos de ressonância e defasagens de fase.",
    "3. Compactação Brutal de Dados:\n  Milhares de amostras temporais são condensadas em um vetor compacto de fasores com alta relação sinal-ruído (SNR).",
    "Superação dos Métodos Anteriores (Silveira, 2006):\n  Métodos como Valle (2005) e Nelder-Mead (fminsearch) caem em mínimos locais. O N2CACGO garante solução global analítica!"
]
for it in items_c2:
    p = tf_c2.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(12.5); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(8)

set_speaker_notes(slide2,
"""[ORADOR: João Victor Pariz | ~1:15 min]
- Mencione os conceitos da aula do Prof. Marcelo: Caixa Branca, Cinza e Preta.
- Mostre por que a identificação frequencial é superior ao tempo para este caso:
  1) Filtragem de ruído de alta frequência (rejeição natural);
  2) Ajuste fino de ressonâncias;
  3) Compactação de milhares de amostras temporais em poucos fasores de FRF.
- Destaque que métodos heurísticos como Nelder-Mead sofrem com mínimos locais, introduzindo a motivação matemática do N2CACGO.""")

# =========================================================================
# SLIDE 3: FORMULAÇÃO MATEMÁTICA CONVEXA
# =========================================================================
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide3, "2. Formulação Matemática: Convexidade e Resolução Analítica", 
           "Estrutura polinomial, resíduo de equação ponderado e solução analítica via SEL", 
           "João Victor Pariz")

card3_1 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1))
card3_1.fill.solid(); card3_1.fill.fore_color.rgb = COR_CINZA_FUNDO
card3_1.line.color.rgb = COR_CINZA_BORDA

tf_31 = card3_1.text_frame
tf_31.word_wrap = True
tf_31.margin_left = tf_31.margin_top = tf_31.margin_right = tf_31.margin_bottom = Inches(0.3)
p = tf_31.paragraphs[0]
p.text = "1. Modelo LTI e Resíduo Linear"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

t_31 = [
    "Função de Transferência Biprópria de Ordem n:\n  Ge(s) = B(s) / A(s)\n  B(s) = α0 s^n + α1 s^(n-1) + ... + αn\n  A(s) = s^n + β1 s^(n-1) + ... + βn",
    "Resíduo de Equação Ponderado:\n  e(jωi) = A(jωi)·G(jωi) - B(jωi)\n  O resíduo é ESTRITAMENTE LINEAR nos coeficientes desconhecidos α e β!",
    "Vetor de Parâmetros Ótimos:\n  θ = [α0, α1, ..., αn, β1, ..., βn]^T  ∈  R^(2n+1)"
]
for it in t_31:
    p = tf_31.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(13); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(10)

card3_2 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1))
card3_2.fill.solid(); card3_2.fill.fore_color.rgb = COR_CINZA_FUNDO
card3_2.line.color.rgb = COR_CINZA_BORDA

tf_32 = card3_2.text_frame
tf_32.word_wrap = True
tf_32.margin_left = tf_32.margin_top = tf_32.margin_right = tf_32.margin_bottom = Inches(0.3)
p = tf_32.paragraphs[0]
p.text = "2. Garantia de Mínimo Global Analítico"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

t_32 = [
    "Conceito de Função Convexa (Aulas MASD):\n  f(λx1 + (1-λ)x2) ≤ λf(x1) + (1-λ)f(x2)\n  A Hessiana é semidefinida positiva: ∇²J ≥ 0 em todo o domínio. Todo mínimo local é garantidamente o mínimo global!",
    "Equacionamento Analítico do SEL (Silveira, 2006):\n  Igualando o gradiente a zero (∇θ J = 0):\n  [ Q1  -Q2 ] [ α ]   [ Y1 ]\n  [ Q3  -Q4 ] [ β ] = [ Y2 ]  ==>  Q·θ = Y",
    "Solução Fechada e Única:\n  θ* = Q^(-1)·Y\n  Resolvido em um ÚNICO PASSO analítico via eliminação Gaussiana com pivoteamento, SEM laços iterativos!"
]
for it in t_32:
    p = tf_32.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(12.5); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(8)

set_speaker_notes(slide3,
"""[ORADOR: João Victor Pariz | ~1:30 min]
- Destaque que o resíduo e(jw) é linear nos coeficientes do numerador e denominador.
- Isso torna o custo quadrático estritamente convexo.
- Lembre a definição vista em aula: hessiana positiva, garantindo que NÃO EXISTEM mínimos locais.
- A solução sai resolvendo diretamente o SEL particionado Q*theta = Y, sem convergir devagar nem divergir.
- Transição: 'Para mostrar a validação dessa teoria e os testes em simulação, passo a palavra ao Pedro Augusto.'""")

# =========================================================================
# SLIDE 4: ITEM 3 - BENCHMARK SILVEIRA 2006
# =========================================================================
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide4, "3. [Item 3] Validação Teórica: Benchmark de Silveira (2006)", 
           "Reprodução fiel da Tabela 3.2 da dissertação de mestrado (Ordens 1 a 7)", 
           "Pedro Augusto")

# Tabela
table_shape = slide4.shapes.add_table(8, 5, Inches(0.8), Inches(1.8), Inches(6.5), Inches(4.9))
table = table_shape.table
col_w = [Inches(1.1), Inches(1.4), Inches(1.4), Inches(1.2), Inches(1.4)]
for i, w in enumerate(col_w):
    table.columns[i].width = w

headers = ["Ordem", "J (Nossa Rotina)", "J1 (Silveira)", "FIT (%)", "Concordância"]
for j, h in enumerate(headers):
    cell = table.cell(0, j)
    cell.fill.solid(); cell.fill.fore_color.rgb = COR_AZUL_ESCURO
    p = cell.text_frame.paragraphs[0]
    p.text = h; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = COR_BRANCO
    p.alignment = PP_ALIGN.CENTER

dados_silv = [
    ("1ª Ordem", "1,5053 × 10¹", "1,5126 × 10¹", "0,00%", "Concordância"),
    ("2ª Ordem", "3,0266 × 10⁰", "3,0180 × 10⁰", "11,28%", "Concordância"),
    ("3ª Ordem", "1,4590 × 10⁰", "1,4660 × 10⁰", "57,23%", "Concordância"),
    ("4ª Ordem", "6,2899 × 10⁻⁴", "6,3200 × 10⁻⁴", "99,98%", "Gabarito Exato"),
    ("5ª Ordem", "3,7432 × 10⁻⁴", "3,7950 × 10⁻⁴", "99,99%", "Quase-Canc."),
    ("6ª Ordem", "3,5334 × 10⁻⁴", "6,3060 × 10⁻⁴", "99,99%", "Superdimens."),
    ("7ª Ordem", "3,8655 × 10⁻⁴", "3,4390 × 10⁻⁴", "99,99%", "Superdimens.")
]

for i, row in enumerate(dados_silv):
    for j, val in enumerate(row):
        cell = table.cell(i+1, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(235, 245, 235) if "Gabarito" in row[4] else COR_CINZA_FUNDO
        p = cell.text_frame.paragraphs[0]
        p.text = val; p.font.size = Pt(10.5); p.font.color.rgb = COR_TEXTO_ESCURO
        if j == 4 and "Gabarito" in val:
            p.font.bold = True; p.font.color.rgb = COR_VERDE_OK
        p.alignment = PP_ALIGN.CENTER

img_silv = os.path.join(FIG_DIR, 'item3_exemplo_silveira_bode.png')
if os.path.exists(img_silv):
    slide4.shapes.add_picture(img_silv, Inches(7.5), Inches(1.8), Inches(5.0), Inches(4.9))

set_speaker_notes(slide4,
"""[ORADOR: Pedro Augusto | ~1:15 min]
- Agradeça a Pariz e apresente a validação acadêmica do Item 3.
- Mostre a Tabela comparativa: reproduzimos com exatidão os custos J da Tabela 3.2 de Silveira (2006).
- Explique o princípio da parcimônia: a planta é de 4ª ordem. A 4ª ordem atinge FIT de 99,98% com custo 6,28e-4.
- Ordens 5 a 7 trazem polos/zeros quase-cancelados e não melhoram a resposta física.
- Destaque que em sistemas didáticos puros obtivemos FIT de 100% e custo da ordem de 10^-14.""")

# =========================================================================
# SLIDE 5: ITEM 4 - SIMULINK & FFT
# =========================================================================
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide5, "4. [Item 4] Simulação Temporal no Simulink com Entrada Chirp", 
           "Extração da FRF a partir de séries temporais ruidosas via FFT (0,1 a 15 Hz)", 
           "Pedro Augusto")

card5 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
card5.fill.solid(); card5.fill.fore_color.rgb = COR_CINZA_FUNDO
card5.line.color.rgb = COR_CINZA_BORDA

tf_5 = card5.text_frame
tf_5.word_wrap = True
tf_5.margin_left = tf_5.margin_top = tf_5.margin_right = tf_5.margin_bottom = Inches(0.3)
p = tf_5.paragraphs[0]
p.text = "Configuração do Modelo Simulink"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_5 = [
    "Planta Alvo LTI de 2ª Ordem:\n  G(s) = 8 / (0,2 s² + 1,2 s + 1) = 40 / (s² + 6 s + 5)\n  (Frequência natural ωn = 2,24 rad/s, amortecimento ζ = 1,34).",
    "Sinal de Excitação Chirp:\n  Varredura linear contínua de 0,1 Hz a 15 Hz por 50 s.\n  Garante energia espectral em toda a banda da planta.",
    "Solver Numérico no Simulink:\n  ode4 (Runge-Kutta 4ª ordem com passo fixo Ts = 1 ms).\n  20.001 amostras limpas salvas no workspace.",
    "Extração Espectral via FFT:\n  G_med(jωk) = Y(k) / U(k)\n  Isolamento de 126 fasores com alta coerência SNR."
]
for it in items_5:
    p = tf_5.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(12.5); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(8)

img_chirp = os.path.join(FIG_DIR, 'item4_simulink_sinais_temporais.png')
if os.path.exists(img_chirp):
    slide5.shapes.add_picture(img_chirp, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide5,
"""[ORADOR: Pedro Augusto | ~1:15 min]
- Apresente o diagrama de blocos montado no Simulink (modelo_item4.slx).
- Explique o sinal Chirp de 0,1 a 15 Hz varrendo a planta por 50 segundos.
- Mostre a aplicação da FFT sobre a entrada u(t) e saída y(t) para extrair 126 fasores com alta coerência sinal-ruído.
- Isso comprova a transição direta do domínio do tempo para o domínio da frequência.""")

# =========================================================================
# SLIDE 6: ITEM 4 - RESULTADOS FFT
# =========================================================================
slide6 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide6, "5. [Item 4] Validação do Modelo Identificado via FFT", 
           "Reconstrução precisa da planta simulada com FIT global de 96,47%", 
           "Pedro Augusto")

card6 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
card6.fill.solid(); card6.fill.fore_color.rgb = COR_CINZA_FUNDO
card6.line.color.rgb = COR_CINZA_BORDA

tf_6 = card6.text_frame
tf_6.word_wrap = True
tf_6.margin_left = tf_6.margin_top = tf_6.margin_right = tf_6.margin_bottom = Inches(0.3)
p = tf_6.paragraphs[0]
p.text = "Comparação: Nominal vs. Identificado"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_6 = [
    "Função de Transferência Identificada:\n  G_id(s) ≈ 40,0 / (s² + 6,005 s + 4,818)\n  (Nominal: 40 / (s² + 6 s + 5)).",
    "Exatidão de Parâmetros:\n  - Polos Estimados: s1 = -0,967 e s2 = -5,038\n    (Nominais: -1,000 e -5,000 — erro < 3%).\n  - Ganho DC Estimado: 8,30 (Nominal: 8,00).",
    "Métricas Espectrais de Desempenho:\n  - FIT Global: 96,47%\n  - RMSE de Módulo: 0,165 dB\n  - RMSE de Fase: 1,025 graus",
    "Robustez a Vazamento Espectral (Leakage):\n  O estimador absorveu naturalmente as bordas finitas da FFT sem distorcer o modelo."
]
for it in items_6:
    p = tf_6.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(12.5); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(8)

img_fft = os.path.join(FIG_DIR, 'item4_simulink_bode_validacao.png')
if os.path.exists(img_fft):
    slide6.shapes.add_picture(img_fft, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide6,
"""[ORADOR: Pedro Augusto | ~1:00 min]
- Mostre o modelo estimado pelo N2CACGO a partir da FFT do Simulink.
- Os polos estimados bateram em -0,97 e -5,04 (quase idênticos aos nominais -1 e -5).
- Destaque as métricas: FIT de 96,47%, erro de módulo de 0,16 dB e erro de fase de apenas 1 grau!
- Transição: 'Agora que validamos a teoria e a simulação, passo a palavra ao Renato Felix para apresentar a identificação em bancada física real de motor elétrico.'""")

# =========================================================================
# SLIDE 7: ITEM 5 - IDENTIFICAÇÃO MOTOR CC
# =========================================================================
slide7 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide7, "6. [Item 5] Aplicação em Bancada Experimental: Motor Elétrico CC", 
           "Processamento metrológico estrito dos ensaios de SSL (Grupo 3, IME)", 
           "Renato Felix")

card7 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
card7.fill.solid(); card7.fill.fore_color.rgb = COR_CINZA_FUNDO
card7.line.color.rgb = COR_CINZA_BORDA

tf_7 = card7.text_frame
tf_7.word_wrap = True
tf_7.margin_left = tf_7.margin_top = tf_7.margin_right = tf_7.margin_bottom = Inches(0.3)
p = tf_7.paragraphs[0]
p.text = "Protocolo Experimental de Tratamento"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_7 = [
    "Base Autêntica e Confiável (Grupo 3):\n  Utilizamos exclusivamente os 26 ensaios senoidais da bancada do Grupo 3 (0,20 a 10 Hz), sem misturar com bases externas.",
    "Eliminação do Transitório de Partida:\n  Descarte estrito dos primeiros 40% das amostras de cada ensaio. A DFT foi aplicada apenas nos 60% finais estacionários.",
    "Varredura de Ordens (n = 1 a 5):\n  - 1ª Ordem: FIT = 88,36% | RMSE Mag = 0,21 dB\n  - 2ª Ordem: FIT = 85,12% | RMSE Mag = 0,22 dB\n  - 3ª Ordem: FIT = 84,82% | RMSE Mag = 0,31 dB\n  - 4ª Ordem: FIT = 87,57% | RMSE Mag = 0,21 dB",
    "Decisão de Engenharia:\n  A 1ª ordem foi selecionada pelo princípio da parcimônia e consistência física eletromecânica."
]
for it in items_7:
    p = tf_7.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(12.5); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(8)

img_motor_todas = os.path.join(FIG_DIR, 'item5_motor_bode_todas_ordens.png')
if os.path.exists(img_motor_todas):
    slide7.shapes.add_picture(img_motor_todas, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide7,
"""[ORADOR: Renato Felix | ~1:30 min]
- Agradeça ao Pedro e apresente o ensaio na bancada experimental do motor CC.
- Enfatize o rigor metrológico: usamos exclusivamente a base autêntica do Grupo 3 (26 senoides).
- Explique o descarte dos primeiros 40% de dados para eliminar o transitório de partida, garantindo regime permanente estrito.
- Mostre no gráfico que ordens superiores sofrem com ruídos de comutação (escovas) sem ganho físico, justificando a escolha da 1ª ordem.""")

# =========================================================================
# SLIDE 8: ITEM 5 - MODELO FÍSICO E PADÉ
# =========================================================================
slide8 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide8, "7. [Item 5] Análise Física do Motor e Atraso de Padé (10,2 ms)", 
           "Interpretação eletromecânica dos parâmetros e do zero no semi-plano direito", 
           "Renato Felix")

card8 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
card8.fill.solid(); card8.fill.fore_color.rgb = COR_CINZA_FUNDO
card8.line.color.rgb = COR_CINZA_BORDA

tf_8 = card8.text_frame
tf_8.word_wrap = True
tf_8.margin_left = tf_8.margin_top = tf_8.margin_right = tf_8.margin_bottom = Inches(0.3)
p = tf_8.paragraphs[0]
p.text = "Modelo Físico Eletromecânico"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_8 = [
    "Função de Transferência Identificada (FIT = 88,36%):\n  G_motor(s) = (-0,2468 s + 48,33) / (s + 4,794)",
    "Parâmetros Físicos Eletromecânicos:\n  • Ganho Estático: Km = 48,33 / 4,794 = 10,08 (rad/s)/V (20,07 dB).\n  • Constante de Tempo Mecânica: τm = 1 / 4,794 = 0,209 segundos.",
    "O Fenômeno do Zero no SPD (s = +195,8 rad/s):\n  NÃO representa instabilidade física, mas sim a APROXIMAÇÃO DE PADÉ de 1ª ordem do atraso puro de transporte:\n  e^(-s·τd) ≈ (1 - s·τd/2) / (1 + s·τd/2)\n  ==> τd = 2 / 195,8 ≈ 10,2 milissegundos!",
    "Significado Físico Real:\n  Os 10,2 ms correspondem perfeitamente ao atraso de conversão D/A, filtro e amostragem da placa de aquisição DAQ!"
]
for it in items_8:
    p = tf_8.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(12.2); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(7)

img_motor_melhor = os.path.join(FIG_DIR, 'item5_motor_melhor_modelo_bode.png')
if os.path.exists(img_motor_melhor):
    slide8.shapes.add_picture(img_motor_melhor, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide8,
"""[ORADOR: Renato Felix | ~2:15 min - Ponto Alto da Defesa!]
- Apresente os parâmetros físicos do motor: Km = 10,08 (rad/s)/V e tau_m = 0,209 s (FIT = 88,36%).
- Destaque o ponto chave para a banca: o zero no semi-plano direito em s = +195,8 rad/s.
- Explique com segurança que isso NÃO é instabilidade, mas a aproximação de Padé de 1ª ordem de um atraso puro de 10,2 ms.
- Esse atraso de 10,2 ms é o atraso de hardware da placa DAQ e explica exatamente a queda de fase experimental além de -90 graus a 10 Hz!
- Transição: 'Para mostrar a validação cega no tempo contra sinais não-senoidais, passo a palavra ao Arthur Scarpini.'""")

# =========================================================================
# SLIDE 9: ITEM 5 - VALIDAÇÃO DINÂMICA COM ONDA QUADRADA E TRIANGULAR
# =========================================================================
slide9 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide9, "8. [Item 5] Validação Temporal Cega (Regra de Ouro)", 
           "Confronto do modelo linear contra ondas quadrada e triangular inéditas a 10 Hz", 
           "Arthur Scarpini")

img_sqr = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_quadrada.png')
img_tri = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_triangular.png')

if os.path.exists(img_sqr):
    slide9.shapes.add_picture(img_sqr, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.2))

if os.path.exists(img_tri):
    slide9.shapes.add_picture(img_tri, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.2))

# Card inferior explicativo
card9_bot = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.1), Inches(11.7), Inches(1.1))
card9_bot.fill.solid(); card9_bot.fill.fore_color.rgb = COR_CINZA_FUNDO
card9_bot.line.color.rgb = COR_CINZA_BORDA
tf_9b = card9_bot.text_frame
tf_9b.word_wrap = True
tf_9b.margin_left = tf_9b.margin_top = tf_9b.margin_right = tf_9b.margin_bottom = Inches(0.12)
p = tf_9b.paragraphs[0]
p.text = "Aplicação da 'Regra de Ouro da Identificação' vista nas aulas de MASD:"
p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO
p2 = tf_9b.add_paragraph()
p2.text = "O modelo estimado com senoides foi testado cegamente com sinais não-senoidais inéditos. Na onda quadrada, reproduziu a taxa de subida exponencial (τm = 0,21 s). Na onda triangular, o polo mecânico arredondou as cúspides com defasagem idêntica à medida experimentalmente!"
p2.font.size = Pt(11.5); p2.font.color.rgb = COR_TEXTO_ESCURO; p2.space_before = Pt(2)

set_speaker_notes(slide9,
"""[ORADOR: Arthur Scarpini | ~1:15 min]
- Agradeça a Renato e cite o conceito da aula: a 'Regra de Ouro da Identificação' (nunca validar com os mesmos dados da estimação).
- Mostre os gráficos de validação cega com onda quadrada e triangular a 10 Hz.
- Destaque que o modelo linear estimado na frequência previu com alta precisão o comportamento no domínio do tempo, com a constante de tempo de 0,21 s e filtragem passa-baixas das cúspides triangulares.""")

# =========================================================================
# SLIDE 10: DIFICULDADES E CONCLUSÃO
# =========================================================================
slide10 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide10, "9. Dificuldades Numéricas Superadas e Conclusões Finais", 
           "Condicionamento da matriz Q, eliminação Gaussiana e síntese do trabalho", 
           "Arthur Scarpini")

card10_1 = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
card10_1.fill.solid(); card10_1.fill.fore_color.rgb = COR_CINZA_FUNDO
card10_1.line.color.rgb = COR_CINZA_BORDA

tf_101 = card10_1.text_frame
tf_101.word_wrap = True
tf_101.margin_left = tf_101.margin_top = tf_101.margin_right = tf_101.margin_bottom = Inches(0.25)
p = tf_101.paragraphs[0]
p.text = "Desafios Numéricos e Soluções"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

diffs_txt = [
    "1. Condicionamento Matricial de Q:\n  Para ordens n ≥ 4, os monômios (jω)^n atingem grandezas de 10^14, levando rcond(Q) para < 10^(-16).\n  Solução: Em vez da pseudoinversa pinv (que truncava direções de autovalores cruciais), mantivemos resolução direta por eliminação Gaussiana com pivoteamento (Q \\ Y), recuperando a exatidão absoluta.",
    "2. Vazamento Espectral da FFT:\n  Controlado aumentando a janela de simulação temporal e selecionando frequências com alta coerência SNR.",
    "3. Transitórios de Partida:\n  Eliminados pelo corte seletivo dos primeiros 40% das amostras na bancada."
]
for it in diffs_txt:
    p = tf_101.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(11.5); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(6)

card10_2 = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.0))
card10_2.fill.solid(); card10_2.fill.fore_color.rgb = COR_CINZA_FUNDO
card10_2.line.color.rgb = COR_CINZA_BORDA

tf_102 = card10_2.text_frame
tf_102.word_wrap = True
tf_102.margin_left = tf_102.margin_top = tf_102.margin_right = tf_102.margin_bottom = Inches(0.25)
p = tf_102.paragraphs[0]
p.text = "Conclusões do Trabalho"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

concls_txt = [
    "Elegância Convexa: O N2CACGO elimina qualquer risco de mínimos locais inerentes a métodos iterativos como Nelder-Mead.",
    "Fidelidade Acadêmica: 100% de concordância com o benchmark histórico de Silveira (2006).",
    "Integração Simulink: Sucesso na extração da FRF via Chirp + FFT com FIT superior a 96%.",
    "Consistência Experimental: O modelo de 1ª ordem do motor CC explicou com clareza a constante mecânica (0,21 s) e o atraso de hardware da placa de aquisição (10,2 ms via Padé).",
    "Repositório Aberto: Scripts MATLAB, modelo Simulink, dados brutos e artigo IEEE disponíveis em:\ngithub.com/VPariz/masd-identificacao-n2cacgo"
]
for it in concls_txt:
    p = tf_102.add_paragraph()
    p.text = "✔ " + it
    p.font.size = Pt(11.5); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(6)

set_speaker_notes(slide10,
"""[ORADOR: Arthur Scarpini & Toda a Equipe | ~2:00 min]
- Explique o desafio do condicionamento matricial rcond(Q) < 10^-16 e como a eliminação Gaussiana com pivoteamento direto (Q \\ Y) garantiu a exatidão.
- Sintetize os sucessos dos 5 itens exigidos no trabalho.
- Convide João Victor, Pedro e Renato a se reunirem à frente.
- Agradeça ao Prof. Dr. Marcelo de Araújo Oliveira e abra a apresentação formalmente para a arguição da banca!""")

prs.save(PPTX_PATH)
print(f"Apresentação PowerPoint atualizada com sucesso em: {PPTX_PATH}")
