
class Player:
    VERSION = "work please"
    name = "weneverwonanything"
    stack = 0

    def get_info(self, game_state):
        for player in game_state.players:
            if player.name == self.name:
                return 1000


    def betRequest(self, gs):
        return gs.players[gs.in_action].stack


    def showdown(self, game_state):
        pass
