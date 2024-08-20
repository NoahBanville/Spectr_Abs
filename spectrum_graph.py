import pandas as pd
import matplotlib.pyplot as plt
import os

plt.figure(figsize=(8,6))
# chemin d'accès au fichier contenant les CSV (à changer selon utilisateur)
repertoire_csv = r"C:\Users\noah\Downloads\test"

#boucle sur nombre CSV
for fichier in os.listdir(repertoire_csv):
    if fichier.endswith(".csv"):
        
        # Lecture du fichier CSV
        df = pd.read_csv(os.path.join(repertoire_csv, fichier), skiprows=13)
        
        x = df['WL(nm)']
        y = df['Abs.']
        
        plt.plot(x, y, label=fichier.split('-')[0])

# mise en forme
plt.title("Spectre d'absorption", fontsize=20)
plt.xlabel("Longueur d'onde (nm)")
plt.ylabel('Absorption')
plt.legend()

plt.show()
