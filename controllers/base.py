import configparser

from serialysers.jsonSerialyser import JsonSerialyser
from serialysers.pickleSerialyser import PickleSerialyser
from serialysers.yamlSerialyser import YamlSerialyser
from services.matchFactory import MatchFactory
from services.matchesService import MatchesService
from views.view import ConsoleView



class BaseController:

    def __init__(self):
        self.view = ConsoleView()
        self.factory = MatchFactory()
        self.service = MatchesService()

    def _getSerialiseMethod(self):
        """
        Choose serialisation method from config file
        :return:
        """
        parser = configparser.ConfigParser()
        parser.read("property.cfg")
        method = parser["serialize_method"]['method']
        if method == "pickle":
            return PickleSerialyser()
        elif method == "yaml":
            return YamlSerialyser()
        elif method == "json":
            return JsonSerialyser()

    def navigation(self):
        pass
