
class Player:
    VERSION = "Default Python rasing player"
    name = "weneverwonanything"
    stack = 0

    def get_info(self, game_state):
        for player in game_state.players:
            if player.name == self.name:
                return 1000

    def betRequest(self, game_state):
        self.stack = self.get_info(game_state)
        return int(self.stack)

    def showdown(self, game_state):
        pass




