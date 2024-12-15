from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("connection established....")
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self, event):
        print(f"message received...  {event['text']}")

    def websocket_disconnect(self, event):
        print("connection closed...")
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connection established....")
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
       print(f"message received...  {event['text']}")

    async def websocket_disconnect(self, event):
        print("connection closed...")
        raise StopConsumer()