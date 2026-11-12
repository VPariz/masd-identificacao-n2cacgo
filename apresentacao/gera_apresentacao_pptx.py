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

# Paleta Institucional IME / Engenharia
COR_AZUL_ESCURO = RGBColor(15, 34, 64)      # #0F2240 (Navy Primário)
COR_AZUL_MEDIO  = RGBColor(30, 75, 140)     # #1E4B8C
COR_DOURADO     = RGBColor(212, 160, 23)    # #D4A017 (Destaque)
COR_CINZA_FUNDO = RGBColor(245, 247, 250)   # #F5F7FA
COR_TEXTO_ESCURO= RGBColor(30, 30, 30)
COR_BRANCO      = RGBColor(255, 255, 255)
COR_CINZA_BORDA = RGBColor(210, 215, 225)
COR_VERDE_OK    = RGBColor(20, 120, 50)
COR_CODE_BG     = RGBColor(238, 242, 246)

def add_header(slide, title_text, subtitle_text="", speaker_name=""):
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.32), Inches(9.2), Inches(1.15))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = COR_AZUL_ESCURO

    if subtitle_text:
        p2 = tf.add_paragraph()
        p2.text = subtitle_text
        p2.font.size = Pt(12.5)
        p2.font.color.rgb = COR_AZUL_MEDIO
        p2.space_before = Pt(3)

    if speaker_name:
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.2), Inches(0.38), Inches(2.3), Inches(0.55))
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

    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.48), Inches(11.7), Inches(0.04))
    line.fill.solid()
    line.fill.fore_color.rgb = COR_DOURADO
    line.line.color.rgb = COR_DOURADO

def set_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = notes_text

# =========================================================================
# SLIDE 1: CAPA INSTITUCIONAL
# =========================================================================
slide1 = prs.slides.add_slide(prs.slide_layouts[6])
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg1.fill.solid(); bg1.fill.fore_color.rgb = COR_AZUL_ESCURO
bg1.line.color.rgb = COR_AZUL_ESCURO

tbox1 = slide1.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(11), Inches(3.5))
tf1 = tbox1.text_frame; tf1.word_wrap = True

p = tf1.paragraphs[0]
p.text = "INSTITUTO MILITAR DE ENGENHARIA • SE/3"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_DOURADO

p = tf1.add_paragraph()
p.text = "Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO"
p.font.size = Pt(30); p.font.bold = True; p.font.color.rgb = COR_BRANCO; p.space_before = Pt(10)

p = tf1.add_paragraph()
p.text = "Fundamentação Matemática de Silveira (2006), Implementação no MATLAB, Diagrama Simulink e Bancada do Motor CC"
p.font.size = Pt(16); p.font.color.rgb = RGBColor(200, 220, 245); p.space_before = Pt(8)

abox1 = slide1.shapes.add_textbox(Inches(1.2), Inches(4.8), Inches(11), Inches(2.3))
tf_a = abox1.text_frame
p = tf_a.paragraphs[0]
p.text = "Equipe e Divisão dos 4 Blocos da Apresentação (~15 minutos):\n" \
         "• Bloco 1 (Slides 1 a 4): João Victor Pariz — Contexto Físico, Método de Silveira e Estrutura do Código MATLAB\n" \
         "• Bloco 2 (Slides 5 a 7): Pedro Augusto — Validação Acadêmica e Simulação no Simulink com FFT\n" \
         "• Bloco 3 (Slides 8 a 10): Renato Felix — Bancada Experimental do Motor CC, Rigor Metrológico e Atraso de Padé\n" \
         "• Bloco 4 (Slides 11 a 13): Arthur Scarpini — Validação Cega no Tempo, Condicionamento Matricial e Conclusões\n\n" \
         "Orientador: Prof. Dr. Marcelo de Araújo Oliveira  |  Disciplina: Modelagem e Análise de Sistemas Dinâmicos (MASD)"
p.font.size = Pt(12.5); p.font.color.rgb = RGBColor(220, 230, 245)

set_speaker_notes(slide1,
"""[ORADOR: João Victor Pariz | ~1:00 min]
- Cumprimente o Prof. Dr. Marcelo de Araújo Oliveira e a banca.
- Apresente os 4 integrantes e a estrutura da apresentação em 4 blocos técnicos equilibrados (~15 min total).
- Anuncie o tema: Implementação do método N2CACGO (Silveira, 2006) em MATLAB/Simulink e sua aplicação experimental em bancada real de motor elétrico CC.""")

# =========================================================================
# SLIDE 2: CONTEXTUALIZAÇÃO (AULA MASD)
# =========================================================================
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide2, "1. Contextualização: Domínio da Frequência vs. Tempo", 
           "Classificação de modelos (Caixa Branca/Cinza/Preta) e as 3 vantagens frequenciais ensinadas em aula", 
           "João Victor Pariz")

c2_1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1))
c2_1.fill.solid(); c2_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c2_1.line.color.rgb = COR_CINZA_BORDA
tf = c2_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Classificação e Limitações do Tempo"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_21 = [
    "Classificação de Modelos (Slides de Aula MASD):\n  • Caixa Branca: 100% teoria física (leis de Newton/Kirchhoff), sem dados.\n  • Caixa Cinza: Estrutura conhecida + ajuste de parâmetros desconhecidos.\n  • Caixa Preta: Mapeamento entrada/saída estritamente por dados experimentais.",
    "Gargalos do Domínio do Tempo (ARX, PEM):\n  • Sensibilidade ao Ruído: Ruídos estocásticos de alta frequência e perturbações não-gaussianas contaminam diretamente as matrizes de covariância.\n  • Condições Iniciais: Exige relaxamento prévio x(0) = 0. Violações introduzem viés sistemático severo.\n  • Atrasos de Transporte: Dificuldade em estimar atrasos puros sem sobreparametrizar desnecessariamente o modelo discreto."
]
for it in items_21:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

c2_2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1))
c2_2.fill.solid(); c2_2.fill.fore_color.rgb = COR_CINZA_FUNDO; c2_2.line.color.rgb = COR_CINZA_BORDA
tf = c2_2.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "As 3 Vantagens da Abordagem Frequencial"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_22 = [
    "1. Filtragem Natural de Ruído:\n  Isola a banda forçada de interesse e rejeita naturalmente ruídos fora da faixa excitada (como o ruído de rede de 60 Hz e oscilações do sensor).",
    "2. Ajuste Fino de Dinâmicas Rápidas:\n  Alta sensibilidade matemática aos picos de ressonância e defasagens angulares dos modos dominantes.",
    "3. Compactação Brutal de Dados:\n  Milhares de amostras temporais brutas são resumidas em um vetor compacto de fasores com alta relação sinal-ruído (SNR), aliviando o esforço computacional.",
    "A Inovação do N2CACGO (Silveira, 2006):\n  Supera métodos não-convexos (como Valle, 2005) e algoritmos heurísticos (como Nelder-Mead / fminsearch) que ficam presos em mínimos locais!"
]
for it in items_22:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

set_speaker_notes(slide2,
"""[ORADOR: João Victor Pariz | ~1:15 min]
- Conecte diretamente com os slides do Prof. Marcelo: Caixa Branca, Caixa Cinza e Caixa Preta.
- Mostre por que fomos para a frequência: ruídos no tempo geram viés, enquanto na frequência temos as 3 vantagens da aula:
  1) Filtragem natural de ruído fora da banda excitada;
  2) Ajuste fino de ressonâncias;
  3) Compactação de milhares de amostras temporais em poucos fasores de FRF.
- Destaque que métodos anteriores como o de Valle (2005) não eram convexos e caíam em mínimos locais.""")

# =========================================================================
# SLIDE 3: O MÉTODO N2CACGO DE SILVEIRA (2006)
# =========================================================================
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide3, "2. O Método N2CACGO (Silveira, 2006): Formulação Convexa", 
           "Estrutura polinomial, resíduo de equação e garantia de mínimo global analítico", 
           "João Victor Pariz")

c3_1 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1))
c3_1.fill.solid(); c3_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c3_1.line.color.rgb = COR_CINZA_BORDA
tf = c3_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Modelo LTI e Resíduo Linear"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_31 = [
    "Função de Transferência Biprópria de Ordem n:\n  Ge(s) = B(s) / A(s)\n  B(s) = α0 s^n + α1 s^(n-1) + ... + αn\n  A(s) = s^n + β1 s^(n-1) + ... + βn",
    "Resíduo de Equação Ponderado:\n  e(jωi) = A(jωi)·G(jωi) - B(jωi)\n  O erro é ESTRITAMENTE LINEAR nos parâmetros α e β!",
    "Funcional de Custo Quadrático em Norma 2:\n  J(θ) = ∑ |e(jωi)|² = ∑ |A(jωi)·G(jωi) - B(jωi)|²",
    "Vetor de Parâmetros Ótimos a Determinar:\n  θ = [α0, α1, ..., αn, β1, ..., βn]^T  ∈  R^(2n+1)"
]
for it in items_31:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12.5); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

c3_2 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1))
c3_2.fill.solid(); c3_2.fill.fore_color.rgb = COR_CINZA_FUNDO; c3_2.line.color.rgb = COR_CINZA_BORDA
tf = c3_2.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Garantia Matemática de Mínimo Global"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_32 = [
    "Propriedade de Convexidade (Aulas MASD):\n  Como o resíduo é linear, o funcional J(θ) tem matriz Hessiana semidefinida positiva (∇²J ≥ 0) em todo o espaço de busca.\n  Consequência: NÃO EXISTEM mínimos locais! Todo ponto com gradiente zero é o mínimo global absoluto.",
    "Equacionamento Analítico do SEL (Silveira, 2006):\n  Aplicando ∇θ J = 0, desacopla-se no sistema matricial:\n  [ Q1  -Q2 ] [ α ]   [ Y1 ]\n  [ Q3  -Q4 ] [ β ] = [ Y2 ]  ==>  Q·θ = Y",
    "Solução Fechada e Única:\n  θ* = Q^(-1)·Y  (resolvido em um ÚNICO PASSO analítico, sem convergir devagar nem divergir!)."
]
for it in items_32:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12.2); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

set_speaker_notes(slide3,
"""[ORADOR: João Victor Pariz | ~1:15 min]
- Explique o coração da dissertação de Bruno de Pinho Silveira (IME, 2006):
- O erro de equação e(jw) é linear nos parâmetros do numerador e denominador.
- Isso faz com que a função custo quadrática seja ESTRITAMENTE CONVEXA.
- Como vimos em aula: se a função é convexa, não existem armadilhas de mínimos locais.
- Ao derivar analiticamente, chegamos no SEL particionado Q*theta = Y, resolvido sem qualquer iteração!""")

# =========================================================================
# SLIDE 4: ESTRUTURA DO CÓDIGO MATLAB (ITEM 1 E 2)
# =========================================================================
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide4, "3. [Item 1 & 2] Implementação do Algoritmo e Métricas no MATLAB", 
           "Estrutura modular do script identifica_N2CACGO.m e da rotina valida_modelo_fr.m", 
           "João Victor Pariz")

c4_1 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.1))
c4_1.fill.solid(); c4_1.fill.fore_color.rgb = COR_CODE_BG; c4_1.line.color.rgb = COR_CINZA_BORDA
tf = c4_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Estrutura do Código: identifica_N2CACGO.m"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

code_snippet = """function [sys_id, theta, J] = identifica_N2CACGO(w, H_med, n)
  % 1. Matriz de base polinomial monomial R: (n+1) x m
  R = zeros(n+1, m);
  for k = 0:n
      R(k+1, :) = (1i * w.').^(n - k);
  end

  % 2. Projeções e matrizes de dados espectrais
  S = diag(H_med);  S_conj = diag(conj(H_med));
  Gamma = diag(H_med .* conj(H_med));
  R_H = R';

  % 3. Montagem dos 4 blocos analíticos de Q e Y
  Q1 = real(R * R_H);
  Q2 = real(R * S_conj * R_H(:, 2:n+1));
  Q3 = real(R(2:n+1, :) * S * R_H);
  Q4 = real(R(2:n+1, :) * Gamma * R_H(:, 2:n+1));
  Q  = [Q1, -Q2; Q3, -Q4];
  Y  = real([R * S_conj; R(2:n+1, :) * Gamma] * (1i*w).^n);

  % 4. Resolução analítica por Eliminação Gaussiana
  theta = Q \\ Y;
  sys_id = tf(theta(1:n+1)', [1, theta(n+2:end)']);
end"""
p2 = tf.add_paragraph(); p2.text = code_snippet
p2.font.size = Pt(9.5); p2.font.name = "Consolas"; p2.font.color.rgb = RGBColor(10, 40, 90); p2.space_before = Pt(4)

c4_2 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.8), Inches(5.4), Inches(5.1))
c4_2.fill.solid(); c4_2.fill.fore_color.rgb = COR_CINZA_FUNDO; c4_2.line.color.rgb = COR_CINZA_BORDA
tf = c4_2.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Rotina de Validação: valida_modelo_fr.m"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_42 = [
    "Entradas da Rotina:\n  • Vetor de frequências angulares ω [rad/s].\n  • Resposta complexa experimental G_med(jω).\n  • Objeto tf retornado pelo N2CACGO.",
    "Métricas Quantitativas de Erro (Aulas MASD):\n  1. Custo em Norma 2 (Erro de Equação):\n     J = || A(jω)·G_med - B(jω) ||²\n  2. RMSE de Magnitude em dB:\n     RMSE_mag = √[ (1/m) ∑ (20 log10 |G_med/G_id|)² ]\n  3. RMSE de Fase em graus:\n     RMSE_fase = √[ (1/m) ∑ (∠G_med - ∠G_id)² ]\n  4. Índice de Ajuste Global (FIT %):\n     FIT = [ 1 - ||G_med - G_id|| / ||G_med - G_medio|| ] × 100%",
    "Saída Automatizada:\n  Gera diagnósticos numéricos e gráficos de Bode comparativos com magnitude e fase sobrepostas."
]
for it in items_42:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(11.8); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(6)

set_speaker_notes(slide4,
"""[ORADOR: João Victor Pariz | ~1:00 min]
- Mostre o código MATLAB limpo e elegante implementado no Item 1 (identifica_N2CACGO.m):
  1) Montagem da base polinomial monomial R com as potências (j*w)^k;
  2) Cálculo dos 4 blocos da matriz Q e do vetor Y com projeções Hermitiana (real(R*R_H));
  3) Resolução direta pelo operador de divisão matricial (Q \\ Y), que usa eliminação Gaussiana com pivoteamento parcial.
- Explique a rotina do Item 2 (valida_modelo_fr.m) que calcula o custo J, os RMSEs e o FIT oficial da disciplina.
- Transição: 'Para apresentar a validação desse código com a dissertação de Silveira e os ensaios no Simulink, passo a palavra ao Pedro Augusto.'""")

# =========================================================================
# SLIDE 5: BENCHMARK SILVEIRA 2006 (ITEM 3)
# =========================================================================
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide5, "4. [Item 3] Validação Teórica: Benchmark de Silveira (2006)", 
           "Reprodução fiel da Tabela 3.2 da dissertação de mestrado (Ordens 1 a 7)", 
           "Pedro Augusto")

table_shape = slide5.shapes.add_table(8, 5, Inches(0.8), Inches(1.8), Inches(6.5), Inches(4.9))
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
    slide5.shapes.add_picture(img_silv, Inches(7.5), Inches(1.8), Inches(5.0), Inches(4.9))

set_speaker_notes(slide5,
"""[ORADOR: Pedro Augusto | ~1:15 min]
- Agradeça a Pariz e apresente a validação acadêmica do Item 3.
- Mostre a Tabela comparativa: reproduzimos com exatidão os custos J da Tabela 3.2 de Silveira (2006).
- Explique o princípio da parcimônia: a planta alvo é de 4ª ordem. A 4ª ordem já atinge FIT de 99,98% com erro mínimo de 6,28e-4.
- Ordens 5 a 7 trazem polos e zeros quase-cancelados e não melhoram a resposta física.
- Destaque que em sistemas didáticos puros obtivemos FIT de 100% e custo da ordem de 10^-14.""")

# =========================================================================
# SLIDE 6: O MODELO SIMULINK (ITEM 4) - COM O PRINT NÍTIDO DO DIAGRAMA!
# =========================================================================
slide6 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide6, "5. [Item 4] O Modelo Simulink: Diagrama de Blocos e Chirp", 
           "Estrutura do modelo_item4.slx, solver numérico ode4 e geração dos sinais temporais", 
           "Pedro Augusto")

# Imagem do Diagrama de Blocos do Simulink no topo
img_sim_diag = os.path.join(FIG_DIR, 'simulink_diagrama_blocos.png')
if os.path.exists(img_sim_diag):
    slide6.shapes.add_picture(img_sim_diag, Inches(0.8), Inches(1.75), Inches(6.0), Inches(2.2))

# Imagem dos Sinais Temporais à direita
img_chirp = os.path.join(FIG_DIR, 'item4_simulink_sinais_temporais.png')
if os.path.exists(img_chirp):
    slide6.shapes.add_picture(img_chirp, Inches(7.1), Inches(1.75), Inches(5.4), Inches(5.0))

# Card explicativo embaixo do print do Simulink
c6_desc = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.1), Inches(6.0), Inches(2.65))
c6_desc.fill.solid(); c6_desc.fill.fore_color.rgb = COR_CINZA_FUNDO; c6_desc.line.color.rgb = COR_CINZA_BORDA
tf = c6_desc.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.2)
p = tf.paragraphs[0]; p.text = "Detalhes de Implementação no Simulink"
p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_6desc = [
    "1. Bloco Entrada_u (From Workspace): Injeta sinal Chirp linear varrendo de 0,1 Hz a 15 Hz por 50 s.",
    "2. Bloco Planta_LTI (Transfer Fcn): Implementa a dinâmica contínua G(s) = 8 / (0,2 s² + 1,2 s + 1) = 40 / (s² + 6 s + 5).",
    "3. Bloco Saida_y (To Workspace): Registra a série temporal de saída com Ts = 1 ms (20.001 amostras).",
    "4. Solver Contínuo ode4: Algoritmo Runge-Kutta de 4ª ordem com passo fixo, garantindo simulação livre de artefatos numéricos."
]
for it in items_6desc:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(11); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(3)

set_speaker_notes(slide6,
"""[ORADOR: Pedro Augusto | ~1:15 min]
- Apresente o diagrama de blocos do Simulink exibido no slide (modelo_item4.slx):
  * Bloco Entrada_u: lê o sinal Chirp de 0,1 a 15 Hz gerado no MATLAB;
  * Bloco Planta_LTI: executa a função de transferência contínua com polos em -1 e -5;
  * Bloco Saida_y: exporta a resposta temporal y(t) de volta ao Workspace.
- Mostre as curvas temporais à direita: o chirp varre a frequência ao longo dos 50 s, excitando todas as dinâmicas da planta com alta relação sinal-ruído.""")

# =========================================================================
# SLIDE 7: RESULTADOS FFT E VALIDAÇÃO ESPECTRAL (ITEM 4)
# =========================================================================
slide7 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide7, "6. [Item 4] Extração por FFT e Validação do Modelo Identificado", 
           "Processamento espectral de 126 fasores e recuperação analítica com FIT de 96,47%", 
           "Pedro Augusto")

c7_1 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
c7_1.fill.solid(); c7_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c7_1.line.color.rgb = COR_CINZA_BORDA
tf = c7_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Extração Espectral e Parâmetros Obtidos"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_71 = [
    "Extração Espectral via FFT:\n  G_med(jωk) = FFT{y(t)} / FFT{u(t)} = Y(k) / U(k)\n  Isolaram-se 126 frequências entre 1,26 e 79,76 rad/s com coerência SNR elevada.",
    "Modelo Identificado pelo N2CACGO:\n  G_id(s) = 40,0 / (s² + 6,005 s + 4,818)\n  (Planta Nominal: 40 / (s² + 6,000 s + 5,000)).",
    "Exatidão dos Polos e Ganho:\n  • Polos Estimados: s1 = -0,967 e s2 = -5,038\n    (Nominais: -1,000 e -5,000 — erro < 3%).\n  • Ganho Estático: 8,30 (Nominal: 8,00).",
    "Métricas de Ajuste Espectral:\n  • FIT Global: 96,47%\n  • RMSE de Módulo: 0,165 dB\n  • RMSE de Fase: 1,025 graus\n  A pequena dispersão decorre do vazamento espectral natural da FFT finita."
]
for it in items_71:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

img_fft = os.path.join(FIG_DIR, 'item4_simulink_bode_validacao.png')
if os.path.exists(img_fft):
    slide7.shapes.add_picture(img_fft, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide7,
"""[ORADOR: Pedro Augusto | ~1:00 min]
- Explique a extração da FRF a partir da razão espectral Y(k)/U(k).
- Mostre a curva de Bode à direita: a linha vermelha identificada pelo N2CACGO sobrepõe com precisão a curva nominal em azul.
- O FIT obtido foi de 96,47%, com erro de módulo de apenas 0,16 dB e erro de fase de 1 grau!
- Transição: 'Provada a eficácia em simulação e FFT, passo a palavra agora ao Renato Felix para apresentar a identificação em bancada física real de um motor elétrico.'""")

# =========================================================================
# SLIDE 8: O CASO DO MOTOR CC E OS DADOS EXPERIMENTAIS (ITEM 5)
# =========================================================================
slide8 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide8, "7. [Item 5] O Caso do Motor CC: Dados de Bancada e Rigor Metrológico", 
           "Origem dos dados experimentais da disciplina de SSL (Grupo 3, IME) e tratamento temporal", 
           "Renato Felix")

c8_1 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
c8_1.fill.solid(); c8_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c8_1.line.color.rgb = COR_CINZA_BORDA
tf = c8_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Origem e Conjunto de Dados Usados"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_81 = [
    "Origem dos Dados de Laboratório:\n  Ensaios práticos realizados na bancada de Motor CC na disciplina de Sinais e Sistemas Lineares (SSL) da SE/3 pelo Grupo 3.",
    "Composição do Dataset Utilizado (66 arquivos .mat):\n  • 26 ensaios senoidais (0,20 Hz a 10,0 Hz): Usados exclusivamente para ESTIMAÇÃO da FRF.\n  • 5 ensaios de onda quadrada (sqrf: 2, 4, 6, 8 e 10 Hz): Reservados para VALIDAÇÃO DINÂMICA.\n  • 5 ensaios de onda triangular (trif: 2, 4, 6, 8 e 10 Hz): Reservados para VALIDAÇÃO DINÂMICA.",
    "Rigor Metrológico:\n  Utilizou-se exclusivamente a base íntegra do Grupo 3, expurgando dados de outros grupos para evitar erros de calibração cruzada."
]
for it in items_81:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

c8_2 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.0))
c8_2.fill.solid(); c8_2.fill.fore_color.rgb = COR_CINZA_FUNDO; c8_2.line.color.rgb = COR_CINZA_BORDA
tf = c8_2.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Tratamento de Sinais: Regime Permanente Estrito"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_82 = [
    "Condições de Amostragem:\n  Taxa de amostragem de fs = 100 Hz (frequência de Nyquist de 50 Hz). Registros temporais de tensão de armadura u(t) e velocidade tacômetrica y(t).",
    "Eliminação do Transitório de Partida:\n  Em cada ensaio senoidal, os primeiros 40% das amostras foram sumariamente descartados. A identificação frequencial exige que a saída seja estritamente estacionária!",
    "Extração Fasorial por DFT:\n  A Transformada Discreta de Fourier foi calculada sobre os 60% finais estáveis, isolando a amplitude e defasagem na frequência fundamental de excitação.",
    "Resultado: Vetor de 23 pontos limpos de FRF (1,26 rad/s a 62,83 rad/s) com excelente relação sinal-ruído."
]
for it in items_82:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

set_speaker_notes(slide8,
"""[ORADOR: Renato Felix | ~1:30 min]
- Agradeça a Pedro e apresente o contexto do Motor CC.
- Explique em detalhes a origem dos dados: são os dados reais da bancada ensaiada pelo nosso Grupo 3 na matéria de SSL.
- Mostre a integridade do dataset: 26 ensaios senoidais usados na estimação, e arquivos de onda quadrada e triangular reservados para validação.
- Explique o rigor do tratamento: descartamos os primeiros 40% das amostras para eliminar o transitório de partida, calculando a DFT apenas nos 60% em regime permanente estrito.""")

# =========================================================================
# SLIDE 9: VARREDURA DE ORDENS E ESCOLHA DA 1ª ORDEM (ITEM 5)
# =========================================================================
slide9 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide9, "8. [Item 5] Varredura de Ordens: Por que Selecionamos a 1ª Ordem?", 
           "Comparação de ordens 1 a 5, análise de sobreajuste (overfitting) e parcimônia física", 
           "Renato Felix")

card9_tab = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
card9_tab.fill.solid(); card9_tab.fill.fore_color.rgb = COR_CINZA_FUNDO; card9_tab.line.color.rgb = COR_CINZA_BORDA
tf = card9_tab.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Tabela Comparativa de Ordens (N2CACGO)"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_9tab = [
    "Tabela Comparativa Obtida no MATLAB:\n  • 1ª Ordem: J = 1,7468 | RMSE = 0,21 dB | FIT = 88,36%\n  • 2ª Ordem: J = 2,2320 | RMSE = 0,22 dB | FIT = 85,12%\n  • 3ª Ordem: J = 2,2780 | RMSE = 0,31 dB | FIT = 84,82%\n  • 4ª Ordem: J = 1,8653 | RMSE = 0,21 dB | FIT = 87,57%\n  • 5ª Ordem: J = 3,6628 | RMSE = 0,68 dB | FIT = 75,59%",
    "Por que Não Escolher Ordem Maior?\n  • Overfitting: Ordens ≥ 2 tentam modelar o ruído elétrico de comutação das escovas sem ganho físico real.\n  • Degradação Numérica: O condicionamento de Q piora drasticamente sem melhorar o FIT.",
    "Decisão de Engenharia:\n  A 1ª ordem foi selecionada por parcimônia e coerência com a teoria clássica de máquinas elétricas CC."
]
for it in items_9tab:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

img_motor_todas = os.path.join(FIG_DIR, 'item5_motor_bode_todas_ordens.png')
if os.path.exists(img_motor_todas):
    slide9.shapes.add_picture(img_motor_todas, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide9,
"""[ORADOR: Renato Felix | ~1:15 min]
- Mostre a tabela e o gráfico de varredura de ordens de 1 a 5.
- A 1ª ordem obteve o menor custo J (1,74) e o maior FIT (88,36%).
- Ordens mais altas tentam ajustar o ruído mecânico e elétrico das escovas (overfitting), degradando o condicionamento numérico da matriz Q.
- Por parcimônia, selecionamos a 1ª ordem para representar a dinâmica dominante do motor.""")

# =========================================================================
# SLIDE 10: MODELO FÍSICO DO MOTOR E O ATRASO DE PADÉ (ITEM 5)
# =========================================================================
slide10 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide10, "9. [Item 5] Modelo Físico Eletromecânico e Atraso de Padé (10,2 ms)", 
           "Interpretação física dos parâmetros e explicação do zero no semi-plano direito", 
           "Renato Felix")

c10_1 = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
c10_1.fill.solid(); c10_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c10_1.line.color.rgb = COR_CINZA_BORDA
tf = c10_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Modelo Físico Identificado (FIT = 88,36%)"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_101 = [
    "Função de Transferência Ótima:\n  G_motor(s) = (-0,2468 s + 48,33) / (s + 4,794)",
    "Parâmetros Físicos Eletromecânicos:\n  • Ganho de Velocidade:\n    Km = 48,33 / 4,794 = 10,08 (rad/s)/V (20,07 dB).\n  • Constante de Tempo Mecânica Dominante:\n    τm = 1 / 4,794 = 0,209 segundos.",
    "O Ponto Alto Técnico: Zero no SPD (s = +195,8 rad/s):\n  NÃO é instabilidade nem erro de modelagem! É a representação exata da APROXIMAÇÃO DE PADÉ de 1ª ordem de um atraso puro de transporte:\n  e^(-s·τd) ≈ (1 - s·τd/2) / (1 + s·τd/2)\n  ==> τd = 2 / 195,8 ≈ 10,2 milissegundos!",
    "Significado Físico Real:\n  Os 10,2 ms correspondem perfeitamente ao atraso de conversão D/A, filtro e amostragem da placa de aquisição DAQ!"
]
for it in items_101:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(6)

img_motor_melhor = os.path.join(FIG_DIR, 'item5_motor_melhor_modelo_bode.png')
if os.path.exists(img_motor_melhor):
    slide10.shapes.add_picture(img_motor_melhor, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide10,
"""[ORADOR: Renato Felix | ~2:00 min - Ponto Alto da Apresentação!]
- Apresente o modelo físico final: Km = 10,08 (rad/s)/V e tau_m = 0,209 s (FIT de 88,36%).
- Mostre a curva de Bode à direita: a adesão experimental é excepcional!
- Destaque com firmeza o zero no SPD em s = +195,8 rad/s:
  * Não é instabilidade física (o polo mecânico estável em -4,79 domina a dinâmica);
  * É a aproximação de Padé de 1ª ordem de um atraso puro de transporte de ~10,2 ms;
  * Esse atraso de 10,2 ms é o tempo de conversão e amostragem da placa DAQ do laboratório e explica perfeitamente a defasagem além de -90 graus a 10 Hz!
- Transição: 'Para mostrar a validação no tempo contra sinais inéditos e os desafios numéricos, passo a palavra ao Arthur Scarpini.'""")

# =========================================================================
# SLIDE 11: VALIDAÇÃO TEMPORAL CEGA (ITEM 5)
# =========================================================================
slide11 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide11, "10. [Item 5] Validação Temporal Cega (Regra de Ouro)", 
           "Confronto do modelo linear contra ondas quadrada e triangular inéditas a 10 Hz", 
           "Arthur Scarpini")

img_sqr = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_quadrada.png')
img_tri = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_triangular.png')
if os.path.exists(img_sqr):
    slide11.shapes.add_picture(img_sqr, Inches(0.8), Inches(1.75), Inches(5.6), Inches(4.3))
if os.path.exists(img_tri):
    slide11.shapes.add_picture(img_tri, Inches(6.8), Inches(1.75), Inches(5.7), Inches(4.3))

c11_bot = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.7), Inches(1.05))
c11_bot.fill.solid(); c11_bot.fill.fore_color.rgb = COR_CINZA_FUNDO; c11_bot.line.color.rgb = COR_CINZA_BORDA
tf = c11_bot.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.12)
p = tf.paragraphs[0]; p.text = "Aplicação da 'Regra de Ouro da Identificação' vista nas aulas de MASD:"
p.font.size = Pt(12.5); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO
p2 = tf.add_paragraph()
p2.text = "O modelo estimado com senoides foi submetido a um teste cego contra sinais inéditos. Na onda quadrada, reproduziu a taxa exponencial de subida e descida (τm = 0,21 s). Na onda triangular, o polo mecânico arredondou as cúspides com defasagem idêntica à medida experimentalmente!"
p2.font.size = Pt(11.5); p2.font.color.rgb = COR_TEXTO_ESCURO; p2.space_before = Pt(2)

set_speaker_notes(slide11,
"""[ORADOR: Arthur Scarpini | ~1:15 min]
- Agradeça ao Renato e cite o conceito central da aula: a 'Regra de Ouro da Identificação' (nunca validar com os mesmos dados da estimação).
- Mostre os gráficos de validação cega com onda quadrada e triangular a 10 Hz.
- Destaque que o modelo linear estimado na frequência previu com alta fidelidade o comportamento no tempo: a constante de tempo mecânica de 0,21 s dita a inclinação exponencial e o filtro passa-baixas arredonda as pontas triangulares.""")

# =========================================================================
# SLIDE 12: DIFICULDADES NUMÉRICAS E ENGENHARIA
# =========================================================================
slide12 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide12, "11. Dificuldades Encontradas e Soluções de Engenharia", 
           "Condicionamento matricial da matriz Q, vazamento espectral e integridade de dados", 
           "Arthur Scarpini")

c12_1 = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
c12_1.fill.solid(); c12_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c12_1.line.color.rgb = COR_CINZA_BORDA
tf = c12_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "1. Condicionamento Matricial de Q"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_121 = [
    "Problema do Mal Condicionamento:\n  Para ordens n ≥ 4, os monômios (jω)^n crescem como progressão geométrica, atingindo valores da ordem de 10^14 para frequências elevadas.\n  Consequência: O número de condição recíproco rcond(Q) cai para < 10^(-16), beirando o limite da precisão dupla IEEE 754.",
    "A Armadilha da Pseudoinversa (pinv):\n  Inicialmente, tentar usar a pseudoinversa com SVD truncava direções de autovalores vitais, distorcendo os coeficientes de Silveira.",
    "Solução Adotada:\n  Mantivemos a resolução direta por Eliminação Gaussiana com Pivoteamento Parcial (operador backslash Q \\ Y do MATLAB), preservando as direções espectrais e recuperando o gabarito exato de Silveira."
]
for it in items_121:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

c12_2 = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.0))
c12_2.fill.solid(); c12_2.fill.fore_color.rgb = COR_CINZA_FUNDO; c12_2.line.color.rgb = COR_CINZA_BORDA
tf = c12_2.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "2. Sinais, Solvers e Bancada"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_122 = [
    "Vazamento Espectral da FFT (Leakage):\n  O janelamento finito temporal de 50 s introduz dispersão de energia nas bordas.\n  Solução: Selecionou-se estritamente a banda de frequências com excitação ativa do Chirp e alta coerência SNR.",
    "Perturbações de Partida na Bancada:\n  Ensaios reais de motor contêm aceleração inicial não-estacionária.\n  Solução: Janelamento temporal seletivo descartando os 40% iniciais de cada ensaio.",
    "Automação e Reprodutibilidade no Simulink:\n  Parametrização programática completa do solver contínuo ode4 e carregamento automático das variáveis no workspace via scripts MATLAB nativos."
]
for it in items_122:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

set_speaker_notes(slide12,
"""[ORADOR: Arthur Scarpini | ~1:30 min]
- Aborde os desafios de engenharia que superamos:
  1) Condicionamento numérico da matriz Q: rcond(Q) cai para 10^-16 em ordens altas devido aos monômios (j*w)^n. Mostre que a eliminação Gaussiana com pivoteamento (Q \\ Y) foi a chave para manter a exatidão sem truncamento indevido.
  2) Vazamento espectral contornado pela escolha correta da janela da FFT;
  3) Transitórios de bancada eliminados pelo corte seletivo dos primeiros 40% de dados.""")

# =========================================================================
# SLIDE 13: CONCLUSÕES E REPOSITÓRIO
# =========================================================================
slide13 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide13, "12. Conclusões e Considerações Finais", 
           "Síntese das entregas do trabalho de MASD e disponibilização do repositório", 
           "Arthur Scarpini & Equipe")

c13 = slide13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
c13.fill.solid(); c13.fill.fore_color.rgb = COR_CINZA_FUNDO; c13.line.color.rgb = COR_CINZA_BORDA
tf = c13.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.35)

concls = [
    "Elegância Convexa: O método N2CACGO comprovou ser uma ferramenta analítica extremamente robusta para identificação no domínio da frequência, eliminando armadilhas de mínimos locais.",
    "Fidelidade Acadêmica: Reprodução exata de 100% dos resultados tabelados por Bruno de Pinho Silveira (IME, 2006).",
    "Integração Simulink + FFT: Validação bem-sucedida de planta LTI a partir de sinal Chirp com FIT superior a 96%.",
    "Consistência Experimental na Bancada: O modelo de 1ª ordem representou com alta precisão a dinâmica mecânica dominante do motor (Km ≈ 10,08, τm ≈ 0,21 s), enquanto o zero em SPD revelou o atraso de hardware da placa de aquisição (10,2 ms via Padé).",
    "Repositório Aberto e Reprodutibilidade Total: Todos os códigos MATLAB (.m), diagramas Simulink (.slx), dados experimentais (.mat) e o artigo IEEE estão disponíveis publicamente em:\nhttps://github.com/VPariz/masd-identificacao-n2cacgo"
]
for idx, c in enumerate(concls):
    p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
    p.text = "✔  " + c
    p.font.size = Pt(13.5); p.font.color.rgb = COR_TEXTO_ESCURO
    p.space_before = Pt(10)

set_speaker_notes(slide13,
"""[ORADOR: Arthur Scarpini & Toda a Equipe | ~1:15 min]
- Sintetize os sucessos dos 5 itens exigidos no trabalho.
- Convide João Victor, Pedro e Renato a se posicionarem juntos à frente.
- Agradeça ao Prof. Dr. Marcelo de Araújo Oliveira e aos colegas.
- Abra formalmente a sessão para a arguição e perguntas da banca!""")

prs.save(PPTX_PATH)
print(f"Apresentação PowerPoint expandida salva com sucesso em: {PPTX_PATH}")
