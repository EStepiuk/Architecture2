from models.model import Match


class MatchesService:
    """
    Class implements actions with matches
    """

    def get_country(self, matches, countryName):
        """
        Find all matches in selected country
        :param matches:
        :param countryName:
        :return:
        """
        res = []
        for m in matches:
            if m.country == countryName:
                res.append(m)
        return res

    def get_team(self, matches, teamName):
        """
        Find all matches in selected team
        :param matches:
        :param teamName:
        :return:
        """
        res = []
        for m in matches:
            if m.team1 == teamName or m.team2 == teamName:
                res.append(m)
        return res

    def add_match(self, matches, country, team1, team2, res1, res2, day, month, year):
        """
        Function add match to list of matches
        :param matches:
        :return:
        """
        matches.append(Match(country, team1, team2, res1, res2, [day, month, year]))
