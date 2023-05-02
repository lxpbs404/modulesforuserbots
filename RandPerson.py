from .. import loader, utils
import random as rand
__version__ = (1,0,0)
@loader.tds
class RandomPerson(loader.Module):
    """Рандомный человек."""
    strings = {
        "name": "RandPerson",
    }
    def 
    @loader.command()
    async def randperson(self, message):
        """- Показывает рандомного человека из чата Филадея\nКод спизжен у @yebannq"""
        await utils.answer(message, self.randmeme(message))
