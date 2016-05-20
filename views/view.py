__author__ = 'Meggapixxel'


class ConsoleView(object):
    """
    Class shows info on console
    """
    @staticmethod
    def render_matches(self, matches):
        """
        Show list of match
        :param matches:
        :return:
        """

        for match in matches:
            print(match)
    @staticmethod
    def render_menu(self):
        """
        Show menu cases
        """
        print("""
        1. Select team
        2. Add match
        3. Load matches from file
        4. Show all matches
        5. Exit
        """)
    @staticmethod
    def msg_output(self, mes):
        print(mes)
    @staticmethod
    def render_console_help(self):
        print("""
        footballtable [option] [args]
        options:
        -a, --add <team1> <team2> <team1 goals> <team2 goals> <date> <month> <year>
        -t, --team= <team>
        -h, --help
        """)