from collections import Counter

"""
Tries to imitate the autodraft behavior by making a list of positions needed to
be filled, and then taking the first player by xrank who plays one of those
positions.
"""
class AutodraftTeam:
    starter_count = {
        'QB': 1,
        'WR': 2,
        'RB': 2,
        'TE': 1,
        'DEF': 1,
        'K': 1
    }
    starter_flex = 6
    bench_count = {
        'QB': 2,
        'WR': 3,
        'RB': 3,
        'TE': 2,
        'DEF': 2,
        'K': 1
    }
    bench_flex = 10

    def __init__(self, roster=None):
        self.roster = roster or []

    def starters_needed(self):
        counter = Counter(player.position for player in self.roster)
        result = set()
        for position, count in self.starter_count.items():
            if counter[position] < count:
                result.add(position)
        if sum(counter[pos] for pos in ('WR', 'RB', 'TE')) < self.starter_flex:
            result.add('WR')
            result.add('RB')
            result.add('TE')
        return result

    def bench_needed(self):
        counter = Counter(player.position for player in self.roster)
        result = set()
        for position, count in self.bench_count.items():
            if counter[position] < count:
                result.add(position)
        if sum(counter[pos] for pos in ('WR', 'RB', 'TE')) < self.bench_flex:
            result.add('WR')
            result.add('RB')
            result.add('TE')
        return result

    def next_pick(self, draft):
        positions_needed = self.starters_needed()
        if len(positions_needed) == 0:
            positions_needed = self.bench_needed()
        for player in draft.available_players:
            position = player.position
            if position in positions_needed:
                self.roster.append(player)
                return player

    def copy(self):
        return AutodraftTeam(self.roster.copy())
