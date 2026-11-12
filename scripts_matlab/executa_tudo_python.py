import os
import re
import numpy as np
import scipy.io
import scipy.signal
import matplotlib.pyplot as plt

# Estilo visual científico limpo
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'dados_motor')
FIG_DIR = os.path.join(BASE_DIR, 'artigo', 'figuras')
os.makedirs(FIG_DIR, exist_ok=True)

print("=" * 70)
print(" EXECUÇÃO INTEGRADA DA IDENTIFICAÇÃO N2CACGO (SILVEIRA, 2006)")
print("=" * 70)

# =========================================================================
# FUNÇÃO N2CACGO (SILVEIRA, 2006)
# =========================================================================
def identifica_N2CACGO(w, H, n):
    w = np.asarray(w).flatten()
    H = np.asarray(H).flatten()
    m = len(w)

    # Matriz R: (n+1) x m
    R = np.zeros((n + 1, m), dtype=complex)
    for k in range(n + 1):
        R[k, :] = (1j * w) ** (n - k)

    S = np.diag(H)
    S_conj = np.diag(np.conj(H))
    S_gamma = np.diag(H * np.conj(H))
    R_H = R.conj().T

    # Blocos da Matriz Q e Vetores Y (Equações 3.32 a 3.39 de Silveira 2006)
    Q1 = np.real(R @ R_H)
    Q2 = np.real(R @ S_conj @ R_H[:, 1:])
    Q3 = np.real(R[1:, :] @ S @ R_H)
    Q4 = np.real(R[1:, :] @ S_gamma @ R_H[:, 1:])

    Y1 = np.real(R @ S_conj @ R_H[:, 0])
    Y2 = np.real(R[1:, :] @ S_gamma @ R_H[:, 0])

    Q = np.block([[Q1, -Q2], [Q3, -Q4]])
    Y = np.concatenate([Y1, Y2])

    theta = np.linalg.solve(Q, Y)
    num = theta[:n + 1]
    den = np.concatenate([[1.0], theta[n + 1:]])

    # Avaliação em frequência
    He = np.polyval(num, 1j * w) / np.polyval(den, 1j * w)
    J = np.linalg.norm(H - He)

    return num, den, He, J

def calcula_metricas(H_orig, H_est):
    mag_orig_db = 20 * np.log10(np.abs(H_orig))
    mag_est_db  = 20 * np.log10(np.abs(H_est))
    fase_orig   = np.angle(H_orig, deg=True)
    fase_est    = np.angle(H_est, deg=True)

    # Desembrulho de fase
    diff_fase = (fase_orig - fase_est + 180) % 360 - 180

    J = np.linalg.norm(H_orig - H_est)
    rmse_mag = np.sqrt(np.mean((mag_orig_db - mag_est_db)**2))
    rmse_fase = np.sqrt(np.mean(diff_fase**2))
    fit = max(0.0, 100.0 * (1.0 - J / np.linalg.norm(H_orig - np.mean(H_orig))))

    return {'J': J, 'RMSE_mag': rmse_mag, 'RMSE_fase': rmse_fase, 'FIT': fit}

# =========================================================================
# ITEM 3: EXEMPLO ACADÊMICO DE SILVEIRA (2006) - 7ª ORDEM BIPRÓPRIA
# =========================================================================
print("\n[ITEM 3] Executando Exemplo Acadêmico 3.4.1 de Silveira (2006)...")

num_7 = [0.100000000, 4.753000000, 90.01275000, 863.2453825, 4417.863626, 11761.82161, 14942.80380, 6958.320022]
den_7 = [1.000000000, 16.82000000, 252.6691000, 2476.872788, 13659.19997, 59044.40987, 131354.0179, 87580.35014]

w_silv = np.logspace(-2, 2, 100)
s_silv = 1j * w_silv
H_silv = np.polyval(num_7, s_silv) / np.polyval(den_7, s_silv)

J_ref_silveira = [15.126, 3.018, 1.466, 6.320e-4, 3.795e-4, 6.306e-4, 3.439e-4]

print("-" * 65)
print(" Ordem | Custo J (Obtido) | Custo J1 (Silveira, 2006) |  FIT (%)")
print("-" * 65)

modelos_silv = {}
for n in range(1, 8):
    num_e, den_e, He, J_obt = identifica_N2CACGO(w_silv, H_silv, n)
    met = calcula_metricas(H_silv, He)
    modelos_silv[n] = (num_e, den_e, He, met)
    print(f"   {n}   |   {J_obt:12.4e}   |       {J_ref_silveira[n-1]:12.4e}        | {met['FIT']:6.2f} %")
print("-" * 65)

# Gráfico do Exemplo Silveira
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
ax1.semilogx(w_silv, 20*np.log10(np.abs(H_silv)), 'k-', lw=2.2, label='G(s) Original (7ª Ordem)')
ax2.semilogx(w_silv, np.angle(H_silv, deg=True), 'k-', lw=2.2, label='G(s) Original (7ª Ordem)')

cores = {1: 'blue', 2: 'purple', 4: 'green', 7: 'red'}
estilos = {1: '--', 2: '-.', 4: '--', 7: '-'}
for n in [1, 2, 4, 7]:
    He = modelos_silv[n][2]
    met = modelos_silv[n][3]
    lbl = f"N2CACGO n={n} (J={met['J']:.2e})"
    ax1.semilogx(w_silv, 20*np.log10(np.abs(He)), color=cores[n], ls=estilos[n], lw=1.5, label=lbl)
    ax2.semilogx(w_silv, np.angle(He, deg=True), color=cores[n], ls=estilos[n], lw=1.5, label=lbl)

ax1.set_ylabel('Magnitude (dB)', fontsize=11)
ax1.set_title('Exemplo Acadêmico 3.4.1 (Silveira, 2006) - Diagrama de Bode', fontsize=12, fontweight='bold')
ax1.grid(True, which='both', ls=':', alpha=0.6)
ax1.legend(loc='best', fontsize=9)

ax2.set_ylabel('Fase (graus)', fontsize=11)
ax2.set_xlabel('Frequência Angular $\\omega$ (rad/s)', fontsize=11)
ax2.grid(True, which='both', ls=':', alpha=0.6)
ax2.legend(loc='best', fontsize=9)

plt.tight_layout()
fig_path_silv = os.path.join(FIG_DIR, 'item3_exemplo_silveira_bode.png')
plt.savefig(fig_path_silv, dpi=300)
plt.close()
print(f"Figura salva: {fig_path_silv}")

# =========================================================================
# ITEM 4: SIMULAÇÃO TEMPORAL -> FFT -> IDENTIFICAÇÃO N2CACGO
# =========================================================================
print("\n[ITEM 4] Executando Simulação Temporal (Chirp), FFT e N2CACGO...")

# Sistema LTI Alvo: G(s) = 8 / (0.2 s^2 + 1.2 s + 1)
num_alvo = [8.0]
den_alvo = [0.2, 1.2, 1.0]
sys_alvo = scipy.signal.TransferFunction(num_alvo, den_alvo)

fs = 200.0
dt = 1.0 / fs
T_total = 10.0
t_sim = np.arange(0, T_total, dt)

f0, f1 = 0.1, 15.0
u_sim = np.sin(2 * np.pi * (f0 + (f1 - f0) * t_sim / (2 * T_total)) * t_sim)

# Resposta temporal y(t)
_, y_sim, _ = scipy.signal.lsim(sys_alvo, U=u_sim, T=t_sim)

# FFT
N_fft = len(t_sim)
U_fft = np.fft.fft(u_sim)
Y_fft = np.fft.fft(y_sim)

N_half = N_fft // 2
U_half = U_fft[:N_half]
Y_half = Y_fft[:N_half]
f_vetor = np.arange(N_half) * (fs / N_fft)
w_fft = 2 * np.pi * f_vetor

# Faixa de frequências com excitação confiável (1 rad/s a 80 rad/s)
idx_valid = (w_fft >= 1.0) & (w_fft <= 80.0)
w_corte = w_fft[idx_valid]
H_fft = Y_half[idx_valid] / U_half[idx_valid]

# N2CACGO para recuperar a 2ª ordem
num_id4, den_id4, He4, J4 = identifica_N2CACGO(w_corte, H_fft, 2)
met4 = calcula_metricas(H_fft, He4)

print(f"Identificação Item 4: Custo J = {J4:.4e} | FIT = {met4['FIT']:.2f}% | RMSE Mag = {met4['RMSE_mag']:.4f} dB")
print(f"  Numerador Alvo: {num_alvo} -> Identificado: {num_id4.round(4)}")
print(f"  Denominador Alvo: {den_alvo} -> Identificado: {den_id4.round(4)}")

# Figura dos Sinais Temporais
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.5), sharex=True)
ax1.plot(t_sim, u_sim, 'b', lw=1.2)
ax1.set_ylabel('Entrada u(t)', fontsize=11)
ax1.set_title('Item 4: Sinais Temporais no Domínio do Tempo (Chirp 0.1 a 15 Hz)', fontsize=12, fontweight='bold')
ax1.grid(True, ls=':', alpha=0.6)

ax2.plot(t_sim, y_sim, 'm', lw=1.2)
ax2.set_ylabel('Saída y(t)', fontsize=11)
ax2.set_xlabel('Tempo (s)', fontsize=11)
ax2.grid(True, ls=':', alpha=0.6)
plt.tight_layout()
fig_path_temp = os.path.join(FIG_DIR, 'item4_simulink_sinais_temporais.png')
plt.savefig(fig_path_temp, dpi=300)
plt.close()
print(f"Figura salva: {fig_path_temp}")

# Figura de Comparação Espectral
w_eval, H_alvo_eval = scipy.signal.freqs(num_alvo, den_alvo, worN=w_corte)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
ax1.semilogx(w_corte, 20*np.log10(np.abs(H_alvo_eval)), 'k-', lw=2.2, label='G(s) Alvo Teórico')
ax1.semilogx(w_corte, 20*np.log10(np.abs(H_fft)), 'co', ms=4, alpha=0.7, label='Estimativa FFT')
ax1.semilogx(w_corte, 20*np.log10(np.abs(He4)), 'r--', lw=1.8, label=f'N2CACGO (FIT={met4["FIT"]:.1f}%)')
ax1.set_ylabel('Magnitude (dB)', fontsize=11)
ax1.set_title(f'Item 4: Validação Espectral (J = {J4:.2e} | FIT = {met4["FIT"]:.1f}%)', fontsize=12, fontweight='bold')
ax1.grid(True, which='both', ls=':', alpha=0.6)
ax1.legend(loc='best', fontsize=10)

ax2.semilogx(w_corte, np.angle(H_alvo_eval, deg=True), 'k-', lw=2.2, label='G(s) Alvo Teórico')
ax2.semilogx(w_corte, np.angle(H_fft, deg=True), 'co', ms=4, alpha=0.7, label='Estimativa FFT')
ax2.semilogx(w_corte, np.angle(He4, deg=True), 'r--', lw=1.8, label='N2CACGO')
ax2.set_ylabel('Fase (graus)', fontsize=11)
ax2.set_xlabel('Frequência Angular $\\omega$ (rad/s)', fontsize=11)
ax2.grid(True, which='both', ls=':', alpha=0.6)
ax2.legend(loc='best', fontsize=10)

plt.tight_layout()
fig_path_bode4 = os.path.join(FIG_DIR, 'item4_simulink_bode_validacao.png')
plt.savefig(fig_path_bode4, dpi=300)
plt.close()
print(f"Figura salva: {fig_path_bode4}")

# =========================================================================
# ITEM 5: IDENTIFICAÇÃO DO MOTOR DC (DADOS DE SSL - GRUPO 3)
# =========================================================================
print("\n[ITEM 5] Processando Ensaios Experimentais do Motor DC...")

sen_ent = [f for f in os.listdir(DATA_DIR) if f.startswith('sen') and f.endswith('Ent.mat')]
freq_dict = {}

for fe in sen_ent:
    m = re.match(r'senf(\d+)a(\d+)Ent\.mat', fe)
    if not m: continue
    f_num = int(m.group(1))
    freq_hz = f_num / 100.0 if f_num != 1000 else 10.0
    fs_file = fe.replace('Ent.mat', 'Sai.mat')
    if not os.path.exists(os.path.join(DATA_DIR, fs_file)): continue

    mat_in = scipy.io.loadmat(os.path.join(DATA_DIR, fe))
    mat_out = scipy.io.loadmat(os.path.join(DATA_DIR, fs_file))
    k_in_val = [k for k in mat_in if 'Value' in k][0]
    k_in_time = [k for k in mat_in if 'Time' in k][0]
    k_out_val = [k for k in mat_out if 'Value' in k][0]

    u = mat_in[k_in_val].flatten()
    t = mat_in[k_in_time].flatten()
    y_mat = mat_out[k_out_val]
    y = y_mat[:, 1] if y_mat.shape[1] > 1 else y_mat[:, 0]

    n_pts = min(len(u), len(t), len(y))
    u = u[:n_pts]; t = t[:n_pts]; y = y[:n_pts]
    idx = int(0.4 * n_pts)

    w = 2 * np.pi * freq_hz
    ref = np.exp(-1j * w * t[idx:])
    U_w = np.sum(u[idx:] * ref)
    Y_w = np.sum(y[idx:] * ref)
    H = Y_w / U_w

    if freq_hz not in freq_dict: freq_dict[freq_hz] = []
    freq_dict[freq_hz].append((w, H))

w_list = []
H_list = []
for f_hz in sorted(freq_dict.keys()):
    w_val = freq_dict[f_hz][0][0]
    H_val = np.mean([item[1] for item in freq_dict[f_hz]])
    w_list.append(w_val)
    H_list.append(H_val)

w_motor = np.array(w_list)
H_motor = np.array(H_list)

print(f"Total de pontos de frequência do motor: {len(w_motor)} ({min(w_motor):.2f} a {max(w_motor):.2f} rad/s)")

print("-" * 75)
print(" Ordem | Custo J (Norma 2) | RMSE Mag (dB) | RMSE Fase (deg) | FIT (%)")
print("-" * 75)

modelos_motor = {}
for ord_m in range(1, 6):
    num_m, den_m, He_m, J_m = identifica_N2CACGO(w_motor, H_motor, ord_m)
    met_m = calcula_metricas(H_motor, He_m)
    modelos_motor[ord_m] = (num_m, den_m, He_m, met_m)
    print(f"  {ord_m:2d}ª  |   {J_m:12.4e}    |    {met_m['RMSE_mag']:8.4f}   |    {met_m['RMSE_fase']:8.4f}     | {met_m['FIT']:6.2f} %")
print("-" * 75)

# Gráfico de todas as ordens do motor
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
ax1.semilogx(w_motor, 20*np.log10(np.abs(H_motor)), 'k-o', lw=2, ms=5, label='Dados Experimentais (SSL)')
ax2.semilogx(w_motor, np.angle(H_motor, deg=True), 'k-o', lw=2, ms=5, label='Dados Experimentais (SSL)')

cores_m = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for ord_m in range(1, 6):
    He_m = modelos_motor[ord_m][2]
    met_m = modelos_motor[ord_m][3]
    lbl = f"{ord_m}ª Ordem (FIT={met_m['FIT']:.1f}%)"
    ax1.semilogx(w_motor, 20*np.log10(np.abs(He_m)), '--', color=cores_m[ord_m-1], lw=1.5, label=lbl)
    ax2.semilogx(w_motor, np.angle(He_m, deg=True), '--', color=cores_m[ord_m-1], lw=1.5, label=lbl)

ax1.set_ylabel('Magnitude (dB)', fontsize=11)
ax1.set_title('Identificação N2CACGO do Motor DC - Comparação de Ordens 1 a 5', fontsize=12, fontweight='bold')
ax1.grid(True, which='both', ls=':', alpha=0.6)
ax1.legend(loc='best', fontsize=9)

ax2.set_ylabel('Fase (graus)', fontsize=11)
ax2.set_xlabel('Frequência Angular $\\omega$ (rad/s)', fontsize=11)
ax2.grid(True, which='both', ls=':', alpha=0.6)
ax2.legend(loc='best', fontsize=9)

plt.tight_layout()
fig_path_mot_all = os.path.join(FIG_DIR, 'item5_motor_bode_todas_ordens.png')
plt.savefig(fig_path_mot_all, dpi=300)
plt.close()
print(f"Figura salva: {fig_path_mot_all}")

# Gráfico do Modelo Selecionado (1ª Ordem Parcimonioso)
num_best, den_best, He_best, met_best = modelos_motor[1]
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5.5), sharex=True)
ax1.semilogx(w_motor, 20*np.log10(np.abs(H_motor)), 'k-o', lw=2.2, ms=6, label='Dados Experimentais (Bancada)')
ax1.semilogx(w_motor, 20*np.log10(np.abs(He_best)), 'r--s', lw=1.8, ms=5, label=f'Modelo 1ª Ordem (FIT={met_best["FIT"]:.1f}%)')
ax1.set_ylabel('Magnitude (dB)', fontsize=11)
ax1.set_title(f'Modelo Selecionado (1ª Ordem) vs Resposta Experimental (RMSE={met_best["RMSE_mag"]:.2f} dB)', fontsize=12, fontweight='bold')
ax1.grid(True, which='both', ls=':', alpha=0.6)
ax1.legend(loc='best', fontsize=10)

ax2.semilogx(w_motor, np.angle(H_motor, deg=True), 'k-o', lw=2.2, ms=6, label='Dados Experimentais (Bancada)')
ax2.semilogx(w_motor, np.angle(He_best, deg=True), 'r--s', lw=1.8, ms=5, label='Modelo 1ª Ordem')
ax2.set_ylabel('Fase (graus)', fontsize=11)
ax2.set_xlabel('Frequência Angular $\\omega$ (rad/s)', fontsize=11)
ax2.grid(True, which='both', ls=':', alpha=0.6)
ax2.legend(loc='best', fontsize=10)

plt.tight_layout()
fig_path_mot_best = os.path.join(FIG_DIR, 'item5_motor_melhor_modelo_bode.png')
plt.savefig(fig_path_mot_best, dpi=300)
plt.close()
print(f"Figura salva: {fig_path_mot_best}")

# Validação com Onda Quadrada e Onda Triangular
sys_best = scipy.signal.TransferFunction(num_best, den_best)

# Onda Quadrada: sqrf1000a200
sqr_in_f = os.path.join(DATA_DIR, 'sqrf1000a200Ent.mat')
sqr_out_f = os.path.join(DATA_DIR, 'sqrf1000a200Sai.mat')
if os.path.exists(sqr_in_f) and os.path.exists(sqr_out_f):
    m_in = scipy.io.loadmat(sqr_in_f)
    m_out = scipy.io.loadmat(sqr_out_f)
    u_sqr = m_in['sqrf1000a200Ent_Value'][:, 0]
    t_sqr = m_in['sqrf1000a200Ent_Time'][:, 0]
    y_sqr_real = m_out['sqrf1000a200Sai_Value'][:, 1]

    n_p = min(len(u_sqr), len(t_sqr), len(y_sqr_real))
    t_sqr, u_sqr, y_sqr_real = t_sqr[:n_p], u_sqr[:n_p], y_sqr_real[:n_p]
    
    # Grid temporal perfeitamente uniforme para o lsim
    dt_sqr = (t_sqr[-1] - t_sqr[0]) / (n_p - 1)
    t_sqr_unif = t_sqr[0] + np.arange(n_p) * dt_sqr
    u_sqr_unif = np.interp(t_sqr_unif, t_sqr, u_sqr)
    _, y_sim_sqr, _ = scipy.signal.lsim(sys_best, U=u_sqr_unif, T=t_sqr_unif)

    plt.figure(figsize=(8, 4.5))
    plt.plot(t_sqr, y_sqr_real, 'k-', lw=1.8, label='Saída Real do Motor (Bancada)')
    plt.plot(t_sqr_unif, y_sim_sqr, 'r--', lw=1.8, label='Modelo Identificado (1ª Ordem N2CACGO)')
    plt.plot(t_sqr_unif, u_sqr_unif, 'b:', lw=1.2, label='Entrada (Onda Quadrada 10 Hz)')
    plt.xlabel('Tempo (s)', fontsize=11)
    plt.ylabel('Amplitude / Tensão (V)', fontsize=11)
    plt.title('Validação Dinâmica Temporal: Entrada de Onda Quadrada (10 Hz)', fontsize=12, fontweight='bold')
    plt.grid(True, ls=':', alpha=0.6)
    plt.legend(loc='best', fontsize=10)
    plt.xlim(7.0, 8.5)
    plt.tight_layout()
    fig_path_sqr = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_quadrada.png')
    plt.savefig(fig_path_sqr, dpi=300)
    plt.close()
    print(f"Figura salva: {fig_path_sqr}")

# Onda Triangular: trif1000a200
tri_in_f = os.path.join(DATA_DIR, 'trif1000a200Ent.mat')
tri_out_f = os.path.join(DATA_DIR, 'trif1000a200Sai.mat')
if os.path.exists(tri_in_f) and os.path.exists(tri_out_f):
    m_in = scipy.io.loadmat(tri_in_f)
    m_out = scipy.io.loadmat(tri_out_f)
    u_tri = m_in['trif1000a200Ent_Value'][:, 0]
    t_tri = m_in['trif1000a200Ent_Time'][:, 0]
    y_tri_real = m_out['trif1000a200Sai_Value'][:, 1]

    n_p = min(len(u_tri), len(t_tri), len(y_tri_real))
    t_tri, u_tri, y_tri_real = t_tri[:n_p], u_tri[:n_p], y_tri_real[:n_p]
    
    # Grid temporal perfeitamente uniforme para o lsim
    dt_tri = (t_tri[-1] - t_tri[0]) / (n_p - 1)
    t_tri_unif = t_tri[0] + np.arange(n_p) * dt_tri
    u_tri_unif = np.interp(t_tri_unif, t_tri, u_tri)
    _, y_sim_tri, _ = scipy.signal.lsim(sys_best, U=u_tri_unif, T=t_tri_unif)

    plt.figure(figsize=(8, 4.5))
    plt.plot(t_tri, y_tri_real, 'k-', lw=1.8, label='Saída Real do Motor (Bancada)')
    plt.plot(t_tri_unif, y_sim_tri, 'r--', lw=1.8, label='Modelo Identificado (1ª Ordem N2CACGO)')
    plt.plot(t_tri_unif, u_tri_unif, 'b:', lw=1.2, label='Entrada (Onda Triangular 10 Hz)')
    plt.xlabel('Tempo (s)', fontsize=11)
    plt.ylabel('Amplitude / Tensão (V)', fontsize=11)
    plt.title('Validação Dinâmica Temporal: Entrada de Onda Triangular (10 Hz)', fontsize=12, fontweight='bold')
    plt.grid(True, ls=':', alpha=0.6)
    plt.legend(loc='best', fontsize=10)
    plt.xlim(7.0, 8.5)
    plt.tight_layout()
    fig_path_tri = os.path.join(FIG_DIR, 'item5_motor_validacao_onda_triangular.png')
    plt.savefig(fig_path_tri, dpi=300)
    plt.close()
    print(f"Figura salva: {fig_path_tri}")

print("\n" + "=" * 70)
print(" EXECUÇÃO CONCLUÍDA! TODAS AS FIGURAS GERADAS COM SUCESSO.")
print("=" * 70)
