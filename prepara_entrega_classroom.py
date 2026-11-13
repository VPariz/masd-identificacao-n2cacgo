import os
import shutil
import zipfile

BASE_DIR = r"c:\Users\jvpar\estudo\3.2\MASD\trabalho_identificacao"
ENTREGA_DIR = os.path.join(BASE_DIR, "entrega_classroom")
ZIP_PATH = os.path.join(BASE_DIR, "Entrega_Classroom_MASD_N2CACGO_Grupo3.zip")

if os.path.exists(ENTREGA_DIR):
    shutil.rmtree(ENTREGA_DIR)
os.makedirs(ENTREGA_DIR, exist_ok=True)

# 1. Copiar Artigo em PDF
pdf_src = os.path.join(BASE_DIR, "artigo", "artigo_identificacao.pdf")
pdf_dst = os.path.join(ENTREGA_DIR, "Artigo_Identificacao_N2CACGO_IME_Grupo3.pdf")
shutil.copy2(pdf_src, pdf_dst)
print("Copied article PDF.")

# 2. Copiar Apresentacao PPTX
pptx_src = os.path.join(BASE_DIR, "apresentacao", "apresentacao_MASD_N2CACGO_IME.pptx")
pptx_dst = os.path.join(ENTREGA_DIR, "Apresentacao_MASD_N2CACGO_IME_Grupo3.pptx")
shutil.copy2(pptx_src, pptx_dst)
print("Copied presentation PPTX.")

# 3. Copiar Roteiro de Fala
roteiro_src = os.path.join(BASE_DIR, "apresentacao", "ROTEIRO_APRESENTACAO.md")
roteiro_dst = os.path.join(ENTREGA_DIR, "ROTEIRO_DE_FALA_E_APRESENTACAO.md")
shutil.copy2(roteiro_src, roteiro_dst)
print("Copied roteiro markdown.")

# 4. Criar pasta de Codigos MATLAB e Simulink
codigos_dst = os.path.join(ENTREGA_DIR, "Codigos_MATLAB")
os.makedirs(codigos_dst, exist_ok=True)

scripts_src = os.path.join(BASE_DIR, "scripts_matlab")
for fname in os.listdir(scripts_src):
    if fname.endswith(".m") or fname.endswith(".slx"):
        shutil.copy2(os.path.join(scripts_src, fname), os.path.join(codigos_dst, fname))

# Copiar modelo_item4.slx da pasta simulink se nao estiver
slx_src = os.path.join(BASE_DIR, "simulink", "modelo_item4.slx")
if os.path.exists(slx_src):
    shutil.copy2(slx_src, os.path.join(codigos_dst, "modelo_item4.slx"))

# 5. Copiar Dados do Motor
dados_dst = os.path.join(ENTREGA_DIR, "dados_motor")
dados_src = os.path.join(BASE_DIR, "dados_motor")
shutil.copytree(dados_src, dados_dst)
print("Copied motor experimental data.")

# 6. Criar LEIA-ME da entrega
leia_me_content = """================================================================================
INSTITUTO MILITAR DE ENGENHARIA (IME) - DE/3 • ENGENHARIA ELÉTRICA
DISCIPLINA: MODELAGEM E ANÁLISE DE SISTEMAS DINÂMICOS (MASD)
DOCENTE: PROF. DR. MARCELO DE ARAÚJO OLIVEIRA
================================================================================

TRABALHO: Identificação de Sistemas SISO no Domínio da Frequência via Método N2CACGO
GRUPO DE AUTORES (Nomes de Guerra em Destaque):
  - Renato Felix (Renato Costa Félix)
  - Pariz (João Victor Tavares Pariz)
  - Pedro Augusto / Peu (Pedro Augusto dos Santos Barbosa)
  - Scarpini (Wagner Scarpini Miranda)

================================================================================
CONTEÚDO DO PACOTE DE ENTREGA:
================================================================================
1. Artigo_Identificacao_N2CACGO_IME_Grupo3.pdf
   - Artigo acadêmico completo de 6 páginas no formato IEEE de duas colunas.
   - Contém fundamentação analítica convexa de Silveira (2006), formulação matricial,
     resultados comparativos dos itens 3, 4 e 5, interpretação do atraso de Padé (10,2 ms)
     e dificuldades de engenharia solucionadas.

2. Apresentacao_MASD_N2CACGO_IME_Grupo3.pptx
   - Apresentação técnica em PowerPoint widescreen (16:9) com 14 slides.
   - Contém notas de orador detalhadas em todos os slides com o roteiro cronometrado (~16 min)
     dividido entre os 4 autores.

3. ROTEIRO_DE_FALA_E_APRESENTACAO.md
   - Guia completo contendo o texto exato da fala slide a slide, cronometragem,
     destaques visuais e respostas detalhadas para as principais perguntas da banca.

4. Pasta 'Codigos_MATLAB/':
   - executa_todos_itens.m       : Script mestre que executa os itens 1 a 5 em sequência com 1 clique.
   - identifica_N2CACGO.m        : [Item 1] Função analítica convexa do método N2CACGO (Silveira, 2006).
   - valida_modelo_fr.m          : [Item 2] Rotina de cálculo de erro de FRF (J, RMSE mag/fase, FIT %).
   - executa_item3_academicos.m  : [Item 3] Benchmark de Silveira (2006) e sistemas didáticos.
   - executa_item4_simulink.m    : [Item 4] Simulação chirp no Simulink e reconstrução espectral via FFT.
   - executa_item5_motor.m       : [Item 5] Identificação da bancada experimental do motor CC e validação cega.
   - carrega_dados_motor.m       : Função auxiliar para carregamento e tratamento das 26 senoides experimentais.
   - modelo_item4.slx            : Modelo dinâmico no Simulink configurado com solver ode4 de passo fixo.

5. Pasta 'dados_motor/':
   - Arquivos '.mat' contendo os registros de ensaios experimentais coletados na bancada de SSL (Grupo 3):
     * 26 ensaios senoidais puros (0,20 Hz a 10,00 Hz) para identificação da FRF.
     * Ensaios com onda quadrada e onda triangular (10 Hz) para validação temporal cega.

================================================================================
INSTRUÇÕES DE EXECUÇÃO RÁPIDA (MATLAB R2020a ou superior):
================================================================================
Passo 1: Abra o MATLAB e adicione a pasta 'Codigos_MATLAB' e 'dados_motor' ao Path, ou navegue até ela:
         >> cd('Codigos_MATLAB')
         >> addpath('../dados_motor')

Passo 2: Para executar todos os itens e gerar todas as figuras e métricas automaticamente:
         >> executa_todos_itens

Passo 3: Para executar itens individualmente:
         >> executa_item3_academicos   % Executa o Item 3
         >> executa_item4_simulink     % Executa o Item 4 (abre e roda o Simulink)
         >> executa_item5_motor        % Executa o Item 5 (processa dados do motor)

================================================================================
REPOSITÓRIO GIT:
================================================================================
Todo o projeto também se encontra versionado no GitHub:
https://github.com/VPariz/masd-identificacao-n2cacgo.git
================================================================================
"""

with open(os.path.join(ENTREGA_DIR, "LEIA-ME_ENTREGA.txt"), "w", encoding="utf-8") as f:
    f.write(leia_me_content)
print("Created LEIA-ME_ENTREGA.txt.")

# 7. Criar ZIP da entrega completa
print(f"Creating zip file: {ZIP_PATH} ...")
with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(ENTREGA_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(ENTREGA_DIR))
            zipf.write(file_path, arcname)

print(f"ZIP package created successfully! Size: {os.path.getsize(ZIP_PATH) / 1024 / 1024:.2f} MB")
