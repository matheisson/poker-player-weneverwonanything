
class Player:
    VERSION = "work please"
    name = "weneverwonanything"
    stack = 0

    def get_info(self, game_state):
        for player in game_state.players:
            if player.name == self.name:
                return 1000

    def betRequest(self, gs):
        self.stack = self.get_info(gs)
        return 1000

    def showdown(self, game_state):
        pass




