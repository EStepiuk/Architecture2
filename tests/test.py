import unittest

from controllers.command_prompt import CommandPromptController
from controllers.interactive import InteractiveController
from serialysers.jsonSerialyser import JsonSerialyser, MatchEncoder
from serialysers.yamlSerialyser import YamlSerialyser
from services.controllerFactory import ControllerFactory
from services.matchFactory import MatchFactory
from services.matchesService import MatchesService
from models.model import Match
from tests.string_support import *
from serialysers.pickleSerialyser import PickleSerialyser


class TestStringMethods(unittest.TestCase):
    def test_json(self):
        serialyser = JsonSerialyser()
        service = MatchFactory()
        m = service.get_all()
        serialyser.save_matches(m)

    def test_config(self):
        controller = InteractiveController()
        obj = controller._get_serializer()
        res = isinstance(obj, JsonSerialyser)
        self.assertEqual(res, True, "OK")

    def test_json_serialise(self):
        JsonSerialyser().save_matches(MatchFactory().get_all())
        strIO = get_string_from_serialyser()
        strIO.seek(0)
        with open("matches.json", "rt") as f:
            for line in f:
                self.assertEqual(strIO.readline(), line)

    def test_yaml_serialise(self):
        YamlSerialyser().save_matches(MatchFactory().get_all())
        strIO = get_string_from_serialyser("matches.yaml")
        strIO.seek(0)
        with open("matches.yaml", "rt") as f:
            for line in f:
                self.assertEqual(strIO.readline(), line)

    def test_teamPrint(self):
        matches = MatchFactory().get_all()
        self.assertTrue(matches[0] == matches[0])
        self.assertFalse(matches[0] == matches[1])

    def test_get_team(self):
        matches = MatchFactory().get_all()
        self.assertIsNotNone(MatchesService().get_team(matches, "MU"))


    def test_add_match(self):
        matches = MatchFactory().get_all()
        self.assertIsNone(MatchesService()
                          .add_match(matches, 'Lester', 'Everton', 2, 0, 26, 2, 2016))

    def test_json_load_matches(self):
        matches = JsonSerialyser.load_matches()
        self.assertIsInstance(matches, list)

    def test_yaml_load_matches(self):
        matches = YamlSerialyser.load_matches()
        self.assertIsInstance(matches, list)

    def test_pickle_load_matches(self):
        matches = PickleSerialyser.load_matches()
        self.assertIsInstance(matches, list)

    def test_pickle_save_matches(self):
        matches = PickleSerialyser.load_matches()
        self.assertIsNone(PickleSerialyser.save_matches(matches))

    def test_json_defaul(self):
        self.assertIsNotNone(MatchEncoder().default(""))

    def test_model_str(self):
        m = Match('Lester', 'Everton', 2, 0, [26, 2, 2016])
        self.assertIsNotNone(m.__str__())

    def test_get_matches_get_country(self):
        self.assertIsNotNone(ControllerFactory.get_controller("configtest1.ini"))
        self.assertIsNotNone(ControllerFactory.get_controller("configtest2.ini"))
        self.assertIsNone(ControllerFactory.get_controller("configtest3.ini"))


if __name__ == '__main__':
    unittest.main()
