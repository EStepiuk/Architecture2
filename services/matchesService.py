from models.model import Match
from views.view import ConsoleView


class MatchesService(object):
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

    def add_match(self, matches):
        """
        Function add match to list of matches
        :param matches:
        :return:
        """
        view = ConsoleView()
        view.printMessage("Enter country: ")
        country = view.inputFromConsole()
        view.printMessage("Enter first team name: ")
        team1 = view.inputFromConsole()
        view.printMessage("Enter second team name: ")
        team2 = view.inputFromConsole()
        view.printMessage("Enter first team score: ")
        res1 = view.inputFromConsole()
        view.printMessage("Enter second team score: ")
        res2 = view.inputFromConsole()
        view.printMessage("Enter day: ")
        day = view.inputFromConsole()
        view.printMessage("Enter month: ")
        month = view.inputFromConsole()
        view.printMessage("Enter year: ")
        year = view.inputFromConsole()

        matches.append(Match(country, team1, team2, res1, res2, [day, month, year]))


