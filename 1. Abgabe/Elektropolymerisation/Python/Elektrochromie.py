import pandas as pd
import matplotlib.pyplot as plt
import os

# Liste deiner Quelldateien
files = [
    r"D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Messwerte\Electrochromism_0_3s.txt", 
    r"D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Messwerte\Electrochromism_0_5s.txt", 
    r"D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Messwerte\Electrochromism_3s.txt"
]

# Zielordner für die Bilder
output_dir = r"D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Bilder"

def process_and_save_to_path(file_list, target_path):
    # Sicherstellen, dass der Zielordner existiert
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"Ordner erstellt: {target_path}")

    for filename in file_list:
        if not os.path.exists(filename):
            print(f"Datei nicht gefunden: {filename}")
            continue
            
        print(f"Verarbeite: {os.path.basename(filename)}...")
        
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        indices = [i for i, line in enumerate(lines) if "Time (s)" in line]
        indices.append(len(lines))
        
        all_segments = []
        
        for start, end in zip(indices, indices[1:]):
            segment_data = [line.strip().split('\t') for line in lines[start+1:end] if line.strip()]
            if not segment_data:
                continue
            
            df_temp = pd.DataFrame(segment_data).apply(pd.to_numeric, errors='coerce').dropna()
            
            # Spaltenpaare extrahieren
            part1 = df_temp.iloc[:, [0, 1]]
            part1.columns = ['Time', 'Current']
            part2 = df_temp.iloc[:, [2, 3]]
            part2.columns = ['Time', 'Current']
            
            all_segments.extend([part1, part2])
        
        if all_segments:
            # Daten zusammenführen und sortieren (kein Offset)
            df_total = pd.concat(all_segments).sort_values(by='Time')
            
            # Plotten
            plt.figure(figsize=(12, 6))
            plt.plot(df_total['Time'], df_total['Current'], color='blue', linewidth=1, label='Messkurve')
            
            plt.title(f"Elektrochromie: {os.path.basename(filename)}")
            plt.xlabel("Zeit (s)")
            plt.ylabel("Strom (A)")
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend()
            plt.tight_layout()
            
            # Speicherpfad zusammenbauen
            base_name = os.path.splitext(os.path.basename(filename))[0]
            save_path = os.path.join(target_path, f"{base_name}.png")
            
            plt.savefig(save_path, dpi=300)
            print(f"Erfolgreich gespeichert unter: {save_path}")
            plt.close()

if __name__ == "__main__":
    process_and_save_to_path(files, output_dir)