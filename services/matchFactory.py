from models.model import Match


class MatchFactory:
    """
    Class produce list of match from hardcoded list
    """

    def __init__(self):
        self._matches = [Match('Lester', 'Everton', 2, 0, [26, 2, 2016]),
                        Match('MU', 'Everton', 3, 0, [27, 2, 2016]),
                        Match('Chelsea', 'Everton', 0, 0, [28, 2, 2016]),
                        Match('Arsenal', 'Everton', 1, 0, [29, 2, 2016]),
                        Match('Barcelona', 'Everton', 2, 0, [26, 2, 2016]),
                        Match('Real', 'Everton', 2, 0, [27, 2, 2016]),
                        Match('Sevilla', 'Everton', 2, 0, [28, 2, 2016]),
                        Match('Eibar', 'Everton', 2, 1, [29, 2, 2016]),
                        Match('Dynamo', 'Everton', 2, 4, [26, 2, 2016]),
                        Match('Vorskla', 'Everton', 2, 2, [27, 2, 2016]),
                        Match('Stal', 'Everton', 2, 6, [28, 2, 2016]),
                        Match('Dnipro', 'Everton', 2, 7, [29, 2, 2016])]

    def get_all(self):
        """
        Create classes from list
        :return:
        """
        res = []
        # for m in self.matches:
        #     res.append(Match(m[1], m[2], m[3], m[4], m[5]))
        # return res
        # return self.matches
        return list(self._matches);

    def __len__(self):
        return len(self._matches)

    def __str__(self):
        return str(self._matches)

    def __repr__(self):
        return repr(self._matches)

    def add(self, value):
        self._matches.append(value)

    def __setitem__(self, key, value):
        self._matches[key] = value

    def __getitem__(self, item):
        if isinstance(item, slice):
            return item(self._matches)
        elif isinstance(item, tuple):
            return [self._matches[x] for x in item]
        elif item == Ellipsis:
            return self._matches.copy()
        else:
            return self._matches[item]

    def __contains__(self, item):
        return item in self._matches

    def __iter__(self):
        for i in self._matches:
            yield i
