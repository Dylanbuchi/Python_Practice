from player.player import Player
from random import randint
from typing import List


class Game:
    MAX_SCORE = 100

    def __init__(self, player_amount: int) -> None:
        self.player_amount = player_amount

    def round(self, player: Player):
        roll_number = randint(1, 6)
        player.score += roll_number

        print(f"Player_{player.number} (rolled a {roll_number})")

    def check_winner(self, player: Player):
        if player.score >= self.MAX_SCORE:
            player.winner = True

    def reset_game(self, players: List[Player]):
        for player in players:
            player.reset()

    def print_score(self, players: List[Player]):
        sorted_players = sorted(players, key=lambda x: x.score, reverse=True)
        [i.print_scores() for i in sorted_players]

    def play_game(self):
        players = [Player(i) for i in range(1, self.player_amount + 1)]
        game_on = True
        round = 1

        while game_on:
            print(f"Round: {round}\n")
            for player in players:
                self.round(player)
                self.check_winner(player)
                if player.winner:
                    print(f"\n{player} wins the game!\n")
                    game_on = False
                    break
            print("-" * 20)
            round += 1

        print("LeaderBoard\n")
        self.print_score(players)
        self.reset_game(players)