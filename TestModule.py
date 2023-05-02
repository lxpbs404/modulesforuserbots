from .. import loader, utils
class TestModule(loader.Module):
    """Test Mldule by @proshiv_rn9"""
    
    strings = {
        "name": "ModuleExample"
        "text": "Тестовый текст"
    }
    
    @loader.command()
    async def example(self, message):
        """- just for test"""
        
        await utils.answer(message, self.strings["text"])