from channels.consumer import SyncConsumer

class MyConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("connection established....")

    def websocket_receive(self, event):
        print("message received...")

    def websocket_disconnect(self, event):
        print("connection closed...")