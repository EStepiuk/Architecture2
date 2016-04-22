import configparser

from controllers.command_prompt import CommandPromptController
from controllers.interactive import InteractiveController


class ControllerFactory():
    """
    Class produce controller. For change controller use config.ini, tag controller
    attribute method. In case either 'command_line' produce CommandLineController or 'console' for MatchesController
    """

    def get_controller(self):
        parser = configparser.ConfigParser()
        parser.read("config.ini")
        method = parser["controller"]['method']
        if method == "command_line":
            return CommandPromptController()
        elif method == "console":
            return InteractiveController()
        else:
            return None
