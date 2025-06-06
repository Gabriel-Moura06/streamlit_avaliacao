import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar e limpar os dados
@st.cache_data
def load_data():
    df = pd.read_csv("MS_Financial Sample.csv", sep=";", engine="python")
    df.columns = df.columns.str.strip()

    cols_to_clean = [
        "Units Sold", "Manufacturing Price", "Sale Price", "Gross Sales",
        "Discounts", "Sales", "COGS", "Profit"
    ]

    def clean_column(col):
        return (
            df[col]
            .astype(str)
            .str.replace(r"\((.*?)\)", r"-\1", regex=True)
            .str.replace("$", "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.strip()
            .replace("-", "0")
            .astype(float)
        )

    for col in cols_to_clean:
        df[col] = clean_column(col)

    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    return df

df = load_data()

st.title("📊 Dashboard Financeiro")

# Gráfico 1: Lucro por país
st.subheader("Lucro total por país")
profit_by_country = df.groupby("Country")["Profit"].sum().sort_values(ascending=False)
st.bar_chart(profit_by_country)

# Gráfico 2: Lucro ao longo do tempo
st.subheader("Lucro ao longo do tempo")
profit_over_time = df.groupby("Date")["Profit"].sum().reset_index()
st.line_chart(profit_over_time.rename(columns={"Date": "index"}).set_index("index"))
