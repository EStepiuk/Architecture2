import unittest

from controllers.command_prompt import CommandPromptController
from controllers.interactive import InteractiveController
from serialysers.jsonSerialyser import JsonSerialyser
from serialysers.yamlSerialyser import YamlSerialyser
from services.matchFactory import MatchFactory
from tests.string_support import *


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
        print(matches[0])
        self.assertTrue(matches[0].equal(matches[0]))

    def test_controller(self):
        contr = CommandPromptController()
        contr.navigation()

if __name__ == '__main__':
    unittest.main()
