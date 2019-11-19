import datetime

import pytest

from aiogram.api.methods import Request, SendPoll
from aiogram.api.types import Chat, Message, Poll, PollOption
from tests.mocked_bot import MockedBot


class TestSendPoll:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(
            SendPoll,
            ok=True,
            result=Message(
                message_id=42,
                date=datetime.datetime.now(),
                poll=Poll(
                    id="QA",
                    question="Q",
                    options=[
                        PollOption(text="A", voter_count=0),
                        PollOption(text="B", voter_count=0),
                    ],
                    is_closed=False,
                ),
                chat=Chat(id=42, type="private"),
            ),
        )

        response: Message = await SendPoll(chat_id=42, question="Q?", options=["A", "B"])
        request: Request = bot.get_request()
        assert request.method == "sendPoll"
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(
            SendPoll,
            ok=True,
            result=Message(
                message_id=42,
                date=datetime.datetime.now(),
                poll=Poll(
                    id="QA",
                    question="Q",
                    options=[
                        PollOption(text="A", voter_count=0),
                        PollOption(text="B", voter_count=0),
                    ],
                    is_closed=False,
                ),
                chat=Chat(id=42, type="private"),
            ),
        )

        response: Message = await bot.send_poll(chat_id=42, question="Q?", options=["A", "B"])
        request: Request = bot.get_request()
        assert request.method == "sendPoll"
        assert response == prepare_result.result
