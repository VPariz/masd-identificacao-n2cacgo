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
COR_EQUACAO_BG  = RGBColor(232, 240, 254)   # Azul suave para destaque de fórmulas

def add_header(slide, title_text, subtitle_text="", speaker_name=""):
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.32), Inches(9.0), Inches(1.15))
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
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(0.38), Inches(2.7), Inches(0.58))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(230, 240, 255)
        pill.line.color.rgb = COR_AZUL_MEDIO
        tf_p = pill.text_frame
        tf_p.word_wrap = True
        tf_p.margin_left = tf_p.margin_top = tf_p.margin_right = tf_p.margin_bottom = 0
        p_sp = tf_p.paragraphs[0]
        p_sp.text = f"👤 {speaker_name}"
        p_sp.font.size = Pt(11.5)
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
# SLIDE 1: CAPA INSTITUCIONAL (RENATO FELIX)
# =========================================================================
slide1 = prs.slides.add_slide(prs.slide_layouts[6])
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg1.fill.solid(); bg1.fill.fore_color.rgb = COR_AZUL_ESCURO
bg1.line.color.rgb = COR_AZUL_ESCURO

tbox1 = slide1.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.3), Inches(3.6))
tf1 = tbox1.text_frame; tf1.word_wrap = True

p = tf1.paragraphs[0]
p.text = "INSTITUTO MILITAR DE ENGENHARIA • DE/3 • MASD"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_DOURADO

p = tf1.add_paragraph()
p.text = "Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO"
p.font.size = Pt(29); p.font.bold = True; p.font.color.rgb = COR_BRANCO; p.space_before = Pt(8)

p = tf1.add_paragraph()
p.text = "Fundamentação Convexa de Silveira (2006), Implementação MATLAB/Simulink e Caracterização Experimental de Motor CC"
p.font.size = Pt(15); p.font.color.rgb = RGBColor(200, 220, 245); p.space_before = Pt(6)

abox1 = slide1.shapes.add_textbox(Inches(1.0), Inches(4.35), Inches(11.3), Inches(2.8))
tf_a = abox1.text_frame; tf_a.word_wrap = True

p = tf_a.paragraphs[0]
p.text = "Equipe de Autores (Nomes de Guerra em Destaque):\n" \
         "• Renato Felix (Renato Costa Félix)  |  • Pariz (João Victor Tavares Pariz)\n" \
         "• Pedro Augusto / Peu (Pedro Augusto dos Santos Barbosa)  |  • Scarpini (Wagner Scarpini Miranda)\n\n" \
         "Divisão dos 4 Blocos da Apresentação Técnica (~15 a 17 min):\n" \
         "1. Teoria dos Métodos e N2CACGO Convexo (Slides 1 a 3) ── 🎤 Renato Felix\n" \
         "2. Códigos MATLAB, Fluxograma e Modelo Simulink (Slides 4 a 6) ── 🎤 Pariz\n" \
         "3. Benchmarks Acadêmicos, FFT e Bancada do Motor CC (Slides 7 a 11) ── 🎤 Pedro Augusto (Peu)\n" \
         "4. Validação Temporal Cega, Dificuldades e Conclusões (Slides 12 a 14) ── 🎤 Scarpini\n\n" \
         "Orientador: Prof. Dr. Marcelo de Araújo Oliveira  |  Disciplina: Modelagem e Análise de Sistemas Dinâmicos"
p.font.size = Pt(12); p.font.color.rgb = RGBColor(220, 230, 245)

set_speaker_notes(slide1,
"""[ORADOR: Renato Felix | ~1:00 min]
- Bom dia / boa tarde ao Prof. Dr. Marcelo de Araújo Oliveira e aos colegas da banca.
- Apresente a equipe: Renato Felix, João Victor Pariz, Pedro Augusto e Wagner Scarpini.
- Apresente o título do trabalho: Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO.
- Explique a divisão dos 4 blocos da apresentação técnica:
  1) Eu (Renato Felix) abro com a fundamentação de modelagem vs. identificação e a teoria matemática convexa de Silveira (2006);
  2) O Pariz explicará a estrutura dos códigos em MATLAB, o fluxograma geral integrado e a montagem do modelo no Simulink;
  3) O Pedro Augusto apresentará a validação do benchmark de Silveira, a reconstrução espectral via FFT e toda a parte experimental do motor CC;
  4) E o Scarpini conduzirá a validação temporal cega no motor com ondas quadrada e triangular, as dificuldades numéricas e as conclusões finais.
- Vamos iniciar direto pela teoria dos métodos de identificação.""")

# =========================================================================
# SLIDE 2: TEORIA DOS MÉTODOS (RENATO FELIX)
# =========================================================================
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide2, "1. Teoria dos Métodos: Modelagem vs. Identificação", 
           "Classificação de modelos (Caixa Branca/Cinza/Preta) e vantagens da abordagem frequencial", 
           "Renato Felix")

c2_1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1))
c2_1.fill.solid(); c2_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c2_1.line.color.rgb = COR_CINZA_BORDA
tf = c2_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Tipologia de Modelos Dinâmicos"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_21 = [
    "Classificação Canônica de Modelos (Aulas MASD):\n  • Caixa Branca (Dedutivo Puro): Leis físicas de primeiros princípios (Newton, Kirchhoff). Sem dados empíricos. Limitado por incertezas paramétricas.\n  • Caixa Cinza (Híbrido): Estrutura fenomenológica conhecida com estimação estatística de parâmetros desconhecidos (ex: resistência de armadura e inércia do rotor).\n  • Caixa Preta (Empírico): Mapeamento matemático estrito de entrada-saída.",
    "Gargalos do Domínio do Tempo (ARX, ARMAX, PEM):\n  • Ruído Colorido: Vulnerabilidade crítica a ruídos estocásticos que polarizam as matrizes de covariância.\n  • Condições Iniciais: Exigência estrita de repouso prévio x(0) = 0. Transitórios iniciais geram viés sistemático.\n  • Atraso de Transporte: Dificuldade em estimar atrasos puros sem sobreparametrizar desnecessariamente o modelo discreto."
]
for it in items_21:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

c2_2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1))
c2_2.fill.solid(); c2_2.fill.fore_color.rgb = COR_CINZA_FUNDO; c2_2.line.color.rgb = COR_CINZA_BORDA
tf = c2_2.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Por que Domínio da Frequência?"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_22 = [
    "1. Filtragem Natural Fora da Banda:\n  A FRF avalia apenas a resposta forçada em frequências discretas ωk, rejeitando integralmente ruídos e perturbações fora da banda excitada.",
    "2. Alta Precisão em Ressonâncias e Amortecimento:\n  Ajuste direto do módulo e da defasagem angular nas frequências críticas de crossover do sistema de controle.",
    "3. Compactação Espectral Brutal:\n  Milhares de amostras temporais brutas são comprimidas em alguns fasores de alta relação sinal-ruído (SNR).",
    "O Dilema dos Métodos Frequenciais Clássicos:\n  • Levy (1959) e Sanathanan-Koerner (1963): Sofrem de ponderação distorcida e dependem de iterações.\n  • Valle (2005) e Nelder-Mead: Otimizações não-convexas sujeitas a mínimos locais espúrios!"
]
for it in items_22:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

set_speaker_notes(slide2,
"""[ORADOR: Renato Felix | ~1:15 min]
- Conceitue as três abordagens fundamentais: Caixa Branca, Caixa Cinza e Caixa Preta, exatamente como o Prof. Marcelo ensina no curso.
- Enfatize por que a identificação no domínio da frequência é superior para sistemas de controle:
  1) Filtragem inerente de ruídos fora da banda útil;
  2) Sensibilidade direta a picos de ressonância e margens de estabilidade;
  3) Compactação de dados pesados em poucos fasores precisos.
- Mencione os métodos clássicos de Levy e Sanathanan-Koerner e aponte que métodos de otimização genéricos não-convexos caem em armadilhas de mínimos locais.""")

# =========================================================================
# SLIDE 3: O MÉTODO N2CACGO DE SILVEIRA (2006) - FORMULAÇÃO DESTACADA E GRANDE
# =========================================================================
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide3, "2. O Método N2CACGO (Silveira, 2006): Formulação Convexa", 
           "Estrutura polinomial, resíduo de equação estritamente linear e solução analítica global única", 
           "Renato Felix")

# Card Superior Esquerdo: Formulação Matemática em DESTAQUE GRANDE
c3_eq = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.1))
c3_eq.fill.solid(); c3_eq.fill.fore_color.rgb = COR_EQUACAO_BG; c3_eq.line.color.rgb = COR_AZUL_MEDIO
tf = c3_eq.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)

p = tf.paragraphs[0]; p.text = "Formulação Matemática do Modelo"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

eq_texts = [
    ("Função de Transferência Biprópria:", Pt(12), False, COR_TEXTO_ESCURO),
    ("Ge(s) = N(s) / D(s)", Pt(20), True, COR_AZUL_ESCURO),
    ("N(s) = α₀ sⁿ + α₁ sⁿ⁻¹ + ... + αₙ\nD(s) = sⁿ + β₁ sⁿ⁻¹ + ... + βₙ  (D monic)", Pt(14), True, RGBColor(10, 50, 110)),
    ("Resíduo Linear de Equação (Silveira, 2006):", Pt(12), False, COR_TEXTO_ESCURO),
    ("e(jωₖ) = D(jωₖ) · G(jωₖ) − N(jωₖ)", Pt(18), True, RGBColor(160, 20, 20)),
    ("Funcional de Custo Quadrático Convexo:", Pt(12), False, COR_TEXTO_ESCURO),
    ("J(θ) = ∑ | e(jωₖ) |² = || D · G − N ||₂²", Pt(18), True, COR_AZUL_ESCURO),
    ("Vetor de Parâmetros Ótimos:  θ = [α₀, ..., αₙ, β₁, ..., βₙ]ᵀ  ∈  ℝ^(2n+1)", Pt(11.5), False, COR_TEXTO_ESCURO)
]
for t, sz, bld, col in eq_texts:
    p = tf.add_paragraph(); p.text = t
    p.font.size = sz; p.font.bold = bld; p.font.color.rgb = col; p.space_before = Pt(6)

# Card Direito: Garantia de Convexidade e SEL Analítico
c3_sel = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.8), Inches(5.4), Inches(5.1))
c3_sel.fill.solid(); c3_sel.fill.fore_color.rgb = COR_CINZA_FUNDO; c3_sel.line.color.rgb = COR_CINZA_BORDA
tf = c3_sel.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Garantia de Convexidade e Solução Única"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_3sel = [
    "Propriedade de Convexidade Estrita:\n  Como o resíduo e(jωk) é ESTRITAMENTE LINEAR nos coeficientes α e β, o funcional J(θ) é uma forma quadrática estritamente convexa.\n  • Matriz Hessiana: ∇²J(θ) > 0 (positiva definida).\n  • Consequência: ZERO mínimos locais! O ponto estacionário é o MÍNIMO GLOBAL ÚNICO.",
    "Sistema de Equações Lineares (SEL Particionado):\n  Derivando analiticamente ∂J/∂θ = 0 obtém-se o sistema:\n  [ Q₁   −Q₂ ] [ α ]   [ Y₁ ]\n  [ Q₃   −Q₄ ] [ β ] = [ Y₂ ]   ==>   Q · θ = Y",
    "Solução Fechada Sem Iteração:\n  θ* = Q⁻¹ · Y  (calculado em UM ÚNICO PASSO via eliminação Gaussiana, livre de divergência numérica!).",
    "Transição de Fala:\n  'Para detalhar como esse algoritmo analítico e as métricas de validação foram implementados em MATLAB, passo a palavra ao João Victor Pariz.'"
]
for it in items_3sel:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(11.8); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(6)

set_speaker_notes(slide3,
"""[ORADOR: Renato Felix | ~1:30 min - Destaque Teórico da Apresentação!]
- Enfatize com clareza a formulação matemática da dissertação de Bruno de Pinho Silveira (IME, 2006):
  * O resíduo e(jw) = D(jw)*G(jw) - N(jw) é estritamente LINEAR nos parâmetros theta.
  * O funcional J(theta) em Norma 2 é uma forma quadrática ESTRITAMENTE CONVEXA com Hessiano positivo definido.
  * Isso garante matematicamente que NÃO EXISTEM MÍNIMOS LOCAIS!
  * A condição de otimalidade grad(J) = 0 conduz diretamente ao sistema linear de equações normais Q*theta = Y.
  * A solução ótima global theta* = Q^-1 * Y é obtida analiticamente em um único passo, sem buscas iterativas.
- Conclua sua fala e passe a palavra: 'Para detalhar como esse algoritmo analítico e as métricas de validação foram implementados em MATLAB, passo a palavra ao João Victor Pariz.'""")

# =========================================================================
# SLIDE 4: CÓDIGOS MATLAB (PARIZ)
# =========================================================================
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide4, "3. [Item 1 & 2] Implementação Vetorizada no MATLAB", 
           "Estrutura modular do script identifica_N2CACGO.m e da rotina valida_modelo_fr.m", 
           "Pariz")

c4_1 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.1))
c4_1.fill.solid(); c4_1.fill.fore_color.rgb = COR_CODE_BG; c4_1.line.color.rgb = COR_CINZA_BORDA
tf = c4_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.2)
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
p2.font.size = Pt(9.2); p2.font.name = "Consolas"; p2.font.color.rgb = RGBColor(10, 40, 90); p2.space_before = Pt(4)

c4_2 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.8), Inches(5.4), Inches(5.1))
c4_2.fill.solid(); c4_2.fill.fore_color.rgb = COR_CINZA_FUNDO; c4_2.line.color.rgb = COR_CINZA_BORDA
tf = c4_2.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Rotina de Validação: valida_modelo_fr.m"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_42 = [
    "Entradas da Rotina de Validação:\n  • Vetor de frequências angulares ω [rad/s].\n  • Resposta em frequência experimental G_med(jω).\n  • Objeto tf retornado pelo N2CACGO.",
    "Métricas de Avaliação Oficial (Aulas MASD):\n  1. Custo J em Norma 2 (Silveira 2006):\n     J = || G_med(jω) − G_id(jω) ||₂\n  2. RMSE de Magnitude em dB:\n     RMSE_mag = √[ (1/m) ∑ (20 log₁₀ |G_med/G_id|)² ]\n  3. RMSE de Fase em graus:\n     RMSE_fase = √[ (1/m) ∑ (∠G_med − ∠G_id)² ]\n  4. Coeficiente de Ajuste Global (FIT %):\n     FIT = [ 1 − ||G_med − G_id|| / ||G_med − G_médio|| ] × 100%",
    "Diagnóstico e Plots Automatizados:\n  Gera diagramas de Bode comparativos com magnitude e fase sobrepostas para inspeção visual imediata."
]
for it in items_42:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(11.8); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(6)

set_speaker_notes(slide4,
"""[ORADOR: Pariz | ~1:15 min]
- Agradeça ao Renato e apresente a arquitetura dos códigos em MATLAB:
  1) No Item 1, implementamos a rotina identifica_N2CACGO.m vetorizada, sem laços de otimização;
  2) Construímos a matriz de base polinomial monomial R com as potências (j*w)^k;
  3) Montamos os quatro blocos da matriz Q e o vetor Y usando projeções Hermitianas (real(R*R_H));
  4) Resolvemos o sistema com o operador backslash (Q \\ Y), que executa a fatoração LU com pivoteamento ótimo.
- No Item 2, criamos a rotina valida_modelo_fr.m, que computa as métricas ensinadas pelo professor: o custo J, os RMSEs de magnitude e fase e o FIT percentual oficial.""")

# =========================================================================
# SLIDE 5: FLUXOGRAMA INTEGRADO: MATLAB & SIMULINK (PARIZ)
# =========================================================================
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide5, "4. Fluxograma Integrado: Do Sinal Temporal à Identificação", 
           "Visão holística da arquitetura de processamento computacional integrando MATLAB e Simulink", 
           "Pariz")

img_fluxo = os.path.join(FIG_DIR, 'fluxograma_matlab_simulink.png')
if os.path.exists(img_fluxo):
    slide5.shapes.add_picture(img_fluxo, Inches(0.8), Inches(1.65), Inches(11.733), Inches(5.4))

set_speaker_notes(slide5,
"""[ORADOR: Pariz | ~1:15 min]
- Apresente o fluxograma geral que desenvolvemos para amarrar todas as etapas do trabalho:
  1) Três Fontes de Dados de Entrada:
     - Modelos didáticos e benchmark de Silveira (Item 3);
     - Simulação dinâmica com excitação Chirp no Simulink (Item 4);
     - Ensaios experimentais senoidais do motor CC da bancada de SSL (Item 5);
  2) Processamento Espectral Intermediário:
     - No caso dos sinais temporais do Simulink, passamos pelo cálculo da FRF via razão de FFTs Y(k)/U(k);
     - No caso do motor, extraímos ganho e fase no regime permanente de cada senoide;
  3) Núcleo Algorítmico Central: N2CACGO em MATLAB:
     - Montagem das matrizes Q e Y;
     - Resolução analítica em passo único;
  4) Rotina de Validação e Diagnóstico:
     - Cálculo de J, RMSE, FIT e validação cega com sinais temporais no motor.""")

# =========================================================================
# SLIDE 6: O MODELO SIMULINK COM O PRINT DO DIAGRAMA (PARIZ)
# =========================================================================
slide6 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide6, "5. [Item 4] O Modelo Simulink: Diagrama de Blocos e Simulação", 
           "Estrutura do modelo_item4.slx, solver contínuo de passo fixo ode4 e geração dos sinais", 
           "Pariz")

# Imagem do Diagrama de Blocos do Simulink no topo/esquerda
img_sim_diag = os.path.join(FIG_DIR, 'simulink_diagrama_blocos.png')
if os.path.exists(img_sim_diag):
    slide6.shapes.add_picture(img_sim_diag, Inches(0.8), Inches(1.75), Inches(6.0), Inches(2.25))

# Imagem dos Sinais Temporais à direita
img_chirp = os.path.join(FIG_DIR, 'item4_simulink_sinais_temporais.png')
if os.path.exists(img_chirp):
    slide6.shapes.add_picture(img_chirp, Inches(7.1), Inches(1.75), Inches(5.4), Inches(5.0))

# Card explicativo embaixo do print do Simulink
c6_desc = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.15), Inches(6.0), Inches(2.6))
c6_desc.fill.solid(); c6_desc.fill.fore_color.rgb = COR_CINZA_FUNDO; c6_desc.line.color.rgb = COR_CINZA_BORDA
tf = c6_desc.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.2)
p = tf.paragraphs[0]; p.text = "Detalhes Técnicos do Modelo Simulink"
p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_6desc = [
    "1. Bloco Entrada_u (From Workspace): Injeta sinal Chirp linear de 0,1 Hz a 15 Hz por 50 s gerado no MATLAB.",
    "2. Bloco Planta_LTI (Transfer Fcn): Implementa a dinâmica contínua G(s) = 8 / (0,2 s² + 1,2 s + 1) = 40 / (s² + 6 s + 5).",
    "3. Bloco Saida_y (To Workspace): Registra a série temporal de saída com Ts = 1 ms (20.001 amostras em formato Array).",
    "4. Solver Contínuo ode4: Algoritmo Runge-Kutta de 4ª ordem com passo fixo (dt = 0,001 s), garantindo precisão absoluta sem truncamento.",
    "Transição de Fala: 'Para apresentar os resultados desse modelo Simulink, a validação acadêmica de Silveira e o caso do motor CC, passo a palavra ao Pedro Augusto.'"
]
for it in items_6desc:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(10.5); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(3)

set_speaker_notes(slide6,
"""[ORADOR: Pariz | ~1:15 min]
- Apresente o modelo do Simulink exibido no slide (modelo_item4.slx):
  * O bloco Entrada_u injeta o sinal Chirp contínuo varrendo de 0,1 a 15 Hz por 50 segundos;
  * O bloco Planta_LTI executa a dinâmica contínua da planta com polos em -1 e -5 e ganho 8;
  * O bloco Saida_y exporta a série temporal y(t) de volta ao Workspace via To Workspace em formato de Array;
  * Usamos o solver contínuo de passo fixo ode4 (Runge-Kutta de 4ª ordem), garantindo alta fidelidade sem ruídos numéricos.
- Destaque que enquanto outros grupos relataram dificuldade em montar o Simulink, nosso modelo funcionou perfeitamente e forneceu dados ideais para a FFT.
- Passe a palavra: 'Para apresentar a validação teórica de Silveira, os resultados espectrais da FFT e o caso do motor CC, passo a palavra ao Pedro Augusto.'""")

# =========================================================================
# SLIDE 7: BENCHMARK SILVEIRA 2006 (PEDRO AUGUSTO)
# =========================================================================
slide7 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide7, "6. [Item 3] Validação Teórica: Benchmark de Silveira (2006)", 
           "Reprodução exata da Tabela 3.2 da dissertação de mestrado (Ordens 1 a 7)", 
           "Pedro Augusto")

table_shape = slide7.shapes.add_table(8, 5, Inches(0.8), Inches(1.8), Inches(6.5), Inches(4.9))
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
    slide7.shapes.add_picture(img_silv, Inches(7.5), Inches(1.8), Inches(5.0), Inches(4.9))

set_speaker_notes(slide7,
"""[ORADOR: Pedro Augusto | ~1:15 min]
- Agradeça ao Pariz e apresente os resultados acadêmicos do Item 3:
- Mostre a tabela de confronto direto: reproduzimos com absoluta fidelidade a Tabela 3.2 da dissertação de Bruno de Pinho Silveira (IME, 2006).
- Explique o princípio da parcimônia:
  * A planta-alvo de Silveira é de 4ª ordem;
  * Até a 3ª ordem, o erro é alto (FIT de 57%);
  * Na 4ª ordem, o erro despenca para 6,28e-4 e o FIT atinge 99,98%!
  * As ordens 5 a 7 trazem apenas polos e zeros que quase se cancelam, confirmando que a 4ª ordem é a ordem ótima.
- Além disso, testamos sistemas didáticos puros de 1ª, 2ª e 3ª ordem, obtendo FIT de 100% e erro numérico residual nulo.""")

# =========================================================================
# SLIDE 8: RESULTADOS SIMULINK E FFT (PEDRO AUGUSTO)
# =========================================================================
slide8 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide8, "7. [Item 4] Extração por FFT e Validação do Modelo Identificado", 
           "Processamento espectral de 126 fasores e recuperação analítica com FIT de 96,47%", 
           "Pedro Augusto")

c8_1 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
c8_1.fill.solid(); c8_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c8_1.line.color.rgb = COR_CINZA_BORDA
tf = c8_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Extração Espectral e Parâmetros Obtidos"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_81 = [
    "Extração Espectral via FFT:\n  G_med(jωₖ) = FFT{y(t)} / FFT{u(t)} = Y(k) / U(k)\n  Isolaram-se 126 frequências entre 1,26 e 79,76 rad/s com coerência SNR elevada.",
    "Modelo Identificado pelo N2CACGO:\n  G_id(s) = 40,0 / (s² + 6,005 s + 4,818)\n  (Planta Nominal: 40 / (s² + 6,000 s + 5,000)).",
    "Exatidão dos Polos e Ganho:\n  • Polos Estimados: s₁ = −0,967 e s₂ = −5,038\n    (Nominais: −1,000 e −5,000 — erro < 3%).\n  • Ganho Estático: 8,30 (Nominal: 8,00).",
    "Métricas de Ajuste Espectral:\n  • FIT Global: 96,47%\n  • RMSE de Módulo: 0,165 dB\n  • RMSE de Fase: 1,025 graus\n  A pequena dispersão decorre do vazamento espectral natural da FFT finita."
]
for it in items_81:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

img_fft = os.path.join(FIG_DIR, 'item4_simulink_bode_validacao.png')
if os.path.exists(img_fft):
    slide8.shapes.add_picture(img_fft, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide8,
"""[ORADOR: Pedro Augusto | ~1:00 min]
- Apresente os resultados espectrais da simulação do Simulink:
  * Calculamos a FRF estimada através da razão fasorial Y(k)/U(k);
  * O algoritmo N2CACGO ajustou uma função de 2ª ordem que recuperou os polos nominais em -1 e -5 com menos de 3% de discrepância;
  * Obtivemos um FIT excelente de 96,47%, com RMSE de módulo de 0,16 dB e RMSE de fase de apenas 1 grau;
  * O gráfico de Bode à direita comprova a perfeita superposição entre o modelo identificado e a planta real.""")

# =========================================================================
# SLIDE 9: O CASO DO MOTOR CC E OS DADOS EXPERIMENTAIS (PEDRO AUGUSTO)
# =========================================================================
slide9 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide9, "8. [Item 5] O Caso do Motor CC: Dados de Bancada Real (SSL)", 
           "Origem dos dados do Grupo 3 de SSL: 26 ensaios senoidais puros e rigor metrológico", 
           "Pedro Augusto")

c9_1 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
c9_1.fill.solid(); c9_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c9_1.line.color.rgb = COR_CINZA_BORDA
tf = c9_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Origem e Características dos Dados"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_91 = [
    "Contexto da Bancada Física (Grupo 3 - SSL):\n  • Planta: Motor de Corrente Contínua (CC) acoplado a carga inercial.\n  • Entrada u(t): Tensão de armadura sintetizada por gerador de sinais e amplificada por ponte H PWM.\n  • Saída y(t): Velocidade angular mensurada por tacômetro digital ótico (pulsos por rotação).",
    "Protocolo Metrológico de Varredura:\n  • 26 ensaios senoidais puros com frequências varrendo de 0,20 Hz a 10,00 Hz (1,26 a 62,83 rad/s).\n  • Amostragem digital com frequência fs = 1 kHz.\n  • Cada ensaio contém 10.000 amostras temporais por canal.",
    "Tratamento Rigoroso de Regime Permanente:\n  Para eliminar transitórios de partida e distorções iniciais, descartamos os primeiros 40% de cada ensaio e processamos apenas os últimos 60% via regressão senoidal de mínimos quadrados."
]
for it in items_91:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

c9_2 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
c9_2.fill.solid(); c9_2.fill.fore_color.rgb = COR_CINZA_FUNDO; c9_2.line.color.rgb = COR_CINZA_BORDA
tf = c9_2.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Extração dos Fasores de Resposta em Frequência"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_92 = [
    "Ajuste Senoidal de Mínimos Quadrados:\n  Para cada frequência ωₖ, ajustou-se analiticamente:\n  u(t) = Aᵤ · cos(ωₖ t + ϕᵤ)\n  y(t) = Aᵧ · cos(ωₖ t + ϕᵧ)",
    "Fasor Experimental da FRF:\n  G_med(jωₖ) = (Aᵧ / Aᵤ) · exp( j(ϕᵧ − ϕᵤ) )\n  Esse procedimento garante imunidade contra distorções harmônicas e ruído de comutação das escovas.",
    "Comportamento Físico Observado:\n  • Em baixas frequências (0,2 Hz): Ganho estático próximo de 10 (rad/s)/V (+20 dB).\n  • Frequência de corte a ~4,8 rad/s (0,76 Hz): Decaimento de magnitude de −20 dB/década.\n  • Defasagem angular ultrapassa −90° em altas frequências, atingindo −104° a 10 Hz! (Mistério físico explicado no Slide 11!)."
]
for it in items_92:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

set_speaker_notes(slide9,
"""[ORADOR: Pedro Augusto | ~1:15 min]
- Explique a origem física dos dados experimentais do Item 5:
  * Foram coletados na disciplina de Sinais e Sistemas Lineares (SSL) pelo Grupo 3;
  * A entrada é a tensão de armadura e a saída é a velocidade angular do rotor;
  * O ensaio envolveu 26 senoides de 0,2 a 10 Hz;
  * Para ter rigor metrológico absoluto, eliminamos os transitórios iniciais e extraímos o ganho e a fase no regime permanente usando ajuste senoidal de mínimos quadrados;
  * Chame atenção para a defasagem que ultrapassa -90 graus a 10 Hz, que será o grande destaque da física.""")

# =========================================================================
# SLIDE 10: VARREDURA DE ORDENS DO MOTOR CC (PEDRO AUGUSTO)
# =========================================================================
slide10 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide10, "9. [Item 5] Varredura de Ordens do Motor CC (Ordens 1 a 5)", 
           "Aplicação do princípio da parcimônia de Box-Jenkins e análise comparativa de desempenho", 
           "Pedro Augusto")

c10_tab = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
c10_tab.fill.solid(); c10_tab.fill.fore_color.rgb = COR_CINZA_FUNDO; c10_tab.line.color.rgb = COR_CINZA_BORDA
tf = c10_tab.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Desempenho por Ordem (N2CACGO)"
p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_10tab = [
    "Tabela Comparativa Obtida no MATLAB:\n  • 1ª Ordem: J = 1,7468 | RMSE = 0,21 dB | FIT = 88,36%\n  • 2ª Ordem: J = 2,2320 | RMSE = 0,22 dB | FIT = 85,12%\n  • 3ª Ordem: J = 2,2780 | RMSE = 0,31 dB | FIT = 84,82%\n  • 4ª Ordem: J = 1,8653 | RMSE = 0,21 dB | FIT = 87,57%\n  • 5ª Ordem: J = 3,6628 | RMSE = 0,68 dB | FIT = 75,59%",
    "Por que Não Escolher Ordem Maior?\n  • Overfitting: Ordens ≥ 2 tentam modelar o ruído elétrico de comutação das escovas sem ganho físico real.\n  • Degradação Numérica: O condicionamento de Q piora drasticamente sem melhorar o FIT.",
    "Decisão de Engenharia:\n  A 1ª ordem foi selecionada por parcimônia e coerência com a teoria clássica de máquinas elétricas CC."
]
for it in items_10tab:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(7)

img_motor_todas = os.path.join(FIG_DIR, 'item5_motor_bode_todas_ordens.png')
if os.path.exists(img_motor_todas):
    slide10.shapes.add_picture(img_motor_todas, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide10,
"""[ORADOR: Pedro Augusto | ~1:15 min]
- Mostre a tabela e o gráfico de varredura de ordens de 1 a 5:
  * A 1ª ordem obteve o menor custo J (1,74) e o maior FIT (88,36%);
  * Ordens mais altas tentam ajustar o ruído mecânico e elétrico das escovas (overfitting), degradando o condicionamento numérico da matriz Q;
  * Pelo princípio da parcimônia ensinado em MASD, selecionamos a 1ª ordem para representar a dinâmica dominante do motor.""")

# =========================================================================
# SLIDE 11: MODELO FÍSICO DO MOTOR E O ATRASO DE PADÉ (PEDRO AUGUSTO)
# =========================================================================
slide11 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide11, "10. [Item 5] Modelo Físico Eletromecânico e Atraso de Padé (10,2 ms)", 
           "Interpretação física dos parâmetros e explicação do zero no semi-plano direito", 
           "Pedro Augusto")

c11_1 = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
c11_1.fill.solid(); c11_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c11_1.line.color.rgb = COR_CINZA_BORDA
tf = c11_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Modelo Físico Identificado (FIT = 88,36%)"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_111 = [
    "Função de Transferência Ótima:\n  G_motor(s) = (−0,2468 s + 48,33) / (s + 4,794)",
    "Parâmetros Físicos Eletromecânicos:\n  • Ganho de Velocidade:\n    Km = 48,33 / 4,794 = 10,08 (rad/s)/V (20,07 dB).\n  • Constante de Tempo Mecânica Dominante:\n    τm = 1 / 4,794 = 0,209 segundos.",
    "O Ponto Alto Técnico: Zero no SPD (s = +195,8 rad/s):\n  NÃO é instabilidade nem erro de modelagem! É a representação exata da APROXIMAÇÃO DE PADÉ de 1ª ordem de um atraso puro de transporte:\n  e^(−s·τd) ≈ (1 − s·τd/2) / (1 + s·τd/2)\n  ==> τd = 2 / 195,8 ≈ 10,2 milissegundos!",
    "Significado Físico Real:\n  Os 10,2 ms correspondem perfeitamente ao atraso de conversão D/A, filtro e amostragem da placa de aquisição DAQ!",
    "Transição de Fala: 'Para apresentar a validação cega no tempo contra sinais inéditos, as dificuldades superadas e as conclusões, passo a palavra ao Arthur Scarpini.'"
]
for it in items_111:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(11.5); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(5)

img_motor_melhor = os.path.join(FIG_DIR, 'item5_motor_melhor_modelo_bode.png')
if os.path.exists(img_motor_melhor):
    slide11.shapes.add_picture(img_motor_melhor, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))

set_speaker_notes(slide11,
"""[ORADOR: Pedro Augusto | ~1:45 min - Ponto Alto da Apresentação!]
- Apresente o modelo físico final: Km = 10,08 (rad/s)/V e tau_m = 0,209 s (FIT de 88,36%).
- Mostre a curva de Bode à direita: a adesão experimental é excepcional!
- Destaque com firmeza o zero no SPD em s = +195,8 rad/s:
  * Não é instabilidade física (o polo mecânico estável em -4,79 domina a dinâmica);
  * É a aproximação de Padé de 1ª ordem de um atraso puro de transporte de ~10,2 ms;
  * Esse atraso de 10,2 ms é o tempo de conversão e amostragem da placa DAQ do laboratório e explica perfeitamente a defasagem além de -90 graus a 10 Hz!
- Transição de fala: 'Para apresentar a validação no tempo contra sinais inéditos, as dificuldades superadas e as conclusões, passo a palavra ao Scarpini.'""")

# =========================================================================
# SLIDE 12: VALIDAÇÃO TEMPORAL CEGA (SCARPINI)
# =========================================================================
slide12 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide12, "11. [Item 5] Validação Temporal Cega (Onda Quadrada e Triangular)", 
           "Aplicação da 'Regra de Ouro da Identificação': modelo validado contra dados nunca vistos", 
           "Scarpini")

img_sqr = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_quadrada.png')
if os.path.exists(img_sqr):
    slide12.shapes.add_picture(img_sqr, Inches(0.8), Inches(1.75), Inches(5.7), Inches(3.8))

img_tri = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_triangular.png')
if os.path.exists(img_tri):
    slide12.shapes.add_picture(img_tri, Inches(6.8), Inches(1.75), Inches(5.7), Inches(3.8))

c12_desc = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.7), Inches(11.7), Inches(1.4))
c12_desc.fill.solid(); c12_desc.fill.fore_color.rgb = COR_CINZA_FUNDO; c12_desc.line.color.rgb = COR_CINZA_BORDA
tf = c12_desc.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.15)
p = tf.paragraphs[0]; p.text = "A 'Regra de Ouro da Identificação' (Slides de Aula MASD):"
p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_12desc = [
    "• Validação com Conjunto de Teste Independente: O modelo estimado exclusivamente a partir de dados senoidais foi submetido a entradas temporais inéditas de Onda Quadrada e Onda Triangular (10 Hz).",
    "• Fidelidade Dinâmica: As curvas vermelhas (modelo N2CACGO) rastreiam com extrema precisão a subida exponencial, o valor de regime permanente e o amortecimento real medido pelo sensor óptico (curvas pretas), sem divergência!"
]
for it in items_12desc:
    p = tf.add_paragraph(); p.text = it
    p.font.size = Pt(11); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(2)

set_speaker_notes(slide12,
"""[ORADOR: Scarpini | ~1:15 min]
- Agradeça ao Pedro Augusto e destaque a Regra de Ouro da Identificação ensinada pelo Prof. Marcelo:
  * Nunca valide um modelo usando apenas os mesmos dados usados para estimá-lo;
  * Nosso modelo foi calibrado com senoides puras e agora é submetido a ondas quadrada e triangular a 10 Hz;
  * Veja nos gráficos: a linha vermelha do modelo N2CACGO segue com fidelidade impecável as respostas reais medidas pelo tacômetro (linha preta);
  * Isso comprova que a constante de tempo de 0,21 s e o ganho estático de 10,08 são parâmetros físicos reais do motor!""")

# =========================================================================
# SLIDE 13: DIFICULDADES ENCONTRADAS E SOLUÇÕES (SCARPINI)
# =========================================================================
slide13 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide13, "12. Dificuldades Encontradas e Soluções de Engenharia", 
           "Desafios numéricos e metrológicos enfrentados durante a execução do trabalho", 
           "Scarpini")

c13_1 = slide13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1))
c13_1.fill.solid(); c13_1.fill.fore_color.rgb = COR_CINZA_FUNDO; c13_1.line.color.rgb = COR_CINZA_BORDA
tf = c13_1.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Desafios Numéricos Matriciais"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_131 = [
    "1. Mal-condicionamento da Matriz de Vandermonde:\n  • Causa: Para ordens n ≥ 5, as potências sᵏ = (jω)ᵏ variam muitas ordens de magnitude (ωⁿ), elevando o número de condição κ(Q) > 10¹⁵ e gerando rcond(Q) ≈ 10⁻¹⁶.\n  • Solução Implementada: Normalização e escalonamento euclidiano de colunas no MATLAB, além do uso de fatoração SVD/pseudoinversa.",
    "2. Fugas Espectrais (Spectral Leakage) na FFT:\n  • Causa: Truncamento do sinal temporal no Simulink causava vazamento de harmônicas na razão FFT Y(k)/U(k).\n  • Solução Implementada: Janelamento temporal de Hann e seleção da faixa ativa com alta coerência espectral (1,26 a 79,8 rad/s)."
]
for it in items_131:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

c13_2 = slide13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1))
c13_2.fill.solid(); c13_2.fill.fore_color.rgb = COR_CINZA_FUNDO; c13_2.line.color.rgb = COR_CINZA_BORDA
tf = c13_2.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Desafios Físicos e Metrológicos"
p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

items_132 = [
    "3. Defasagem Além de −90° em Alta Frequência:\n  • Causa: O motor apresentava defasagem de −104° a 10 Hz, impossível de modelar por uma FT estritamente de 1ª ordem sem atraso.\n  • Solução de Engenharia: Identificação de que o zero no SPD sintetizado pelo N2CACGO atua como aproximação de Padé de um atraso puro de transporte da placa DAQ (10,2 ms).",
    "4. Não-Linearidades Mecânicas (Zona Morta e Atrito):\n  • Causa: Atrito estático e de Coulomb distorcem a resposta em amplitudes reduzidas.\n  • Solução Implementada: Ajuste senoidal restrito aos últimos 60% do registro, garantindo regime permanente linearizado."
]
for it in items_132:
    p = tf.add_paragraph(); p.text = "• " + it
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

set_speaker_notes(slide13,
"""[ORADOR: Scarpini | ~1:15 min]
- Apresente as dificuldades reais encontradas e como as solucionamos como engenheiros:
  1) Mal-condicionamento da matriz Q para ordens altas: superado com escalonamento de colunas e uso de decomposição SVD;
  2) Vazamento espectral na FFT: mitigado com janelamento de Hann e corte de bordas;
  3) Atraso de transporte da bancada: absorvido elegantemente pela aproximação de Padé sintetizada no zero de fase não-mínima;
  4) Não-linearidades de atrito: tratadas descartando o transitório inicial e usando regressão senoidal de regime permanente.""")

# =========================================================================
# SLIDE 14: CONCLUSÕES FINAIS (SCARPINI)
# =========================================================================
slide14 = prs.slides.add_slide(prs.slide_layouts[6])
add_header(slide14, "13. Conclusões Finais e Fechamento", 
           "Síntese das realizações técnicas e cumprimento integral dos 8 itens do trabalho", 
           "Scarpini")

c14 = slide14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.1))
c14.fill.solid(); c14.fill.fore_color.rgb = COR_CINZA_FUNDO; c14.line.color.rgb = COR_CINZA_BORDA
tf = c14.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]; p.text = "Principais Conquistas Técnicas do Trabalho"
p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = COR_AZUL_ESCURO

conclusoes = [
    "1. Eficácia do Método N2CACGO: A formulação convexa de Bruno de Pinho Silveira (IME, 2006) comprovou-se imune a mínimos locais, com solução analítica fechada sem custo iterativo.",
    "2. Cumprimento dos 8 Itens do Trabalho:\n   • Item 1: Rotina identifica_N2CACGO.m implementada e vetorizada no MATLAB.\n   • Item 2: Rotina valida_modelo_fr.m com métricas completas (J, RMSE mag/fase, FIT %).\n   • Item 3: Validação acadêmica reproduzindo a Tabela 3.2 de Silveira e sistemas didáticos (FIT 100%).\n   • Item 4: Simulação dinâmica no Simulink (modelo_item4.slx) com recuperação espectral FFT (FIT 96,47%).\n   • Item 5: Identificação física da bancada de motor CC com interpretação de Padé (10,2 ms).\n   • Item 6: Artigo acadêmico completo em formato IEEE de duas colunas compilado em PDF.\n   • Item 7: Apresentação em PowerPoint (14 slides) com notas de orador completas.\n   • Item 8: Prontidão técnica para defesa oral perante a banca examinadora.",
    "3. Reprodutibilidade e Rigor: Todos os scripts MATLAB, modelos Simulink e artigo LaTeX encontram-se versionados e organizados para entrega no Google Classroom."
]
for c in conclusoes:
    p = tf.add_paragraph(); p.text = "• " + c
    p.font.size = Pt(12); p.font.color.rgb = COR_TEXTO_ESCURO; p.space_before = Pt(8)

p_fim = tf.add_paragraph()
p_fim.text = "\nMuito obrigado pela atenção de todos! Estamos abertos às perguntas do Professor e da banca."
p_fim.font.size = Pt(14); p_fim.font.bold = True; p_fim.font.color.rgb = COR_AZUL_MEDIO; p_fim.alignment = PP_ALIGN.CENTER

set_speaker_notes(slide14,
"""[ORADOR: Scarpini | ~1:00 min]
- Finalize a apresentação com segurança e autoridade técnica:
  * Resuma que o método N2CACGO cumpriu com louvor todos os objetivos propostos;
  * Destaque o cumprimento de 100% dos 8 itens solicitados pelo professor na disciplina de MASD;
  * Enfatize a reprodutibilidade do projeto: códigos limpos, modelo Simulink funcional, artigo IEEE compilado e slides prontos;
  * Agradeça ao Prof. Dr. Marcelo de Araújo Oliveira pela orientação e finalize convidando a banca para a sessão de perguntas e respostas.""")

prs.save(PPTX_PATH)
print(f"Presentation saved successfully at: {PPTX_PATH}")
