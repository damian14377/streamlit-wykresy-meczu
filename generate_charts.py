import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_high_quality_charts(file_path, output_folder="output"):
    # Wczytanie pliku
    df = pd.read_csv(file_path)

    # Filtrowanie danych dla Split Name = Game
    df_filtered = df[df["Split Name"].str.lower() == "game"]

    # Sprawdzenie tytułu sesji
    session_title = df_filtered["Session Title"].iloc[0]

    # Utworzenie folderu output z nazwą session_title
    os.makedirs(output_folder, exist_ok=True)

    # --- 1. Dystans (km) ---
    df_sorted = df_filtered.sort_values(by="Distance (km)", ascending=False)
    plt.figure(figsize=(16, 10))  # Większy rozmiar wykresu
    bars = plt.bar(df_sorted["Player Name"], df_sorted["Distance (km)"], color="blue")
    plt.ylabel("Dystans (km)", fontsize=16)
    plt.suptitle(f"vs {session_title}", fontsize=22, fontweight='bold', y=1.05)
    plt.title("Dystans (km)", fontsize=18, pad=10)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.2f}", ha='center', va='bottom', fontsize=12)
    plt.xticks(rotation=45, fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(axis="y", linestyle='--', alpha=0.7)
    plt.tight_layout(pad=4.0)  # Dodanie przestrzeni wokół wykresu
    plt.savefig(f"{output_folder}/dystans_{session_title}.png", dpi=300)  # Zapis w wysokiej jakości
    plt.clf()

    # --- 2. Top Speed (km/h) ---
    df_sorted_speed = df_filtered.sort_values(by="Top Speed (km/h)", ascending=False)
    plt.figure(figsize=(16, 10))  # Większy rozmiar wykresu
    bars = plt.bar(df_sorted_speed["Player Name"], df_sorted_speed["Top Speed (km/h)"], color="red")
    plt.ylabel("Top Speed (km/h)", fontsize=16)
    plt.suptitle(f"vs {session_title}", fontsize=22, fontweight='bold', y=1.05)  # Ustawienie subtitle
    plt.title("Top Speed (km/h)", fontsize=18, pad=10)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.2f}", ha='center', va='bottom', fontsize=12)
    plt.xticks(rotation=45, fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(axis="y", linestyle='--', alpha=0.7)
    plt.tight_layout(pad=4.0)  # Dodanie przestrzeni wokół wykresu
    plt.savefig(f"{output_folder}/top_speed_{session_title}.png", dpi=300)  # Zapis w wysokiej jakości
    plt.clf()

    # --- 3. Dystans na minutę (m/min) ---
    df_sorted_dpm = df_filtered.sort_values(by="Distance Per Min (m/min)", ascending=False)
    plt.figure(figsize=(16, 10))  # Większy rozmiar wykresu
    bars = plt.bar(df_sorted_dpm["Player Name"], df_sorted_dpm["Distance Per Min (m/min)"], color="green")
    plt.ylabel("Dystans na minutę (m/min)", fontsize=16)
    plt.suptitle(f"vs {session_title}", fontsize=22, fontweight='bold', y=1.05)  # Ustawienie subtitle
    plt.title("Dystans na minutę (m/min)", fontsize=18, pad=10)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{int(height)}", ha='center', va='bottom', fontsize=12)
    plt.xticks(rotation=45, fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(axis="y", linestyle='--', alpha=0.7)
    plt.tight_layout(pad=4.0)  # Dodanie przestrzeni wokół wykresu
    plt.savefig(f"{output_folder}/dystans_na_minute_{session_title}.png", dpi=300)  # Zapis w wysokiej jakości
    plt.clf()

    # --- 4. Przyspieszenia i hamowania (1-2 m/s²) ---
    df_sorted_acc_dec = df_filtered.sort_values(by=["Accelerations Zone Count: 1 - 2 m/s/s", "Deceleration Zone Count: 1 - 2 m/s/s"], ascending=False)
    plt.figure(figsize=(16, 10))  # Większy rozmiar wykresu
    bar_width = 0.4
    x = np.arange(len(df_sorted_acc_dec["Player Name"]))
    plt.bar(x - bar_width/2, df_sorted_acc_dec["Accelerations Zone Count: 1 - 2 m/s/s"], width=bar_width, label="Przyspieszenia (1-2 m/s²)", color="blue")
    plt.bar(x + bar_width/2, df_sorted_acc_dec["Deceleration Zone Count: 1 - 2 m/s/s"], width=bar_width, label="Hamowania (1-2 m/s²)", color="red")
    plt.xticks(x, df_sorted_acc_dec["Player Name"], rotation=45, fontsize=14)
    plt.ylabel("Liczba przyspieszeń i hamowań", fontsize=16)
    plt.suptitle(f"vs {session_title}", fontsize=22, fontweight='bold', y=1.05)  # Ustawienie subtitle
    plt.title("Przyspieszenia i hamowania (1-2 m/s²)", fontsize=18, pad=10)
    for i, (acc, dec) in enumerate(zip(df_sorted_acc_dec["Accelerations Zone Count: 1 - 2 m/s/s"], df_sorted_acc_dec["Deceleration Zone Count: 1 - 2 m/s/s"])):
        plt.text(i - bar_width/2, acc, f"{int(acc)}", ha='center', va='bottom', fontsize=12)
        plt.text(i + bar_width/2, dec, f"{int(dec)}", ha='center', va='bottom', fontsize=12)
    plt.grid(axis="y", linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout(pad=4.0)  # Dodanie przestrzeni wokół wykresu
    plt.savefig(f"{output_folder}/przyspieszenia_i_hamowania_{session_title}.png", dpi=300)  # Zapis w wysokiej jakości
    plt.clf()

    # --- 5. Dystans w strefach prędkości 4 i 5 (m) ---
    df_sorted_speed_zones = df_filtered.sort_values(by=["Distance in Speed Zone 4  (km)", "Distance in Speed Zone 5  (km)"], ascending=False)
    plt.figure(figsize=(16, 10))  # Większy rozmiar wykresu
    bar_width = 0.4
    x = np.arange(len(df_sorted_speed_zones["Player Name"]))
    plt.bar(x - bar_width/2, df_sorted_speed_zones["Distance in Speed Zone 4  (km)"] * 1000, width=bar_width, label="High Speed Running (m)", color="blue")  # Przeliczone na metry
    plt.bar(x + bar_width/2, df_sorted_speed_zones["Distance in Speed Zone 5  (km)"] * 1000, width=bar_width, label="Sprint (m)", color="red")  # Przeliczone na metry
    plt.xticks(x, df_sorted_speed_zones["Player Name"], rotation=45, fontsize=14)
    plt.ylabel("Dystans w strefach prędkości (m)", fontsize=16)
    plt.suptitle(f"vs {session_title}", fontsize=22, fontweight='bold', y=1.05)  # Ustawienie subtitle
    plt.title("Dystans w strefach prędkości 4 (High Speed Running) i 5 (Sprint) (m)", fontsize=18, pad=10)
    for i, (zone4, zone5) in enumerate(zip(df_sorted_speed_zones["Distance in Speed Zone 4  (km)"], df_sorted_speed_zones["Distance in Speed Zone 5  (km)"])):
        plt.text(i - bar_width/2, zone4 * 1000, f"{int(zone4 * 1000)}", ha='center', va='bottom', fontsize=12)
        plt.text(i + bar_width/2, zone5 * 1000, f"{int(zone5 * 1000)}", ha='center', va='bottom', fontsize=12)
    plt.grid(axis="y", linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout(pad=4.0)  # Dodanie przestrzeni wokół wykresu
    plt.savefig(f"{output_folder}/strefy_predkosci_4_5_{session_title}.png", dpi=300)  # Zapis w wysokiej jakości
    plt.savefig(f"{output_folder}/strefy_predkosci_4_5_{session_title}.pdf")  # Zapis w formacie PDF (wektorowy)
    plt.clf()

    return output_folder

# Wywołanie funkcji (po załadowaniu pliku)
output_folder = generate_high_quality_charts(file_path, output_folder)
output_folder
