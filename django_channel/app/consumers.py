from channels.consumer import SyncConsumer
from channels.consumer import AsyncConsumer


class MyConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("connection established....")

    def websocket_receive(self, event):
        print("message received...")

    def websocket_disconnect(self, event):
        print("connection closed...")


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connection established....")

    async def websocket_receive(self, event):
        print("message received...")

    async def websocket_disconnect(self, event):
        print("connection closed...")