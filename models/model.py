class Match:
    """
    Class implements info about match
    """
    def __init__(self, country, team1, team2, res1, res2, date):
        self.country = country
        self.team1 = team1
        self.team2 = team2
        self.res1 = res1
        self.res2 = res2
        self.date = date

    def __str__(self):
        return ("%-10s : %-10s vs %-10s | %-2s:%-2s | %s-%s-%s" %
                (self.country, self.team1, self.team2, self.res1, self.res2,
                 self.date[0], self.date[1], self.date[2]))

    def equal(self, match):
        if isinstance(match, Match):
            if self.team1 == match.team1 and self.team2 == match.team2:
                return True
        else:
            return False
