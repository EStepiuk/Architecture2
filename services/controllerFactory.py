import configparser

from controllers.command_line_controller import CommandLineController
from controllers.controller import MatchesController


class ControllerFactory():
    """
    Class produce controller. For change controller use property.cfg, tag controller
    attribute method. In case either 'command_line' produce CommandLineController or 'console' for MatchesController
    """


    def get_controller(self):
        parser = configparser.ConfigParser()
        parser.read("property.cfg")
        method = parser["controller"]['method']
        if method == "command_line":
            return CommandLineController() 
        elif method == "console":
            return MatchesController()
        else:
            return None
