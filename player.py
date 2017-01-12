
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
        return current_buy_in - players[in_action][bet] + minimum_raise

    def showdown(self, game_state):
        pass
