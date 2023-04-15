import asyncio
from bleak import BleakScanner
from bleak.backends.scanner import AdvertisementData

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
    print("Found %d devices." % len(scan_results))

    for data in scan_results:
        adv_data: AdvertisementData = data[1]
        if not adv_data:
            continue

        man_data = adv_data.manufacturer_data
        print(man_data)

        
    

asyncio.run(main())