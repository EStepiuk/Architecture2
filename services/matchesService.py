from models.model import Match


class MatchesService:
    """
    Class implements actions with matches
    """
    @staticmethod
    def get_team(matches, teamName):
        """
        Find all matches in selected team
        :param matches:
        :param teamName:
        :return:
        """
        res = []
        for m in matches:
            if m._team_one == teamName or m._team_two == teamName:
                res.append(m)
        return res

    @staticmethod
    def add_match(matches, team1, team2, res1, res2, day, month, year):
        """
        Function add match to list of matches
        :param matches:
        :return:
        """
        matches.append(Match(team1, team2, res1, res2, [day, month, year]))
