from pymem import Pymem
from pymem.process import module_from_name
from requests import get


process_address = get("")


process = 0x4581938
var = float(input("Distance:",))


try:
    mem = Pymem("dota2.exe")
    game_module = module_from_name(mem.process_handle, "client.dll").lpBaseOfDll
    mem.write_float(game_module + process, var)
    print("Successful")
except Exception as e:
    print(f"error {e}")
