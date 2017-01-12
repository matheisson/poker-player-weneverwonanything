
class Player:
    VERSION = "work please"
    name = "weneverwonanything"
    stack = 0
    current_bid = 0
    player = True
    bet = 0
    hand = True
    good_cards = ["10", "J", "Q", "K", "A"]
    counter = 0



    def get_info(self, gs):
        self.current_bid = gs.get("current_buy_in")
        players = gs.get("players")
        self.player = players[gs.get("in_action")]
        self.stack = self.player.get("stack")
        self.bet = self.player.get("bet")
        self.hand = self.player.get("hole_cards")
        pass


    def betRequest(self, gs):
        self.get_info(gs)
        while(self.counter == 0):
            if self.hand[0]["rank"] in self.good_cards:
                if self.hand[0]["rank"] == self.hand[1]["rank"]:
                    self.counter += 1
                    return 1000
            return 0
        if self.hand[0]["rank"] in self.good_cards and self.hand[1]["rank"] in self.good_cards:
            return 10000
        return 0



    def showdown(self, game_state):
        pass
