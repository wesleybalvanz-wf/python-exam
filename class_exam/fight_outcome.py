import random


class UserStats(object):
    def __init__(self, name):
        self.name = name
        self.stats = random.randint(1, 10)

    def get_name(self):
        return self.name

    def get_stats(self):
        return self.stats

    def get_name_and_stats(self):
        return self.name, self.stats


class Outcome(UserStats, object):
    def __init__(self, user, opponent):
        self.user_name, self.user_stats = UserStats(user).get_name_and_stats()
        self.opponent_name, self.opponent_stats = UserStats(
            opponent).get_name_and_stats()

    def fight_outcome(self):
        if self.user_stats > self.opponent_stats:
            return "%s stats are %d and your stats are %d, you win!"\
                   % (self.opponent_name, self.opponent_stats, self.user_stats)
        elif self.user == self.opponent:
            return "%s stats are %d and your stats are %d, it's a tie." \
                   % (self.opponent_name, self.opponent_stats, self.user_stats)
        elif self.user < self.opponent:
            return "%s stats are %d and your stats are %d, you lose." \
                   % (self.opponent_name, self.opponent_stats, self.user_stats)


def fight(opponents, user):
    for opponent in opponents:
        print Outcome.fight_outcome(opponent, user)