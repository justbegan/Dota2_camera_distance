from pymem import Pymem
from pymem.process import module_from_name
from requests import get

try:
    process_address = get("https://raw.githubusercontent.com/justbegan/Dota2_camera_distance/master/data.json")
except Exception as e:
    raise Exception(e)

data = f"0x{process_address.json()['address']}"
process = int(data, 16)
var = float(input("Distance:"))


try:
    mem = Pymem("dota2.exe")
    game_module = module_from_name(mem.process_handle, "client.dll").lpBaseOfDll
    mem.write_float(game_module + process, var)
    print("Successful")
except Exception as e:
    print(f"error {e}")
