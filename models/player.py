import datetime


class Player:
    """
    Définit la classe du joueur
    Defines the player class
    """
    def __init__(self, **kwargs):
        self.first_name = kwargs["first_name"]
        self.last_name = kwargs["last_name"]
        self.dob = datetime.datetime.strptime(kwargs["dob"], "%d/%m/%Y").date()
        self.identifiant = kwargs.get("identifiant", None)

    def score_in_tournament(self, tournament):
        pass

    def total_score(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
