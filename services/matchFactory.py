from models.model import Match


class MatchFactory:
    """
    Class produce list of match from hardcoded list
    """

    def __init__(self):
        self.matches = [['England', 'Lester', 'Everton', 2, 0, [26, 2, 2016]],
                        ['England', 'MU', 'Everton', 3, 0, [27, 2, 2016]],
                        ['England', 'Chelsea', 'Everton', 0, 0, [28, 2, 2016]],
                        ['England', 'Arsenal', 'Everton', 1, 0, [29, 2, 2016]],
                        ['Spain', 'Barcelona', 'Everton', 2, 0, [26, 2, 2016]],
                        ['Spain', 'Real', 'Everton', 2, 0, [27, 2, 2016]],
                        ['Spain', 'Sevilla', 'Everton', 2, 0, [28, 2, 2016]],
                        ['Spain', 'Eibar', 'Everton', 2, 1, [29, 2, 2016]],
                        ['Ukraine', 'Dynamo', 'Everton', 2, 4, [26, 2, 2016]],
                        ['Ukraine', 'Vorskla', 'Everton', 2, 2, [27, 2, 2016]],
                        ['Ukraine', 'Stal', 'Everton', 2, 6, [28, 2, 2016]],
                        ['Ukraine', 'Dnipro', 'Everton', 2, 7, [29, 2, 2016]]]

    def get_all(self):
        """
        Create classes from list
        :return:
        """
        res = []
        for m in self.matches:
            res.append(Match(m[0], m[1], m[2], m[3], m[4], m[5]))
        return res
