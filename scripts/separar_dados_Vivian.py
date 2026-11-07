import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path

# ==================================================
# 0. IDENTIFICAÇÃO E SEMENTE
# ==================================================

NOME = "Vivian"
MATRICULA = "20240045345"
SEMENTE = int(MATRICULA[-6:])  # 045345 -> 45345

SEMENTE_PARTICAO = 42  # Semente fixa para a separação treino-teste

# ==================================================
# 1. LEITURA DA BASE ANALÍTICA
# ==================================================

arquivo = Path("data/processed/base_analitica_pb.csv")
pasta_saida = Path("data/processed")
pasta_saida.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(arquivo)

# Sexo será preservado para avaliação por grupo,
# mas não será utilizado como preditor.
colunas_preditoras = [
    "Idade",
    "Escolaridade Após 2005 - Código",
    "CBO 2002 Ocupação - Código",
    "Município - Código"
]

X = df[colunas_preditoras]
y = df["Remuneracao"]

# ==================================================
# 2. PARTIÇÃO TREINO-TESTE
# ==================================================

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=SEMENTE_PARTICAO
)

# Preservar sexo para avaliação posterior por grupo
sexo_treino = df.loc[X_treino.index, "Sexo - Código"]
sexo_teste = df.loc[X_teste.index, "Sexo - Código"]

treino_completo = X_treino.copy()
treino_completo["Remuneracao"] = y_treino
treino_completo["Sexo - Código"] = sexo_treino

teste = X_teste.copy()
teste["Remuneracao"] = y_teste
teste["Sexo - Código"] = sexo_teste

# ==================================================
# 3. AMOSTRA INDIVIDUAL DE 2.000 VÍNCULOS
# ==================================================

Dtreino = treino_completo.sample(
    n=2000,
    random_state=SEMENTE
)

# ==================================================
# 4. SALVAMENTO
# ==================================================

arquivo_amostra = pasta_saida / "Dtreino_Vivian.csv"
arquivo_teste = pasta_saida / "teste_reservado_Vivian.csv"

Dtreino.to_csv(arquivo_amostra, index=False)
teste.to_csv(arquivo_teste, index=False)

# ==================================================
# 5. CONFERÊNCIA
# ==================================================

print("\nPARTIÇÃO E AMOSTRA CONCLUÍDAS")
print("Estudante:", NOME)
print("Matrícula:", MATRICULA)
print("Semente individual:", MATRICULA[-6:])
print("Semente numérica utilizada:", SEMENTE)

print("\nPARTIÇÃO ORIGINAL")
print("Base completa:", len(df))
print("Treino disponível:", len(treino_completo))
print("Teste reservado:", len(teste))

print("\nAMOSTRA INDIVIDUAL")
print("Dtreino:", len(Dtreino))
print("Preditores antes do One-Hot:", len(colunas_preditoras))
print("Variável-alvo: Remuneracao")
print("Sexo reservado para avaliação por grupo")

print("\nARQUIVOS")
print(arquivo_amostra.resolve())
print(arquivo_teste.resolve())
