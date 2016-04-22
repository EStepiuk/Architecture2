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
        matches = self.factory.get_all()
        serialyser = self._get_serializer()
        while True:
            self.view.render_menu()
            inp = getch()
            if inp == '1':
                self.view.render_matches(self.service.get_country(matches, "England"))
            elif inp == '2':
                self.view.render_matches(self.service.get_country(matches, "Spain"))
            elif inp == '3':
                self.view.render_matches(self.service.get_country(matches, "Ukraine"))
            elif inp == '4':
                self.view.render_matches(self.service.get_team(matches, input("Enter team name:")))
            elif inp == '5':
                self.service.add_match(matches, input('Country: '), input('Team 1: '), input('Team 2: '),
                                       input('Team 1 goals count: '), input('Team 2 goals count: '),
                                       input('Date: '), input('Month: '), input('Year: '))
            elif inp == '6':
                matches = serialyser.load_matches()
            elif inp == '7':
                self.view.render_matches(matches)
            elif inp == '8':
                serialyser.save_matches(matches)
                exit(0)
