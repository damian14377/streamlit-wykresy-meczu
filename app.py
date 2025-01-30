import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 📌 Konfiguracja strony
st.set_page_config(page_title="Analiza Meczu", layout="wide")

# 📌 Nagłówek aplikacji
st.title("📊 Analiza Danych GPS – Wykresy Klubowe")
st.write("Wgraj plik CSV, aby automatycznie wygenerować wykresy.")

# 📌 Wgraj plik CSV
uploaded_file = st.file_uploader("Prześlij plik CSV", type=["csv"])

# 📌 Jeśli plik został przesłany
if uploaded_file is not None:
    # Wczytaj dane
    data = pd.read_csv(uploaded_file)

    # Pobierz tytuł sesji
    session_title = data["Session Title"].iloc[0] if "Session Title" in data.columns else "Sesja"

    # 📊 1. Przyspieszenia i hamowania (1-2 m/s²)
    acc_dec_columns = ['Accelerations Zone Count: 1 - 2 m/s/s', 'Deceleration Zone Count: 1 - 2 m/s/s']
    filtered_acc_dec_data = data[['Player Name'] + acc_dec_columns].copy()
    filtered_acc_dec_data['Total Counts'] = (
        filtered_acc_dec_data['Accelerations Zone Count: 1 - 2 m/s/s'] +
        filtered_acc_dec_data['Deceleration Zone Count: 1 - 2 m/s/s']
    )
    sorted_acc_dec_data = filtered_acc_dec_data.sort_values(by='Total Counts', ascending=False)

    # Tworzenie wykresu
    st.subheader(f"📊 vs {session_title} – Przyspieszenia i hamowania (1-2 m/s²)")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sorted_acc_dec_data['Player Name'], sorted_acc_dec_data['Accelerations Zone Count: 1 - 2 m/s/s'], label="Przyspieszenia", color="blue")
    ax.bar(sorted_acc_dec_data['Player Name'], sorted_acc_dec_data['Deceleration Zone Count: 1 - 2 m/s/s'], bottom=sorted_acc_dec_data['Accelerations Zone Count: 1 - 2 m/s/s'], label="Hamowania", color="orange")
    ax.set_xlabel("Zawodnik")
    ax.set_ylabel("Liczba")
    ax.set_xticklabels(sorted_acc_dec_data['Player Name'], rotation=45)
    ax.legend()
    st.pyplot(fig)

    # 📊 2. Dystans całkowity (km)
    st.subheader(f"📊 vs {session_title} – Dystans całkowity (km)")
    sorted_total_distance = data.sort_values(by='Distance (km)', ascending=False)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sorted_total_distance['Player Name'], sorted_total_distance['Distance (km)'], color="blue")
    ax.set_xlabel("Zawodnik")
    ax.set_ylabel("Dystans (km)")
    ax.set_xticklabels(sorted_total_distance['Player Name'], rotation=45)
    st.pyplot(fig)
