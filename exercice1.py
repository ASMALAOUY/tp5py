class TransactionException(Exception):
    pass

class SoldeInsuffisantException(TransactionException):
    def __init__(self, message="Solde insuffisant pour ce retrait."):
        super().__init__(message)

class MontantNegatifException(TransactionException):
    def __init__(self, message="Le montant ne peut pas être négatif."):
        super().__init__(message)

class CompteBancaire:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        if montant < 0:
            raise MontantNegatifException()
        self.solde += montant

    def retirer(self, montant):
        if montant < 0:
            raise MontantNegatifException()
        if montant > self.solde:
            raise SoldeInsuffisantException()
        self.solde -= montant

    def afficher(self):
        print(f"Compte: {self.nom}, Solde: {self.solde}€")

try:
    compte = CompteBancaire("Alice", 100)
    compte.afficher()
    compte.retirer(150)
except TransactionException as e:
    print("Erreur:", e)
