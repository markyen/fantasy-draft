"""
Given a draft state and a plan, evaluates the plan to assess its value.
"""
class Forecast:
    def __init__(self, draft, plan):
        self.draft = draft
        self.plan = plan

    def execute_plan(self):
        for position in self.plan:
            self.draft.draft_to_next_decision()
            if len(self.draft.draft_order) == 0:
                break
            pick = self.best_player_available(self.draft.available_players, position)
            self.draft.draft(pick)
        self.draft.draft_to_end_of_round()

    def best_player_available(self, available_players, position):
        best_player = None
        for player in available_players:
            if player.position == position and (best_player is None or player.fan_pts > best_player.fan_pts):
                best_player = player
        return best_player

    def vorp_diff(self):
        return self.draft.vorp_for() - self.draft.vorp_against()

    def __str__(self):
        return f'VORP: {self.vorp_diff():.2f} Picks: {self.draft.my_team().roster} Plan: {self.plan}'
