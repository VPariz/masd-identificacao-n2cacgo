import os
import subprocess

BASE_DIR = r"c:\Users\jvpar\estudo\3.2\MASD\trabalho_identificacao"
FIG_DIR = os.path.join(BASE_DIR, "artigo", "figuras")
PRES_ID = "1_Sr_WVNnsS-IkV3xVQcYDCkbzBw24G0Q9dqB1BGLlKY"

images_to_insert = [
    # Slide 5: Fluxograma
    {
        "slide": "slide_1794529720825667300_42",
        "file": os.path.join(FIG_DIR, "fluxograma_matlab_simulink.png"),
        "x": 40, "y": 78, "w": 640, "h": 315
    },
    # Slide 6: Simulink diag + Sinais
    {
        "slide": "slide_1794529720825667300_50",
        "file": os.path.join(FIG_DIR, "simulink_diagrama_blocos.png"),
        "x": 30, "y": 80, "w": 330, "h": 150
    },
    {
        "slide": "slide_1794529720825667300_50",
        "file": os.path.join(FIG_DIR, "item4_simulink_sinais_temporais.png"),
        "x": 380, "y": 80, "w": 310, "h": 305
    },
    # Slide 7: Silveira Bode
    {
        "slide": "slide_1794529720825667300_61",
        "file": os.path.join(FIG_DIR, "item3_exemplo_silveira_bode.png"),
        "x": 400, "y": 80, "w": 290, "h": 305
    },
    # Slide 8: FFT Bode
    {
        "slide": "slide_1794529720825667300_72",
        "file": os.path.join(FIG_DIR, "item4_simulink_bode_validacao.png"),
        "x": 380, "y": 80, "w": 310, "h": 305
    },
    # Slide 10: Motor todas ordens
    {
        "slide": "slide_1794529720825667300_97",
        "file": os.path.join(FIG_DIR, "item5_motor_bode_todas_ordens.png"),
        "x": 380, "y": 80, "w": 310, "h": 305
    },
    # Slide 11: Motor melhor modelo
    {
        "slide": "slide_1794529720825667300_108",
        "file": os.path.join(FIG_DIR, "item5_motor_melhor_modelo_bode.png"),
        "x": 380, "y": 80, "w": 310, "h": 305
    },
    # Slide 12: Validação Onda Quadrada + Triangular
    {
        "slide": "slide_1794529720825667300_119",
        "file": os.path.join(FIG_DIR, "item5_motor_validacao_onda_quadrada.png"),
        "x": 30, "y": 80, "w": 320, "h": 210
    },
    {
        "slide": "slide_1794529720825667300_119",
        "file": os.path.join(FIG_DIR, "item5_motor_validacao_onda_triangular.png"),
        "x": 370, "y": 80, "w": 320, "h": 210
    }
]

for idx, img in enumerate(images_to_insert):
    cmd = [
        "gslides", "mutate", "insert-image-from-file", PRES_ID,
        "--slide", img["slide"],
        "--file", img["file"],
        "--x", str(img["x"]),
        "--y", str(img["y"]),
        "--width", str(img["w"]),
        "--height", str(img["h"])
    ]
    print(f"[{idx+1}/{len(images_to_insert)}] Inserting {os.path.basename(img['file'])} into {img['slide']}...")
    res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if res.returncode != 0:
        print(f"Error: {res.stderr}")
    else:
        print("Success:", res.stdout.strip())

print("All images inserted into Google Slides!")
