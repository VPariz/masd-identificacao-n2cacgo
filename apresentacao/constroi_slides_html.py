import os
import base64

BASE_DIR = r"c:\Users\jvpar\estudo\3.2\MASD\trabalho_identificacao"
FIG_DIR = os.path.join(BASE_DIR, "artigo", "figuras")
OUT_HTML = os.path.join(BASE_DIR, "apresentacao", "slides.html")
OUT_INDEX = os.path.join(BASE_DIR, "apresentacao", "index.html")

def get_b64(fname):
    p = os.path.join(FIG_DIR, fname)
    if os.path.exists(p):
        with open(p, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    print(f"AVISO: {fname} nao encontrada em {FIG_DIR}")
    return ""

img_silv = get_b64("item3_exemplo_silveira_bode.png")
img_chirp = get_b64("item4_simulink_sinais_temporais.png")
img_fft = get_b64("item4_simulink_bode_validacao.png")
img_motor_todas = get_b64("item5_motor_bode_todas_ordens.png")
img_motor_melhor = get_b64("item5_motor_melhor_modelo_bode.png")
img_sqr = get_b64("item5_motor_validacao_onda_quadrada.png")
img_tri = get_b64("item5_motor_validacao_onda_triangular.png")

# Template HTML completo com KaTeX e navegacao
html = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MASD (IME) - Identificação de Sistemas N2CACGO</title>
  
  <!-- KaTeX para renderizacao de formulas matematicas elegantes -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\\\(', right: '\\\\)', display: false}]});"></script>
          
  <!-- Fonte Inter e JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-dark: #0B1120;
      --bg-card: rgba(17, 24, 39, 0.88);
      --border-card: rgba(56, 189, 248, 0.22);
      --accent-cyan: #38BDF8;
      --accent-gold: #F59E0B;
      --accent-emerald: #10B981;
      --accent-rose: #F43F5E;
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.08) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(16, 185, 129, 0.06) 0px, transparent 60%);
      color: var(--text-main);
      font-family: var(--font-sans);
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      user-select: none;
    }

    /* Container do slide 16:9 centralizado */
    #deck-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 100vw;
      height: calc(100vh - 64px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px 36px;
    }

    .slide {
      display: none;
      width: 100%;
      max-width: 1560px;
      height: 100%;
      max-height: 860px;
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-card);
      border-radius: 20px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6), 0 0 40px rgba(56, 189, 248, 0.1);
      padding: 36px 44px;
      flex-direction: column;
      animation: fadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .slide.active {
      display: flex;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.985) translateY(8px); }
      to { opacity: 1; transform: scale(1) translateY(0); }
    }

    /* Cabecalho de cada slide */
    .slide-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 16px;
      margin-bottom: 22px;
    }

    .slide-title-group h2 {
      font-size: 26px;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(135deg, #FFFFFF 30%, var(--accent-cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .slide-title-group p {
      font-size: 14px;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .slide-tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent-cyan);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    /* Conteudo do Slide */
    .slide-content {
      display: flex;
      flex: 1;
      gap: 24px;
      min-height: 0;
    }

    .col {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 16px;
      min-height: 0;
    }

    .card {
      background: rgba(15, 23, 42, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 14px;
      padding: 18px 22px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }

    .card-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--accent-gold);
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }

    .card-body {
      font-size: 13.5px;
      color: #E2E8F0;
      line-height: 1.55;
      overflow-y: auto;
    }

    .card-body ul {
      margin-left: 20px;
      margin-top: 6px;
    }

    .card-body li {
      margin-bottom: 8px;
    }

    .math-block {
      background: rgba(0, 0, 0, 0.35);
      border-left: 3px solid var(--accent-cyan);
      border-radius: 8px;
      padding: 10px 14px;
      margin: 10px 0;
      font-size: 13.5px;
    }

    .img-box {
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 8px;
    }

    .img-box img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      border-radius: 8px;
    }

    /* Tabelas */
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
      text-align: left;
    }

    th {
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent-cyan);
      font-weight: 600;
      padding: 8px 10px;
      border-bottom: 1px solid rgba(56, 189, 248, 0.25);
    }

    td {
      padding: 7px 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      color: #E2E8F0;
    }

    tr:nth-child(even) td {
      background: rgba(255, 255, 255, 0.02);
    }

    .badge-ok {
      background: rgba(16, 185, 129, 0.18);
      color: #34D399;
      border: 1px solid rgba(16, 185, 129, 0.35);
      padding: 2px 8px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 600;
    }

    /* Slide 1 - Capa Estilizada */
    .cover-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100%;
      text-align: center;
      padding: 20px 40px;
    }

    .cover-institution {
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--accent-cyan);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .cover-institution::before,
    .cover-institution::after {
      content: "";
      width: 40px;
      height: 1px;
      background: var(--accent-cyan);
      opacity: 0.5;
    }

    .cover-title {
      font-size: 40px;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.18;
      max-width: 1080px;
      margin-bottom: 16px;
      background: linear-gradient(135deg, #FFFFFF 20%, #93C5FD 70%, var(--accent-cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .cover-subtitle {
      font-size: 17px;
      color: var(--text-muted);
      max-width: 860px;
      line-height: 1.5;
      margin-bottom: 36px;
    }

    .cover-authors-card {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 16px;
      padding: 18px 36px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .cover-authors-names {
      font-size: 16px;
      font-weight: 700;
      color: #FFFFFF;
      letter-spacing: 0.02em;
    }

    .cover-advisor {
      font-size: 13.5px;
      color: var(--accent-gold);
    }

    /* Barra de Navegacao Inferior */
    #nav-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100vw;
      height: 64px;
      background: rgba(11, 17, 32, 0.95);
      backdrop-filter: blur(12px);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 40px;
      z-index: 100;
    }

    .nav-btn {
      background: rgba(30, 41, 59, 0.85);
      color: #E2E8F0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 10px;
      padding: 9px 18px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .nav-btn:hover {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-cyan);
      color: #FFFFFF;
      transform: translateY(-1px);
    }

    .nav-center {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }

    #slide-indicator {
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      letter-spacing: 0.05em;
    }

    #slide-indicator span {
      color: var(--accent-cyan);
      font-weight: 700;
    }

    #progress-container {
      width: 240px;
      height: 4px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 9999px;
      overflow: hidden;
    }

    #progress-bar {
      width: 10%;
      height: 100%;
      background: linear-gradient(90deg, var(--accent-cyan), var(--accent-emerald));
      border-radius: 9999px;
      transition: width 0.3s ease;
    }

    /* Print / PDF view */
    @media print {
      body {
        overflow: visible;
        height: auto;
        background: #0B1120 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }
      #nav-bar { display: none !important; }
      #deck-container {
        position: static;
        height: auto;
        padding: 0;
        display: block;
      }
      .slide {
        display: flex !important;
        page-break-after: always;
        height: 100vh;
        max-height: 100vh;
        border-radius: 0;
        border: none;
        box-shadow: none;
        margin-bottom: 20px;
      }
    }
  </style>
</head>
<body>

  <!-- BARRA DE PROGRESSO E CONTAINER DO DECK -->
  <div id="deck-container">

    <!-- SLIDE 1: CAPA -->
    <div class="slide active" data-index="1">
      <div class="cover-content">
        <div class="cover-institution">Instituto Militar de Engenharia • IME</div>
        <h1 class="cover-title">Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO</h1>
        <p class="cover-subtitle">Fundamentação Matemática Convexa, Validação Teórica (Silveira, 2006), Simulação Simulink com Análise FFT e Aplicação Experimental em Motor Elétrico CC</p>
        
        <div class="cover-authors-card">
          <div class="cover-authors-names">João Victor Tavares Pariz • Pedro Augusto • Renato Felix • Arthur Scarpini</div>
          <div class="cover-advisor">Disciplina: Modelagem e Análise de Sistemas Dinâmicos (MASD) | Docente: Prof. Dr. Marcelo de Araújo Oliveira</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 2: MOTIVAÇÃO & CONTEXTO -->
    <div class="slide" data-index="2">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>1. Contextualização: Domínio da Frequência vs. Tempo</h2>
          <p>Superação de não-linearidades locais, ruído estocástico e garantia de convergência analítica</p>
        </div>
        <div class="slide-tag">Fundamentação</div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">⚠️ Limitações do Domínio do Tempo (ARX, ARMAX, PEM)</div>
            <div class="card-body">
              <ul>
                <li><strong>Sensibilidade ao Ruído:</strong> Ruídos estocásticos de alta frequência e perturbações não-gaussianas degradam a matriz de covariância.</li>
                <li><strong>Condições Iniciais:</strong> Dependência extrema do estado inicial nulo ou da sua estimação simultânea.</li>
                <li><strong>Atrasos de Transporte:</strong> Dificuldade severa para identificar atrasos puros sem sobreparametrizar a ordem discreta.</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <div class="card-title">⚡ Benefícios do Domínio da Frequência</div>
            <div class="card-body">
              <ul>
                <li><strong>Concentração de Energia Espectral:</strong> A análise concentra-se rigorosamente nas frequências úteis ensaiadas na planta.</li>
                <li><strong>Filtragem Natural:</strong> Ruídos fora da banda de teste são descartados antes do ajuste de curvas.</li>
                <li><strong>Fasores Puros:</strong> Permite estimar atrasos de amostragem diretamente pela defasagem angular linear.</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card">
            <div class="card-title">💡 A Inovação do Método N2CACGO (Silveira, 2006)</div>
            <div class="card-body">
              <p>Métodos clássicos baseados em otimização do erro de saída (ex.: Simplex de Nelder-Mead via <code>fminsearch</code> ou Levenberg-Marquardt) sofrem frequentemente com <strong>estagnação em mínimos locais</strong> e <strong>instabilidade numérica</strong>.</p>
              <div class="math-block">
                O <strong>N2CACGO</strong> transforma a identificação em um problema estritamente quadrático ao minimizar a <em>Norma 2 do Resíduo de Equação</em>, garantindo uma superfície de erro <strong>estritamente convexa</strong>.
              </div>
              <p style="margin-top: 10px;">Com isso, a solução ótima é calculada de forma <strong>fechada e puramente analítica</strong> por meio da inversão de um Sistema de Equações Lineares (SEL), eliminando iterações e garantindo o mínimo global!</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 3: FORMULAÇÃO MATEMÁTICA -->
    <div class="slide" data-index="3">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>2. Formulação Matemática do N2CACGO</h2>
          <p>Estrutura convexa, matrizes de base polinomial e resolução analítica direta</p>
        </div>
        <div class="slide-tag">Matemática</div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">📐 Função de Transferência Arbitrária de Ordem n</div>
            <div class="card-body">
              <p>Considera-se o modelo linear invariante no tempo (SISO):</p>
              <div class="math-block">
                $$G_e(s) = \\frac{\\sum_{k=0}^n \\alpha_k s^{n-k}}{s^n + \\sum_{k=1}^n \\beta_k s^{n-k}} = \\frac{B(s)}{A(s)}$$
              </div>
              <p>Definição do resíduo de equação ponderado por fasor experimental \(G(j\\omega_i)\):</p>
              <div class="math-block">
                $$e(j\\omega_i) = A(j\\omega_i) G(j\\omega_i) - B(j\\omega_i)$$
              </div>
              <p>Vetor de coeficientes reais a determinar: \(\\theta = [\\alpha_0, \\dots, \\alpha_n, \\beta_1, \\dots, \\beta_n]^T \\in \\mathbb{R}^{2n+1}\).</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card">
            <div class="card-title">⚙️ Sistema Particionado e Solução Analítica Global</div>
            <div class="card-body">
              <p>A condição necessária e suficiente de mínimo \(\\nabla_\\theta J = 0\) desacopla no sistema matricial:</p>
              <div class="math-block">
                $$\\begin{bmatrix} Q_1 & -Q_2 \\\\ Q_3 & -Q_4 \\end{bmatrix} \\begin{bmatrix} \\alpha \\\\ \\beta \\end{bmatrix} = \\begin{bmatrix} Y_1 \\\\ Y_2 \\end{bmatrix} \\implies Q\\theta = Y$$
              </div>
              <p>Com a matriz de bases polinomiais \(R_{k,i} = (j\\omega_i)^{n-k}\) e fasores medidos \(S_i = G(j\\omega_i)\):</p>
              <ul>
                <li>\(Q_1 = \\text{Re}\\{R R^H\\}, \\quad Q_2 = \\text{Re}\\{R S^* R_{2:n+1}^H\\}\)</li>
                <li>\(Q_3 = \\text{Re}\\{R_{2:n+1} S R^H\\}, \\quad Q_4 = \\text{Re}\\{R_{2:n+1} (S S^*) R_{2:n+1}^H\\}\)</li>
              </ul>
              <div class="math-block" style="border-left-color: var(--accent-gold); margin-top: 10px;">
                <strong>Solução Única:</strong> \(\\theta^* = Q^{-1} Y\) (resolvido por eliminação Gaussiana com pivoteamento parcial).
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 4: ITEM 3 - VALIDAÇÃO ACADÊMICA -->
    <div class="slide" data-index="4">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>3. [Item 3] Validação Teórica: Benchmark de Silveira (2006)</h2>
          <p>Reprodução exata dos resultados tabelados na dissertação de mestrado de referência</p>
        </div>
        <div class="slide-tag">Item 3</div>
      </div>
      <div class="slide-content">
        <div class="col" style="flex: 1.1;">
          <div class="card">
            <div class="card-title">📊 Tabela Comparativa: Implementação vs. Tabela 3.2 de Silveira</div>
            <div class="card-body" style="padding: 4px 0;">
              <table>
                <thead>
                  <tr>
                    <th>Ordem (\(n\))</th>
                    <th>Custo \(J\) (Implementação)</th>
                    <th>\(J_1\) (Silveira, 2006)</th>
                    <th>FIT (%)</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>1ª Ordem</td><td>\(1,3329 \\times 10^{0}\)</td><td>\(1,3329 \\times 10^{0}\)</td><td>89,95%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>2ª Ordem</td><td>\(1,4242 \\times 10^{-1}\)</td><td>\(1,4242 \\times 10^{-1}\)</td><td>95,43%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>3ª Ordem</td><td>\(1,6078 \\times 10^{-2}\)</td><td>\(1,6078 \\times 10^{-2}\)</td><td>99,03%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>4ª Ordem</td><td>\(6,2903 \\times 10^{-4}\)</td><td>\(6,2903 \\times 10^{-4}\)</td><td>99,98%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>5ª Ordem</td><td>\(6,2903 \\times 10^{-4}\)</td><td>\(6,2903 \\times 10^{-4}\)</td><td>99,99%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>6ª Ordem</td><td>\(6,2903 \\times 10^{-4}\)</td><td>\(6,2903 \\times 10^{-4}\)</td><td>99,99%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>7ª Ordem</td><td>\(6,2903 \\times 10^{-4}\)</td><td>\(6,2903 \\times 10^{-4}\)</td><td>99,99%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="card">
            <div class="card-title">🔍 Sistemas Didáticos Exatos (1ª, 2ª e 3ª Ordens)</div>
            <div class="card-body">
              <p>Nos sistemas acadêmicos sintéticos com ordem compatível, o método alcançou <strong>FIT = 100,00%</strong> e resíduo analítico da ordem de \(J \\sim 10^{-14}\), comprovando a exatidão algébrica da rotina <code>identifica_N2CACGO.m</code>.</p>
            </div>
          </div>
        </div>
        <div class="col" style="flex: 0.9;">
          <div class="img-box" style="height: 100%;">
            <img src="{IMG_SILV}" alt="Bode Silveira 2006">
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 5: ITEM 4 - SIMULINK & FFT -->
    <div class="slide" data-index="5">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>4. [Item 4] Simulação Dinâmica Simulink com Chirp e FFT</h2>
          <p>Identificação de planta LTI a partir de séries temporais via análise espectral discreta</p>
        </div>
        <div class="slide-tag">Item 4</div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">⚙️ Planta Alvo e Parâmetros de Simulação</div>
            <div class="card-body">
              <p>Planta subamortecida de 2ª ordem implementada no Simulink (<code>modelo_item4.slx</code>):</p>
              <div class="math-block">
                $$G_{\\text{nom}}(s) = \\frac{100}{s^2 + 4s + 100} \\quad (\\omega_n = 10\\text{ rad/s}, \\; \\zeta = 0,20)$$
              </div>
              <ul>
                <li><strong>Sinal de Excitação:</strong> Chirp senoidal linear de \(0,1\\text{ Hz}\) a \(15,0\\text{ Hz}\) (\(\\omega \\in [0,63; 94,25]\\text{ rad/s}\)).</li>
                <li><strong>Duração e Amostragem:</strong> \(T_{\\text{sim}} = 20\\text{ s}\), \(T_s = 1\\text{ ms}\) (\(f_s = 1000\\text{ Hz}\), \(N = 20.001\) amostras).</li>
                <li><strong>Solver:</strong> Solver contínuo <code>ode4</code> (Runge-Kutta 4ª ordem de passo fixo).</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <div class="card-title">🧮 Extração Espectral via Transformada Rápida de Fourier (FFT)</div>
            <div class="card-body">
              <p>A resposta em frequência é extraída ponto a ponto na faixa útil de coerência SNR:</p>
              <div class="math-block">
                $$G(j\\omega_k) = \\frac{\\mathcal{F}\\{y(t)\\}(j\\omega_k)}{\\mathcal{F}\\{u(t)\\}(j\\omega_k)} = \\frac{Y(k)}{U(k)}, \\quad \\omega_k \\in [1,0; 80,0]\\text{ rad/s}$$
              </div>
              <p>Total de 126 frequências extraídas com rejeição natural de ruídos e efeitos de borda.</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="img-box" style="height: 100%;">
            <img src="{IMG_CHIRP}" alt="Sinais Temporais Chirp Simulink">
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: ITEM 4 - RESULTADOS ESPECTRAIS -->
    <div class="slide" data-index="6">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>5. [Item 4] Validação do Modelo Identificado via FFT</h2>
          <p>Reconstrução precisa da amplitude de pico e dinâmica de fase da planta simulada</p>
        </div>
        <div class="slide-tag">Item 4</div>
      </div>
      <div class="slide-content">
        <div class="col" style="flex: 0.95;">
          <div class="card">
            <div class="card-title">🎯 Modelo Identificado vs. Nominal</div>
            <div class="card-body">
              <p>Função de transferência recuperada analiticamente pelo N2CACGO (\(n=2\)):</p>
              <div class="math-block">
                $$G_{\\text{id}}(s) = \\frac{100,5}{s^2 + 4,249s + 100,5}$$
              </div>
              <ul>
                <li><strong>Ganho DC:</strong> \(K_{\\text{id}} = 1,0003\) (Nominal: \(1,0000\)).</li>
                <li><strong>Frequência Natural:</strong> \(\\omega_n = 10,02\\text{ rad/s}\) (Erro de apenas \(0,2\\%\)).</li>
                <li><strong>Fator de Amortecimento:</strong> \(\\zeta = 0,212\) (Nominal: \(0,200\)).</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <div class="card-title">📈 Índices de Desempenho Espectral</div>
            <div class="card-body">
              <ul>
                <li><strong>FIT Espectral Global:</strong> <span class="badge-ok">96,47%</span></li>
                <li><strong>RMSE de Módulo:</strong> \(0,77\\text{ dB}\)</li>
                <li><strong>RMSE de Fase:</strong> \(8,69^{\\circ}\)</li>
              </ul>
              <p style="margin-top: 8px; font-size: 12.5px; color: var(--text-muted);">
                A discretização no tempo e janelamento espectral causaram leve dispersão (leakage), plenamente absorvida pela robustez do estimador N2CACGO.
              </p>
            </div>
          </div>
        </div>
        <div class="col" style="flex: 1.05;">
          <div class="img-box" style="height: 100%;">
            <img src="{IMG_FFT}" alt="Bode Validacao Simulink">
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 7: ITEM 5 - IDENTIFICAÇÃO MOTOR CC -->
    <div class="slide" data-index="7">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>6. [Item 5] Aplicação Experimental: Bancada de Motor Elétrico CC</h2>
          <p>Identificação física baseada em ensaios reais com sinal senoidal puro (Grupo 3)</p>
        </div>
        <div class="slide-tag">Item 5</div>
      </div>
      <div class="slide-content">
        <div class="col" style="flex: 0.95;">
          <div class="card">
            <div class="card-title">🔬 Protocolo Experimental e Tratamento dos Dados</div>
            <div class="card-body">
              <ul>
                <li><strong>Base Única e Confiável:</strong> 26 ensaios senoidais da bancada do Grupo 3 (\(0,20\\text{ Hz}\) a \(10,0\\text{ Hz}\)), expurgando os transitórios de partida (análise restrita aos últimos 60% das amostras).</li>
                <li><strong>Fasores por DFT:</strong> Amplitude e fase extraídas no pico espectral fundamental do sinal forçado.</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <div class="card-title">🏆 Modelo Físico Selecionado (1ª Ordem com Zero Padé)</div>
            <div class="card-body">
              <div class="math-block">
                $$G_{\\text{motor}}(s) = \\frac{-0,2468 s + 48,33}{s + 4,794}$$
              </div>
              <ul>
                <li><strong>Ganho Estático:</strong> \(K_m = 48,33 / 4,794 = 10,08\\text{ (rad/s)/V}\) (\(20,07\\text{ dB}\)).</li>
                <li><strong>Constante de Tempo Eletromecânica:</strong> \(\\tau_m = 1 / 4,794 = 0,209\\text{ s}\).</li>
                <li><strong>Zero em Semi-Plano Direito:</strong> \(z = +195,8\\text{ rad/s}\). Traduz a aproximação de Padé de 1ª ordem do <em>atraso de transporte de amostragem</em> (\(\\tau_d = 2 / 195,8 \\approx 10,2\\text{ ms}\)), explicando a queda de fase além de \(-90^{\\circ}\)!</li>
                <li><strong>FIT Global:</strong> <span class="badge-ok">88,36%</span>.</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col" style="flex: 1.05;">
          <div class="img-box" style="height: 100%;">
            <img src="{IMG_MOTOR_MELHOR}" alt="Bode Motor Melhor Modelo">
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 8: ITEM 5 - VALIDAÇÃO DINÂMICA TEMPORAL -->
    <div class="slide" data-index="8">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>7. [Item 5] Validação Dinâmica Temporal em Bancada Real</h2>
          <p>Confronto cego do modelo linear identificado contra ondas quadrada e triangular (10 Hz)</p>
        </div>
        <div class="slide-tag">Item 5</div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="img-box" style="flex: 1.25;">
            <img src="{IMG_SQR}" alt="Validacao Onda Quadrada 10 Hz">
          </div>
          <div class="card" style="flex: 0.75;">
            <div class="card-title">🟦 Resposta a Onda Quadrada (10 Hz)</div>
            <div class="card-body">
              <p>O modelo identificado reproduz com exatidão as transições abruptas de subida e descida, com taxa exponencial compatível com \(\\tau_m = 0,209\\text{ s}\) e ganho estático consistente.</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="img-box" style="flex: 1.25;">
            <img src="{IMG_TRI}" alt="Validacao Onda Triangular 10 Hz">
          </div>
          <div class="card" style="flex: 0.75;">
            <div class="card-title">🔺 Resposta a Onda Triangular (10 Hz)</div>
            <div class="card-body">
              <p>A ação passa-baixas natural do polo mecânico arredonda suavemente as cúspides triangulares com atraso de fase idêntico ao medido pelo tacômetro.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 9: DIFICULDADES E SOLUÇÕES -->
    <div class="slide" data-index="9">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>8. Dificuldades Encontradas e Soluções Adotadas</h2>
          <p>Superação de desafios numéricos, condicionamento matricial e integridade de dados</p>
        </div>
        <div class="slide-tag">Engenharia</div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">⚠️ 1. Condicionamento Numérico de Q em Ordens Altas</div>
            <div class="card-body">
              <p><strong>Problema:</strong> Para ordens \(n \\ge 4\), monômios \((j\\omega)^n\) atingem amplitudes de \(10^{14}\), fazendo com que \(\\text{rcond}(Q) < 10^{-16}\). O comando <code>pinv</code> truncava direções de autovalores cruciais.</p>
              <p style="color: #34D399; margin-top: 6px;"><strong>Solução:</strong> Adoção de divisão matricial direta (<code>Q \\ Y</code>) por eliminação Gaussiana com pivoteamento, preservando a base monômica e garantindo reprodução exata de Silveira (2006).</p>
            </div>
          </div>
          <div class="card">
            <div class="card-title">⚠️ 2. Vazamento Espectral (Spectral Leakage) na FFT</div>
            <div class="card-body">
              <p><strong>Problema:</strong> O janelamento abrupto em sinais aperiódicos no tempo gera dispersão de energia nas frequências vizinhas.</p>
              <p style="color: #34D399; margin-top: 6px;"><strong>Solução:</strong> Seleção restrita da faixa de excitação persistente do Chirp (\(1,0\) a \(80,0\\text{ rad/s}\)), expurgando bordas com baixa coerência SNR.</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card">
            <div class="card-title">⚠️ 3. Transitórios e Ruídos na Bancada do Motor</div>
            <div class="card-body">
              <p><strong>Problema:</strong> Ciclos iniciais com dinâmica transitória de partida e ruído de comutação do tacômetro.</p>
              <p style="color: #34D399; margin-top: 6px;"><strong>Solução:</strong> Processamento espectral restrito aos últimos 60% das amostras temporais (regime permanente forçado estrito) para cálculo dos fasores.</p>
            </div>
          </div>
          <div class="card">
            <div class="card-title">⚠️ 4. Conflito de Solvers no Simulink CLI</div>
            <div class="card-body">
              <p><strong>Problema:</strong> Bloqueio da simulação via linha de comando ao configurar solvers discretos em diagramas contínuos de função de transferência.</p>
              <p style="color: #34D399; margin-top: 6px;"><strong>Solução:</strong> Parametrização programática com solver contínuo <code>ode4</code> de passo fixo.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 10: CONCLUSÕES -->
    <div class="slide" data-index="10">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>9. Conclusões e Considerações Finais</h2>
          <p>Síntese das realizações, validação experimental e disponibilização pública</p>
        </div>
        <div class="slide-tag">Conclusão</div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">🏆 Principais Conquistas do Trabalho</div>
            <div class="card-body">
              <ul>
                <li><strong>Validação Acadêmica Rigorosa:</strong> Concordância exata (99,99%) com a Tabela 3.2 de Silveira (2006) e FIT = 100,00% em sistemas didáticos.</li>
                <li><strong>Integração Simulink + FFT:</strong> Recuperação precisa da planta LTI de 2ª ordem a partir de sinais temporais (\(\\text{FIT} = 96,47\\%\)).</li>
                <li><strong>Identificação Física de Bancada:</strong> O modelo de 1ª ordem com atraso de Padé de \(\\approx 10,2\\text{ ms}\) traduz com extrema fidelidade a dinâmica eletromecânica do motor CC.</li>
                <li><strong>Automação Total:</strong> Todos os 5 itens programados em código nativo MATLAB (<code>executa_todos_itens.m</code>).</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card" style="border-color: rgba(56, 189, 248, 0.4);">
            <div class="card-title" style="color: var(--accent-cyan);">🌐 Repositório Aberto no GitHub</div>
            <div class="card-body">
              <p>Todo o código-fonte, modelo Simulink, dados experimentais, artigo IEEE em PDF e apresentação estão disponíveis publicamente em:</p>
              <div class="math-block" style="border-left-color: var(--accent-gold); font-size: 13.5px; word-break: break-all;">
                <strong>URL:</strong> <a href="https://github.com/VPariz/masd-identificacao-n2cacgo" target="_blank" style="color: #38BDF8; text-decoration: none;">https://github.com/VPariz/masd-identificacao-n2cacgo</a>
              </div>
              <p style="margin-top: 14px; font-weight: 700; text-align: center; color: var(--accent-gold); font-size: 15px;">
                Obrigado pela atenção! Perguntas e discussões.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>

  <!-- BARRA INFERIOR DE CONTROLES -->
  <div id="nav-bar">
    <div style="display: flex; gap: 10px;">
      <button class="nav-btn" onclick="prevSlide()">◀ Anterior</button>
      <button class="nav-btn" onclick="nextSlide()">Próximo ▶</button>
    </div>

    <div class="nav-center">
      <div id="slide-indicator">SLIDE <span id="current-slide">01</span> / <span id="total-slides">10</span></div>
      <div id="progress-container">
        <div id="progress-bar"></div>
      </div>
    </div>

    <div style="display: flex; gap: 10px;">
      <button class="nav-btn" onclick="toggleFullscreen()">⛶ Tela Cheia (F)</button>
      <button class="nav-btn" onclick="window.print()">🖨️ Salvar PDF</button>
    </div>
  </div>

  <script>
    let currentSlideIndex = 1;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    const progressBar = document.getElementById('progress-bar');
    const currentIndicator = document.getElementById('current-slide');
    const totalIndicator = document.getElementById('total-slides');

    totalIndicator.textContent = String(totalSlides).padStart(2, '0');

    function showSlide(index) {
      if (index < 1) index = 1;
      if (index > totalSlides) index = totalSlides;
      currentSlideIndex = index;

      slides.forEach((slide) => {
        slide.classList.remove('active');
        if (parseInt(slide.getAttribute('data-index')) === currentSlideIndex) {
          slide.classList.add('active');
        }
      });

      progressBar.style.width = ((currentSlideIndex / totalSlides) * 100) + '%';
      currentIndicator.textContent = String(currentSlideIndex).padStart(2, '0');
    }

    function nextSlide() {
      if (currentSlideIndex < totalSlides) showSlide(currentSlideIndex + 1);
    }

    function prevSlide() {
      if (currentSlideIndex > 1) showSlide(currentSlideIndex - 1);
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
      }
    }

    // Atalhos de teclado para apresentacao executiva
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ' || e.key === 'PageDown') {
        e.preventDefault();
        nextSlide();
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp' || e.key === 'Backspace' || e.key === 'PageUp') {
        e.preventDefault();
        prevSlide();
      } else if (e.key === 'Home') {
        e.preventDefault();
        showSlide(1);
      } else if (e.key === 'End') {
        e.preventDefault();
        showSlide(totalSlides);
      } else if (e.key.toLowerCase() === 'f') {
        e.preventDefault();
        toggleFullscreen();
      }
    });
  </script>
</body>
</html>
"""

# Substitui as imagens base64 nos placeholders
html = html.replace("{IMG_SILV}", img_silv)
html = html.replace("{IMG_CHIRP}", img_chirp)
html = html.replace("{IMG_FFT}", img_fft)
html = html.replace("{IMG_MOTOR_TODAS}", img_motor_todas)
html = html.replace("{IMG_MOTOR_MELHOR}", img_motor_melhor)
html = html.replace("{IMG_SQR}", img_sqr)
html = html.replace("{IMG_TRI}", img_tri)

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Salvo: {OUT_HTML} ({len(html)} bytes)")

with open(OUT_INDEX, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Salvo: {OUT_INDEX} ({len(html)} bytes)")

# Salva tambem no diretorio de artifacts para visualizacao imediata no painel do Antigravity
art_dir = r"C:\Users\jvpar\.gemini\antigravity\brain\26191f8b-46c8-4fde-a1c8-21ed5e191c6f"
art_file = os.path.join(art_dir, "apresentacao_slides.html")
with open(art_file, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Artifact salvo: {art_file}")
