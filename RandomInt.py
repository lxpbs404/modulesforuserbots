from .. import loader, utils
import random as rand
__version__ = (1,0,1)
@loader.tds
class RandomInt(loader.Module):
    """Рандомное число"""
    strings = {
        "name": "RandomInt",
    }
    def randomint_core(self, message):
        integers = rand.randint(1, 100)
        return (
            f'<i>Рандомная цифра:</i> <b>{integers}</b>'
        )
    @loader.command()
    async def randomint(self, message):
        """Выводит рандомное число от 1 до 100"""
        await utils.answer(message, self.randomint_core(message))