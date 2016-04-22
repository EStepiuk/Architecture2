import sys

from getopt import getopt
from controllers.base import BaseController


class CommandPromptController(BaseController):
    def navigation(self):
        serialyser = self._getSerialiseMethod()
        matches = self.factory.get_all()
        self.command_interpreter(matches)

    def command_interpreter(self, matches):
        opts, args = getopt(sys.argv[1:], 'aht:c:', ['add', 'help', 'team=', 'country='])
        if opts.__len__() == 0:
            self.view.render_matches(matches)
        elif opts.__len__() > 1 or (opts[0][0] in ('-a', '--add') and args.__len__() != 8) or opts[0][0] in ('-h', '--help'):
            self.view.render_console_help()
        elif opts[0][0] in ('-a', '--add'):
            self.service.add_match(matches, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
            self.view.render_matches(matches)
        elif opts[0][0] in ('-t', '--team'):
            self.view.render_matches(self.service.get_team(matches, opts[0][1]))
        elif opts[0][0] in ('-c', '--country'):
            self.view.render_matches(self.service.get_country(matches, opts[0][1]))
        exit(0)
