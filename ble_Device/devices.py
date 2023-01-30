import asyncio
from bleak import BleakClient
from discovery import My_Discovery
from connect import My_Connect
from service import My_Services

class My_Device:
    async def device(self):
        new_device = My_Discovery()
        if new_device:
            print(f"Device_found\nName :{new_device.name}\nMac add:{new_device.address}")
            print("Connecting to...")
            async with BleakClient(new_device.address) as client:
                connect = My_Connect()
                await connect.connect_to_device(client)
                services = My_Services()
                await services.get_services(client)
        else:
            print("Device not found.")
