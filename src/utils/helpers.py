import os
import glob
import time

def limpa_e_renomeia():
    pasta = r"J:\Repositorio_QLIK\APEX\ROBO_DUMP_PF"
    destino_instr = os.path.join(pasta, "instrumentos.xlsx")
    destino_pf = os.path.join(pasta, "pf.xlsx")

    # 1. Remove todos os arquivos .xlsx da pasta
    arquivos_antigos = glob.glob(os.path.join(pasta, "*.xlsx"))
    for arquivo in arquivos_antigos:
        try:
            os.chmod(arquivo, 0o777)  # Garante permissão
            os.remove(arquivo)
            print(f"Removido: {os.path.basename(arquivo)}")
        except Exception as e:
            print(f"Erro ao remover {arquivo}: {e}")

    print("🧹 Pasta limpa meu patrão. Aguarde os novos arquivos serem baixados...")

    # 2. Aguarda até que dois novos arquivos sejam baixados
    timeout = 60  # segundos
    intervalo = 2
    tempo_passado = 0

    while tempo_passado < timeout:
        arquivos_novos = glob.glob(os.path.join(pasta, "*.xlsx"))
        if len(arquivos_novos) >= 2:
            break
        time.sleep(intervalo)
        tempo_passado += intervalo

    if len(arquivos_novos) < 2:
        print("⏳ Timeout: Deu chabu.")
        return

    # 3. Renomeia os dois mais recentes
    arquivos_novos = sorted(arquivos_novos, key=os.path.getmtime, reverse=True)

    try:
        os.rename(arquivos_novos[0], destino_instr)
        os.rename(arquivos_novos[1], destino_pf)
        print("✅ Renomeados com sucesso para 'instrumentos.xlsx' e 'pf.xlsx'.")
    except Exception as e:
        print(f"Erro ao renomear: {e}")
