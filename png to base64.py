import base64
import os
import pandas as pd

# === CONFIGURAZIONE ===
# Cartella dove hai i loghi .png
input_folder = "Loghi squadre"
# File CSV di output
output_csv = "loghi.csv"

rows = []

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        squadra = os.path.splitext(filename)[0].capitalize()  # es: juventus.png -> Juventus
        file_path = os.path.join(input_folder, filename)
        
        # Legge immagine e converte in base64
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            data_url = f"data:image/png;base64,{encoded}"
        
        rows.append({"Squadra": squadra, "LogoBase64": data_url})

# Crea DataFrame e salva CSV
df = pd.DataFrame(rows)
df.to_csv(output_csv, index=False, encoding="utf-8")

print(f"Creato file {output_csv} con {len(rows)} loghi.")