from .. import loader, utils
import random as rand

__version__ = (1, 0, 1)

@loader.tds

class MagicBall(loader.Module):
    """Магический Шар 8 в твоём Telegram."""
    strings = {
        "name": "MagicBall",
        }

    def ball_core(self, message):

        question_core = message.message.split()

        question = question_core[1:]

        answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется - «да»", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - «да»", "Да", "Пока не ясно, попробуй снова", "Спроси позже", "Лучше не расссказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - «нет»", "По моим данным - «нет»", "Перспективы не очень хорошие", "Весьма сомнительно"]

        return (
            f'<b>Твой вопрос:</b> <code>{" ".join(question)}<code>\n'
            '\n'
            f'<b>Мой ответ:</b> <i>{rand.choice(answers)}</i>'
        )

    @loader.command()

    async def ball(self, message):
        """<вопрос> - Магический Шар 8. Говорят что он выводит правду..."""
        await utils.answer(message, self.ball_core(message))