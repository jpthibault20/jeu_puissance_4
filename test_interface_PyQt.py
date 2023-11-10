import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

class Puissance4App(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Création des widgets
        self.label = QLabel('Nom du joueur :', self)
        self.text_input = QLineEdit(self)
        self.bouton_jouer = QPushButton('Jouer', self)
        self.bouton_quitter = QPushButton('Quitter', self)

        # Gestionnaire de mise en page
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.bouton_jouer)
        layout.addWidget(self.bouton_quitter)

        # Définition du gestionnaire de mise en page pour la fenêtre principale
        self.setLayout(layout)

        # Connexion des signaux aux slots
        self.bouton_jouer.clicked.connect(self.jouer)
        self.bouton_quitter.clicked.connect(self.quitter)

        # Fixer la taille de la fenêtre
        self.setFixedSize(300, 200)

        # Configuration de la fenêtre principale
        self.setWindowTitle('Puissance 4')
        self.show()

    def jouer(self):
        nom_joueur = self.text_input.text()
        print(f"Le joueur {nom_joueur} a joué !")

    def quitter(self):
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Puissance4App()
    sys.exit(app.exec_())
