
class Player:
    VERSION = "Default Python rasing player"
    name = "weneverwonanything"
    stack = 0




    def betRequest(self, game_state):
        return game_state.current_buy_in - game_state.players[game_state.in_action][game_state.bet]

    def showdown(self, game_state):
        pass




