"""
Holds stats about each player, such as expert rank, name, position, and fantasy
point projection.
"""
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
