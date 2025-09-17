import os

def renomeia_arquivo():

    # Caminho da pasta onde estão os arquivos
    pasta = r"J:\Repositorio_QLIK\APEX\ROBO_DUMP_PF"

    # Lista todos os arquivos .xlsx, excluindo 'dump_apex.xlsx'
    arquivos_xlsx = [
        f for f in os.listdir(pasta)
        if f.endswith(".xlsx") and f != "dump_apex.xlsx"
    ]

    # Renomeia cada arquivo encontrado
    for i, nome_antigo in enumerate(arquivos_xlsx, start=1):
        caminho_antigo = os.path.join(pasta, nome_antigo)
        novo_nome = f"dump_apex.xlsx"  # ou qualquer lógica que você quiser
        caminho_novo = os.path.join(pasta, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_antigo} → {novo_nome}")
