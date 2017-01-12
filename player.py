
class Player:
    VERSION = "We're kicking your ass!"
    name = "weneverwonanything"
    stack = 0
    current_bid = 0
    player = True
    bet = 0
    hand = True
    good_cards = ["J", "Q", "K", "A"]
    counter = 0
    common_cards = []
    suit = False

    def get_info(self, gs):
        self.current_bid = gs.get("current_buy_in")
        players = gs.get("players")
        self.player = players[gs.get("in_action")]
        self.stack = self.player.get("stack")
        self.bet = self.player.get("bet")
        self.hand = self.player.get("hole_cards")
        self.common_cards = gs.get("community_cards")
        self.suit = self.hand[0]["suit"] == self.hand[1]["suit"]
        pass

    def betRequest(self, gs):
        self.get_info(gs)
        while(self.counter == 0):
            if self.hand[0]["rank"] in self.good_cards:
                if self.hand[0]["rank"] == self.hand[1]["rank"]:
                    self.counter += 1
                    return 100
                if self.hand[1]["rank"] in self.good_cards:
                    self.counter += 1
                    return 50
            if self.suit:
                return 50
            return 15
        if self.hand[0]["rank"] in self.good_cards and self.hand[1]["rank"] in self.good_cards:
            if len(self.common_cards) == 0:
                return 20
        if len(self.common_cards) >= 3:
            flush_checker = self.check_flush()
            if flush_checker is not False:
                return flush_checker
            if self.hand[0]["rank"] in self.common_cards.values() and self.hand[1]["rank"] in self.common_cards.values():
                return self.current_bid - self.bet
            if self.hand[0]["rank"] in self.common_cards.values() or self.hand[1]["rank"] in self.common_cards.values():
                if self.hand[0]["rank"] == self.hand[1]["rank"]:
                    return 1000
                for i in range(len(self.common_cards)):  # drill
                    for j in range(len(self.common_cards) - 1):
                        if i != j+1:
                            if self.common_cards[i].get("rank") == self.common_cards[j+1].get("rank"):
                                return 1000
                return 100
            return 0
        return 0

    def showdown(self, game_state):
        pass

    def check_flush(self):
        flush_counter = 2
        for i in range(len(self.common_cards)):
            if self.suit == self.common_cards[i].get("suit"):
                flush_counter += 1
        if len(self.common_cards) == 3:
            if flush_counter == 4:
                return 50
            if flush_counter == 5:
                return 1000
            if len(self.common_cards) == 4:
                if flush_counter == 4:
                    return 50
                if flush_counter == 5:
                    return 1000
            if len(self.common_cards) == 5:
                if flush_counter == 5:
                    return 1000
        return False
