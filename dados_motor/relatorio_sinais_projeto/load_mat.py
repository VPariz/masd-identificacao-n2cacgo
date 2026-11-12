from pathlib import Path

import pandas as pd
import scipy.io


def convert_mat_to_csv(origin, destine, title):
    # 1. Carregar o arquivo .mat
    mat_data = scipy.io.loadmat(origin)

    # Nota: Arquivos .mat contêm metadados. Para ver o nome real da
    # variável que guarda os seus dados, você pode listar as chaves:
    print(
        "Variáveis disponíveis:", [k for k in mat_data.keys() if not k.startswith("__")]
    )
    variables = [k for k in mat_data.keys() if not k.startswith("__")]

    # 2. Substitua 'nome_da_sua_variavel' pelo nome encontrado acima
    time = mat_data[f"{str(variables[0])}"].flatten()
    value = mat_data[f"{str(variables[1])}"].flatten()

    # 3. Converter para DataFrame e salvar em CSV
    df = pd.DataFrame({"Time": time, "Value": value})

    df.to_csv(f"{destine}/{title}.csv", index=False)

    print("Conversão concluída com sucesso!")


def list_mat_names(path):
    list_names = []
    list_arqv = []
    for arqv in path.glob("*.mat"):
        if arqv.is_file():
            name_without_ext = arqv.stem
            list_names.append(name_without_ext)
            convert_mat_to_csv(str(arqv), str(arqv.parent), name_without_ext)
        list_arqv.append(arqv)
    return list_arqv, list_names


def main():
    sen = Path("./data/sen/")
    quad = Path("./data/quad/")
    trig = Path("./data/trig/")

    sen_arqv, sen_names = list_mat_names(sen)
    quad_arqv, quad_names = list_mat_names(quad)
    trig_arqv, trig_names = list_mat_names(trig)
    print("Processo concluido")


if __name__ == "__main__":
    main()
