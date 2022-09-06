from collections import Counter, deque

class Player:
    def __init__(self, xrank, name, position, fan_pts):
        self.xrank = xrank
        self.name = name
        self.position = position
        self.fan_pts = fan_pts
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

class Draft:
    roster_size = 15
    positions = ['RB', 'WR', 'QB', 'TE', 'DEF', 'K']
    all_players = [
        Player(1, "Jonathan Taylor", "RB", 315.66),
        Player(2, "Christian McCaffrey", "RB", 321.5),
        Player(3, "Justin Jefferson", "WR", 259.14),
        Player(4, "Cooper Kupp", "WR", 267.2),
        Player(5, "Austin Ekeler", "RB", 301.19),
        Player(6, "Dalvin Cook", "RB", 260.92),
        Player(7, "Ja'Marr Chase", "WR", 255.64),
        Player(8, "Derrick Henry", "RB", 261.93),
        Player(9, "Stefon Diggs", "WR", 241.79),
        Player(10, "CeeDee Lamb", "WR", 228.72),
        Player(11, "Joe Mixon", "RB", 255.58),
        Player(12, "Davante Adams", "WR", 229.31),
        Player(13, "Najee Harris", "RB", 252.6),
        Player(14, "Saquon Barkley", "RB", 250.62),
        Player(15, "Aaron Jones", "RB", 233.98),
        Player(16, "D'Andre Swift", "RB", 256.26),
        Player(17, "Alvin Kamara", "RB", 257.44),
        Player(18, "Leonard Fournette", "RB", 250.9),
        Player(19, "Travis Kelce", "TE", 224.38),
        Player(20, "Mike Evans", "WR", 229.17),
        Player(21, "Nick Chubb", "RB", 235.6),
        Player(22, "Tyreek Hill", "WR", 218.58),
        Player(23, "Javonte Williams", "RB", 222.44),
        Player(24, "Mark Andrews", "TE", 201.36),
        Player(25, "Michael Pittman Jr.", "WR", 193.33),
        Player(26, "Deebo Samuel", "WR", 232.83),
        Player(27, "Tee Higgins", "WR", 210.6),
        Player(28, "A.J. Brown", "WR", 214.75),
        Player(29, "DJ Moore", "WR", 187.79),
        Player(30, "James Conner", "RB", 231.91),
        Player(31, "Keenan Allen", "WR", 207.2),
        Player(32, "Ezekiel Elliott", "RB", 238.02),
        Player(33, "Kyle Pitts", "TE", 174.95),
        Player(34, "Eli Mitchell", "RB", 209.02),
        Player(35, "Josh Allen", "QB", 416.04),
        Player(36, "Travis Etienne Jr.", "RB", 181.57),
        Player(37, "Breece Hall", "RB", 162.97),
        Player(38, "Mike Williams", "WR", 198.72),
        Player(39, "Terry McLaurin", "WR", 191.68),
        Player(40, "Courtland Sutton", "WR", 211.82),
        Player(41, "Allen Robinson II", "WR", 198.07),
        Player(42, "Diontae Johnson", "WR", 194.43),
        Player(43, "AJ Dillon", "RB", 174.65),
        Player(44, "Chase Edmonds", "RB", 202.76),
        Player(45, "Jaylen Waddle", "WR", 182.36),
        Player(46, "Lamar Jackson", "QB", 384.11),
        Player(47, "Amon-Ra St. Brown", "WR", 173.58),
        Player(48, "Dameon Pierce", "RB", 146.8),
        Player(49, "George Kittle", "TE", 158.99),
        Player(50, "DK Metcalf", "WR", 171.75),
        Player(51, "Darren Waller", "TE", 166.2),
        Player(52, "Justin Herbert", "QB", 382.72),
        Player(53, "Gabe Davis", "WR", 189.08),
        Player(54, "J.K. Dobbins", "RB", 189.97),
        Player(55, "Brandin Cooks", "WR", 174.45),
        Player(56, "Patrick Mahomes", "QB", 380.18),
        Player(57, "JuJu Smith-Schuster", "WR", 192.81),
        Player(58, "David Montgomery", "RB", 222.25),
        Player(59, "Cam Akers", "RB", 219.49),
        Player(60, "Rashod Bateman", "WR", 179.44),
        Player(61, "Dalton Schultz", "TE", 151.8),
        Player(62, "Josh Jacobs", "RB", 198.1),
        Player(63, "Jerry Jeudy", "WR", 193.15),
        Player(64, "Jalen Hurts", "QB", 336.91),
        Player(65, "Joe Burrow", "QB", 347.65),
        Player(66, "Elijah Moore", "WR", 171.62),
        Player(67, "Damien Harris", "RB", 176.59),
        Player(68, "Rashaad Penny", "RB", 173.19),
        Player(69, "Marquise Brown", "WR", 162.41),
        Player(70, "Kyler Murray", "QB", 382.72),
        Player(71, "Darnell Mooney", "WR", 172.35),
        Player(72, "Clyde Edwards-Helaire", "RB", 176.67),
        Player(73, "Antonio Gibson", "RB", 142.05),
        Player(74, "Dallas Goedert", "TE", 142.05),
        Player(75, "Tony Pollard", "RB", 170.25),
        Player(76, "Devin Singletary", "RB", 159.83),
        Player(77, "Brandon Aiyuk", "WR", 157.27),
        Player(78, "Rhamondre Stevenson", "RB", 201.8),
        Player(79, "Hunter Renfrow", "WR", 169.9),
        Player(80, "Adam Thielen", "WR", 189.03),
        Player(81, "Michael Thomas", "WR", 198.47),
        Player(82, "Tom Brady", "QB", 347.84),
        Player(83, "Miles Sanders", "RB", 170.07),
        Player(84, "Trey Lance", "QB", 317.23),
        Player(85, "Amari Cooper", "WR", 185.23),
        Player(86, "Christian Kirk", "WR", 183.75),
        Player(87, "Melvin Gordon III", "RB", 167.06),
        Player(88, "Chris Godwin", "WR", 175.04),
        Player(89, "Russell Wilson", "QB", 335.2),
        Player(90, "Allen Lazard", "WR", 153.71),
        Player(91, "DeVonta Smith", "WR", 166.31),
        Player(92, "Kareem Hunt", "RB", 170.15),
        Player(93, "Dawson Knox", "TE", 142.4),
        Player(94, "Cordarrelle Patterson", "RB", 157.39),
        Player(95, "T.J. Hockenson", "TE", 164.2),
        Player(96, "Dak Prescott", "QB", 330.38),
        Player(97, "Robert Woods", "WR", 173.66),
        Player(98, "Michael Carter", "RB", 163.67),
        Player(99, "Darrell Henderson Jr.", "RB", 163.67),
        Player(100, "Matthew Stafford", "QB", 322.15),
        Player(101, "Cole Kmet", "TE", 138.12),
        Player(102, "Drake London", "WR", 177.03),
        Player(103, "Tyler Lockett", "WR", 162.69),
        Player(104, "Kirk Cousins", "QB", 302.19),
        Player(105, "James Cook", "RB", 90.66),
        Player(106, "DeAndre Hopkins", "WR", 124.45),
        Player(107, "Kadarius Toney", "WR", 177.84),
        Player(108, "Nyheim Hines", "RB", 133.22),
        Player(109, "Aaron Rodgers", "QB", 332.46),
        Player(110, "Zach Ertz", "TE", 154.49),
        Player(111, "Derek Carr", "QB", 315.16),
        Player(112, "Trevor Lawrence", "QB", 286.04),
        Player(113, "Russell Gage", "WR", 81.22),
        Player(114, "Chris Olave", "WR", 133.32),
        Player(115, "Pat Freiermuth", "TE", 128.6),
        Player(116, "George Pickens", "WR", 153.85),
        Player(117, "Kenneth Walker III", "RB", 122.96),
        Player(118, "Alexander Mattison", "RB", 104.31),
        Player(119, "Justin Fields", "QB", 296.67),
        Player(120, "David Njoku", "TE", 131.34),
        Player(121, "Jamaal Williams", "RB", 119.58),
        Player(122, "Khalil Herbert", "RB", 97.98),
        Player(123, "Rachaad White", "RB", 76.85),
        Player(124, "Jakobi Meyers", "WR", 137.64),
        Player(125, "Tua Tagovailoa", "QB", 290.72),
        Player(126, "James Robinson", "RB", 90.02),
        Player(127, "Isaiah McKenzie", "WR", 155.57),
        Player(128, "Kenneth Gainwell", "RB", 140.52),
        Player(129, "Nico Collins", "WR", 144.98),
        Player(130, "Raheem Mostert", "RB", 147.67),
        Player(131, "Chase Claypool", "WR", 156.47),
        Player(132, "Tyler Boyd", "WR", 136.71),
        Player(133, "Irv Smith Jr.", "TE", 121.28),
        Player(134, "DeVante Parker", "WR", 174.51),
        Player(135, "Hunter Henry", "TE", 121.76),
        Player(136, "Austin Hooper", "TE", 119.96),
        Player(137, "Tyler Higbee", "TE", 122.92),
        Player(138, "Daniel Jones", "QB", 255.82),
        Player(139, "Buffalo", "DEF", 143.44),
        Player(140, "Julio Jones", "WR", 119.68),
        Player(141, "Jarvis Landry", "WR", 105.02),
        Player(142, "Evan Engram", "TE", 80.89),
        Player(143, "DJ Chark Jr.", "WR", 171.73),
        Player(144, "Matt Ryan", "QB", 265.54),
        Player(145, "J.D. McKissic", "RB", 106.98),
        Player(146, "Albert Okwuegbunam", "TE", 139.33),
        Player(147, "Rondale Moore", "WR", 109.25),
        Player(148, "Isiah Pacheco", "RB", 51.65),
        Player(149, "San Francisco", "DEF", 118.21),
        Player(150, "Treylon Burks", "WR", 142.43),
        Player(151, "Gerald Everett", "TE", 101.27),
        Player(152, "Jared Goff", "QB", 287.85),
        Player(153, "Tampa Bay", "DEF", 121.65),
        Player(154, "Mo Alie-Cox", "TE", 65.35),
        Player(155, "Tyler Allgeier", "RB", 79.86),
        Player(156, "Marquez Valdes-Scantling", "WR", 139.65),
        Player(157, "Joshua Palmer", "WR", 141.32),
        Player(158, "Mike Gesicki", "TE", 118.76),
        Player(159, "Romeo Doubs", "WR", 86.81),
        Player(160, "Brian Robinson Jr.", "RB", 81.92),
        Player(161, "Jeff Wilson Jr.", "RB", 72.78),
        Player(162, "Jameis Winston", "QB", 314.78),
        Player(163, "Denver", "DEF", 108.45),
        Player(164, "Jahan Dotson", "WR", 111.37),
        Player(165, "Green Bay", "DEF", 110.36),
        Player(166, "D'Onta Foreman", "RB", 28.97),
        Player(167, "Eno Benjamin", "RB", 65.71),
        Player(168, "Skyy Moore", "WR", 144.83),
        Player(169, "Samaje Perine", "RB", 75.07),
        Player(170, "Mac Jones", "QB", 307.46),
        Player(171, "Ryan Tannehill", "QB", 262.59),
        Player(172, "Justin Tucker", "K", 159.26),
        Player(173, "Mark Ingram II", "RB", 131.45),
        Player(174, "Indianapolis", "DEF", 105.02),
        Player(175, "Boston Scott", "RB", 80.54),
        Player(176, "Dontrell Hilliard", "RB", 53.44),
        Player(177, "Kenny Golladay", "WR", 133.88),
        Player(178, "K.J. Osborn", "WR", 104.68),
        Player(179, "Jalen Tolbert", "WR", 135.27),
        Player(180, "Carson Wentz", "QB", 252.8),
        Player(181, "New Orleans", "DEF", 110.37),
        Player(182, "Garrett Wilson", "WR", 86.07),
        Player(183, "Los Angeles Rams", "DEF", 119.7),
        Player(184, "Robbie Anderson", "WR", 106.36),
        Player(185, "Los Angeles Chargers", "DEF", 105.41),
        Player(186, "Zamir White", "RB", 45.82),
        Player(187, "Robert Tonyan", "TE", 113.95),
        Player(188, "Isiah Spiller", "RB", 44.79),
        Player(189, "Evan McPherson", "K", 160.49),
        Player(190, "Mike Davis", "RB", 76.37),
        Player(191, "D'Ernest Johnson", "RB", 37.79),
        Player(192, "Noah Fant", "TE", 113.27),
        Player(193, "Baker Mayfield", "QB", 283.46),
        Player(194, "Daniel Carlson", "K", 150.91),
        Player(195, "Corey Davis", "WR", 104.83),
        Player(196, "New England", "DEF", 107.67),
        Player(197, "Mecole Hardman", "WR", 131.13),
        Player(198, "Marcus Mariota", "QB", 295.32),
        Player(199, "Darrel Williams", "RB", 31.91),
        Player(200, "Marlon Mack", "RB",0),
        Player(201, "Jaylen Warren", "RB", 0.35),
        Player(202, "Van Jefferson", "WR", 106.55),
        Player(203, "Damien Williams", "RB", 57.17),
        Player(204, "Hayden Hurst", "TE", 101.22),
        Player(205, "Davis Mils", "QB", 266.63),
        Player(206, "Parris Campbell", "WR", 134.32),
        Player(207, "Tyler Bass", "K", 157.93),
        Player(208, "Wan'Dale Robinson", "WR", 124.73),
        Player(209, "Kansas City", "DEF", 102.5),
        Player(210, "Rex Burkhead", "RB", 143.44),
        Player(211, "Ronald Jones II", "RB", 31.92),
        Player(212, "Baltimore", "DEF", 111.89),
        Player(213, "David Bell", "WR", 105.78),
        Player(214, "Matt Gay", "K", 156.23),
        Player(215, "Philadelphia", "DEF", 101.36),
        Player(216, "Isiah Likely", "TE", 55.45),
        Player(217, "Pittsburgh", "DEF", 97.97),
        Player(218, "Curtis Samuel", "WR", 109.63),
        Player(219, "Jerick McKinnon", "RB", 66.03),
        Player(220, "Kenyan Drake", "RB", 11.17),
        Player(221, "Myles Gaskin", "RB", 34.25),
        Player(222, "Sony Michel", "RB", 20.39),
        Player(223, "Alec Pierce", "WR", 113.25),
        Player(224, "Kendrick Bourne", "WR", 101.73),
        Player(225, "Cameron Brate", "TE", 80.05),
        Player(226, "Harrison Butker", "K", 149.46),
        Player(227, "Logan Thomas", "TE", 109.6),
        Player(228, "Marvin Jones Jr.", "WR", 107.22),
        Player(229, "Kene Nwangwu", "RB", 42.34),
        Player(230, "Kyren Williams", "RB", 23.4),
        Player(231, "Michael Gallup", "WR", 116.25),
        Player(232, "Dallas", "DEF", 118.52),
        Player(233, "Minnesota", "DEF", 98.18),
        Player(234, "Deshaun Watson", "QB", 116.32),
        Player(235, "Greg Joseph", "K", 126.6),
        Player(236, "KJ Hamler", "WR", 115.18),
        Player(237, "Miami", "DEF", 98.26),
        Player(238, "Robbie Gould", "K", 137.83),
        Player(239, "Cleveland", "DEF", 100.59),
        Player(240, "Cincinnati", "DEF", 105.04),
        Player(241, "Nick Folk", "K", 138.23),
        Player(242, "A.J. Green", "WR", 74.2),
        Player(243, "Brevin Jordan", "TE",90),
        Player(244, "Matt Prater", "K", 146.29),
        Player(245, "Ryan Succop", "K", 138.84),
        Player(246, "Jake Elliott", "K", 133.39),
        Player(247, "New York", "DEF", 78.67),
        Player(248, "Zay Jones", "WR", 165.64),
        Player(249, "Dustin Hopkins", "K", 139.57),
        Player(250, "Kyle Philips", "WR", 31.14),
        Player(251, "Tennesee", "DEF", 101.47),
        Player(252, "Younghoe Koo", "K", 129.7),
        Player(253, "Rodrigo Blankenship", "K", 109.16),
        Player(255, "Jason Sanders", "K", 130.06),
        Player(261, "Brandon McManus", "K", 141.17),
        Player(262, "Las Vegas", "DEF", 96.55)
    ]

    def __init__(self, pick_ordinal, league_size=12, teams=None, available_players=None, draft_order=None):
        if teams or available_players or draft_order:
            self.teams = teams
            self.available_players = available_players
            self.draft_order = draft_order
            self.pick_index = pick_ordinal - 1
            self.league_size = league_size
        else:
            self.initialize(pick_ordinal, league_size)

    # Invariants:
    # Picked players are stored in self.teams[i].roster[j]
    # Available players are stored in self.available_players
    # Remaining draft order is kept in self.draft_order
    # Indices are zero-indexed and ordinals are unit-indexed
    def initialize(self, pick_ordinal, league_size=12):
        self.league_size = league_size
        self.teams = [AutodraftTeam() for _ in range(pick_ordinal-1)] + [MinimaxTeam()] + [AutodraftTeam() for _ in range(league_size-pick_ordinal)]
        self.available_players = self.all_players.copy()
        self.pick_index = pick_ordinal - 1
        self.draft_order = deque()
        i = 0
        snake = 1
        while len(self.draft_order) < league_size * self.roster_size:
            self.draft_order.append(i)
            i += snake
            if i == 11:
                snake -= 1
            elif i == 0:
                snake += 1
        replacements = self.replacement_players()
        for player in self.available_players:
            player.vorp = player.fan_pts - replacements[player.position]

    @classmethod
    def from_file(self, filename, pick_ordinal, league_size=12):
        previously_drafted = []
        with open(filename) as f:
            for line in f:
                for player in self.all_players:
                    if line.strip().lower() == player.name.lower():
                        previously_drafted.append(player)
                        break
                else:
                    raise AttributeError(f'Player not found: {line.strip()}')
        
        draft = Draft(pick_ordinal, league_size)
        for player in previously_drafted:
            draft.draft(player)
        return draft
        
    def replacement_players(self):
        teams = [AutodraftTeam() for _ in range(12)]
        draft = Draft(self.pick_index+1, self.league_size, teams, self.all_players.copy(), self.draft_order)
        for i in self.draft_order:
            pick = teams[i].next_pick(draft)
            draft.available_players.remove(pick)
        return {pos: max(p.fan_pts for p in draft.available_players if p.position == pos) for pos in self.positions}
    
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
    
    def create_forecast(self, plan):
        draft = Draft(self.pick_index+1, self.league_size, [t.copy() for t in self.teams], self.available_players.copy(), self.draft_order.copy())
        return Forecast(draft, plan)

    def my_team(self):
        return self.teams[self.pick_index]
    
    def __str__(self):
        i = 0
        j = 0
        snake = 1
        result = []
        for _ in range(self.roster_size*self.league_size - len(self.draft_order)):
            result.append(f'Round {j+1} Team {i+1}: {self.teams[i].roster[j].name}')
            i += snake
            if snake == 0:
                j += 1
            if i == 11:
                snake -= 1
            elif i == 0:
                snake += 1
        return '\n'.join(result)

class Forecast:
    def __init__(self, draft, plan):
        self.draft = draft
        self.plan = plan
 
    def execute_plan(self):
        while len(self.plan) > 0 and len(self.draft.draft_order) > 0:
            self.draft.draft_to_next_decision()
            if len(self.draft.draft_order) == 0:
                break
            pick = self.best_player_available(self.draft.available_players, self.plan[0])
            self.draft.draft(pick)
            self.plan = self.plan[1:]
        self.draft.draft_to_end_of_round()

    def best_player_available(self, available_players, position):
        best_player = available_players[0]
        for player in available_players[1:]:
            if player.fan_pts > best_player.fan_pts and player.position == position:
                best_player = player
        return best_player
    
    def vorp_diff(self):
        return self.draft.vorp_for() - self.draft.vorp_against()
    
    def __str__(self):
        return f'VORP: {self.vorp_diff()} Picks: {self.draft.my_team().roster}'

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
        'K': 2
    }
    min_flex = 6
    search_depth = 6
    
    def __init__(self, roster=None):
        self.roster = roster or []

    def generate_plans(self):
        candidates = [(pos,) for pos in self.min_counts.keys()]
        return self.generate_plans_inner(candidates, len(self.roster), self.search_depth)
    
    def generate_plans_inner(self, prev_candidates, round, depth):
        print(f'Round {round}: {len(prev_candidates)}')
        if round > Draft.roster_size or depth <= 0:
            return prev_candidates
        candidates = []
        for prev_candidate in prev_candidates:
            for candidate in [prev_candidate + (pos,) for pos in self.min_counts.keys()]:
                counts = Counter(candidate)
                counts.update(player.position for player in self.roster)
                needed = sum(min_count - counts[pos] for pos, min_count in self.min_counts.items() if min_count > counts[pos])
                needed_flex = self.min_flex - (counts['RB'] + counts['WR'] + counts['TE'])
                # TODO: Fix bug that causes "needed" constraints to not be followed in considered candidates
                # Potentially `round` could be removed in favor of `len(prev_candidates[0]) + len(self.roster)`
                if max(needed, needed_flex) <= Draft.roster_size - round and all(counts[pos] <= max_count for pos, max_count in self.max_counts.items()):
                    candidates.append(candidate)
        return self.generate_plans_inner(candidates, round + 1, depth - 1)
    
    def next_pick(self, draft):
        draft_forecasts = [draft.create_forecast(plan) for plan in self.generate_plans()]
        best_forecast = 0
        forecast = draft_forecasts[best_forecast]
        forecast.execute_plan()
        best_vorp = forecast.vorp_diff()
        print(forecast)
        for i in range(1, len(draft_forecasts)):
            forecast = draft_forecasts[i]
            forecast.execute_plan()
            if forecast.vorp_diff() > best_vorp:
                best_forecast = i
                best_vorp = forecast.vorp_diff()
                print(forecast)
        pick = draft_forecasts[best_forecast].draft.my_team().roster[len(self.roster)]
        self.roster.append(pick)
        return pick

    def copy(self):
        return MinimaxTeam(self.roster.copy())
    
def main():
    draft = Draft.from_file('players.csv', 11)
    draft.draft_to_next_decision()
    draft.draft()
    draft.draft_to_end_of_round()
    print(draft.vorp_for() - draft.vorp_against())
    print(draft)

if __name__ == '__main__':
    main()