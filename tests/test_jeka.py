import unittest

from controllers.command_prompt import CommandPromptController
from controllers.interactive import InteractiveController
from serialysers.jsonSerialyser import JsonSerialyser
from serialysers.yamlSerialyser import YamlSerialyser
from serialysers.pickleSerialyser import PickleSerialyser
from services.controllerFactory import ControllerFactory
from services.matchFactory import MatchFactory
from tests.string_support import *


class TestStringMethods(unittest.TestCase):
    def test_json(self):
        serialyser = JsonSerialyser()
        service = MatchFactory()
        m = service.get_all()
        serialyser.save_matches(m)

    def test_json_load_matches(self):
        matches = JsonSerialyser.load_matches()
        self.assertIsInstance(matches, list)

    def test_yaml_load_matches(self):
        matches = YamlSerialyser.load_matches()
        self.assertIsInstance(matches, list)

    def test_pickle_load_matches(self):
        matches = PickleSerialyser.load_matches()
        self.assertIsInstance(matches, list)

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

if __name__ == '__main__':
    unittest.main()
