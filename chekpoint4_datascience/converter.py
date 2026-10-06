
import pandas as pd

arquivo = "Dados_abertos_Consumo_Mensal.xlsx"

colunas = [
    "Data", "DataExcel", "Regiao", "Sistema",
    "Classe", "TipoConsumidor", "Consumo",
    "Consumidores", "DataVersao"
]

# A primeira aba é a única permitida.
df = pd.read_excel(
    arquivo,
    sheet_name=0
)

if df.columns.tolist() != colunas:
    raise ValueError(
        f"Colunas inesperadas: {df.columns.tolist()}"
    )

# Conferir campos numéricos antes da exportação.
for campo in ["Data", "DataExcel", "Consumo",
              "Consumidores", "DataVersao"]:
    df[campo] = pd.to_numeric(
        df[campo], errors="raise"
    )

# Data permanece como inteiro AAAAMMDD.
df["Data"] = df["Data"].astype("int64")

if df["Data"].isna().any():
    raise ValueError("Datas ausentes encontradas.")

# Exportar com ponto decimal, UTF-8 e vírgula.
nome_saida = "Joao_Vitor_Xavier_de_Carvalho.csv"

df.to_csv(
    nome_saida,
    index=False,
    encoding="utf-8-sig",
    sep=",",
    decimal="."
)

print("Total de registros:", len(df))
print("Data mais recente:", df["Data"].max())
print("\nAmostra:")
print(df.head(10).to_string(index=False))
