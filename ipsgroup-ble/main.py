import asyncio
from bleak import BleakScanner
from bleak.backends.scanner import AdvertisementData
from bleak.backends.device import BLEDevice
from parksmarterutils import *

async def main():
    stop_event = asyncio.Event()

    scan_results = []

    def callback(device, advertising_data):
        scan_results.append((device, advertising_data))
        pass

    async with BleakScanner(callback) as scanner:
        await scanner.start()

        print("Scanning...")

        await asyncio.sleep(5.0)
        await scanner.stop()
        # Important! Wait for an event to trigger stop, otherwise scanner
        # will stop immediately.
        # await stop_event.wait()

    # scanner stops when block exits
    print("Scan complete.")

    number_of_each_manufacturer_id = {}

    for data in scan_results:
        device: BLEDevice = data[0]
        adv_data: AdvertisementData = data[1]
        if not adv_data or len(list(adv_data.manufacturer_data.values())) == 0:
            continue
        
        manufacturer_data = adv_data.manufacturer_data
        for key in manufacturer_data:
            count = number_of_each_manufacturer_id.get(key, 0)
            number_of_each_manufacturer_id[key] = count + 1

    for key in number_of_each_manufacturer_id:
        print(f"{key}: {number_of_each_manufacturer_id[key]}")

    # loop through one adv data for each manufacturer id
    list_of_man_keys = list(number_of_each_manufacturer_id.keys())
    for key in list_of_man_keys:
        for data in scan_results:
            device: BLEDevice = data[0]
            adv_data: AdvertisementData = data[1]
            if not adv_data or len(list(adv_data.manufacturer_data.values())) == 0:
                continue
            
            manufacturer_data = adv_data.manufacturer_data
            if key in manufacturer_data:
                print(f"{key}: {manufacturer_data[key]}")
                break

asyncio.run(main())