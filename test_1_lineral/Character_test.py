from character import Character

class Character_test(Character):
    def __init__(self, person=None, web=None):
        super().__init__(person, web)

    def draw(self, display):
        self.person.draw(display)

