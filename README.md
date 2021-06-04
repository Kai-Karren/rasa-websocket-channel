# Rasa Custom WebSocket Channel

This repo contains an example on how a Rasa custom channel could be realized using the WebSocket protocol.

Has been tested with Rasa 2.6

## Usage

Add the following to your Rasa credentials.yml file.
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

