
class My_Services:
    async def get_services(self, client):
        print("Services:")
        print(dir(client))
        services = await client.get_services()
        print("services loop...")
        for service in services:
            print([services])
            print(service)
            char = await client.get_characteristic()
            print(f"Characteristic: {char}")
            print(f"UUID: {char.uuid}")
            print(f"Handle: {char.handle}")
            print(f"Properties: {char.properties}")
            data = await char.read()
            print(f"Data: {data}")
            return data
