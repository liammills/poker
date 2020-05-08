class Player():
    def __init__(self,name):
        self.name = name
        self.chips = 0
        self.stake = 0
        self.stake_gap = 0
        self.cards = []
        self.score = []
        self.fold = False
        self.ready = False
        self.all_in = False
        self.list_of_special_attributes = []
        self.win = False

    def __repr__(self):
        return self.name
