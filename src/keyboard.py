from src.item import Item


class MixinLang:
    Language = {'EN', 'RU'}

    def __init__(self):
        self.language = 'EN'


    def change_lang(self):
        """
        Меняет атрибут клавиатуры language (раскладку клавиатуры).
        """
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'


class Keyboard(Item, MixinLang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)






