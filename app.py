import streamlit as st
import os
from generate_charts import generate_charts

# Tytuł aplikacji
st.title('Automatyczne Generowanie Wykresów')

# Opcja wgrania pliku
uploaded_file = st.file_uploader("Wgraj plik CSV", type=["csv"])

if uploaded_file is not None:
    # Zapisanie pliku w folderze data
    data_path = "data"
    os.makedirs(data_path, exist_ok=True)
    file_path = os.path.join(data_path, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Generowanie wykresów
    st.write("Generowanie wykresów...")
    generate_charts(file_path)

    st.success(f"Wykresy zostały zapisane w folderze 'output'.")
