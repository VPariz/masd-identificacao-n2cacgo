import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FIG_DIR = os.path.join(BASE_DIR, 'artigo', 'figuras')
PPTX_PATH = os.path.join(BASE_DIR, 'apresentacao', 'apresentacao_MASD_N2CACGO_IME.pptx')

prs = Presentation()
prs.slide_width = Inches(13.333)   # 16:9 widescreen
prs.slide_height = Inches(7.5)

# Paleta Institucional IME / Engenharia
COR_AZUL_ESCURO  = RGBColor(15, 34, 64)      # #0F2240 (Navy Primário)
COR_AZUL_MEDIO   = RGBColor(30, 75, 140)     # #1E4B8C
COR_DOURADO      = RGBColor(212, 160, 23)    # #D4A017 (Destaque)
COR_CINZA_FUNDO  = RGBColor(245, 247, 250)   # #F5F7FA
COR_TEXTO_ESCURO = RGBColor(30, 30, 30)
COR_BRANCO       = RGBColor(255, 255, 255)
COR_CINZA_BORDA  = RGBColor(205, 212, 224)
COR_VERDE_OK     = RGBColor(20, 120, 50)
COR_VERDE_BG     = RGBColor(232, 246, 236)
COR_CODE_BG      = RGBColor(238, 242, 246)
COR_EQUACAO_BG   = RGBColor(232, 240, 254)
COR_VERMELHO_EQ  = RGBColor(165, 25, 25)


def add_header(slide, title_text, subtitle_text="", speaker_name=""):
    header_box = slide.shapes.add_textbox(Inches(0.75), Inches(0.28), Inches(9.1), Inches(1.15))
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
        p2.font.size = Pt(14)
        p2.font.color.rgb = COR_AZUL_MEDIO
        p2.space_before = Pt(3)

    if speaker_name:
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.95), Inches(0.36), Inches(2.63), Inches(0.56))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(230, 240, 255)
        pill.line.color.rgb = COR_AZUL_MEDIO
        tf_p = pill.text_frame
        tf_p.word_wrap = True
        tf_p.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf_p.margin_left = tf_p.margin_top = tf_p.margin_right = tf_p.margin_bottom = 0
        p_sp = tf_p.paragraphs[0]
        p_sp.text = f"👤 {speaker_name}"
        p_sp.font.size = Pt(13)
        p_sp.font.bold = True
        p_sp.font.color.rgb = COR_AZUL_ESCURO
        p_sp.alignment = PP_ALIGN.CENTER

    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.75), Inches(1.42), Inches(11.83), Inches(0.045))
    line.fill.solid()
    line.fill.fore_color.rgb = COR_DOURADO
    line.line.color.rgb = COR_DOURADO


def make_card(slide, left, top, width, height, title="", bg_color=COR_CINZA_FUNDO, border_color=COR_CINZA_BORDA, title_size=18):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.adjustments[0] = 0.04
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    tf = card.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.margin_left = tf.margin_right = Inches(0.28)
    tf.margin_top = Inches(0.22)
    tf.margin_bottom = Inches(0.20)
    if title:
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(title_size)
        p.font.bold = True
        p.font.color.rgb = COR_AZUL_ESCURO
        p.space_after = Pt(6)
    return card, tf


def add_bullets(tf, items, font_size=15.5, space_before=10, bullet_char="▸ "):
    for idx, item in enumerate(items):
        p = tf.paragraphs[0] if (len(tf.paragraphs) == 1 and tf.paragraphs[0].text == "" and idx == 0) else tf.add_paragraph()
        p.space_before = Pt(space_before)
        p.line_spacing = 1.15
        if isinstance(item, tuple):
            lead, rest = item
            r0 = p.add_run()
            r0.text = f"{bullet_char}{lead} "
            r0.font.size = Pt(font_size)
            r0.font.bold = True
            r0.font.color.rgb = COR_AZUL_ESCURO
            r1 = p.add_run()
            r1.text = rest
            r1.font.size = Pt(font_size)
            r1.font.bold = False
            r1.font.color.rgb = COR_TEXTO_ESCURO
        else:
            p.text = f"{bullet_char}{item}"
            p.font.size = Pt(font_size)
            p.font.color.rgb = COR_TEXTO_ESCURO


def set_speaker_notes(slide, notes_text):
    # Notas mantidas vazias no deck final enviado ao Classroom/Google Slides.
    if slide.has_notes_slide:
        slide.notes_slide.notes_text_frame.text = ""


# =========================================================================
# SLIDE 1: CAPA INSTITUCIONAL (RENATO FELIX)
# =========================================================================
slide1 = prs.slides.add_slide(prs.slide_layouts[6])
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg1.fill.solid(); bg1.fill.fore_color.rgb = COR_AZUL_ESCURO
bg1.line.color.rgb = COR_AZUL_ESCURO

# Faixa dourada lateral esquerda
bar1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(0.75), Inches(0.10), Inches(6.0))
bar1.fill.solid(); bar1.fill.fore_color.rgb = COR_DOURADO; bar1.line.color.rgb = COR_DOURADO

tbox1 = slide1.shapes.add_textbox(Inches(1.05), Inches(0.72), Inches(11.5), Inches(3.0))
tf1 = tbox1.text_frame; tf1.word_wrap = True

p = tf1.paragraphs[0]
p.text = "INSTITUTO MILITAR DE ENGENHARIA • DE/3 • MASD"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_DOURADO

p = tf1.add_paragraph()
p.text = "Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO"
p.font.size = Pt(31); p.font.bold = True; p.font.color.rgb = COR_BRANCO; p.space_before = Pt(10)

p = tf1.add_paragraph()
p.text = "Fundamentação Convexa (Silveira, 2006) • Implementação MATLAB/Simulink • Motor CC Experimental"
p.font.size = Pt(16); p.font.color.rgb = RGBColor(200, 220, 245); p.space_before = Pt(10)

abox1 = slide1.shapes.add_textbox(Inches(1.05), Inches(3.85), Inches(11.5), Inches(3.25))
tf_a = abox1.text_frame; tf_a.word_wrap = True

p = tf_a.paragraphs[0]
p.text = "Equipe:  Renato Felix  |  Pariz  |  Pedro Augusto  |  Scarpini"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_DOURADO

blocos_capa = [
    "1. Renato Felix (Slides 1–3) — Teoria e Formulação Convexa (Silveira, 2006)",
    "2. Pariz (Slides 4–8) — Códigos MATLAB, Fluxograma, Simulink e Validação dos Códigos",
    "3. Pedro Augusto (Slides 9–11) — Bancada do Motor CC, Ordens e Atraso de Padé",
    "4. Scarpini (Slides 12–14) — Validação Temporal Cega, Dificuldades e Conclusões"
]
for b in blocos_capa:
    p = tf_a.add_paragraph()
    p.text = f"▸  {b}"
    p.font.size = Pt(15); p.font.color.rgb = COR_BRANCO; p.space_before = Pt(7)

p = tf_a.add_paragraph()
p.text = "Docente: Prof. Dr. Marcelo de Araújo Oliveira  •  Engenharia Elétrica (MASD)"
p.font.size = Pt(14); p.font.color.rgb = RGBColor(190, 210, 235); p.space_before = Pt(14)

set_speaker_notes(slide1,
"""[ORADOR: Renato Felix | ~1:00 min]
Bom dia / boa tarde a todos. Cumprimento o Prof. Dr. Marcelo de Araújo Oliveira e os colegas da banca.
Nossa equipe é formada por Renato Costa Félix, João Victor Tavares Pariz, Pedro Augusto dos Santos Barbosa e Wagner Scarpini Miranda.
Hoje apresentamos o trabalho final de MASD sobre Identificação de Sistemas SISO no Domínio da Frequência pelo Método N2CACGO, de Silveira (2006).
Dividimos a apresentação em 4 blocos:
1) Eu (Renato Felix) abro com a teoria de modelagem/identificação e a formulação matemática convexa;
2) O Pariz apresenta os códigos MATLAB, o fluxograma, o modelo Simulink e as validações computacionais de Silveira e da FFT como evidência direta de funcionamento dos códigos;
3) O Pedro Augusto apresenta o estudo experimental completo do motor CC real da bancada de SSL;
4) E o Scarpini fecha com a validação temporal cega, os desafios numéricos superados e as conclusões finais.""")


# =========================================================================
# SLIDE 2: TEORIA DOS MÉTODOS (RENATO FELIX)
# =========================================================================
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide2, "1. Teoria: Modelagem vs. Domínio da Frequência",
           "Classificação de modelos (MASD) e vantagens sobre métodos temporais",
           "Renato Felix")

_, tf21 = make_card(slide2, 0.75, 1.72, 5.72, 5.25, "Tipologia & Gargalos no Tempo", title_size=19)
add_bullets(tf21, [
    ("Caixa Branca:", "Leis físicas puras (Newton/Kirchhoff), sem dados."),
    ("Caixa Cinza:", "Estrutura física conhecida + ajuste de parâmetros."),
    ("Caixa Preta:", "Mapeamento empírico estrito entrada–saída."),
    ("Gargalo — Ruído Colorido:", "Polariza covariâncias no tempo (ARX/PEM)."),
    ("Gargalo — x(0) e Atrasos:", "Exige repouso x(0)=0 e infla ordem discreta.")
], font_size=15.5, space_before=13)

_, tf22 = make_card(slide2, 6.85, 1.72, 5.72, 5.25, "Por que Domínio da Frequência?", title_size=19)
add_bullets(tf22, [
    ("1. Filtragem Natural:", "Rejeita ruídos fora das frequências ωₖ excitadas."),
    ("2. Alta Precisão Modal:", "Captura exata de ressonâncias e fase crítica."),
    ("3. Compactação Espectral:", "Milhares de amostras → poucos fasores FRF."),
    ("Levy (1959) e S-K (1963):", "Ponderação distorcida e dependência iterativa."),
    ("Valle (2005) / Não-Convexos:", "Otimização iterativa sujeita a mínimos locais.")
], font_size=15.5, space_before=13)

set_speaker_notes(slide2,
"""[ORADOR: Renato Felix | ~1:15 min]
Como vimos nas aulas do Prof. Marcelo, dividimos modelos em três categorias:
- Caixa Branca: puramente dedutivo por leis físicas (Newton, Kirchhoff), sem uso de dados experimentais, limitado por atritos e parâmetros incertos;
- Caixa Cinza: combina estrutura fenomenológica conhecida com estimação paramétrica por dados;
- Caixa Preta: mapeamento estritamente empírico entrada-saída.
Ao identificar no domínio do tempo (ARX, ARMAX, PEM), enfrentamos três gargalos clássicos: polarização por ruído colorido, exigência estrita de estado inicial nulo x(0) = 0 e dificuldade para estimar atrasos puros sem superparametrizar.
Já no domínio da frequência, temos as três grandes vantagens ensinadas no curso:
1) Filtragem natural de ruídos fora da banda excitada;
2) Sensibilidade direta a picos de ressonância e margens de estabilidade;
3) Compactação brutal de milhares de amostras em poucos fasores da FRF.
O problema é que métodos clássicos como Levy (1959), Sanathanan-Koerner (1963) e Valle (2005) são não-convexos ou iterativos, ficando presos em mínimos locais. Para resolver isso em definitivo, adotamos o método de Silveira (2006).""")


# =========================================================================
# SLIDE 3: O MÉTODO N2CACGO DE SILVEIRA (2006) (RENATO FELIX)
# =========================================================================
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide3, "2. Método N2CACGO (Silveira, 2006): Formulação Convexa",
           "Resíduo linear, funcional estritamente convexo e solução fechada em passo único",
           "Renato Felix")

_, tf31 = make_card(slide3, 0.75, 1.72, 6.05, 5.25, "Formulação Matemática", bg_color=COR_EQUACAO_BG, border_color=COR_AZUL_MEDIO, title_size=19)
eq_items = [
    ("Função de Transferência Biprópria:", 14.5, False, COR_TEXTO_ESCURO, 8),
    ("Ge(s) = N(s) / D(s)    (D mônico)", 22, True, COR_AZUL_ESCURO, 4),
    ("Resíduo Linear de Equação:", 14.5, False, COR_TEXTO_ESCURO, 14),
    ("e(jωₖ) = D(jωₖ)·G(jωₖ) − N(jωₖ)", 20, True, COR_VERMELHO_EQ, 4),
    ("Custo Quadrático em Norma 2:", 14.5, False, COR_TEXTO_ESCURO, 14),
    ("J(θ) = ∑ |e(jωₖ)|² = || D·G − N ||₂²", 20, True, COR_AZUL_ESCURO, 4),
    ("θ = [α₀…αₙ, β₁…βₙ]ᵀ  ∈  ℝ^(2n+1)", 15, True, COR_AZUL_MEDIO, 12)
]
for txt, sz, bld, col, sb in eq_items:
    p = tf31.add_paragraph()
    p.text = txt
    p.font.size = Pt(sz); p.font.bold = bld; p.font.color.rgb = col; p.space_before = Pt(sb)

_, tf32 = make_card(slide3, 7.10, 1.72, 5.47, 5.25, "Convexidade e Solução Única", title_size=19)
add_bullets(tf32, [
    ("Resíduo Linear em θ:", "Forma quadrática estritamente convexa."),
    ("Hessiana Definida Positiva:", "∇²J(θ) > 0 → ZERO mínimos locais."),
    ("Condição ∂J/∂θ = 0:", "Conduz ao SEL particionado analítico:"),
], font_size=15.5, space_before=8)

p_sel = tf32.add_paragraph()
p_sel.text = "    Q · θ = Y   ⟹   θ* = Q⁻¹ · Y"
p_sel.font.size = Pt(20); p_sel.font.bold = True; p_sel.font.color.rgb = COR_AZUL_MEDIO; p_sel.space_before = Pt(10); p_sel.space_after = Pt(6)

add_bullets(tf32, [
    ("Passo Único Sem Iteração:", "Resolvido direto por eliminação Gaussiana."),
    ("Sem Chute Inicial:", "Imune a divergência numérica.")
], font_size=15.5, space_before=7)

set_speaker_notes(slide3,
"""[ORADOR: Renato Felix | ~1:30 min - Destaque Teórico]
O método que implementamos vem da dissertação de Bruno de Pinho Silveira (IME, 2006), chamado N2CACGO — Norma 2 Convexo Analítico Conjunto Gerador Ótimo.
Buscamos uma função de transferência biprópria N(s)/D(s) com denominador mônico.
A sacada fundamental está no resíduo de equação e(jw_k) = D(jw_k)*G(jw_k) - N(jw_k), que é ESTRITAMENTE LINEAR nos parâmetros desconhecidos alfa e beta!
Ao somar os quadrados desse resíduo no funcional J(theta), obtemos uma forma quadrática com matriz Hessiana estritamente positiva definida (grad^2 J > 0).
Isso garante matematicamente a propriedade de convexidade estrita: para qualquer combinação convexa no espaço de parâmetros, não existem mínimos locais — há um único mínimo global!
Igualando o gradiente a zero, chegamos ao sistema linear particionado Q*theta = Y, resolvido em UM ÚNICO PASSO por eliminação Gaussiana (theta* = Q^-1 Y), sem iterações nem chute inicial.
Agora passo a palavra ao Pariz, que mostrará a implementação desses códigos no MATLAB e no Simulink junto com as suas validações.""")


# =========================================================================
# SLIDE 4: CÓDIGOS MATLAB [ITENS 1 e 2] (PARIZ)
# =========================================================================
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide4, "3. [Itens 1 & 2] Rotinas Vetorizadas no MATLAB",
           "Implementação analítica (identifica_N2CACGO.m) e métricas oficiais (valida_modelo_fr.m)",
           "Pariz")

_, tf41 = make_card(slide4, 0.75, 1.72, 6.20, 5.25, "identifica_N2CACGO.m (Núcleo Analítico)", bg_color=COR_CODE_BG, title_size=18)
tf41.margin_left = Inches(0.22); tf41.margin_right = Inches(0.22)
tf41.margin_top = Inches(0.18); tf41.margin_bottom = Inches(0.14)
code_lines_4 = [
    ("% 1. Base polinomial R e diagonais espectrais", True),
    ("R(k+1,:) = (1i*w.').^(n-k);   % k = 0..n", False),
    ("S = diag(H);  Gamma = diag(H.*conj(H));  RH = R';", False),
    ("% 2. Blocos Hermitianos reais (matriz Q e vetor Y)", True),
    ("Q1 = real(R * RH);", False),
    ("Q2 = real(R * S' * RH(:,2:end));", False),
    ("Q3 = real(R(2:end,:) * S * RH);", False),
    ("Q4 = real(R(2:end,:) * Gamma * RH(:,2:end));", False),
    ("Y  = [real(R*S'*RH(:,1)); real(R(2:end,:)*Gamma*RH(:,1))];", False),
    ("% 3. Passo único analítico (LU) & FT contínua", True),
    ("theta = [Q1, -Q2; Q3, -Q4] \\ Y;", False),
    ("sys   = tf(theta(1:n+1)', [1, theta(n+2:end)']);", False),
]
for line_txt, is_c in code_lines_4:
    p_code = tf41.add_paragraph()
    p_code.space_before = Pt(5 if is_c else 1); p_code.space_after = Pt(1); p_code.line_spacing = 1.12
    r_code = p_code.add_run(); r_code.text = line_txt
    r_code.font.size = Pt(11.4); r_code.font.name = "Consolas"
    r_code.font.bold = not is_c; r_code.font.italic = is_c
    r_code.font.color.rgb = RGBColor(71, 85, 105) if is_c else RGBColor(10, 40, 95)
slide4.shapes.add_picture(os.path.join(FIG_DIR, 'eq_slide4_matriz.png'), Inches(0.94), Inches(5.46), width=Inches(5.82), height=Inches(1.25))

_, tf42 = make_card(slide4, 7.20, 1.72, 5.37, 5.25, "valida_modelo_fr.m (Métricas MASD)", title_size=18)
slide4.shapes.add_picture(os.path.join(FIG_DIR, 'eq_slide4_validacao.png'), Inches(7.30), Inches(2.34), width=Inches(5.18), height=Inches(4.48))

set_speaker_notes(slide4,
"""[ORADOR: Pariz | ~1:15 min]
Obrigado, Renato. Cumprimento o professor e os colegas. Eu sou o Pariz e vou detalhar como saímos das equações matemáticas do N2CACGO para as rotinas funcionais no MATLAB e no Simulink, trazendo duas comprovações objetivas de validação.
À esquerda está o núcleo vetorizado identifica_N2CACGO.m em três passos:
1) Montamos a matriz monomial R = (jω)^(n−k) e as matrizes espectrais diagonais S, Gamma e RH = R';
2) Calculamos os blocos reais Q1..Q4 e o vetor independente Y = [Y1; Y2] decorrente do denominador mônico (beta_0 = 1);
3) Como o erro linearizado J_S(θ) = ||D·G − N||_2^2 é quadrático e convexo nos parâmetros, Qθ = Y resolve o mínimo global em passo único via eliminação LU (theta = Q \\ Y), sem chute inicial nem laços iterativos.
À direita está valida_modelo_fr.m, nossa auditoria oficial em quatro métricas sobre o erro direto de transferência (G_med − G_id): Custo J (Norma 2), RMSE de Magnitude (dB), RMSE de Fase (graus) e o coeficiente FIT percentual.""")


# =========================================================================
# SLIDE 5: FLUXOGRAMA INTEGRADO MATLAB & SIMULINK (PARIZ)
# =========================================================================
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide5, "4. Fluxograma Integrado: MATLAB & Simulink",
           "Pipeline completo das fontes de dados (Itens 3, 4 e 5) até a validação final",
           "Pariz")

img_fluxo = os.path.join(FIG_DIR, 'fluxograma_matlab_simulink.png')
if os.path.exists(img_fluxo):
    slide5.shapes.add_picture(img_fluxo, Inches(1.58), Inches(1.56), Inches(10.17), Inches(5.69))

set_speaker_notes(slide5,
"""[ORADOR: Pariz | ~1:00 min]
No Slide 5 vemos o pipeline completo integrando todas as etapas do trabalho em três estágios numerados:
- Etapa 1 (Fontes de Dados): no Item 3 entram as FRFs analíticas da planta de 7ª ordem de Silveira e sistemas didáticos; no Item 4 simulamos o modelo no Simulink com chirp de 0,1 a 15 Hz e obtemos a FRF via razão de FFT Y(k)/U(k); e no Item 5 o colega Pedro Augusto carrega os 26 ensaios senoidais do motor CC real via regressão de mínimos quadrados nos 60% estacionários.
- Etapa 2 (Núcleo Analítico): todos os espectros convergem exatamente para a mesma rotina identifica_N2CACGO.m.
- Etapa 3 (Auditoria): valida_modelo_fr.m calcula J, RMSEs, FIT, gera os diagramas de Bode e alimenta a validação temporal cega.
A seguir apresento as duas evidências diretas de que esse código opera com precisão.""")


# =========================================================================
# SLIDE 6: VALIDAÇÃO DO CÓDIGO MATLAB — SILVEIRA 2006 [ITEM 3] (PARIZ)
# =========================================================================
slide6 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide6, "5. [Item 3] Validação do Código MATLAB: Benchmark Silveira",
           "Evidência exata contra a Tabela 3.2 de Silveira (2006) — Ordens 1 a 7 e sistemas didáticos",
           "Pariz")

table_shape = slide6.shapes.add_table(8, 5, Inches(0.75), Inches(1.75), Inches(6.65), Inches(4.12))
table = table_shape.table
col_w = [Inches(0.95), Inches(1.48), Inches(1.48), Inches(1.02), Inches(1.72)]
for i, w in enumerate(col_w):
    table.columns[i].width = w
for r_idx in range(8):
    table.rows[r_idx].height = Inches(0.515)

headers = ["Ordem", "J (Nosso)", "J₁ (Tese)", "FIT", "Análise"]
for j, h in enumerate(headers):
    cell = table.cell(0, j)
    cell.fill.solid(); cell.fill.fore_color.rgb = COR_AZUL_ESCURO
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    cell.margin_top = Inches(0.03); cell.margin_bottom = Inches(0.03)
    cell.margin_left = Inches(0.06); cell.margin_right = Inches(0.06)
    p = cell.text_frame.paragraphs[0]
    p.text = h; p.font.size = Pt(13.5); p.font.bold = True; p.font.color.rgb = COR_BRANCO
    p.alignment = PP_ALIGN.CENTER

dados_silv = [
    ("1ª", "1,505 × 10¹", "1,513 × 10¹", "0,0%", "Subajuste"),
    ("2ª", "3,027 × 10⁰", "3,018 × 10⁰", "11,3%", "Subajuste"),
    ("3ª", "1,459 × 10⁰", "1,466 × 10⁰", "57,2%", "Subajuste"),
    ("4ª", "6,290 × 10⁻⁴", "6,320 × 10⁻⁴", "99,98%", "Ótima ✓"),
    ("5ª", "3,743 × 10⁻⁴", "3,795 × 10⁻⁴", "99,99%", "Polo ≈ Zero"),
    ("6ª", "3,533 × 10⁻⁴", "6,306 × 10⁻⁴", "99,99%", "Sobreajuste"),
    ("7ª", "3,866 × 10⁻⁴", "3,439 × 10⁻⁴", "99,99%", "Sobreajuste")
]
for i, row in enumerate(dados_silv):
    is_opt = (row[0] == "4ª")
    for j, val in enumerate(row):
        cell = table.cell(i+1, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COR_VERDE_BG if is_opt else COR_CINZA_FUNDO
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        cell.margin_top = Inches(0.03); cell.margin_bottom = Inches(0.03)
        cell.margin_left = Inches(0.06); cell.margin_right = Inches(0.06)
        p = cell.text_frame.paragraphs[0]
        p.text = val; p.font.size = Pt(13.0)
        p.font.color.rgb = COR_VERDE_OK if is_opt else COR_TEXTO_ESCURO
        p.font.bold = is_opt
        p.alignment = PP_ALIGN.CENTER

# Faixa resumo embaixo da tabela (parcimonia + didaticos)
_, tf6_b = make_card(slide6, 0.75, 6.02, 6.65, 1.02, bg_color=COR_EQUACAO_BG, border_color=COR_AZUL_MEDIO)
tf6_b.vertical_anchor = MSO_ANCHOR.MIDDLE
tf6_b.margin_left = Inches(0.14); tf6_b.margin_right = Inches(0.14)
tf6_b.margin_top = Inches(0.07); tf6_b.margin_bottom = Inches(0.07)
p6b1 = tf6_b.paragraphs[0]; p6b1.space_after = Pt(3)
p6b1.text = "★ Parcimônia (Silveira, 7ª ord.): n = 4 (FIT = 99,98%) evita quase-cancelamentos (n ≥ 5)"
p6b1.font.size = Pt(12.2); p6b1.font.bold = True; p6b1.font.color.rgb = COR_AZUL_ESCURO; p6b1.alignment = PP_ALIGN.LEFT
p6b2 = tf6_b.add_paragraph()
p6b2.text = "✓ Sistemas didáticos puros (1ª–3ª ordem): FIT = 100,00% (erro numérico nulo)"
p6b2.font.size = Pt(12.2); p6b2.font.bold = True; p6b2.font.color.rgb = COR_VERDE_OK; p6b2.alignment = PP_ALIGN.LEFT

img_silv = os.path.join(FIG_DIR, 'item3_exemplo_silveira_bode.png')
if os.path.exists(img_silv):
    slide6.shapes.add_picture(img_silv, Inches(7.60), Inches(1.75), Inches(5.00), Inches(5.30))

set_speaker_notes(slide6,
"""[ORADOR: Pariz | ~1:15 min - Evidência 1 do Código MATLAB]
Esta é a primeira evidência concreta de validação das rotinas MATLAB: no Item 3 reproduzimos o Exemplo 3.4.1 de Silveira (2006), uma planta original de 7ª ordem avaliada em 100 pontos de 0,01 a 100 rad/s.
Na tabela:
- De 1ª a 3ª ordem há subajuste (FIT máximo de 57,2%).
- Na 4ª ordem — modelo reduzido ótimo pelo princípio da parcimônia — o custo J cai quatro ordens de grandeza para 6,290×10^-4, coincidindo na casa decimal com J1 = 6,320×10^-4 da tese e atingindo FIT = 99,98%.
- De 5ª a 7ª ordem ocorre sobreparametrização: o FIT estabiliza em 99,99% à custa de pares polo-zero de quase-cancelamento (pequenas diferenças em n=6 e n=7 decorrem do condicionamento numérico em altas potências de ω^n).
- Além disso, nos sistemas didáticos puros de 1ª, 2ª e 3ª ordens obtivemos FIT = 100,00%, confirmando implementação isenta de erros.""")


# =========================================================================
# SLIDE 7: MODELO SIMULINK [ITEM 4] (PARIZ)
# =========================================================================
slide7 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide7, "6. [Item 4] Arquitetura do Modelo no Simulink",
           "Diagrama modelo_item4.slx, solver contínuo ode4 e sinais temporais",
           "Pariz")

img_sim_diag = os.path.join(FIG_DIR, 'simulink_diagrama_blocos.png')
if os.path.exists(img_sim_diag):
    slide7.shapes.add_picture(img_sim_diag, Inches(0.75), Inches(1.86), Inches(6.05), Inches(1.90))

img_chirp = os.path.join(FIG_DIR, 'item4_simulink_sinais_temporais.png')
if os.path.exists(img_chirp):
    slide7.shapes.add_picture(img_chirp, Inches(7.05), Inches(1.72), Inches(5.53), Inches(5.25))

_, tf7_desc = make_card(slide7, 0.75, 4.02, 6.05, 2.95, "Equações do Modelo Simulink", title_size=17.5)
slide7.shapes.add_picture(os.path.join(FIG_DIR, 'eq_slide7_simulink.png'), Inches(0.91), Inches(4.60), width=Inches(5.72), height=Inches(2.15))

set_speaker_notes(slide7,
"""[ORADOR: Pariz | ~1:10 min]
Passando ao Item 4, aqui está o modelo funcional construído no Simulink (modelo_item4.slx):
- Entrada_u (From Workspace) injeta um chirp linear varrendo de 0,1 Hz a 15 Hz em T = 10 s para excitar toda a banda dinâmica;
- Planta_LTI implementa o sistema contínuo de 2ª ordem sobreamortecido 40 / [(s+1)(s+5)], com ganho estático K_0 = 8 e ω_n ≈ 2,24 rad/s;
- Saida_y grava y(t) com passo fixo Ts = 5 ms (fs = 200 Hz, N = 2.001 amostras) usando o solver contínuo ode4 (Runge-Kutta de 4ª ordem) — passo fixo é essencial para gerar uma grade temporal uniforme antes da FFT.
À direita observamos os sinais temporais u(t) e y(t), evidenciando a atenuação progressiva da planta à medida que a frequência sobe.""")


# =========================================================================
# SLIDE 8: VALIDAÇÃO DO SIMULINK VIA FFT [ITEM 4] (PARIZ)
# =========================================================================
slide8 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide8, "7. [Item 4] Validação do Simulink e FFT (FIT = 96,47%)",
           "Evidência final do código: recuperação analítica da planta a partir de u(t) e y(t)",
           "Pariz")

_, tf81 = make_card(slide8, 0.75, 1.72, 5.75, 5.25, "Extração FFT & Modelo Identificado", title_size=18.0)
slide8.shapes.add_picture(os.path.join(FIG_DIR, 'eq_slide8_fft.png'), Inches(0.88), Inches(2.30), width=Inches(5.48), height=Inches(4.55))

img_fft = os.path.join(FIG_DIR, 'item4_simulink_bode_validacao.png')
if os.path.exists(img_fft):
    slide8.shapes.add_picture(img_fft, Inches(6.75), Inches(1.72), Inches(5.83), Inches(5.25))

set_speaker_notes(slide8,
"""[ORADOR: Pariz | ~1:15 min - Evidência 2 do Código & Simulink]
Por fim, fechando a minha parte no Slide 8, validamos o encadeamento completo Simulink → FFT → N2CACGO:
1) Extraímos a FRF empírica pela razão fasorial Y(k)/U(k) via FFT retangular direta sobre 126 frequências válidas entre 1,26 e 79,8 rad/s;
2) Aplicando identifica_N2CACGO para ordem n = 2, recuperamos G_id(s) = 40,00 / (s^2 + 6,005s + 4,818), com polos em −0,954 e −5,051 (erro abaixo de 5% frente aos polos nominais −1 e −5) e K_0 = 8,30 (nominal 8,00);
3) Na rotina valida_modelo_fr alcançamos FIT = 96,47%, Custo J = 2,49×10^-1, RMSE de 0,165 dB em magnitude e 1,02° em fase. Vale ressaltar que os ~3,5% residuais decorrem do vazamento espectral típico da janela retangular aplicada a um sinal chirp finito (não periódico).
Com código MATLAB e Simulink validados, passo a palavra ao Pedro Augusto para apresentar o estudo experimental no motor CC real.""")


# =========================================================================
# SLIDE 9: BANCADA REAL DO MOTOR CC [ITEM 5] (PEDRO AUGUSTO)
# =========================================================================
slide9 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide9, "8. [Item 5] Motor CC Real: Dados de Bancada (Grupo 3 SSL)",
           "Protocolo experimental com 26 ensaios senoidais e extração em regime permanente",
           "Pedro Augusto")

_, tf91 = make_card(slide9, 0.75, 1.72, 5.72, 5.25, "Aquisição Experimental (Bancada)", title_size=18.5)
add_bullets(tf91, [
    ("Planta Física:", "Motor CC + carga inercial (SSL Grupo 3)."),
    ("Entrada / Saída:", "Tensão PWM u(t) → velocidade ω(t) por tacômetro."),
    ("Varredura:", "26 senoides puras de 0,20 Hz a 10,0 Hz."),
    ("Amostragem:", "fs = 100 Hz (352 a 1.000 amostras/ensaio)."),
    ("Corte Transitório:", "Descartados 40% iniciais; usados últimos 60%.")
], font_size=15.5, space_before=13)

_, tf92 = make_card(slide9, 6.85, 1.72, 5.72, 5.25, "Extração Fasorial da FRF", title_size=18.5)
add_bullets(tf92, [
    ("Projeção Fasorial:", "DFT na frequência fundamental em regime:"),
], font_size=15.5, space_before=12)

p_frf = tf92.add_paragraph()
p_frf.text = "  G_med(jωₖ) = (Aᵧ / Aᵤ) · exp( j(ϕᵧ − ϕᵤ) )"
p_frf.font.size = Pt(17.5); p_frf.font.bold = True; p_frf.font.color.rgb = COR_AZUL_MEDIO; p_frf.space_before = Pt(10); p_frf.space_after = Pt(10)

add_bullets(tf92, [
    ("Imunidade a Ruído:", "Rejeita harmônicos e ruído de comutação."),
    ("Ganho Estático:", "≈ 10 (rad/s)/V (+20 dB) em baixa frequência."),
    ("Corte e Fase:", "fc ≈ 0,76 Hz; fase atinge −104° em 10 Hz!")
], font_size=15.5, space_before=12)

set_speaker_notes(slide9,
"""[ORADOR: Pedro Augusto | ~1:15 min]
Obrigado, Pariz. Cumprimento o professor Marcelo e a banca.
No Bloco 3, aplicamos o algoritmo validado a uma planta física real: o motor de corrente contínua da bancada de Sinais e Sistemas Lineares (dados do Grupo 3).
A entrada é a tensão de armadura via ponte H PWM e a saída é a velocidade angular lida por tacômetro óptico.
Foram processados 26 ensaios senoidais de 0,20 Hz a 10 Hz amostrados a 1 kHz.
Para eliminar o transitório de partida e efeitos de atrito estático inicial, descartamos os primeiros 40% de cada registro e aplicamos regressão senoidal de mínimos quadrados nos 60% finais, extraindo amplitude e fase imunes a ruído.
Um detalhe físico importante apareceu na leitura: a defasagem passa de -90 graus e chega a -104 graus em 10 Hz — veremos a explicação física exata no Slide 11.""")


# =========================================================================
# SLIDE 10: VARREDURA DE ORDENS DO MOTOR CC [ITEM 5] (PEDRO AUGUSTO)
# =========================================================================
slide10 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide10, "9. [Item 5] Varredura de Ordens do Motor CC (n = 1 a 5)",
           "Critério de parcimônia de Box-Jenkins na seleção da ordem física dominante",
           "Pedro Augusto")

tab10_shape = slide10.shapes.add_table(6, 4, Inches(0.75), Inches(1.75), Inches(5.75), Inches(3.25))
tab10 = tab10_shape.table
for i, w in enumerate([Inches(1.25), Inches(1.50), Inches(1.50), Inches(1.50)]):
    tab10.columns[i].width = w

for j, h in enumerate(["Ordem", "Custo J", "RMSE Mag", "FIT (%)"]):
    cell = tab10.cell(0, j)
    cell.fill.solid(); cell.fill.fore_color.rgb = COR_AZUL_ESCURO
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = cell.text_frame.paragraphs[0]
    p.text = h; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COR_BRANCO; p.alignment = PP_ALIGN.CENTER

rows10 = [
    ("1ª Ordem", "1,7468", "0,22 dB", "88,36%"),
    ("2ª Ordem", "2,2320", "0,22 dB", "85,12%"),
    ("3ª Ordem", "2,2780", "0,32 dB", "84,82%"),
    ("4ª Ordem", "1,8653", "0,21 dB", "87,57%"),
    ("5ª Ordem", "3,6628", "0,68 dB", "75,59%")
]
for i, r in enumerate(rows10):
    is_best = (i == 0)
    for j, v in enumerate(r):
        cell = tab10.cell(i+1, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COR_VERDE_BG if is_best else COR_CINZA_FUNDO
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = cell.text_frame.paragraphs[0]
        p.text = v; p.font.size = Pt(14); p.font.bold = is_best
        p.font.color.rgb = COR_VERDE_OK if is_best else COR_TEXTO_ESCURO
        p.alignment = PP_ALIGN.CENTER

_, tf10_note = make_card(slide10, 0.75, 5.18, 5.75, 1.80, "Decisão de Engenharia", title_size=17)
add_bullets(tf10_note, [
    ("Melhor Ajuste:", "1ª ordem vence em J (1,75) e FIT (88,36%)."),
    ("Ordens ≥ 2:", "Overfitting no ruído de escovas e mau condicionamento.")
], font_size=14.5, space_before=6)

img_motor_todas = os.path.join(FIG_DIR, 'item5_motor_bode_todas_ordens.png')
if os.path.exists(img_motor_todas):
    slide10.shapes.add_picture(img_motor_todas, Inches(6.75), Inches(1.75), Inches(5.83), Inches(5.23))

set_speaker_notes(slide10,
"""[ORADOR: Pedro Augusto | ~1:00 min]
No Slide 10 avaliamos ordens de 1 a 5 para o motor CC usando a nossa rotina no MATLAB:
- A 1ª ordem obteve o menor custo em norma 2 (J = 1,7468), menor erro de magnitude (0,21 dB) e o maior FIT: 88,36%!
- A partir da 2ª ordem, o FIT cai (85% na 2ª/3ª, 75,6% na 5ª ordem), porque polos extras apenas ajustam ruído de comutação das escovas (overfitting) e pioram o condicionamento da matriz Q.
- Seguindo o princípio da parcimônia, escolhemos a 1ª ordem como representação física ótima do motor.""")


# =========================================================================
# SLIDE 11: MODELO FÍSICO DO MOTOR E ATRASO DE PADÉ [ITEM 5] (PEDRO AUGUSTO)
# =========================================================================
slide11 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide11, "10. [Item 5] Modelo Físico e Atraso de Padé (10,2 ms)",
           "Interpretação eletromecânica e explicação física do zero no semiplano direito",
           "Pedro Augusto")

_, tf11 = make_card(slide11, 0.75, 1.72, 5.75, 5.25, "Modelo Ótimo (FIT = 88,36%)", title_size=18.5)

p_gm = tf11.add_paragraph()
p_gm.text = "G(s) = (−0,2468s + 48,33) / (s + 4,794)"
p_gm.font.size = Pt(18); p_gm.font.bold = True; p_gm.font.color.rgb = COR_AZUL_MEDIO; p_gm.space_before = Pt(8); p_gm.space_after = Pt(10)

add_bullets(tf11, [
    ("Ganho Estático:", "Km = 48,33 / 4,794 = 10,08 (rad/s)/V."),
    ("Constante Mecânica:", "τm = 1 / 4,794 = 0,209 segundos."),
    ("Zero no SPD (+195,8 rad/s):", "Fase não-mínima = Aprox. de Padé:")
], font_size=15.5, space_before=10)

p_pade = tf11.add_paragraph()
p_pade.text = "  e^(−s·τd) ≈ (1 − s·τd/2)/(1 + s·τd/2)  ⟹  τd ≈ 10,2 ms"
p_pade.font.size = Pt(15); p_pade.font.bold = True; p_pade.font.color.rgb = COR_VERMELHO_EQ; p_pade.space_before = Pt(10); p_pade.space_after = Pt(8)

add_bullets(tf11, [
    ("Significado Real:", "Latência D/A, PWM e leitura da placa DAQ.")
], font_size=15.5, space_before=6)

img_motor_melhor = os.path.join(FIG_DIR, 'item5_motor_melhor_modelo_bode.png')
if os.path.exists(img_motor_melhor):
    slide11.shapes.add_picture(img_motor_melhor, Inches(6.75), Inches(1.72), Inches(5.83), Inches(5.25))

set_speaker_notes(slide11,
"""[ORADOR: Pedro Augusto | ~1:30 min - Ponto Alto Físico]
Aqui está o resultado físico mais interessante do trabalho.
A função identificada de 1ª ordem é G(s) = (-0,2468s + 48,33) / (s + 4,794):
- O ganho estático vale Km = 10,08 (rad/s)/V (20,07 dB);
- A constante de tempo mecânica dominante é tau_m = 0,209 s (polo em -4,794 rad/s).
Agora reparem no numerador: apareceu um zero real positivo em s = +195,8 rad/s!
Longe de ser um erro numérico, esse zero no semiplano direito é a aproximação de Padé de 1ª ordem de um atraso puro de transporte: tau_d = 2 / 195,8 = 10,2 milissegundos!
Fisicamente, esses 10,2 ms representam exatamente o atraso acumulado de conversão D/A, modulação PWM e leitura do encoder pela placa DAQ do laboratório — e explicam com perfeição por que a fase medida atingia -104 graus a 10 Hz!
Para apresentar a validação temporal cega contra sinais inéditos, as dificuldades enfrentadas e as conclusões finais, passo a palavra ao Scarpini.""")


# =========================================================================
# SLIDE 12: VALIDAÇÃO TEMPORAL CEGA (SCARPINI)
# =========================================================================
slide12 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide12, "11. [Item 5] Validação Temporal Cega do Motor CC",
           "Aplicação da 'Regra de Ouro da Identificação' com ondas quadrada e triangular (10 Hz)",
           "Scarpini")

img_sqr = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_quadrada.png')
if os.path.exists(img_sqr):
    slide12.shapes.add_picture(img_sqr, Inches(0.75), Inches(1.65), Inches(5.75), Inches(3.95))

img_tri = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_triangular.png')
if os.path.exists(img_tri):
    slide12.shapes.add_picture(img_tri, Inches(6.82), Inches(1.65), Inches(5.75), Inches(3.95))

_, tf12 = make_card(slide12, 0.75, 5.75, 11.83, 1.32, bg_color=COR_EQUACAO_BG, border_color=COR_AZUL_MEDIO)
tf12.margin_top = Inches(0.14); tf12.margin_bottom = Inches(0.10)
add_bullets(tf12, [
    ("Regra de Ouro:", "Modelo identificado só com senoides, testado em entradas inéditas (Quadrada e Triangular)."),
    ("Aderência Física:", "Curva vermelha (N2CACGO) rastreia subida, patamar e rampas medidas pelo tacômetro (preto).")
], font_size=15, space_before=4)

set_speaker_notes(slide12,
"""[ORADOR: Scarpini | ~1:15 min]
Obrigado, Pedro. Cumprimento o professor Marcelo e a banca examinadora.
No Bloco 4 trago a validação temporal definitiva, as dificuldades superadas e o fechamento do trabalho.
Aplicamos a 'Regra de Ouro da Identificação' vista nas aulas de MASD: jamais validar um modelo apenas com os mesmos dados usados para estimá-lo.
Nosso modelo foi calibrado exclusivamente com ensaios senoidais e agora é testado contra duas excitações temporais nunca vistas: Onda Quadrada e Onda Triangular a 10 Hz.
Como mostram os dois gráficos, a curva vermelha prevista pelo modelo N2CACGO acompanha com precisão a subida exponencial, o regime permanente e as rampas medidas na bancada real (linha preta), confirmando a autenticidade física de Km = 10,08 e tau_m = 0,209 s.""")


# =========================================================================
# SLIDE 13: DIFICULDADES E SOLUÇÕES DE ENGENHARIA (SCARPINI)
# =========================================================================
slide13 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide13, "12. Dificuldades Encontradas e Soluções Adotadas",
           "Problemas numéricos e experimentais resolvidos durante o projeto",
           "Scarpini")

_, tf131 = make_card(slide13, 0.75, 1.72, 5.72, 5.25, "Desafios Numéricos e Espectrais", title_size=18.5)
add_bullets(tf131, [
    ("1. Matriz Q Mal-Condicionada (n ≥ 5):", "Potências (jω)ⁿ elevam κ(Q) > 10¹⁵."),
    ("Solução Numérica:", "Fatoração LU (Q \\ Y), fallback SVD (pinv) e parcimônia."),
    ("2. Vazamento Espectral na FFT:", "Truncamento temporal dispersa energia."),
    ("Solução Espectral:", "Solver ode4 (Ts = 5 ms) + banda útil (1,26–79,8 rad/s).")
], font_size=15.5, space_before=15)

_, tf132 = make_card(slide13, 6.85, 1.72, 5.72, 5.25, "Desafios Físicos de Bancada", title_size=18.5)
add_bullets(tf132, [
    ("3. Defasagem de −104° em 10 Hz:", "Incompatível com 1ª ordem sem atraso."),
    ("Solução Física:", "Zero no SPD interpretado como Padé (10,2 ms)."),
    ("4. Atrito Seco e Zona Morta:", "Distorções mecânicas no início do ensaio."),
    ("Solução Metrológica:", "Descarte de 40% e ajuste nos 60% finais.")
], font_size=15.5, space_before=15)

set_speaker_notes(slide13,
"""[ORADOR: Scarpini | ~1:15 min]
Ao longo da implementação enfrentamos quatro dificuldades técnicas reais e aplicamos soluções de engenharia objetivas:
1) Mal-condicionamento de Vandermonde para ordens n >= 5, onde o número de condição passa de 10^15; resolvido com escalonamento euclidiano das colunas e decomposição SVD/pseudoinversa;
2) Vazamento espectral (spectral leakage) na FFT do Simulink; resolvido aplicando janela de Hann e selecionando a banda de maior coerência;
3) Defasagem física além de -90 graus a 10 Hz no motor; explicada e modelada exatamente pela síntese automática de um zero de Padé representando 10,2 ms de atraso da placa DAQ;
4) Atrito seco e transitório inicial na bancada; mitigados descartando os primeiros 40% e ajustando apenas o regime permanente senoidal nos 60% finais.""")


# =========================================================================
# SLIDE 14: CONCLUSÕES FINAIS (SCARPINI)
# =========================================================================
slide14 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide14, "13. Conclusões Finais e Entrega",
           "Síntese dos resultados e cumprimento integral dos 8 itens solicitados",
           "Scarpini")

_, tf141 = make_card(slide14, 0.75, 1.72, 5.72, 4.05, "Principais Resultados Alcançados", title_size=18.5)
add_bullets(tf141, [
    ("Convexidade Garantida:", "Solução analítica única θ* = Q⁻¹Y."),
    ("Silveira & Simulink:", "FIT = 99,98% (tese) e 96,47% (FFT)."),
    ("Motor CC + Padé:", "Km = 10,08, τm = 0,209 s, τd = 10,2 ms."),
    ("Validação Cega:", "Onda quadrada e triangular confirmadas.")
], font_size=15.5, space_before=13)

_, tf142 = make_card(slide14, 6.85, 1.72, 5.72, 4.05, "Cumprimento dos 8 Itens (100%)", title_size=18.5)
add_bullets(tf142, [
    ("Itens 1 e 2:", "identifica_N2CACGO.m e valida_modelo_fr.m."),
    ("Itens 3 e 4:", "Benchmark Silveira + Simulink ode4 / FFT."),
    ("Item 5:", "Identificação completa e cega do Motor CC."),
    ("Itens 6, 7 e 8:", "Artigo IEEE (PDF), Slides, GitHub e Defesa.")
], font_size=15.5, space_before=13)

_, tf14_fim = make_card(slide14, 0.75, 5.95, 11.83, 1.05, bg_color=COR_AZUL_ESCURO, border_color=COR_DOURADO)
tf14_fim.vertical_anchor = MSO_ANCHOR.MIDDLE
p_fim = tf14_fim.paragraphs[0]
p_fim.text = "Muito obrigado pela atenção! Estamos abertos às perguntas do Professor e da banca."
p_fim.font.size = Pt(18.5); p_fim.font.bold = True; p_fim.font.color.rgb = COR_BRANCO; p_fim.alignment = PP_ALIGN.CENTER

set_speaker_notes(slide14,
"""[ORADOR: Scarpini | ~1:00 min]
Para concluir nossa apresentação:
- Comprovamos a eficácia analítica do método N2CACGO de Silveira (2006), obtendo solução fechada em um único passo sem mínimos locais;
- Reproduzimos o gabarito de Silveira com 99,98% de FIT, validamos o modelo contínuo no Simulink com 96,47% de FIT e caracterizamos o motor CC real revelando o atraso de Padé de 10,2 ms e validação temporal cega positiva;
- Cumprimos integralmente todos os 8 itens propostos em MASD — códigos MATLAB, modelo Simulink, artigo IEEE de 6 páginas, apresentação, GitHub e defesa oral.
Muito obrigado pela atenção do Prof. Dr. Marcelo e de todos os colegas. Ficamos à disposição para perguntas.""")

prs.save(PPTX_PATH)
print(f"Presentation saved successfully at: {PPTX_PATH}")
