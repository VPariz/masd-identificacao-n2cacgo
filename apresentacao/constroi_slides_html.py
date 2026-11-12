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
          onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
          
  <!-- Fontes do Google -->
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
      padding: 34px 44px;
      flex-direction: column;
      animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .slide.active {
      display: flex;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.985) translateY(6px); }
      to { opacity: 1; transform: scale(1) translateY(0); }
    }

    /* Cabecalho de cada slide */
    .slide-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 14px;
      margin-bottom: 20px;
    }

    .slide-title-group h2 {
      font-size: 25px;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(135deg, #FFFFFF 30%, var(--accent-cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .slide-title-group p {
      font-size: 13.5px;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .slide-header-tags {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .slide-tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 5px 13px;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent-cyan);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .speaker-badge {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.04em;
      padding: 5px 13px;
      border-radius: 9999px;
      background: rgba(245, 158, 11, 0.14);
      color: var(--accent-gold);
      border: 1px solid rgba(245, 158, 11, 0.35);
      display: flex;
      align-items: center;
      gap: 5px;
    }

    /* Conteudo do Slide */
    .slide-content {
      display: flex;
      flex: 1;
      gap: 22px;
      min-height: 0;
    }

    .col {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 15px;
      min-height: 0;
    }

    .card {
      background: rgba(15, 23, 42, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 14px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }

    .card-title {
      font-size: 14.5px;
      font-weight: 700;
      color: var(--accent-gold);
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 9px;
    }

    .card-body {
      font-size: 13px;
      color: #E2E8F0;
      line-height: 1.55;
      overflow-y: auto;
    }

    .card-body ul {
      margin-left: 20px;
      margin-top: 5px;
    }

    .card-body li {
      margin-bottom: 7px;
    }

    .math-block {
      background: rgba(0, 0, 0, 0.38);
      border-left: 3px solid var(--accent-cyan);
      border-radius: 8px;
      padding: 9px 13px;
      margin: 9px 0;
      font-size: 13px;
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
      cursor: zoom-in;
      transition: border-color 0.2s ease, transform 0.2s ease;
      position: relative;
    }

    .img-box:hover {
      border-color: var(--accent-cyan);
      transform: scale(1.008);
    }

    .img-box::after {
      content: "🔍 Clique para ampliar";
      position: absolute;
      bottom: 8px;
      right: 12px;
      background: rgba(0, 0, 0, 0.7);
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 11px;
      color: var(--accent-cyan);
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.2s;
    }

    .img-box:hover::after {
      opacity: 1;
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
      font-size: 12px;
      text-align: left;
    }

    th {
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent-cyan);
      font-weight: 600;
      padding: 7px 9px;
      border-bottom: 1px solid rgba(56, 189, 248, 0.25);
    }

    td {
      padding: 6px 9px;
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
      padding: 2px 7px;
      border-radius: 9999px;
      font-size: 10.5px;
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
      margin-bottom: 14px;
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
      font-size: 38px;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.18;
      max-width: 1100px;
      margin-bottom: 14px;
      background: linear-gradient(135deg, #FFFFFF 20%, #93C5FD 70%, var(--accent-cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .cover-subtitle {
      font-size: 16px;
      color: var(--text-muted);
      max-width: 880px;
      line-height: 1.5;
      margin-bottom: 30px;
    }

    .cover-authors-card {
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 16px;
      padding: 18px 36px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .cover-authors-names {
      font-size: 16px;
      font-weight: 700;
      color: #FFFFFF;
      letter-spacing: 0.02em;
      display: flex;
      justify-content: center;
      gap: 18px;
      flex-wrap: wrap;
    }

    .cover-speaker-pill {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 13.5px;
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
      padding: 0 32px;
      z-index: 100;
    }

    .nav-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .nav-btn {
      background: rgba(30, 41, 59, 0.85);
      color: #E2E8F0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9px;
      padding: 8px 14px;
      font-size: 12.5px;
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

    .nav-btn.active-btn {
      background: rgba(56, 189, 248, 0.28);
      border-color: var(--accent-cyan);
      color: #FFFFFF;
    }

    .nav-center {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 5px;
    }

    #slide-indicator {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-muted);
      letter-spacing: 0.05em;
    }

    #slide-indicator span {
      color: var(--accent-cyan);
      font-weight: 700;
    }

    #progress-container {
      width: 220px;
      height: 4px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 9999px;
      overflow: hidden;
    }

    #progress-bar {
      width: 9%;
      height: 100%;
      background: linear-gradient(90deg, var(--accent-cyan), var(--accent-emerald));
      border-radius: 9999px;
      transition: width 0.25s ease;
    }

    /* Widget Cronometro */
    #timer-widget {
      font-family: var(--font-mono);
      font-size: 13px;
      color: var(--accent-gold);
      background: rgba(0, 0, 0, 0.4);
      padding: 5px 11px;
      border-radius: 8px;
      border: 1px solid rgba(245, 158, 11, 0.3);
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }

    /* Painel de Notas do Orador (Drawer) */
    #notes-drawer {
      position: fixed;
      bottom: 64px;
      right: 24px;
      width: 480px;
      max-height: 420px;
      background: rgba(15, 23, 42, 0.96);
      backdrop-filter: blur(18px);
      border: 1px solid var(--accent-cyan);
      border-radius: 14px 14px 0 0;
      box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.6);
      display: none;
      flex-direction: column;
      z-index: 150;
      animation: slideUp 0.25s ease forwards;
    }

    #notes-drawer.open {
      display: flex;
    }

    @keyframes slideUp {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    .notes-header {
      padding: 10px 16px;
      background: rgba(56, 189, 248, 0.15);
      border-bottom: 1px solid rgba(56, 189, 248, 0.25);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .notes-header h4 {
      font-size: 13px;
      color: var(--accent-cyan);
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .notes-close {
      background: none;
      border: none;
      color: #94A3B8;
      cursor: pointer;
      font-size: 16px;
    }

    .notes-close:hover {
      color: #FFF;
    }

    .notes-body {
      padding: 14px 18px;
      overflow-y: auto;
      font-size: 13px;
      color: #F1F5F9;
      line-height: 1.6;
    }

    .notes-speaker-tag {
      display: inline-block;
      background: rgba(245, 158, 11, 0.2);
      color: var(--accent-gold);
      border: 1px solid rgba(245, 158, 11, 0.4);
      padding: 2px 9px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 11.5px;
      margin-bottom: 8px;
    }

    .notes-body strong {
      color: var(--accent-gold);
    }

    .notes-body ul {
      margin-left: 18px;
      margin-top: 6px;
    }

    .notes-body li {
      margin-bottom: 6px;
    }

    /* Modal de Zoom Lightbox */
    #lightbox {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(3, 7, 18, 0.92);
      backdrop-filter: blur(10px);
      z-index: 300;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 40px;
      cursor: zoom-out;
    }

    #lightbox.open {
      display: flex;
    }

    #lightbox img {
      max-width: 95%;
      max-height: 95%;
      border-radius: 12px;
      box-shadow: 0 0 50px rgba(56, 189, 248, 0.3);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    /* Modal Mosaico / Slide Grid */
    #grid-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(11, 17, 32, 0.96);
      backdrop-filter: blur(16px);
      z-index: 250;
      display: none;
      flex-direction: column;
      padding: 30px 50px;
    }

    #grid-modal.open {
      display: flex;
    }

    .grid-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
    }

    .grid-header h3 {
      font-size: 22px;
      color: #FFF;
    }

    .grid-cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 18px;
      overflow-y: auto;
      padding-bottom: 20px;
    }

    .grid-card {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 16px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .grid-card:hover {
      border-color: var(--accent-cyan);
      transform: translateY(-3px);
      background: rgba(56, 189, 248, 0.12);
    }

    .grid-card.current {
      border-color: var(--accent-gold);
      box-shadow: 0 0 15px rgba(245, 158, 11, 0.3);
    }

    .grid-card-num {
      font-size: 11px;
      font-weight: 700;
      color: var(--accent-cyan);
      letter-spacing: 0.05em;
    }

    .grid-card-title {
      font-size: 13.5px;
      font-weight: 600;
      color: #FFF;
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
      #nav-bar, #notes-drawer, #lightbox, #grid-modal { display: none !important; }
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

  <!-- CONTAINER PRINCIPAL DO DECK -->
  <div id="deck-container">

    <!-- SLIDE 1: CAPA -->
    <div class="slide active" data-index="1">
      <div class="cover-content">
        <div class="cover-institution">Instituto Militar de Engenharia • IME</div>
        <h1 class="cover-title">Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO</h1>
        <p class="cover-subtitle">Fundamentação Matemática Convexa, Validação Teórica (Silveira, 2006), Simulação Simulink com Análise FFT e Aplicação Experimental em Motor Elétrico CC</p>
        
        <div class="cover-authors-card">
          <div class="cover-authors-names">
            <span class="cover-speaker-pill">👤 <strong>João Victor Pariz</strong> (Abertura & Teoria)</span>
            <span class="cover-speaker-pill">👤 <strong>Pedro Augusto</strong> (Benchmark & Simulink)</span>
            <span class="cover-speaker-pill">👤 <strong>Renato Felix</strong> (Bancada & Padé)</span>
            <span class="cover-speaker-pill">👤 <strong>Arthur Scarpini</strong> (Validação & Fechamento)</span>
          </div>
          <div class="cover-advisor">Disciplina: Modelagem e Análise de Sistemas Dinâmicos (MASD) | Docente: Prof. Dr. Marcelo de Araújo Oliveira</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 2: MOTIVAÇÃO & CONTEXTO -->
    <div class="slide" data-index="2">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>1. Contextualização: Domínio da Frequência vs. Tempo</h2>
          <p>Superação de ruídos de alta frequência, condições iniciais e garantia de convexidade analítica</p>
        </div>
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: João Victor Pariz</div>
          <div class="slide-tag">Fundamentação</div>
        </div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">⚠️ Limitações do Domínio do Tempo (ARX, ARMAX, PEM)</div>
            <div class="card-body">
              <ul>
                <li><strong>Sensibilidade ao Ruído:</strong> Ruídos estocásticos de alta frequência e perturbações não-gaussianas degradam diretamente a matriz de covariância.</li>
                <li><strong>Dependência de Condições Iniciais:</strong> Exige condições iniciais estritamente nulas ou a sua co-estimação, introduzindo viés.</li>
                <li><strong>Atrasos de Transporte:</strong> Dificuldade severa para identificar atrasos puros sem sobreparametrizar a ordem discreta.</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <div class="card-title">⚡ Benefícios do Domínio da Frequência</div>
            <div class="card-body">
              <ul>
                <li><strong>Concentração de Energia Espectral:</strong> A análise restringe-se às frequências forçadas com alta relação sinal-ruído (SNR).</li>
                <li><strong>Filtragem Natural:</strong> Ruídos fora da faixa ensaiada são automaticamente expurgados no cálculo dos fasores.</li>
                <li><strong>Tratamento de Fase e Atrasos:</strong> O atraso puro manifesta-se linearmente na fase espectral (\(-\omega \tau_d\)).</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card">
            <div class="card-title">💡 A Inovação do Método N2CACGO (Silveira, 2006)</div>
            <div class="card-body">
              <p>Métodos clássicos baseados em otimização do erro de saída (ex.: Simplex de Nelder-Mead via <code>fminsearch</code> ou Levenberg-Marquardt) sofrem frequentemente com <strong>mínimos locais e divergência numérica</strong>.</p>
              <div class="math-block">
                O <strong>N2CACGO</strong> formula a identificação minimizando a <em>Norma 2 do Resíduo de Equação</em>, gerando um funcional de custo <strong>estritamente convexo</strong>.
              </div>
              <p style="margin-top: 10px;">A condição de ótimo é obtida por solução direta de um Sistema de Equações Lineares (SEL), garantindo o <strong>mínimo global de forma analítica e sem iterações</strong>!</p>
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
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: João Victor Pariz</div>
          <div class="slide-tag">Matemática</div>
        </div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">📐 Função de Transferência Arbitrária de Ordem n</div>
            <div class="card-body">
              <p>Considera-se o modelo linear invariante no tempo (SISO) de ordem \(n\):</p>
              <div class="math-block">
                $$G_e(s) = \frac{\sum_{k=0}^n \alpha_k s^{n-k}}{s^n + \sum_{k=1}^n \beta_k s^{n-k}} = \frac{B(s)}{A(s)}$$
              </div>
              <p>Definição do resíduo de equação ponderado por fasor experimental \(G(j\omega_i)\):</p>
              <div class="math-block">
                $$e(j\omega_i) = A(j\omega_i) G(j\omega_i) - B(j\omega_i)$$
              </div>
              <p>Vetor de coeficientes reais a determinar: \(\theta = [\alpha_0, \dots, \alpha_n, \beta_1, \dots, \beta_n]^T \in \mathbb{R}^{2n+1}\).</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card">
            <div class="card-title">⚙️ Sistema Particionado e Solução Analítica Global</div>
            <div class="card-body">
              <p>A condição necessária e suficiente de mínimo \(\nabla_\theta J = 0\) desacopla no sistema matricial:</p>
              <div class="math-block">
                $$\begin{bmatrix} Q_1 & -Q_2 \\ Q_3 & -Q_4 \end{bmatrix} \begin{bmatrix} \alpha \\ \beta \end{bmatrix} = \begin{bmatrix} Y_1 \\ Y_2 \end{bmatrix} \implies Q\theta = Y$$
              </div>
              <p>Com a matriz de bases polinomiais \(R_{k,i} = (j\omega_i)^{n-k}\) e fasores medidos \(S_i = G(j\omega_i)\):</p>
              <ul>
                <li>\(Q_1 = \text{Re}\{R R^H\}, \quad Q_2 = \text{Re}\{R S^* R_{2:n+1}^H\}\)</li>
                <li>\(Q_3 = \text{Re}\{R_{2:n+1} S R^H\}, \quad Q_4 = \text{Re}\{R_{2:n+1} (S S^*) R_{2:n+1}^H\}\)</li>
              </ul>
              <div class="math-block" style="border-left-color: var(--accent-gold); margin-top: 8px;">
                <strong>Solução Única:</strong> \(\theta^* = Q^{-1} Y\) (resolvido por eliminação Gaussiana com pivoteamento parcial).
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
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: Pedro Augusto</div>
          <div class="slide-tag">Item 3</div>
        </div>
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
                  <tr><td>1ª Ordem</td><td>\(1,3329 \times 10^{0}\)</td><td>\(1,3329 \times 10^{0}\)</td><td>89,95%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>2ª Ordem</td><td>\(1,4242 \times 10^{-1}\)</td><td>\(1,4242 \times 10^{-1}\)</td><td>95,43%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>3ª Ordem</td><td>\(1,6078 \times 10^{-2}\)</td><td>\(1,6078 \times 10^{-2}\)</td><td>99,03%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>4ª Ordem</td><td>\(6,2903 \times 10^{-4}\)</td><td>\(6,2903 \times 10^{-4}\)</td><td>99,98%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>5ª Ordem</td><td>\(6,2903 \times 10^{-4}\)</td><td>\(6,2903 \times 10^{-4}\)</td><td>99,99%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>6ª Ordem</td><td>\(6,2903 \times 10^{-4}\)</td><td>\(6,2903 \times 10^{-4}\)</td><td>99,99%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                  <tr><td>7ª Ordem</td><td>\(6,2903 \times 10^{-4}\)</td><td>\(6,2903 \times 10^{-4}\)</td><td>99,99%</td><td><span class="badge-ok">Concordância 100%</span></td></tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="card">
            <div class="card-title">🔍 Sistemas Didáticos Exatos (1ª, 2ª e 3ª Ordens)</div>
            <div class="card-body">
              <p>Nos sistemas acadêmicos sintéticos com ordem compatível, o algoritmo alcançou <strong>FIT = 100,00%</strong> e resíduo analítico da ordem de \(J \sim 10^{-14}\), comprovando a exatidão algébrica da rotina <code>identifica_N2CACGO.m</code>.</p>
            </div>
          </div>
        </div>
        <div class="col" style="flex: 0.9;">
          <div class="img-box" style="height: 100%;" onclick="openLightbox('{IMG_SILV}')">
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
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: Pedro Augusto</div>
          <div class="slide-tag">Item 4</div>
        </div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">⚙️ Planta Alvo e Parâmetros de Simulação</div>
            <div class="card-body">
              <p>Planta subamortecida de 2ª ordem implementada no Simulink (<code>modelo_item4.slx</code>):</p>
              <div class="math-block">
                $$G_{\text{nom}}(s) = \frac{100}{s^2 + 4s + 100} \quad (\omega_n = 10\text{ rad/s}, \; \zeta = 0,20)$$
              </div>
              <ul>
                <li><strong>Sinal de Excitação:</strong> Chirp senoidal linear de \(0,1\text{ Hz}\) a \(15,0\text{ Hz}\) (\(\omega \in [0,63; 94,25]\text{ rad/s}\)).</li>
                <li><strong>Duração e Amostragem:</strong> \(T_{\text{sim}} = 20\text{ s}\), \(T_s = 1\text{ ms}\) (\(f_s = 1000\text{ Hz}\), \(N = 20.001\) amostras).</li>
                <li><strong>Solver:</strong> Solver contínuo <code>ode4</code> (Runge-Kutta 4ª ordem de passo fixo).</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <div class="card-title">🧮 Extração Espectral via Transformada Rápida de Fourier (FFT)</div>
            <div class="card-body">
              <p>A resposta em frequência é extraída ponto a ponto na faixa útil de coerência SNR:</p>
              <div class="math-block">
                $$G(j\omega_k) = \frac{\mathcal{F}\{y(t)\}(j\omega_k)}{\mathcal{F}\{u(t)\}(j\omega_k)} = \frac{Y(k)}{U(k)}, \quad \omega_k \in [1,0; 80,0]\text{ rad/s}$$
              </div>
              <p>Total de 126 frequências extraídas com rejeição natural de ruídos e efeitos de borda.</p>
            </div>
          </div>
        </div>
        <div class="col" style="flex: 1.05;">
          <div class="img-box" style="height: 100%;" onclick="openLightbox('{IMG_CHIRP}')">
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
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: Pedro Augusto</div>
          <div class="slide-tag">Item 4</div>
        </div>
      </div>
      <div class="slide-content">
        <div class="col" style="flex: 0.95;">
          <div class="card">
            <div class="card-title">🎯 Modelo Identificado vs. Nominal</div>
            <div class="card-body">
              <p>Função de transferência recuperada analiticamente pelo N2CACGO (\(n=2\)):</p>
              <div class="math-block">
                $$G_{\text{id}}(s) = \frac{100,5}{s^2 + 4,249s + 100,5}$$
              </div>
              <ul>
                <li><strong>Ganho DC:</strong> \(K_{\text{id}} = 1,0003\) (Nominal: \(1,0000\)).</li>
                <li><strong>Frequência Natural:</strong> \(\omega_n = 10,02\text{ rad/s}\) (Erro de apenas \(0,2\%\)).</li>
                <li><strong>Fator de Amortecimento:</strong> \(\zeta = 0,212\) (Nominal: \(0,200\)).</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <div class="card-title">📈 Índices de Desempenho Espectral</div>
            <div class="card-body">
              <ul>
                <li><strong>FIT Espectral Global:</strong> <span class="badge-ok">96,47%</span></li>
                <li><strong>RMSE de Módulo:</strong> \(0,77\text{ dB}\)</li>
                <li><strong>RMSE de Fase:</strong> \(8,69^{\circ}\)</li>
              </ul>
              <p style="margin-top: 8px; font-size: 12.5px; color: var(--text-muted);">
                A discretização no tempo e janelamento espectral causaram leve dispersão (*leakage*), plenamente absorvida pela robustez do estimador N2CACGO.
              </p>
            </div>
          </div>
        </div>
        <div class="col" style="flex: 1.05;">
          <div class="img-box" style="height: 100%;" onclick="openLightbox('{IMG_FFT}')">
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
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: Renato Felix</div>
          <div class="slide-tag">Item 5</div>
        </div>
      </div>
      <div class="slide-content">
        <div class="col" style="flex: 0.95;">
          <div class="card">
            <div class="card-title">🔬 Protocolo Experimental e Tratamento dos Dados</div>
            <div class="card-body">
              <ul>
                <li><strong>Base Única e Confiável:</strong> 26 ensaios senoidais da bancada do Grupo 3 (\(0,20\text{ Hz}\) a \(10,0\text{ Hz}\)). Expurgou-se integralmente qualquer base externa para manter integridade metrológica.</li>
                <li><strong>Regime Permanente Estrito:</strong> Processamento DFT restrito aos últimos 60% das amostras temporais, eliminando o transitório de partida do motor.</li>
                <li><strong>Fasores por DFT:</strong> Amplitude e fase extraídas no pico espectral fundamental do sinal forçado.</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <div class="card-title">📊 Varredura de Ordens (n = 1 a 4)</div>
            <div class="card-body">
              <p>O teste de múltiplas ordens mostrou que modelos de ordem superior (\(n \ge 2\)) sofrem sobreajuste (*overfitting*) a ruídos de comutação sem ganho de representatividade física.</p>
              <p style="color: #34D399; margin-top: 6px;">
                <strong>Decisão de Engenharia:</strong> Seleção do modelo de 1ª ordem, compatível com a teoria eletromecânica clássica de motores CC.
              </p>
            </div>
          </div>
        </div>
        <div class="col" style="flex: 1.05;">
          <div class="img-box" style="height: 100%;" onclick="openLightbox('{IMG_MOTOR_TODAS}')">
            <img src="{IMG_MOTOR_TODAS}" alt="Bode Todas Ordens Motor CC">
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 8: ITEM 5 - MODELO FÍSICO & PADÉ -->
    <div class="slide" data-index="8">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>7. [Item 5] Parâmetros Físicos e Zero de Não-Fase Mínima (Padé)</h2>
          <p>Compreensão física dos parâmetros eletromecânicos e do atraso de amostragem da bancada</p>
        </div>
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: Renato Felix</div>
          <div class="slide-tag">Item 5</div>
        </div>
      </div>
      <div class="slide-content">
        <div class="col" style="flex: 0.95;">
          <div class="card">
            <div class="card-title">🏆 Modelo Físico Selecionado</div>
            <div class="card-body">
              <div class="math-block">
                $$G_{\text{motor}}(s) = \frac{-0,2468 s + 48,33}{s + 4,794}$$
              </div>
              <ul>
                <li><strong>Ganho Estático:</strong> \(K_m = 48,33 / 4,794 = 10,08\text{ (rad/s)/V}\) (\(20,07\text{ dB}\)).</li>
                <li><strong>Constante de Tempo Eletromecânica:</strong> \(\tau_m = 1 / 4,794 = 0,209\text{ s}\).</li>
                <li><strong>FIT Global:</strong> <span class="badge-ok">88,36%</span>.</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <div class="card-title">💡 O Fenômeno Físico do Zero no SPD (s = +195,8 rad/s)</div>
            <div class="card-body">
              <p>O zero no semi-plano direito não representa instabilidade física, mas sim a <strong>aproximação de Padé de 1ª ordem</strong> do atraso puro de transporte da placa de aquisição:</p>
              <div class="math-block">
                $$e^{-s \tau_d} \approx \frac{1 - s \frac{\tau_d}{2}}{1 + s \frac{\tau_d}{2}} \implies \tau_d = \frac{2}{195,8} \approx 10,2\text{ ms}$$
              </div>
              <p style="font-size: 12.5px; color: var(--accent-cyan);">
                Isso explica perfeitamente por que a fase experimental ultrapassa os \(-90^{\circ}\) em altas frequências (10 Hz)!
              </p>
            </div>
          </div>
        </div>
        <div class="col" style="flex: 1.05;">
          <div class="img-box" style="height: 100%;" onclick="openLightbox('{IMG_MOTOR_MELHOR}')">
            <img src="{IMG_MOTOR_MELHOR}" alt="Bode Motor Melhor Modelo">
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 9: ITEM 5 - VALIDAÇÃO DINÂMICA TEMPORAL -->
    <div class="slide" data-index="9">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>8. [Item 5] Validação Dinâmica Temporal em Bancada Real</h2>
          <p>Confronto cego do modelo linear identificado contra ondas quadrada e triangular (10 Hz)</p>
        </div>
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: Arthur Scarpini</div>
          <div class="slide-tag">Item 5</div>
        </div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="img-box" style="flex: 1.25;" onclick="openLightbox('{IMG_SQR}')">
            <img src="{IMG_SQR}" alt="Validacao Onda Quadrada 10 Hz">
          </div>
          <div class="card" style="flex: 0.75;">
            <div class="card-title">🟦 Resposta a Onda Quadrada (10 Hz)</div>
            <div class="card-body">
              <p>O modelo identificado reproduz com exatidão as transições abruptas de subida e descida, com taxa exponencial compatível com \(\tau_m = 0,209\text{ s}\) e ganho estático consistente.</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="img-box" style="flex: 1.25;" onclick="openLightbox('{IMG_TRI}')">
            <img src="{IMG_TRI}" alt="Validacao Onda Triangular 10 Hz">
          </div>
          <div class="card" style="flex: 0.75;">
            <div class="card-title">🔺 Resposta a Onda Triangular (10 Hz)</div>
            <div class="card-body">
              <p>A ação passa-baixas natural do polo mecânico (\(s = -4,79\text{ rad/s}\)) arredonda suavemente as cúspides triangulares com atraso de fase idêntico ao medido pelo tacômetro.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 10: DIFICULDADES E SOLUÇÕES -->
    <div class="slide" data-index="10">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>9. Dificuldades Encontradas e Soluções de Engenharia</h2>
          <p>Superação de desafios numéricos, condicionamento matricial e integridade de dados</p>
        </div>
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: Arthur Scarpini</div>
          <div class="slide-tag">Engenharia</div>
        </div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">⚠️ 1. Condicionamento Numérico de Q em Ordens Altas</div>
            <div class="card-body">
              <p><strong>Problema:</strong> Para ordens \(n \ge 4\), monômios \((j\omega)^n\) atingem amplitudes de \(10^{14}\), fazendo com que \(\text{rcond}(Q) < 10^{-16}\). O comando <code>pinv</code> truncava direções de autovalores cruciais.</p>
              <p style="color: #34D399; margin-top: 6px;"><strong>Solução:</strong> Adoção de divisão matricial direta (<code>Q \ Y</code>) por eliminação Gaussiana com pivoteamento, preservando a base monômica e garantindo reprodução exata de Silveira (2006).</p>
            </div>
          </div>
          <div class="card">
            <div class="card-title">⚠️ 2. Vazamento Espectral (*Leakage*) na FFT</div>
            <div class="card-body">
              <p><strong>Problema:</strong> O janelamento abrupto em sinais aperiódicos no tempo gera dispersão de energia nas frequências vizinhas.</p>
              <p style="color: #34D399; margin-top: 6px;"><strong>Solução:</strong> Seleção restrita da faixa de excitação persistente do Chirp (\(1,0\) a \(80,0\text{ rad/s}\)), expurgando bordas com baixa coerência SNR.</p>
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

    <!-- SLIDE 11: CONCLUSÕES -->
    <div class="slide" data-index="11">
      <div class="slide-header">
        <div class="slide-title-group">
          <h2>10. Conclusões e Considerações Finais</h2>
          <p>Síntese das realizações, validação experimental e disponibilização pública</p>
        </div>
        <div class="slide-header-tags">
          <div class="speaker-badge">👤 Orador: Arthur Scarpini & Equipe</div>
          <div class="slide-tag">Conclusão</div>
        </div>
      </div>
      <div class="slide-content">
        <div class="col">
          <div class="card">
            <div class="card-title">🏆 Principais Conquistas do Trabalho</div>
            <div class="card-body">
              <ul>
                <li><strong>Validação Acadêmica Rigorosa:</strong> Concordância exata (99,99%) com a Tabela 3.2 de Silveira (2006) e FIT = 100,00% em sistemas didáticos.</li>
                <li><strong>Integração Simulink + FFT:</strong> Recuperação precisa da planta LTI de 2ª ordem a partir de sinais temporais (\(\text{FIT} = 96,47\%\)).</li>
                <li><strong>Identificação Física de Bancada:</strong> O modelo de 1ª ordem com atraso de Padé de \(\approx 10,2\text{ ms}\) traduz com extrema fidelidade a dinâmica eletromecânica do motor CC.</li>
                <li><strong>Automação Total:</strong> Todos os 5 itens programados em código nativo MATLAB (<code>executa_todos_itens.m</code>).</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card" style="border-color: rgba(56, 189, 248, 0.4);">
            <div class="card-title" style="color: var(--accent-cyan);">🌐 Repositório Aberto no GitHub</div>
            <div class="card-body">
              <p>Todo o código-fonte, modelo Simulink, dados experimentais, artigo IEEE em PDF e apresentação interativa estão disponíveis publicamente em:</p>
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
    <div class="nav-group">
      <button class="nav-btn" onclick="prevSlide()">◀ Anterior</button>
      <button class="nav-btn" onclick="nextSlide()">Próximo ▶</button>
      <button class="nav-btn" id="btn-grid" onclick="toggleGrid()">▦ Mosaico (O)</button>
    </div>

    <div class="nav-center">
      <div id="slide-indicator">SLIDE <span id="current-slide">01</span> / <span id="total-slides">11</span></div>
      <div id="progress-container">
        <div id="progress-bar"></div>
      </div>
    </div>

    <div class="nav-group">
      <div id="timer-widget" onclick="toggleTimer()" title="Clique para Iniciar/Pausar, Shift+Clique para Zerar">
        ⏱️ <span id="timer-display">00:00</span>
      </div>
      <button class="nav-btn" id="btn-notes" onclick="toggleNotes()">📝 Notas (N)</button>
      <button class="nav-btn" onclick="toggleFullscreen()">⛶ Tela Cheia (F)</button>
      <button class="nav-btn" onclick="window.print()">🖨️ PDF</button>
    </div>
  </div>

  <!-- PAINEL RETRÁTIL DE NOTAS DO ORADOR (SPEAKER NOTES) -->
  <div id="notes-drawer">
    <div class="notes-header">
      <h4>📝 Roteiro do Orador - Slide <span id="notes-slide-num">1</span></h4>
      <button class="notes-close" onclick="toggleNotes()">✕</button>
    </div>
    <div class="notes-body" id="notes-content">
      <!-- Inserido dinamicamente via JS -->
    </div>
  </div>

  <!-- MODAL DE ZOOM (LIGHTBOX) -->
  <div id="lightbox" onclick="closeLightbox()">
    <img id="lightbox-img" src="" alt="Zoom Imagem">
  </div>

  <!-- MODAL MOSAICO (SLIDE GRID) -->
  <div id="grid-modal">
    <div class="grid-header">
      <h3>▦ Visão Geral dos Slides (Pressione ESC ou clique para voltar)</h3>
      <button class="nav-btn" onclick="toggleGrid()">✕ Fechar</button>
    </div>
    <div class="grid-cards" id="grid-cards-container">
      <!-- Preenchido dinamicamente -->
    </div>
  </div>

  <script>
    // Roteiro do Orador individualizado por integrante com tempos balanceados (Total: ~14 a 16 min)
    const speakerNotes = {
      1: `<div class="notes-speaker-tag">👤 Orador: João Victor Pariz (Abertura da Equipe) | ~1:00 min</div>
          <strong>Abertura e Apresentação Formal:</strong>
          <ul>
            <li>Cumprimente o Prof. Dr. Marcelo de Araújo Oliveira e a banca avaliadora.</li>
            <li>Apresente a equipe dividida em 4 frentes:
              <ul>
                <li><strong>João Victor Pariz:</strong> Abertura, Contexto e Formulação Matemática Convexa;</li>
                <li><strong>Pedro Augusto:</strong> Benchmark de Silveira (2006) e Simulação Simulink com FFT;</li>
                <li><strong>Renato Felix:</strong> Dados Experimentais de Bancada e Modelo Físico com Padé;</li>
                <li><strong>Arthur Scarpini:</strong> Validação Dinâmica Temporal Cega, Desafios Numéricos e Conclusão.</li>
              </ul>
            </li>
            <li>Anuncie o tema: <em>Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO</em>.</li>
          </ul>`,
      2: `<div class="notes-speaker-tag">👤 Orador: João Victor Pariz | ~1:15 min</div>
          <strong>Contexto: Por que Domínio da Frequência?</strong>
          <ul>
            <li>Destaque os problemas do domínio do tempo (ARX, PEM): ruído estocástico de alta frequência contamina matrizes de covariância, e o estado inicial não nulo introduz viés severo.</li>
            <li>Explique a vantagem do domínio da frequência: energia concentrada estritamente nas frequências ensaiadas, com filtragem natural de ruídos.</li>
            <li><strong>Ponto Crítico:</strong> Métodos como Nelder-Mead (<code>fminsearch</code>) minimizam o erro de saída e caem em <em>mínimos locais</em>. O <strong>N2CACGO</strong> usa o erro de equação e torna o espaço <strong>estritamente convexo</strong>, garantindo solução global única!</li>
          </ul>`,
      3: `<div class="notes-speaker-tag">👤 Orador: João Victor Pariz | ~1:30 min</div>
          <strong>Formulação Matemática do N2CACGO:</strong>
          <ul>
            <li>Apresente a função de transferência arbitrária \(G_e(s) = B(s)/A(s)\).</li>
            <li>Mostre o resíduo de equação ponderado por fasor: \(e(j\omega_i) = A(j\omega_i) G(j\omega_i) - B(j\omega_i)\).</li>
            <li>Explique a minimização analítica: igualando o gradiente \(\nabla_\theta J = 0\), chega-se ao sistema particionado \(Q \theta = Y\).</li>
            <li>Destaque que a solução \(\theta^* = Q^{-1} Y\) é <em>fechada e puramente analítica</em>, sem iterações ou risco de divergência.</li>
            <li><strong>Transição de Fala:</strong> <em>"Para apresentar como validamos essa teoria matematicamente e a aplicação no Simulink, passo a palavra agora para o Pedro Augusto."</em></li>
          </ul>`,
      4: `<div class="notes-speaker-tag">👤 Orador: Pedro Augusto | ~1:15 min</div>
          <strong>Item 3: Benchmark Acadêmico de Silveira (2006):</strong>
          <ul>
            <li>Agradeça a passagem de João Victor.</li>
            <li>Mostre a Tabela 3.2: reproduzimos com <strong>100% de concordância</strong> todos os valores de \(J\) da dissertação original (ordens 1 a 7).</li>
            <li>Explique que para ordens \(n \ge 4\), o custo estaciona exatamente em \(6,2903 \times 10^{-4}\), provando que ordens maiores são redundantes para a dinâmica daquela planta.</li>
            <li>Mencione que em sistemas didáticos sintéticos com ordem compatível, o algoritmo obteve \(FIT = 100,00\%\) e erro resíduo \(J \sim 10^{-14}\).</li>
          </ul>`,
      5: `<div class="notes-speaker-tag">👤 Orador: Pedro Augusto | ~1:15 min</div>
          <strong>Item 4: Simulação Simulink & Análise FFT:</strong>
          <ul>
            <li>Descreva o modelo Simulink (<code>modelo_item4.slx</code>): planta subamortecida de 2ª ordem (\(\omega_n = 10\text{ rad/s}, \zeta = 0,20\)).</li>
            <li>Explique o sinal de entrada: Chirp senoidal linear varrendo de \(0,1\) a \(15,0\text{ Hz}\), amostrado a \(1000\text{ Hz}\) (\(N = 20.001\) amostras).</li>
            <li>Explique a extração fasorial por FFT: \(G(j\omega_k) = Y(k)/U(k)\), isolando 126 frequências com alta coerência SNR.</li>
          </ul>`,
      6: `<div class="notes-speaker-tag">👤 Orador: Pedro Augusto | ~1:00 min</div>
          <strong>Item 4: Validação do Modelo Identificado via FFT:</strong>
          <ul>
            <li>Mostre o modelo identificado: \(\omega_n = 10,02\text{ rad/s}\) (erro de apenas \(0,2\%\)) e ganho unitário com erro \(< 0,03\%\).</li>
            <li>Apresente os índices de desempenho: <strong>FIT = 96,47%</strong>, RMSE de módulo \(0,77\text{ dB}\) e RMSE de fase \(8,69^{\circ}\).</li>
            <li>Justifique a pequena dispersão residual como efeito inevitável de vazamento espectral (*spectral leakage*) na FFT, plenamente absorvido pelo estimador.</li>
            <li><strong>Transição de Fala:</strong> <em>"Agora que vimos a robustez do N2CACGO em simulação, passo a palavra ao Renato Felix para apresentar a identificação em bancada física real de um motor CC."</em></li>
          </ul>`,
      7: `<div class="notes-speaker-tag">👤 Orador: Renato Felix | ~1:30 min</div>
          <strong>Item 5: Bancada Experimental do Motor CC:</strong>
          <ul>
            <li>Agradeça a passagem de Pedro Augusto.</li>
            <li><strong>Rigor Metrológico:</strong> Enfatize que utilizamos exclusivamente a base de dados autêntica do <em>Grupo 3</em> (26 ensaios senoidais de \(0,20\) a \(10,0\text{ Hz}\)). Nenhuma base externa foi misturada.</li>
            <li>Explique o tratamento dos dados: para cada frequência, os fasores foram extraídos via DFT sobre os últimos 60% das amostras temporais, garantindo regime permanente estrito e eliminando transitórios de partida.</li>
            <li>Varredura de ordens (1 a 4): mostre no gráfico que ordens maiores sofrem sobreajuste (*overfitting*) a ruídos de comutação sem ganho físico real. Justifique a seleção da 1ª ordem.</li>
          </ul>`,
      8: `<div class="notes-speaker-tag">👤 Orador: Renato Felix | ~2:00 min (Ponto Alto Técnico)</div>
          <strong>Item 5: Parâmetros Físicos e Atraso de Padé:</strong>
          <ul>
            <li>Apresente o modelo adotado: \(G(s) = \frac{-0,2468 s + 48,33}{s + 4,794}\) (\(FIT = 88,36\%\)).</li>
            <li>Discuta a física: ganho estático \(K_m = 10,08\text{ (rad/s)/V}\) e constante de tempo \(\tau_m = 0,209\text{ s}\).</li>
            <li><strong>Explicação Crucial para a Banca:</strong> O modelo possui um zero no semi-plano direito (\(s = +195,8\text{ rad/s}\)). Explique que <em>não é instabilidade</em>, mas sim a aproximação de Padé de 1ª ordem do atraso puro de amostragem (\(\tau_d = 2/195,8 \approx 10,2\text{ ms}\)).</li>
            <li>Esse atraso de amostragem de \(\approx 10,2\text{ ms}\) da placa explica matematicamente por que a fase experimental cai além de \(-90^{\circ}\) a 10 Hz!</li>
            <li><strong>Transição de Fala:</strong> <em>"Para apresentar a validação dinâmica cega no tempo, as dificuldades numéricas e as conclusões, passo a palavra para o Arthur Scarpini."</em></li>
          </ul>`,
      9: `<div class="notes-speaker-tag">👤 Orador: Arthur Scarpini | ~1:15 min</div>
          <strong>Item 5: Validação Dinâmica Temporal Cega:</strong>
          <ul>
            <li>Agradeça a passagem de Renato Felix.</li>
            <li>Mostre o teste cego com sinais de onda quadrada (<code>sqrf</code>) e triangular (<code>trif</code>) a \(10\text{ Hz}\).</li>
            <li>Destaque que o modelo linear identificado no domínio da frequência simulou a resposta temporal real com excelente precisão:</li>
            <li>Na onda quadrada, acompanha as transições exponenciais e taxa de subida. Na onda triangular, arredonda suavemente as pontas pela ação do polo mecânico (\(s = -4,79\text{ rad/s}\)).</li>
          </ul>`,
      10: `<div class="notes-speaker-tag">👤 Orador: Arthur Scarpini | ~1:30 min</div>
          <strong>Dificuldades Encontradas e Soluções de Engenharia:</strong>
          <ul>
            <li><em>1. Condicionamento Numérico de Q:</em> Para ordens \(n \ge 4\), as potências \((j\omega)^n\) atingem \(10^{14}\) e \(\text{rcond}(Q) < 10^{-16}\). O comando <code>pinv</code> truncava autovalores essenciais. Resolvemos usando eliminação Gaussiana com pivoteamento (<code>Q \ Y</code>), recuperando o erro nulo exato de Silveira.</li>
            <li><em>2. Vazamento da FFT:</em> Contornado limitando a faixa de frequências úteis a \([1,0; 80,0]\text{ rad/s}\).</li>
            <li><em>3. Transitórios na Bancada:</em> Expurgados pela janela dos últimos 60%.</li>
            <li><em>4. Solvers no Simulink:</em> Parametrização programática com o solver contínuo <code>ode4</code> de passo fixo.</li>
          </ul>`,
      11: `<div class="notes-speaker-tag">👤 Orador: Arthur Scarpini & Toda a Equipe | ~1:15 min</div>
          <strong>Conclusões e Repositório Aberto:</strong>
          <ul>
            <li>Sintetize as entregas: os 5 itens foram executados e automatizados com sucesso em scripts MATLAB nativos (<code>executa_todos_itens.m</code>).</li>
            <li>Mostre o link do GitHub aberto: repositório completo com dados, diagramas Simulink, artigo IEEE em PDF de 5 páginas e apresentação interativa.</li>
            <li>Convide os 3 colegas (João Victor, Pedro e Renato) para se posicionarem juntos para a banca.</li>
            <li>Agradeça ao Prof. Dr. Marcelo de Araújo Oliveira e abra formalmente a sessão para perguntas!</li>
          </ul>`
    };

    let currentSlideIndex = 1;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    const progressBar = document.getElementById('progress-bar');
    const currentIndicator = document.getElementById('current-slide');
    const totalIndicator = document.getElementById('total-slides');
    const notesDrawer = document.getElementById('notes-drawer');
    const notesContent = document.getElementById('notes-content');
    const notesSlideNum = document.getElementById('notes-slide-num');
    const btnNotes = document.getElementById('btn-notes');
    const gridModal = document.getElementById('grid-modal');
    const gridContainer = document.getElementById('grid-cards-container');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    totalIndicator.textContent = String(totalSlides).padStart(2, '0');

    // Inicializa os cards do mosaico
    function initGrid() {
      gridContainer.innerHTML = '';
      slides.forEach((slide, idx) => {
        const num = idx + 1;
        const titleEl = slide.querySelector('.slide-title-group h2') || slide.querySelector('.cover-title');
        const title = titleEl ? titleEl.textContent : `Slide ${num}`;
        const card = document.createElement('div');
        card.className = `grid-card ${num === currentSlideIndex ? 'current' : ''}`;
        card.onclick = () => {
          showSlide(num);
          toggleGrid();
        };
        card.innerHTML = `
          <div class="grid-card-num">SLIDE ${String(num).padStart(2, '0')}</div>
          <div class="grid-card-title">${title}</div>
        `;
        gridContainer.appendChild(card);
      });
    }

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
      notesSlideNum.textContent = String(currentSlideIndex);

      if (speakerNotes[currentSlideIndex]) {
        notesContent.innerHTML = speakerNotes[currentSlideIndex];
      } else {
        notesContent.innerHTML = '<p>Nenhuma nota específica para este slide.</p>';
      }

      initGrid();
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

    function toggleNotes() {
      notesDrawer.classList.toggle('open');
      btnNotes.classList.toggle('active-btn', notesDrawer.classList.contains('open'));
    }

    function toggleGrid() {
      gridModal.classList.toggle('open');
      if (gridModal.classList.contains('open')) {
        initGrid();
      }
    }

    function openLightbox(src) {
      lightboxImg.src = src;
      lightbox.classList.add('open');
    }

    function closeLightbox() {
      lightbox.classList.remove('open');
    }

    // Cronometro / Timer de Apresentacao
    let timerSeconds = 0;
    let timerInterval = null;
    let timerRunning = false;
    const timerDisplay = document.getElementById('timer-display');

    function updateTimerDisplay() {
      const mins = Math.floor(timerSeconds / 60);
      const secs = timerSeconds % 60;
      timerDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }

    function toggleTimer(event) {
      if (window.event && window.event.shiftKey) {
        // Shift + clique zera o cronometro
        timerSeconds = 0;
        updateTimerDisplay();
        return;
      }
      if (timerRunning) {
        clearInterval(timerInterval);
        timerRunning = false;
        document.getElementById('timer-widget').style.borderColor = 'rgba(245, 158, 11, 0.3)';
      } else {
        timerInterval = setInterval(() => {
          timerSeconds++;
          updateTimerDisplay();
        }, 1000);
        timerRunning = true;
        document.getElementById('timer-widget').style.borderColor = 'var(--accent-emerald)';
      }
    }

    // Atalhos de teclado para apresentacao executiva
    document.addEventListener('keydown', (e) => {
      // Se lightbox ou grid estiver aberto, ESC fecha
      if (e.key === 'Escape') {
        if (lightbox.classList.contains('open')) {
          closeLightbox();
          return;
        }
        if (gridModal.classList.contains('open')) {
          toggleGrid();
          return;
        }
      }

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
      } else if (e.key.toLowerCase() === 'n') {
        e.preventDefault();
        toggleNotes();
      } else if (e.key.toLowerCase() === 'o') {
        e.preventDefault();
        toggleGrid();
      } else if (e.key.toLowerCase() === 't') {
        e.preventDefault();
        toggleTimer();
      }
    });

    // Inicializacao da primeira tela e notas
    showSlide(1);
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
