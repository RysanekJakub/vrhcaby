class Bar:
    def __init__(self):
        self.board = [0] * 24
        self.bar = [0] * 2

    def add_to_bar(self, player, count=1):
        self.bar[player] += count

    def remove_from_bar(self, player, count=1):
        if self.bar[player] >= count:
            self.bar[player] -= count
            return True
        else:
            return False
