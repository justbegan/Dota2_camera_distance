import pymem
import pymem.process

# Открываем процесс
pm = pymem.Pymem("dota2.exe")  # Замените "имя_процесса.exe" на имя вашего процесса

# Получаем базовый адрес процесса
base_address = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
# Значение float, которое вы ищете
target_float_value = 1200.0  # Замените на значение, которое вы ищете

# Размер типа float в байтах
float_size = 4  # Для большинства платформ размер типа float составляет 4 байта

# Размер блока сканирования памяти
scan_size = 4096  # Можно настроить по вашему усмотрению

# Проход по блокам памяти в поисках значения float
print(base_address)
for address in range(base_address, base_address + 0x7fffffff):
    try:
        # Читаем значение float из текущего адреса
        value = pm.read_float(address)
        # Если значение совпадает с целевым, печатаем адрес
        if value == target_float_value:
            print("Найдено значение {} по адресу: 0x{:x}".format(target_float_value, address))
    except pymem.exception.MemoryReadError:
        # Пропускаем ошибки доступа к памяти
        pass
