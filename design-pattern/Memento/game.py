
class Game:
    def __init__(self):
        self.a_score = 0
        self.b_score = 0

    def save_game(self):
        return Game_save(self)

    def get_point(self, team_name):
        if team_name == "a":
            self.a_score += 1
        else:
            self.b_score += 1


class Game_save:

    def __init__(self, game):
        self.game = game

    def load(self):
        return self.game


g1 = Game()
g2 = Game()

print(g1 == g2)

g1.get_point("b")

print(g1.a_score)
print(g1.b_score)

gs = g1.save_game()

print(type(gs.game))
