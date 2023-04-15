import asyncio
from bleak import BleakScanner
from parksmarterutils import parse_manufacturer_specific

async def main():  
    devices = await BleakScanner.discover()

    print(len(devices))

    # for d in devices:
    #     uuid = d.address
    #     uuid_bytes = uuid.encode('utf-8')
    #     # convert to bytearray
    #     uuid_bytearray = bytearray(uuid_bytes)

    #     result = parse_manufacturer_specific(uuid_bytearray)
    #     print(d)



    # async with BleakClient(target_client.address) as client:
    #     print("Initializing client connection.")
    #     processManager = ProcessManager(client, TYPE_2_VENDOR_SPECIFIC_CHARACTERISTIC)
    #     services_collection = await client.get_services()
    #     # services = services_collection.services
    #     characteristics = services_collection.characteristics

    #     for c in characteristics:
    #         print(characteristics.get(c))

    #     # listen
    #     await client.start_notify(TYPE_2_VENDOR_SPECIFIC_CHARACTERISTIC, processManager.characteristic_callback)
    #     await processManager.start()
        
    #     await asyncio.sleep(30.0)
    #     await client.stop_notify(TYPE_2_VENDOR_SPECIFIC_CHARACTERISTIC)
            
asyncio.run(main())