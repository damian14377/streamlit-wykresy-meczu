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

    # Wykres 1: Dystans (km)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_filtered["Player Name"], df_filtered["Distance (km)"], color="blue")
    plt.ylabel("Dystans (km)")
    plt.suptitle(f"vs {session_title}", fontsize=18, fontweight='bold', y=1.05)
    plt.title("Dystans (km)", fontsize=14, pad=10)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.2f}", ha='center', va='bottom', fontsize=10)
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/dystans_{session_title}.png")
    plt.clf()

    # Wykres 2: Top Speed (km/h)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_filtered["Player Name"], df_filtered["Top Speed (km/h)"], color="red")
    plt.ylabel("Top Speed (km/h)")
    plt.suptitle(f"vs {session_title}", fontsize=18, fontweight='bold', y=1.05)
    plt.title("Top Speed (km/h)", fontsize=14, pad=10)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.2f}", ha='center', va='bottom', fontsize=10)
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/top_speed_{session_title}.png")
    plt.clf()

    # Wykres 3: Dystans na minutę (m/min)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_filtered["Player Name"], df_filtered["Distance Per Min (m/min)"], color="green")
    plt.ylabel("Dystans na minutę (m/min)")
    plt.suptitle(f"vs {session_title}", fontsize=18, fontweight='bold', y=1.05)
    plt.title("Dystans na minutę (m/min)", fontsize=14, pad=10)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{int(height)}", ha='center', va='bottom', fontsize=10)
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/dystans_na_minute_{session_title}.png")
    plt.clf()

    # Wykres 4: Przyspieszenia i hamowania (1-2 m/s²)
    plt.figure(figsize=(12, 6))
    bar_width = 0.4
    x = np.arange(len(df_filtered["Player Name"]))
    plt.bar(x - bar_width/2, df_filtered["Accelerations Zone Count: 1 - 2 m/s/s"], width=bar_width, label="Przyspieszenia (1-2 m/s²)", color="blue")
    plt.bar(x + bar_width/2, df_filtered["Deceleration Zone Count: 1 - 2 m/s/s"], width=bar_width, label="Hamowania (1-2 m/s²)", color="red")
    plt.xticks(x, df_filtered["Player Name"], rotation=45)
    plt.ylabel("Liczba przyspieszeń i hamowań")
    plt.suptitle(f"vs {session_title}", fontsize=18, fontweight='bold', y=1.05)
    plt.title("Przyspieszenia i hamowania (1-2 m/s²)", fontsize=14, pad=10)
    for i, (acc, dec) in enumerate(zip(df_filtered["Accelerations Zone Count: 1 - 2 m/s/s"], df_filtered["Deceleration Zone Count: 1 - 2 m/s/s"])):
        plt.text(i - bar_width/2, acc, f"{int(acc)}", ha='center', va='bottom', fontsize=10)
        plt.text(i + bar_width/2, dec, f"{int(dec)}", ha='center', va='bottom', fontsize=10)
    plt.grid(axis="y")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_folder}/przyspieszenia_i_hamowania_{session_title}.png")
    plt.clf()

    # Wykres 5: Dystans w strefach prędkości 4 i 5 (m)
    plt.figure(figsize=(12, 6))
    bar_width = 0.4
    x = np.arange(len(df_filtered["Player Name"]))
    plt.bar(x - bar_width/2, df_filtered["Distance in Speed Zone 4  (km)"] * 1000, width=bar_width, label="High Speed Running (m)", color="blue")  # Przeliczone na metry
    plt.bar(x + bar_width/2, df_filtered["Distance in Speed Zone 5  (km)"] * 1000, width=bar_width, label="Sprint (m)", color="red")  # Przeliczone na metry
    plt.xticks(x, df_filtered["Player Name"], rotation=45)
    plt.ylabel("Dystans w strefach prędkości (m)")
    plt.suptitle(f"vs {session_title}", fontsize=18, fontweight='bold', y=1.05)
    plt.title("Dystans w strefach prędkości 4 (High Speed Running) i 5 (Sprint) (m)", fontsize=14, pad=10)
    for i, (zone4, zone5) in enumerate(zip(df_filtered["Distance in Speed Zone 4  (km)"], df_filtered["Distance in Speed Zone 5  (km)"])):
        plt.text(i - bar_width/2, zone4 * 1000, f"{int(zone4 * 1000)}", ha='center', va='bottom', fontsize=10)
        plt.text(i + bar_width/2, zone5 * 1000, f"{int(zone5 * 1000)}", ha='center', va='bottom', fontsize=10)
    plt.grid(axis="y")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_folder}/strefy_predkosci_4_5_{session_title}.png")
    plt.clf()

    print(f"Wykresy zostały zapisane w folderze: {output_folder}")
