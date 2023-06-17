from collections import Counter

from forecast import Forecast
from league import League

"""
Represents a team that tries to optimize its picks by generating all possible
"plans" (or arrays of positions to pick in the next serveral rounds that meet
constraints), and then creates a forecast for each plan to evaluate it and
assess its value.
"""
class MinimaxTeam():
    min_counts = {
        'RB': 2,
        'WR': 2,
        'TE': 1,
        'QB': 1,
        'DEF': 1,
        'K': 1
    }
    max_counts = {
        'TE': 3,
        'QB': 2,
        'DEF': 2,
        'K': 2,
        'RB': 6,
        'WR': 6,
        'TE': 6
    }
    min_flex = 6
    search_depth = 5

    def __init__(self, roster=None):
        self.roster = roster or []

    def generate_plans(self):
        candidates = []
        counts = Counter(player.position for player in self.roster)
        for pos in self.min_counts.keys():
            counts[pos] += 1
            if self.satisfies_constraints(counts, len(self.roster)+1):
                candidates.append((pos,))
            counts[pos] -= 1
        print(f'Round {len(self.roster)+1}: {len(candidates)}')
        return self.generate_plans_inner(candidates, self.search_depth)

    def generate_plans_inner(self, prev_candidates, depth):
        round = len(self.roster) + len(prev_candidates[0]) + 1
        if round > League.roster_size or depth <= 0:
            return prev_candidates
        candidates = []
        for prev_candidate in prev_candidates:
            for candidate in [prev_candidate + (pos,) for pos in self.min_counts.keys()]:
                counts = Counter(candidate)
                counts.update(player.position for player in self.roster)
                if self.satisfies_constraints(counts, round):
                    candidates.append(candidate)
        print(f'Round {round}: {len(candidates)}')
        return self.generate_plans_inner(candidates, depth - 1)

    def satisfies_constraints(self, counts, round):
        needed = sum(min_count - counts[pos] for pos, min_count in self.min_counts.items() if min_count > counts[pos])
        needed_flex = self.min_flex - (counts['RB'] + counts['WR'] + counts['TE'])
        return max(needed, needed_flex) <= League.roster_size - round and all(counts[pos] <= max_count for pos, max_count in self.max_counts.items())

    def next_pick(self, draft):
        draft_forecasts = [Forecast(draft.copy(), plan) for plan in self.generate_plans()]
        best_forecast = 0
        forecast = draft_forecasts[best_forecast]
        forecast.execute_plan()
        best_vorp = forecast.vorp_diff()
        print(forecast)
        for i in range(1, len(draft_forecasts)):
            forecast = draft_forecasts[i]
            forecast.execute_plan()
            curr_vorp = forecast.vorp_diff()
            if curr_vorp > best_vorp:
                best_forecast = i
                best_vorp = curr_vorp
                print(forecast)
        pick = draft_forecasts[best_forecast].draft.my_team().roster[len(self.roster)]
        self.roster.append(pick)
        return pick

    def copy(self):
        return MinimaxTeam(self.roster.copy())
