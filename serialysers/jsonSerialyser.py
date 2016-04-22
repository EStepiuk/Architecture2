import json

from models.model import Match


class MatchEncoder(json.JSONEncoder):
    """
    Json encoder for Match object
    """

    def default(self, o):
        if isinstance(o, Match):
            return {"country": o.country,
                    "team1": o.team1,
                    "team2": o.team2,
                    "res1": o.res1,
                    "res2": o.res2,
                    "date": o.date
                    }
        return json.JSONEncoder.default(self, o)


class JsonSerialyser:
    @staticmethod
    def load_matches(fileName='matches.json'):
        """
        Load objects from file
        :param fileName:
        :return:
        """
        with open(fileName, 'rt') as f:
            list_of_matches = json.load(f)
            matches = []
            for m in list_of_matches:
                matches.append(Match(m["country"], m["team1"], m["team2"],
                                     m["res1"], m["res2"], m["date"]))
            return matches

    @staticmethod
    def save_matches(matches, fileName='matches.json'):
        """
        Save objects to file
        :param matches:
        :param fileName:
        :return:
        """
        with open(fileName, 'wt') as f:
            json.dump(matches, f, cls=MatchEncoder, indent=4)
