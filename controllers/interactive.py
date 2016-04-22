import configparser

from getch import getch
from controllers.base import BaseController


class InteractiveController(BaseController):
    """
    Controller witch connect console view and matches services
    """

    def navigation(self):
        """
        Main function for navigation in program
        :return:
        """
        matches = self.factory.getAllMatches()
        serialyser = self._getSerialiseMethod()
        while True:
            self.view.showMenu()
            inp = getch()
            if inp == '1':
                self.view.showMatches(self.service.getMatchByCountry(matches, "England"))
            elif inp == '2':
                self.view.showMatches(self.service.getMatchByCountry(matches, "Spain"))
            elif inp == '3':
                self.view.showMatches(self.service.getMatchByCountry(matches, "Ukraine"))
            elif inp == '4':
                self.view.showMatches(self.service.getMatchByTeam(matches, input("Enter team name:")))
            elif inp == '5':
                self.service.addMatch(matches, input('Country: '), input('Team 1: '), input('Team 2: '),
                                      input('Team 1 goals count: '), input('Team 2 goals count: '),
                                      input('Date: '), input('Month: '), input('Year: '))
            elif inp == '6':
                matches = serialyser.loadMatches()
            elif inp == '7':
                self.view.showMatches(matches)
            elif inp == '8':
                serialyser.saveMatches(matches)
                exit(0)
