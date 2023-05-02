from .. import loader, utils
import random as rand
__version__ = (1,0,0)
@loader.tds
class RandomPerson(loader.Module):
    """Рандомный человек."""
    strings = {
        "name": "RandPerson",
    }
    def randmeme_core(self, message):
        persones = ["Филард", "Фин", "Анозерггс", "Джекизз", "Ексур", "Яйцелиз Мурино", "Ямадей", "Кальк пдров", "Стакед", "Гг", "Даниила"]
        return (
            '<b>Кто ты из чата Филадея?<b>\n'
            '\n'
            f'<b>Ты {rand.choice(persones)}</b>'
        )
    @loader.command()
    async def randperson(self, message):
        """- Показывает рандомного человека из чата Филадея."""
        await utils.answer(message, self.randmeme_core(message))