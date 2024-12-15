from channels.consumer import SyncConsumer, AsyncConsumer



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


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connection established....")

    async def websocket_receive(self, event):
        print("message received...")

    async def websocket_disconnect(self, event):
        print("connection closed...")