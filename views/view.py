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
            print("%-10s : %-10s vs %-10s | %-2s:%-2s | %s-%s-%s" % (match[0], match[1], match[2], match[3], match[4], match[5][0], match[5][1], match[5][2]))

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