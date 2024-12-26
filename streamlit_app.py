import streamlit as st

st.set_page_config(page_title="Análise de Dados de Atividades", layout="wide")
st.title("Dashboard de Treinamento")


import pandas as pd

@st.cache
def load_data(sheet_name):
    # Exemplo com pandas e Google Sheets API
    url = "https://docs.google.com/spreadsheets/d/10pefcY6VI4Z45M8Y69D6JxIoqOkjzSlSpV1PMLXoYlI/edit?gid=0#gid=0A"
    return pd.read_excel(url, sheet_name=sheet_name)

import matplotlib.pyplot as plt

def plot_activity(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Data'], data['RPE'])
    plt.title("RPE ao longo do tempo")
    plt.xlabel("Data")
    plt.ylabel("RPE")
    st.pyplot(plt)

def calculate_effort(data):
    data["Effort"] = data["RPE"] * data["Tempo(min)"]
    return data

selected_years = st.multiselect("Selecione os anos:", [2022, 2023, 2024, 2025])
filtered_data = data[data["Data"].dt.year.isin(selected_years)]

