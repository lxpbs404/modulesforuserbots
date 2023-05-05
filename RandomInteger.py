from .. import loader, utils
import random as rd
__version__ = (1, 1, 0)
@loader.tds
class RandomInteger(loader.Module):
    strings = {
        "name": "RandomInteger",
    }
    def rdint_core(self, message):
        Random = message.message.split(" ")
        Integers = rd.randint(int(Random[1]), int(Random[2]))
        try:
            return (
            f'<i>Рандомное число:</i> <b>{Integers}</b>'
            )
        expect:
            return (

            f'<i>Введите параметры</i>'

            )
    @loader.command()
    async def rdint(self, message):
        """<1-ый параметр> <2-ой параметр> - Выводит рандомное число (параметры)"""
        await utils.answer(message, self.rdint_core(message))
