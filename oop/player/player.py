class Player:
    def __init__(self, number: int) -> None:
        self.number = number
        self.score = 0
        self.winner = False

    def reset(self) -> None:
        self.score = 0
        self.winner = False

    def print_scores(self) -> None:
        print(self, f"Score: {self.score}")

    def __repr__(self) -> str:
        return f"Player_{self.number}"