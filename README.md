# Rasa Custom WebSocket Channel Connector

This repo contains an example on how a Rasa custom channel connector could be realized using the WebSocket protocol.
The WebSocket server uses Sanics WebSocket implementation that is passed to Rasa's Sanic server as a sanic blueprint
from the custom input channel as described in [Rasa Custom Connectors](https://rasa.com/docs/rasa/connectors/custom-connectors/)

Has been tested with Rasa 2.6

## Usage

Add the custom channel into your Rasa directory (or a sub-folder).

Then add the following to your Rasa credentials.yml file.
```
websocket_channel.WebsocketInputChannel:
```

Then you can run rasa with your custom channel with

```
rasa run
```

Or with

```
rasa run --credentials credentials.yml
```

## Example Request and Response

The example implemtents the following request and response formats.

### Request
```
{
    "id": "your id"
    "text":"user input"
}
```

### Response
```
{
    "id":"your id",
    "text": "the response to your input"
}
```

