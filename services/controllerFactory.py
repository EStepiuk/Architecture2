import configparser

from controllers.command_prompt import CommandPromptController
from controllers.interactive import InteractiveController


class ControllerFactory:
    """
    Class produce controller. For change controller use config.ini, tag controller
    attribute method. In case either 'command_line' produce CommandLineController or 'console' for MatchesController
    """

    @staticmethod
    def get_controller(filename="config.ini"):
        parser = configparser.ConfigParser()
        parser.read(filename)
        method = parser["controller"]['method']
        if method == "command_prompt":
            return CommandPromptController()
        elif method == "interactive":
            return InteractiveController()
        else:
            return None
