import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_charts(file_path, output_folder="output"):
    # Wczytanie pliku
    df = pd.read_csv(file_path)

    # Filtrowanie danych dla Split Name = Game
    df_filtered = df[df["Split Name"].str.lower() == "game"]

    # Sprawdzenie tytułu sesji
    session_title = df_filtered["Session Title"].iloc[0]

    # Utworzenie folderu output z nazwą session_title
    os.makedirs(output_folder, exist_ok=True)

    # --- Dystans (km) ---
    # Posortowanie danych
    df_sorted = df_filtered.sort_values(by="Distance (km)", ascending=False)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_sorted["Player Name"], df_sorted["Distance (km)"], color="blue")
    plt.ylabel("Dystans (km)")
    plt.title(f"vs {session_title}", fontsize=18, fontweight='bold')
    plt.figtext(0.5, 0.95, "Dystans (km)", ha='center', fontsize=14, weight='bold', color='black')  # Subtitle jako figtext
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.2f}", ha='center', va='bottom', fontsize=10)
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/dystans_{session_title}.png", dpi=600)
    plt.clf()

    # --- Top Speed (km/h) ---
    df_sorted_speed = df_filtered.sort_values(by="Top Speed (km/h)", ascending=False)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_sorted_speed["Player Name"], df_sorted_speed["Top Speed (km/h)"], color="red")
    plt.ylabel("Top Speed (km/h)")
    plt.title(f"vs {session_title}", fontsize=18, fontweight='bold')
    plt.figtext(0.5, 0.95, "Top Speed (km/h)", ha='center', fontsize=14, weight='bold', color='black')  # Subtitle jako figtext
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.2f}", ha='center', va='bottom', fontsize=10)
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/top_speed_{session_title}.png", dpi=600)
    plt.clf()

    # --- Dystans na minutę (m/min) ---
    df_sorted_dpm = df_filtered.sort_values(by="Distance Per Min (m/min)", ascending=False)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_sorted_dpm["Player Name"], df_sorted_dpm["Distance Per Min (m/min)"], color="green")
    plt.ylabel("Dystans na minutę (m/min)")
    plt.title(f"vs {session_title}", fontsize=18, fontweight='bold')
    plt.figtext(0.5, 0.95, "Dystans na minutę (m/min)", ha='center', fontsize=14, weight='bold', color='black')  # Subtitle jako figtext
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{int(height)}", ha='center', va='bottom', fontsize=10)
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/dystans_na_minute_{session_title}.png", dpi=600)
    plt.clf()

    # --- Przyspieszenia i hamowania (1-2 m/s²) ---
    df_sorted_acc_dec = df_filtered.sort_values(by=["Accelerations Zone Count: 1 - 2 m/s/s", "Deceleration Zone Count: 1 - 2 m/s/s"], ascending=False)
    plt.figure(figsize=(12, 6))
    bar_width = 0.4
    x = np.arange(len(df_sorted_acc_dec["Player Name"]))
    plt.bar(x - bar_width/2, df_sorted_acc_dec["Accelerations Zone Count: 1 - 2 m/s/s"], width=bar_width, label="Przyspieszenia (1-2 m/s²)", color="blue")
    plt.bar(x + bar_width/2, df_sorted_acc_dec["Deceleration Zone Count: 1 - 2 m/s/s"], width=bar_width, label="Hamowania (1-2 m/s²)", color="red")
    plt.xticks(x, df_sorted_acc_dec["Player Name"], rotation=45)
    plt.ylabel("Liczba przyspieszeń i hamowań")
    plt.title(f"vs {session_title}", fontsize=18, fontweight='bold')
    plt.figtext(0.5, 0.95, "Przyspieszenia i hamowania (1-2 m/s²)", ha='center', fontsize=14, weight='bold', color='black')  # Subtitle jako figtext
    for i, (acc, dec) in enumerate(zip(df_sorted_acc_dec["Accelerations Zone Count: 1 - 2 m/s/s"], df_sorted_acc_dec["Deceleration Zone Count: 1 - 2 m/s/s"])):
        plt.text(i - bar_width/2, acc, f"{int(acc)}", ha='center', va='bottom', fontsize=10)
        plt.text(i + bar_width/2, dec, f"{int(dec)}", ha='center', va='bottom', fontsize=10)
    plt.grid(axis="y")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_folder}/przyspieszenia_i_hamowania_{session_title}.png", dpi=600)
    plt.clf()

    # --- Dystans w strefach prędkości 4 i 5 (m) ---
    df_sorted_speed_zones = df_filtered.sort_values(by=["Distance in Speed Zone 4  (km)", "Distance in Speed Zone 5  (km)"], ascending=False)
    plt.figure(figsize=(12, 6))
    bar_width = 0.4
    x = np.arange(len(df_sorted_speed_zones["Player Name"]))
    plt.bar(x - bar_width/2, df_sorted_speed_zones["Distance in Speed Zone 4  (km)"] * 1000, width=bar_width, label="High Speed Running (m)", color="blue")  # Przeliczone na metry
    plt.bar(x + bar_width/2, df_sorted_speed_zones["Distance in Speed Zone 5  (km)"] * 1000, width=bar_width, label="Sprint (m)", color="red")  # Przeliczone na metry
    plt.xticks(x, df_sorted_speed_zones["Player Name"], rotation=45)
    plt.ylabel("Dystans w strefach prędkości (m)")
    plt.title(f"vs {session_title}", fontsize=18, fontweight='bold')
    plt.figtext(0.5, 0.95, "Dystans w strefach prędkości 4 (High Speed Running) i 5 (Sprint) (m)", ha='center', fontsize=14, weight='bold', color='black')  # Subtitle jako figtext
    for i, (zone4, zone5) in enumerate(zip(df_sorted_speed_zones["Distance in Speed Zone 4  (km)"], df_sorted_speed_zones["Distance in Speed Zone 5  (km)"])):
        plt.text(i - bar_width/2, zone4 * 1000, f"{int(zone4 * 1000)}", ha='center', va='bottom', fontsize=10)
        plt.text(i + bar_width/2, zone5 * 1000, f"{int(zone5 * 1000)}", ha='center', va='bottom', fontsize=10)
    plt.grid(axis="y")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_folder}/strefy_predkosci_4_5_{session_title}.png", dpi=600)
    plt.clf()

    print(f"Wykresy zostały zapisane w folderze: {output_folder}")

# Wywołanie funkcji
file_path = "path_to_your_csv_file.csv"  # Wstaw ścieżkę do pliku CSV
output_folder = "output_folder_path"  # Wstaw ścieżkę do folderu, w którym chcesz zapisać wykresy
generate_charts(file_path, output_folder)
