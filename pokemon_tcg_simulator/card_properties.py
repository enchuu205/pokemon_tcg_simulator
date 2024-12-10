class Card(__name__):
    def __init__(self) -> None:
        self.name = __name__
        self.moves = {"the moves of the mon"}
    def details(self):
        details_obj = {
            "name": self.name,
            "moves": self.moves,
        }
        return
