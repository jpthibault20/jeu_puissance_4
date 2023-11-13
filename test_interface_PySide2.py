from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        # Initialiser l'interface utilisateur
        self.init_ui()

    def init_ui(self):
        # Créer des widgets
        label = QLabel('Entrez votre nom:')
        self.input_nom = QLineEdit(self)
        bouton_valider = QPushButton('Valider', self)
        bouton_quitter = QPushButton('Quitter', self)

        # Définir la disposition de la fenêtre
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.input_nom)
        layout.addWidget(bouton_valider)
        layout.addWidget(bouton_quitter)

        # Connecter les signaux aux fonctions
        bouton_valider.clicked.connect(self.valider_click)
        bouton_quitter.clicked.connect(self.quitter_click)

        # Configurer la fenêtre principale
        self.setWindowTitle('Exemple PySide2')
        self.setGeometry(300, 300, 300, 150)

    def valider_click(self):
        nom = self.input_nom.text()
        print('Nom validé :', nom)

    def quitter_click(self):
        self.close()

if __name__ == '__main__':
    # Créer l'application Qt
    app = QApplication([])

    # Créer une instance de la fenêtre
    fenetre = MaFenetre()

    # Afficher la fenêtre
    fenetre.show()

    # Exécuter l'application
    app.exec_()
