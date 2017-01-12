
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
    common_cards = []



    def get_info(self, gs):
        self.current_bid = gs.get("current_buy_in")
        players = gs.get("players")
        self.player = players[gs.get("in_action")]
        self.stack = self.player.get("stack")
        self.bet = self.player.get("bet")
        self.hand = self.player.get("hole_cards")
        self.common_cards = gs.get("community_cards")
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
            if len(self.common_cards) == 0:
                return 100
            if len(self.common_cards) >= 3:
                if self.hand[0]["rank"] in self.common_cards.values() and self.hand[1]["rank"] in self.common_cards.values():
                    return 10000
                if self.hand[0]["rank"] in self.common_cards.values() or self.hand[1]["rank"] in self.common_cards.values():
                    if self.hand[0]["rank"] == self.hand[1]["rank"]:
                        return 10000
                    for i in range(len(self.common_cards)) :
                        for j in range(len(self.common_cards) - 1):
                            if i != j+1:
                                if self.common_cards[i].get("rank") == self.common_cards[j+1].get("rank"):
                                    return 10000
                    return 300
            return 0
        return 0



    def showdown(self, game_state):
        pass
