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
    
    # Generowanie wykresów
    session_title = uploaded_file.name.split('.')[0]  # Przyjmujemy nazwę pliku jako Session Title
    output_folder = os.path.join("output", session_title)
    os.makedirs(output_folder, exist_ok=True)

    # Przekazanie do funkcji generującej wykresy
    generate_charts(file_path, output_folder)

    st.success(f"Wykresy zostały zapisane w folderze '{output_folder}'.")

    # Pobieranie wykresów z folderu
    for file_name in os.listdir(output_folder):
        if file_name.endswith(".png"):
            file_path = os.path.join(output_folder, file_name)
            
            # Dodanie przycisku do pobrania pliku
            with open(file_path, "rb") as f:
                st.download_button(
                    label=f"Pobierz wykres: {file_name}",
                    data=f,
                    file_name=file_name,
                    mime="image/png"
                )
