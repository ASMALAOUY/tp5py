from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException,
    CsvException
)

def main():
    chemin = "articles.csv"

    try:
        data = charger_csv(chemin)
    except FichierIntrouvableException as e:
        pass
    except LigneInvalideException as e:
        pass
    except PrixNegatifException as e:
        pass
    except CsvException as e:
        pass

if __name__ == "__main__":
    main()
