
class Player:
    VERSION = "work please"
    name = "weneverwonanything"
    stack = 0

    def get_info(self, game_state):
        current_buy_in = game_state["current_buy_in"]
        print current_buy_in


    def betRequest(self, gs):
        current_buy_in = gs["current_buy_in"]
        print current_buy_in
        gs.current_buy_in - gs.players[gs.in_action].bet
        return 500


    def showdown(self, game_state):
        pass
