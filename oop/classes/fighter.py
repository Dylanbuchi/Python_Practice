class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        self.dead = False

    def __str__(self):
        return "Fighter({}, {}, {})".format(self.name, self.health,
                                            self.damage_per_attack)

    def attack(self, other):
        other.health -= self.damage_per_attack

    def is_dead(self):
        if self.health <= 0:
            self.dead = True
            return True
        return False

    def battle_round(self, other):
        self.attack(other)
        self.is_dead()
        winner = self.get_name_of_the_winner(other)
        return winner

    def check_fight_is_over(self, round_1, round_2):
        if round_1 or round_2:
            return round_1 or round_2

    def fight(self, other):
        while True:
            round_1 = self.battle_round(other)
            round_2 = other.battle_round(self)
            winner = self.check_fight_is_over(round_1, round_2)
            if winner:
                return winner

    def get_name_of_the_winner(self, other):
        if self.dead:
            return other.name
        if other.dead:
            return self.name

    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        return fighter1.fight(fighter2)
    else:
        return fighter2.fight(fighter1)


def main():
    print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))


if __name__ == "__main__":
    main()
