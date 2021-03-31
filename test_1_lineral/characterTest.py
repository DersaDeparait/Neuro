from common.web import Web
from common.character import Character
from test_1_lineral.personTest import PersonTest


class CharacterTest(Character):

    def __init__(self, person=None, web=None) -> None:
        super(CharacterTest, self).__init__(person, web)
