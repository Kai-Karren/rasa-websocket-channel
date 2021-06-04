from sanic import Sanic
from sanic.websocket import WebSocketProtocol
from sanic import Blueprint, response

from typing import Any, Awaitable, Callable, Dict, Iterable, List, Optional, Text

from rasa.core.channels.channel import InputChannel, OutputChannel, UserMessage, CollectingOutputChannel

import json

class WebsocketInputChannel(InputChannel):

    def name(self) -> Text:
        return "websocket_input_channel"

    def blueprint(
        self, on_new_message: Callable[[UserMessage], Awaitable[None]]
    ) -> Blueprint:

        sanic_blueprint = Blueprint("websocket_blueprint")

        @sanic_blueprint.websocket('/channel')
        async def feed(request, ws):

            output_channel = WebSocketOutputChannel(ws)

            while True:
                raw_request = await ws.recv()
                request = json.loads(raw_request)
                
                sender_id = request["id"]
                text = request["text"]

                input_channel = self.name()
                metadata = self.get_metadata(request)

                await on_new_message(
                    UserMessage(
                        text,
                        output_channel,
                        sender_id,
                        input_channel=input_channel,
                        metadata=metadata,
                    )
                )
            

        return sanic_blueprint


class WebSocketOutputChannel(OutputChannel):

    def __init__(self, ws) -> None:
        self.ws = ws

    def name(self) -> Text:
        return "websocket_output_channel"

    async def send_response(self, recipient_id, message):

        # only support text responses right now over websocket

        response = {
            "id": recipient_id,
            "text": message.get("text")
        }

        await self.ws.send(json.dumps(response))


