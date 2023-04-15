
def parse_company(param_bytearray: bytearray, param_short: int) -> int:
    b = param_bytearray[param_short + 3]
    return param_bytearray[param_short + 2] & 0xFF | (b & 0xFF) << 8

class BleModule:
    def __init__(self, company: int, serialNumber: str):
        self.company = company
        self.serialNumber = serialNumber

def get_serial_number(param_bytearray: bytearray) -> str:
    if len(param_bytearray) >= 19:
        stringBuilder = ""
        for i in range(18, 15, -1):
            stringBuilder += str(param_bytearray[i])
        return str(int(stringBuilder, 16))
    return ""

def parse_manufacturer_specific(param_bytearray: bytearray) -> BleModule:
    for s in range(0, 64):
        if param_bytearray[s] != 0 and s < 64:
            if param_bytearray[s + 1] == -1:
                i = parse_company(param_bytearray, s)
                if i == 487:
                    bleModule = BleModule(i, get_serial_number(param_bytearray))
                    return bleModule
                break
            s1 = param_bytearray[s] + 1 + s
            if s1 == s or s1 >= len(param_bytearray):
                break

