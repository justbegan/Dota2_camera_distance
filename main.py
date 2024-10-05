from pymem import Pymem
from pymem.process import module_from_name
from pymem.exception import MemoryReadError
import struct


def find_value_in_module():
    process_name = "dota2.exe"
    module_name = "client.dll" 
    value_type = 'float'
    target_value = 1200.0
    pm = Pymem(process_name)
    module = module_from_name(pm.process_handle, module_name)
    base_address = module.lpBaseOfDll
    module_size = module.SizeOfImage

    if value_type == 'float':
        target_value = float(target_value)
        bytes_to_read = 4
        format_string = 'f'
    else:
        raise ValueError("Unsupported value type. Use 'float'.")
    addresses = []
    print("in progress")
    for address in range(base_address, base_address + module_size, bytes_to_read):
        try:
            bytes = pm.read_bytes(address, bytes_to_read)
            read_value = struct.unpack(format_string, bytes)[0]
            if read_value == target_value:
                addresses.append(address)
        except (MemoryReadError, struct.error):
            pass

    return [addr for addr in addresses]


for i in find_value_in_module():
    var = float(input("Distance:"))
    try:
        mem = Pymem("dota2.exe")
        mem.write_float(i, var)
        print("Successful")
    except Exception as e:
        print(f"error {e}")
