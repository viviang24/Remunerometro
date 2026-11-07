import pandas as pd
from pathlib import Path

arquivo = Path(r"C:\Dados\RAIS\RAIS_VINC_PUB_NORDESTE.COMT")
saida = Path("data/processed/base_analitica_pb.csv")
saida.parent.mkdir(parents=True, exist_ok=True)

colunas = [
    "Município - Código",
    "Ind Vínculo Ativo 31/12 - Código",
    "Vl Rem Dezembro Nom",
    "Idade",
    "Escolaridade Após 2005 - Código",
    "CBO 2002 Ocupação - Código",
    "Sexo - Código"
]

if saida.exists():
    saida.unlink()

total = 0
primeiro_bloco = True

for bloco in pd.read_csv(
    arquivo,
    encoding="cp1252",
    usecols=colunas,
    dtype=str,
    chunksize=200_000
):
    municipio = bloco["Município - Código"].fillna("").str.strip()
    ativo = bloco["Ind Vínculo Ativo 31/12 - Código"].fillna("").str.strip()
    salario = pd.to_numeric(bloco["Vl Rem Dezembro Nom"], errors="coerce")

    filtro = municipio.str.startswith("25") & ativo.eq("1") & salario.gt(0)

    dados = bloco.loc[filtro, [
        "Idade",
        "Escolaridade Após 2005 - Código",
        "CBO 2002 Ocupação - Código",
        "Município - Código",
        "Sexo - Código"
    ]].copy()

    dados["Remuneracao"] = salario.loc[filtro]

    dados.to_csv(
        saida,
        index=False,
        mode="w" if primeiro_bloco else "a",
        header=primeiro_bloco,
        encoding="utf-8"
    )

    total += len(dados)
    primeiro_bloco = False

    print(f"Registros processados e salvos: {total:,}".replace(",", "."))

print("\nBASE ANALÍTICA CRIADA")
print("Arquivo:", saida.resolve())
print("Total de registros:", f"{total:,}".replace(",", "."))
print("Total de colunas:", len(colunas) - 2 + 1)
