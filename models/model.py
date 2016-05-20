__author__ = 'Kryvonis'


class Match:
    def __init__(self, team1, team2, res1, res2, date):
        """
        initializer
        :param team1: first team
        :param team2: second team
        :param res1: result first team
        :param res2: result second team
        :param date: date of match
        :return: none
        """
        self._team_one = team1
        self._team_two = team2
        self._res_one = res1
        self._res_two = res2
        self._date = date

    def __str__(self):
        return "{} - {},{}:{},{}".format(self._team_one, self._team_two, self._res_one, self._res_two, self._date)

    def __repr__(self):
        return "Game({} - {},{}:{},{})".format(self._team_one, self._team_two, self._res_one, self._res_two, self._date)

    def __eq__(self, other):
        if isinstance(other, Match):
            return self._team_one == other._team_one and \
                   self._team_two == other._team_two and \
                   self._res_one == other._res_one and \
                   self._res_two == other._res_two and \
                   self._date == other._date
        return False

    def __lt__(self, other):
        if isinstance(other, Match):
            return self._team_one < other._team_one and \
                   self._team_two < other._team_two and \
                   self._res_one < other._res_one and \
                   self._res_two < other._res_two and \
                   self._date < other._date
        return False

    def __hash__(self):
        return hash(self._date)
