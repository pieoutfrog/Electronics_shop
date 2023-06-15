from src.item import Item


class MixingLanguage:
    def __init__(self):
        self.__language = 'EN'

    def get_lang(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixingLanguage):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixingLanguage.__init__(self)

    @property
    def language(self):
        return self.get_lang()
