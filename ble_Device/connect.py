import asyncio

class My_Connect:
    async def connect_to_device(self, client):
        await asyncio.sleep(2)
        if client.is_connected:
            print("Connected to device.")
        else:
            print("Not connected to device.")