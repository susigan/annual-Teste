import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Análise de Dados de Atividades", layout="wide")
st.title("Dashboard de Treinamento")

# Função para carregar dados
@st.cache_data
def load_data(sheet_name):
    # Exemplo com pandas e Google Sheets API
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/10pefcY6VI4Z45M8Y69D6JxIoqOkjzSlSpV1PMLXoYlI/edit#gid=0")
    worksheet = sheet.worksheet(sheet_name)
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

# Função para plotar dados
def plot_activity(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Data'], data['RPE'])
    plt.title("RPE ao longo do tempo")
    plt.xlabel("Data")
    plt.ylabel("RPE")
    st.pyplot(plt)
    plt.close()

# Função para calcular esforço
def calculate_effort(data):
    data["Effort"] = data["RPE"] * data["Tempo(min)"]
    return data

# Carregar dados
data = load_data("Nome_da_Planilha")  # Substitua pelo nome da sua planilha

# Filtrar dados por ano
selected_years = st.multiselect("Selecione os anos:", [2022, 2023, 2024, 2025])
filtered_data = data[data["Data"].dt.year.isin(selected_years)]

# Exibir dados filtrados
st.write("Dados Filtrados:", filtered_data)

# Plotar gráfico
plot_activity(filtered_data)

# Calcular e exibir esforço
if st.button("Calcular Esforço"):
    effort_data = calculate_effort(filtered_data)
    st.write("Dados com Esforço Calculado:", effort_data)