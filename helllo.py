from .. import loader, utils
__version__ = (1,0,0)
@loader.tds
class KuFiladey(loader.Module):
    strings {
      "name": "KuFiladey",
    }
    async def client(self):
        if "Termux" in utils.get_named_platform():
            raise loader.SelfUnload
    def hello_filadey(self,message):
        hello = 'Приветствую всех в Чате Филадея!'
        return (
            f'<b>{hello}</b>\n'
        )
    @loader.command(ru_doc="- Модуль был написан только для @FiIard_Chat")
    async def ku(self, message):
        await utils.answer(message, self.hello_filadey(message))