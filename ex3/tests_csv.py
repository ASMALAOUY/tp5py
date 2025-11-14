import unittest
from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)

class TestCsvReader(unittest.TestCase):

    def test_csv_valide(self):
        pass

    def test_fichier_absent(self):
        pass

    def test_prix_non_numerique(self):
        pass

    def test_prix_negatif(self):
        pass

if __name__ == "__main__":
    unittest.main()
