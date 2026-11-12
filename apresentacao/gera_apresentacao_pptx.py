import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FIG_DIR = os.path.join(BASE_DIR, 'artigo', 'figuras')
PPTX_PATH = os.path.join(BASE_DIR, 'apresentacao', 'apresentacao_identificacao_N2CACGO.pptx')

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

def add_header(slide, title_text, subtitle_text=""):
    # Barra de topo
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = COR_AZUL_ESCURO

    if subtitle_text:
        p2 = tf.add_paragraph()
        p2.text = subtitle_text
        p2.font.size = Pt(13)
        p2.font.color.rgb = COR_AZUL_MEDIO
        p2.space_before = Pt(4)

    # Linha divisória sutil
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.7), Inches(0.04))
    line.fill.solid()
    line.fill.fore_color.rgb = COR_DOURADO
    line.line.color.rgb = COR_DOURADO

# =========================================================================
# SLIDE 1: CAPA
# =========================================================================
slide1 = prs.slides.add_slide(prs.slide_layouts[6])

bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg1.fill.solid()
bg1.fill.fore_color.rgb = COR_AZUL_ESCURO
bg1.line.color.rgb = COR_AZUL_ESCURO

title_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11), Inches(3.2))
tf1 = title_box.text_frame
tf1.word_wrap = True

p = tf1.paragraphs[0]
p.text = "INSTITUTO MILITAR DE ENGENHARIA"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = COR_DOURADO

p2 = tf1.add_paragraph()
p2.text = "Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO"
p2.font.size = Pt(32)
p2.font.bold = True
p2.font.color.rgb = COR_BRANCO
p2.space_before = Pt(14)

p3 = tf1.add_paragraph()
p3.text = "Fundamentação Analítica, Validação Teórica e Aplicação em Bancada de Motor CC"
p3.font.size = Pt(18)
p3.font.color.rgb = RGBColor(200, 220, 245)
p3.space_before = Pt(10)

author_box = slide1.shapes.add_textbox(Inches(1.2), Inches(5.2), Inches(11), Inches(1.8))
tf_a = author_box.text_frame
p4 = tf_a.paragraphs[0]
p4.text = "Autores: João Victor Tavares Pariz, Pedro Augusto, Renato Felix, Scarpini\nDocente: Prof. Dr. Marcelo de Araújo Oliveira\nDisciplina: Modelagem e Análise de Sistemas Dinâmicos (MASD)"
p4.font.size = Pt(14)
p4.font.color.rgb = RGBColor(220, 230, 245)

# =========================================================================
# SLIDE 2: MOTIVAÇÃO E O QUE É O N2CACGO
# =========================================================================
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide2, "1. Contextualização: Identificação no Domínio da Frequência", "Por que N2CACGO? Vantagens frente a abordagens clássicas")

# Card Esquerdo
card1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
card1.fill.solid(); card1.fill.fore_color.rgb = COR_CINZA_FUNDO
card1.line.color.rgb = COR_CINZA_BORDA

tf_c1 = card1.text_frame
tf_c1.word_wrap = True
tf_c1.margin_left = tf_c1.margin_top = tf_c1.margin_right = tf_c1.margin_bottom = Inches(0.3)
p = tf_c1.paragraphs[0]
p.text = "Identificação Frequencial vs. Temporal"
p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_c1 = [
    "Foco direto na faixa de operação útil (largura de banda, margem de fase, ressonância).",
    "Filtragem natural de ruídos estocásticos fora da banda de interesse.",
    "Independência das condições iniciais x(0) do sistema.",
    "Imunidade a derivas de nível DC e facilidade no tratamento de atrasos de transporte."
]
for it in items_c1:
    p = tf_c1.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(14); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(10)

# Card Direito
card2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.0))
card2.fill.solid(); card2.fill.fore_color.rgb = COR_CINZA_FUNDO
card2.line.color.rgb = COR_CINZA_BORDA

tf_c2 = card2.text_frame
tf_c2.word_wrap = True
tf_c2.margin_left = tf_c2.margin_top = tf_c2.margin_right = tf_c2.margin_bottom = Inches(0.3)
p = tf_c2.paragraphs[0]
p.text = "O Método N2CACGO (Silveira, 2006)"
p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_c2 = [
    "Norma 2 Convexo Analítico Conjunto Gerador Ótimo (IME, 2006).",
    "Problema de otimização ESTRITAMENTE CONVEXO em norma 2.",
    "Solução ANALÍTICA global única via Sistema de Equações Lineares (SEL): Qθ = Y.",
    "Elimina otimizações não-lineares heurísticas (e.g. fminsearch / Nelder-Mead) que sofrem com mínimos locais.",
    "Capacidade natural de modelar polos reais, complexos conjugados e zeros arbitrários."
]
for it in items_c2:
    p = tf_c2.add_paragraph()
    p.text = "• " + it
    p.font.size = Pt(14); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(10)

# =========================================================================
# SLIDE 3: FORMULAÇÃO MATEMÁTICA
# =========================================================================
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide3, "2. Formulação Matemática do N2CACGO", "Estrutura polinomial, função custo e equacionamento matricial")

card3 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
card3.fill.solid(); card3.fill.fore_color.rgb = COR_CINZA_FUNDO
card3.line.color.rgb = COR_CINZA_BORDA

tf3 = card3.text_frame
tf3.word_wrap = True
tf3.margin_left = tf3.margin_top = tf3.margin_right = tf3.margin_bottom = Inches(0.4)

p = tf3.paragraphs[0]
p.text = "1. Modelo Estimado de Ordem n (Bipróprio):"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

p = tf3.add_paragraph()
p.text = "   Ge(s) = N(α, s) / D(β, s) = (α0 s^n + α1 s^{n-1} + ... + αn) / (s^n + β1 s^{n-1} + ... + βn),   onde β0 = 1"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COR_AZUL_MEDIO; p.space_before = Pt(4)

p = tf3.add_paragraph()
p.text = "2. Função Custo Convexa (Erro de Equação em Norma 2):"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO; p.space_before = Pt(14)

p = tf3.add_paragraph()
p.text = "   JS(θ) = || D(β, jω) G(jω) - N(α, jω) ||_2^2 = Σ | D(β, jω_i) G(jω_i) - N(α, jω_i) |^2"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COR_AZUL_MEDIO; p.space_before = Pt(4)

p = tf3.add_paragraph()
p.text = "3. Resolução Analítica Global via SEL Particionado:"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO; p.space_before = Pt(14)

p = tf3.add_paragraph()
p.text = "   [ Q1   -Q2 ] [ α ]   [ Y1 ]\n   [ Q3   -Q4 ] [ β ] = [ Y2 ]    ===>    θ = Q \\ Y    (Solução instantânea e sem aproximações numéricas)"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = RGBColor(180, 40, 20); p.space_before = Pt(4)

p = tf3.add_paragraph()
p.text = "   onde Q1 = Re{R R^H},  Q2 = Re{R S* R^H(:, 2:n+1)},  Q3 = Re{R(2:n+1,:) S R^H},  Q4 = Re{R(2:n+1,:) S S* R^H(:, 2:n+1)}"
p.font.size = Pt(13); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

# =========================================================================
# SLIDE 4: ITEM 3 - VALIDAÇÃO ACADÊMICA (SILVEIRA 2006)
# =========================================================================
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide4, "3. [Item 3] Validação: Exemplo 3.4.1 de Silveira (2006)", "Reprodução fiel do sistema bipróprio de 7ª ordem e fase mínima da literatura")

# Inserção da Imagem
img_silv = os.path.join(FIG_DIR, 'item3_exemplo_silveira_bode.png')
if os.path.exists(img_silv):
    slide4.shapes.add_picture(img_silv, Inches(0.8), Inches(1.8), Inches(6.5), Inches(5.0))

# Caixa lateral com Tabela e Comentários
card_t3 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.6), Inches(1.8), Inches(4.9), Inches(5.0))
card_t3.fill.solid(); card_t3.fill.fore_color.rgb = COR_CINZA_FUNDO
card_t3.line.color.rgb = COR_CINZA_BORDA

tf_t3 = card_t3.text_frame
tf_t3.word_wrap = True
tf_t3.margin_left = tf_t3.margin_top = tf_t3.margin_right = tf_t3.margin_bottom = Inches(0.25)

p = tf_t3.paragraphs[0]
p.text = "Confronto com Tabela 3.2 de Silveira:"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

tab_text = (
    "Ordem | J (Implementado) | J1 (Silveira)\n"
    "-----------------------------------------\n"
    "  1ª   |     15,053       |    15,126\n"
    "  2ª   |      3,027       |     3,018\n"
    "  3ª   |      1,459       |     1,466\n"
    "  4ª   |    6,290e-4      |   6,320e-4\n"
    "  5ª   |    3,743e-4      |   3,795e-4\n"
    "  6ª   |    3,533e-4      |   6,306e-4\n"
    "  7ª   |    3,865e-4      |   3,439e-4\n"
)
p = tf_t3.add_paragraph()
p.text = tab_text
p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = COR_AZUL_MEDIO; p.space_before = Pt(6)

p = tf_t3.add_paragraph()
p.text = "Principais Conclusões:\n• Exata concordância numérica com a dissertação.\n• A partir de n = 4, o erro decai para ordem 10^-4 (FIT = 99,98%).\n• O método atua eficientemente na redução balanceada de modelos."
p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(6)

# =========================================================================
# SLIDE 5: ITEM 4 - SIMULINK + FFT + IDENTIFICAÇÃO
# =========================================================================
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide5, "4. [Item 4] Simulação Temporal no Simulink e FFT", "Geração de chirp (0,1 a 15 Hz), extração da FRF empírica e ajuste N2CACGO")

img_temp4 = os.path.join(FIG_DIR, 'item4_simulink_sinais_temporais.png')
img_bode4 = os.path.join(FIG_DIR, 'item4_simulink_bode_validacao.png')

if os.path.exists(img_temp4):
    slide5.shapes.add_picture(img_temp4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))

if os.path.exists(img_bode4):
    slide5.shapes.add_picture(img_bode4, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))

# =========================================================================
# SLIDE 6: ITEM 5 - IDENTIFICAÇÃO DO MOTOR EXPERIMENTAL
# =========================================================================
slide6 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide6, "5. [Item 5] Identificação do Motor DC (Dados de Bancada)", "Ensaios de Sinais e Sistemas Lineares (SSL - Grupo 3, IME)")

img_mot_all = os.path.join(FIG_DIR, 'item5_motor_bode_todas_ordens.png')
if os.path.exists(img_mot_all):
    slide6.shapes.add_picture(img_mot_all, Inches(0.8), Inches(1.8), Inches(6.5), Inches(5.0))

card_t5 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.6), Inches(1.8), Inches(4.9), Inches(5.0))
card_t5.fill.solid(); card_t5.fill.fore_color.rgb = COR_CINZA_FUNDO
card_t5.line.color.rgb = COR_CINZA_BORDA

tf_t5 = card_t5.text_frame
tf_t5.word_wrap = True
tf_t5.margin_left = tf_t5.margin_top = tf_t5.margin_right = tf_t5.margin_bottom = Inches(0.25)

p = tf_t5.paragraphs[0]
p.text = "Tabela Comparativa de Ordens (1 a 5):"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

tab_m = (
    "Ordem | Custo J | RMSE Mag | RMSE Fase | FIT (%)\n"
    "-------------------------------------------------\n"
    " 1ª   |  1,7468 | 0,22 dB  |  2,19°    | 88,36 %\n"
    " 2ª   |  2,2320 | 0,22 dB  |  2,76°    | 85,12 %\n"
    " 3ª   |  2,2780 | 0,32 dB  |  2,85°    | 84,82 %\n"
    " 4ª   |  1,8653 | 0,21 dB  |  2,34°    | 87,57 %\n"
    " 5ª   |  3,6628 | 0,68 dB  |  5,46°    | 75,59 %\n"
)
p = tf_t5.add_paragraph()
p.text = tab_m
p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = COR_AZUL_MEDIO; p.space_before = Pt(6)

p = tf_t5.add_paragraph()
p.text = "Compromisso de Parcimônia:\n• A 1ª ordem atinge o menor custo J (1,7468) e menor RMSE (0,22 dB).\n• Aumentar a ordem para 2 ou 3 não melhora o ajuste e introduz polos/zeros de alta frequência espúrios."
p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(6)

# =========================================================================
# SLIDE 7: ANÁLISE FÍSICA DO MODELO DO MOTOR
# =========================================================================
slide7 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide7, "6. Análise Física da Função de Transferência do Motor", "Interpretação eletromecânica dos parâmetros identificados")

img_best = os.path.join(FIG_DIR, 'item5_motor_melhor_modelo_bode.png')
if os.path.exists(img_best):
    slide7.shapes.add_picture(img_best, Inches(0.8), Inches(1.8), Inches(6.5), Inches(5.0))

card_f = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.6), Inches(1.8), Inches(4.9), Inches(5.0))
card_f.fill.solid(); card_f.fill.fore_color.rgb = COR_CINZA_FUNDO
card_f.line.color.rgb = COR_CINZA_BORDA

tf_f = card_f.text_frame
tf_f.word_wrap = True
tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = Inches(0.3)

p = tf_f.paragraphs[0]
p.text = "Modelo de 1ª Ordem Identificado:"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

p = tf_f.add_paragraph()
p.text = "G(s) = (-0,2468 s + 48,33) / (s + 4,794)\n     ≈ 10,08 / (0,209 s + 1)"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = RGBColor(180, 40, 20); p.space_before = Pt(6)

p = tf_f.add_paragraph()
p.text = "Conexão com a Teoria Eletromecânica:\n" \
         "1. Ganho Estático:\n   Km = 48,33 / 4,794 = 10,08 (20,07 dB).\n" \
         "2. Polo Dominante Mecânico:\n   s = -4,794 rad/s  =>  τm ≈ 0,209 s.\n" \
         "3. Constante Elétrica:\n   Como τe = La/Ra << τm, a 1ª ordem domina a faixa de teste até 10 Hz.\n" \
         "4. Atraso e Fase Não-Mínima:\n   O zero em s = +195,8 rad/s é a aproximação de Padé do atraso puro de transporte (τd ≈ 10,2 ms)."
p.font.size = Pt(11); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(6)

# =========================================================================
# SLIDE 8: VALIDAÇÃO TEMPORAL: ONDA QUADRADA E TRIANGULAR
# =========================================================================
slide8 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide8, "7. Validação Dinâmica com Sinais Não-Senoidais", "Resposta temporal do modelo identificado vs saída experimental real a 10 Hz")

img_sqr = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_quadrada.png')
img_tri = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_triangular.png')

if os.path.exists(img_sqr):
    slide8.shapes.add_picture(img_sqr, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))

if os.path.exists(img_tri):
    slide8.shapes.add_picture(img_tri, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))

# =========================================================================
# SLIDE 9: DIFICULDADES ENCONTRADAS E SOLUÇÕES
# =========================================================================
slide9 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide9, "8. Dificuldades Encontradas e Soluções Adotadas", "Desafios numéricos, processamento de sinais e modelagem prática")

diffs = [
    ("Condicionamento Numérico de Q em Ordens Altas",
     "Para ordens n >= 6, as potências (jω)^n geram números com ordens de grandeza muito díspares.",
     "Solução: Normalização do vetor de frequências e uso de pseudoinversa (pinv) via SVD quando rcond(Q) < 1e-15."),

    ("Fugas Espectrais (Leakage) na FFT",
     "O truncamento temporal abrupto no cálculo da FFT introduz espalhamento de energia espectral nas bordas.",
     "Solução: Seleção cuidadosa da janela temporal e descarte de frequências sem excitação ativa do Chirp."),

    ("Perturbações de Partida e Ruído de Bancada",
     "Os ensaios experimentais do motor contêm transitórios de aceleração inicial e ruído do sensor.",
     "Solução: Processamento DFT restrito aos últimos 60% das amostras (regime permanente puramente forçado).")
]

for i, (tit, desc, sol) in enumerate(diffs):
    card_d = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8 + i*1.7), Inches(11.7), Inches(1.45))
    card_d.fill.solid(); card_d.fill.fore_color.rgb = COR_CINZA_FUNDO
    card_d.line.color.rgb = COR_CINZA_BORDA

    tf_d = card_d.text_frame
    tf_d.word_wrap = True
    tf_d.margin_left = tf_d.margin_top = tf_d.margin_right = tf_d.margin_bottom = Inches(0.18)

    p = tf_d.paragraphs[0]
    p.text = f"{i+1}. {tit}"
    p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

    p2 = tf_d.add_paragraph()
    p2.text = f"Problema: {desc}"
    p2.font.size = Pt(12); p2.font.color.rgb = RGBColor(160, 40, 20); p2.space_before = Pt(2)

    p3 = tf_d.add_paragraph()
    p3.text = f"Abordagem: {sol}"
    p3.font.size = Pt(12); p3.font.color.rgb = RGBColor(20, 110, 50); p3.space_before = Pt(2)

# =========================================================================
# SLIDE 10: CONCLUSÃO
# =========================================================================
slide10 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide10, "9. Conclusões e Considerações Finais", "Síntese dos resultados obtidos no trabalho de MASD")

card_c = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
card_c.fill.solid(); card_c.fill.fore_color.rgb = COR_CINZA_FUNDO
card_c.line.color.rgb = COR_CINZA_BORDA

tf_c = card_c.text_frame
tf_c.word_wrap = True
tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = Inches(0.4)

concls = [
    "O método N2CACGO comprovou ser uma ferramenta analítica extremamente elegante, rápida e robusta para identificação SISO no domínio da frequência.",
    "A solução analítica via sistema linear particionado (Qθ = Y) elimina qualquer risco de mínimos locais inerentes a algoritmos heurísticos como o Nelder-Mead.",
    "A validação acadêmica reproduziu com exatidão os custos de erro tabelados na dissertação de Bruno de Pinho Silveira (IME, 2006).",
    "A integração temporal Simulink + FFT demonstrou a viabilidade de estimar a FRF empírica e recuperar plantas LTI com FIT superior a 96%.",
    "A identificação prática da bancada do motor CC revelou que o modelo de 1ª ordem (K ≈ 10,08, τm ≈ 0,21 s) representa com precisão cirúrgica a dinâmica dominante mecânica (RMSE de magnitude de apenas 0,21 dB), validado com sucesso em ondas quadrada e triangular."
]

for idx, c in enumerate(concls):
    p = tf_c.paragraphs[0] if idx == 0 else tf_c.add_paragraph()
    p.text = f"✔  {c}"
    p.font.size = Pt(14); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(12)

prs.save(PPTX_PATH)
print(f"Apresentação PowerPoint salva com sucesso em: {PPTX_PATH}")
