class Rule:

    def delear_draw_check(self, score):
        return score < 17

    def end_game(self, player, dealer):
        result = '[Dealer Win!!!!!]'
        if self.bust_check(player.get_score()):
            if player.get_score() > dealer.get_score():
                result = '[Player Win !!!!!]'
            elif player.get_score() == dealer.get_score():
                result = '[Draw Game~]'
        return result

    def bust_check(self, score):
        return score > 21
