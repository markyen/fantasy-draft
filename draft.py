from collections import deque

from autodraft import AutodraftTeam
from league import League
from minimax import MinimaxTeam

"""
Holds the state of a draft in progress.
"""
class Draft:
    def __init__(self, pick_ordinal, league_size=12, teams=None, available_players=None, draft_order=None):
        if teams or available_players or draft_order:
            self.teams = teams
            self.available_players = available_players
            self.draft_order = draft_order
            self.pick_index = pick_ordinal - 1
            self.league_size = league_size
        else:
            self.initialize(pick_ordinal, league_size)

    """
    Given your pick number and league size, sets up a draft with all autodraft
    teams, plus a minimax team in your position.
    """
    def initialize(self, pick_ordinal, league_size=12):
        self.league_size = league_size
        self.teams = [AutodraftTeam() for _ in range(pick_ordinal-1)] + [MinimaxTeam()] + [AutodraftTeam() for _ in range(league_size-pick_ordinal)]
        self.available_players = League.all_players.copy()
        self.pick_index = pick_ordinal - 1
        self.draft_order = deque()
        i = 0
        snake = 1
        while len(self.draft_order) < league_size * League.roster_size:
            self.draft_order.append(i)
            i += snake
            if i == league_size - 1:
                snake -= 1
            elif i == 0:
                snake += 1
        replacements = self.replacement_players()
        print(replacements)
        for player in self.available_players:
            player.vorp = player.fan_pts - replacements[player.position]

    """
    Reads in the state of the draft from a file. Expects player names
    delimited by new lines, in draft order.
    """
    @classmethod
    def from_file(self, filename, pick_ordinal, league_size=12):
        previously_drafted = []
        with open(filename) as f:
            for line in f:
                for player in League.all_players:
                    if line.strip().lower() == player.name.lower():
                        previously_drafted.append(player)
                        break
                else:
                    raise AttributeError(f'Player not found: {line.strip()}')
        
        draft = Draft(pick_ordinal, league_size)
        for player in previously_drafted:
            draft.draft(player)
        return draft

    """
    Identifies the "replacement" players, the best players expected to still
    be available on the waiver wire after the draft is complete. We use VORP,
    or "value over replacement player" as a way to standardize value of drafted
    players across positions.
    """
    def replacement_players(self):
        teams = [AutodraftTeam() for _ in range(self.league_size)]
        draft = Draft(self.pick_index+1, self.league_size, teams, League.all_players.copy(), self.draft_order)
        for i in self.draft_order:
            pick = teams[i].next_pick(draft)
            draft.available_players.remove(pick)
        return {pos: max(p.fan_pts for p in draft.available_players if p.position == pos) for pos in League.positions}
    
    def draft_to_next_decision(self):
        while len(self.draft_order) > 0 and self.draft_order[0] != self.pick_index:
            self.draft()
    
    def draft_to_end_of_round(self):
        for _ in range(len(self.draft_order) % self.league_size):
            self.draft()
    
    def vorp_for(self):
        return sum(player.vorp for player in self.my_team().roster)

    def vorp_against(self):
        vorp = 0
        for team in self.teams[:self.pick_index] + self.teams[self.pick_index+1:]:
            for player in team.roster:
                vorp += player.vorp
        return vorp / (self.league_size - 1)

    def draft(self, pick=None):
        if pick is None:
            pick = self.teams[self.draft_order[0]].next_pick(self)
        else:
            self.teams[self.draft_order[0]].roster.append(pick)
        self.available_players.remove(pick)
        self.draft_order.popleft()
    
    def copy(self):
        return Draft(self.pick_index+1, self.league_size, [t.copy() for t in self.teams], self.available_players.copy(), self.draft_order.copy())

    def my_team(self):
        return self.teams[self.pick_index]
    
    def __str__(self):
        i = 0
        j = 0
        snake = 1
        result = []
        for _ in range(League.roster_size*self.league_size - len(self.draft_order)):
            result.append(f'Round {j+1} Team {i+1}: {self.teams[i].roster[j].name} ({self.teams[i].roster[j].vorp:.2f})')
            i += snake
            if snake == 0:
                j += 1
            if i == self.league_size - 1:
                snake -= 1
            elif i == 0:
                snake += 1
        return '\n'.join(result)
 
def main():
    draft = Draft.from_file('players.csv', 1, 12)
    draft.draft_to_next_decision()
    draft.draft()
    print(draft)

if __name__ == '__main__':
    main()
