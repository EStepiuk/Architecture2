__author__ = 'Meggapixxel'


class ConsoleView(object):
    """
    Class shows info on console
    """

    def render_matches(self, matches):
        """
        Show list of match
        :param matches:
        :return:
        """

        for match in matches:
            print(match)

    def render_menu(self):
        """
        Show menu cases
        """
        print("""
        1. England
        2. Spain
        3. Ukraine
        4. Select team
        5. Add match
        6. Load matches from file
        7. Show all matches
        8. Exit
        """)

    def msg_output(self, mes):
        print(mes)

    def render_console_help(self):
        print("""
        footballtable [option] [args]
        options:
        -a, --add <country> <team1> <team2> <team1 goals> <team2 goals> <date> <month> <year>
        -c, --country= <country>
        -t, --team= <team>
        -h, --help
        """)