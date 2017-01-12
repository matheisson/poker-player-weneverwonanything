
class Player:
    VERSION = "Default Python rasing player"
    name = "weneverwonanything"
    stack = 0

    def get_info(self, game_state):
        for player in game_state.players:
            if player.name == self.name:
                return player.stack

    def betRequest(self, game_state):
        self.stack = self.get_info(game_state)
        return self.stack - game_state.players[game_state.in_action][game_state.bet]

    def showdown(self, game_state):
        pass




