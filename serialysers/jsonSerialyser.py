import json

from models.model import Match


class MatchEncoder(json.JSONEncoder):
    """
    Json encoder for Match object
    """

    def default(self, o):
        if isinstance(o, Match):
            return {
                "team1": o._team_one,
                "team2": o._team_two,
                "res1": o._res_one,
                "res2": o._res_two,
                "date": o._date
            }
        return json.JSONEncoder


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
                matches.append(m)
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
