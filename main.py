import os
import getpass
import random

username = getpass.getuser()
folder = rf"C:\Users\{username}\Desktop"


if not os.path.exists(folder):
    print("ERR0R : Le dossier n'existe pas !")
    exit()
extensions = [".txt", ".json", ".csv"]  


files_found = []
for root, dirs, files in os.walk(folder):
    for f in files:
        if any(f.lower().endswith(ext) for ext in extensions):
            files_found.append(os.path.join(root, f))


if not files_found:
    print("ERRN0FILE : Aucun fichier trouvé avec les extensions :", extensions)
    exit()
filepath = random.choice(files_found)


try:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"=== Contenu du fichier '{os.path.basename(filepath)}' ===\n")
    print(content)
except Exception as e:
    print(f"Impossible de lire le fichier : {e}")
