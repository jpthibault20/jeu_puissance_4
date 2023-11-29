import tkinter as tk

def clic_bouton():
    texte = champ_texte.get()
    etiquette.config(text="Bonjour, " + texte)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Exemple d'interface graphique")

# Définition de la taille par défaut
fenetre.geometry("400x200")  # Largeur x Hauteur

# Étiquette
etiquette = tk.Label(fenetre, text="Entrez votre nom:")
etiquette.pack()

# Champ de texte
champ_texte = tk.Entry(fenetre)
champ_texte.pack()

# Bouton
bouton = tk.Button(fenetre, text="Cliquez-moi", command=clic_bouton)
bouton.pack()

# Lancement de la boucle principale
fenetre.mainloop()
