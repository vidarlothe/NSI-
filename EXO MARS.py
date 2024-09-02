import tkinter as tk

class Personnage:
    def __init__(self, x=0, y=0, z=0, hp=100):
        self.x = x
        self.y = y
        self.z = z
        self.hp = hp

    def avance(self):
        self.x += 1

    def droite(self):
        self.y += 1

    def saute(self):
        self.z += 1

    def coord(self):
        return (self.x, self.y, self.z)

    def subir_degats(self, degats):
        self.hp -= degats

    def attaquer(self, cible):
        cible.subir_degats(10)  # Par exemple, l'attaque inflige 10 points de dégâts

    def afficher_hp(self):
        print("Points de vie:", self.hp)


def avancer():
    joueur.avance()
    afficher_coordonnees()


def aller_droite():
    joueur.droite()
    afficher_coordonnees()


def sauter():
    joueur.saute()
    afficher_coordonnees()


def attaquer():
    joueur.attaquer(monstre)
    afficher_hp()


def afficher_coordonnees():
    label_coordonnees.config(text="Coordonnées: " + str(joueur.coord()))


def afficher_hp():
    joueur.afficher_hp()
    label_hp.config(text="Points de vie: " + str(joueur.hp))


joueur = Personnage()
monstre = Personnage(x=5, y=5, z=0, hp=50)  # Exemple de création d'un monstre

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu de personnage")

# Création des boutons
btn_avancer = tk.Button(root, text="Avancer", command=avancer)
btn_avancer.pack()

btn_droite = tk.Button(root, text="Aller à droite", command=aller_droite)
btn_droite.pack()

btn_sauter = tk.Button(root, text="Sauter", command=sauter)
btn_sauter.pack()

btn_attaquer = tk.Button(root, text="Attaquer", command=attaquer)
btn_attaquer.pack()

# btn_potion = tk.Button(root, text = "Healing", commande=heal)
# btn_heal.pack()

# btn_hp = tk.button(root, text = "afficher hp", commande=afficher_hp)
# btn_hp.pack()

# Étiquette pour afficher les coordonnées
label_coordonnees = tk.Label(root, text="Coordonnées: " + str(joueur.coord()))
label_coordonnees.pack()

# Étiquette pour afficher les points de vie
label_hp = tk.Label(root, text="Points de vie: " + str(joueur.hp))
label_hp.pack()

root.mainloop()

