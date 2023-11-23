""" Get a example of loop to test the custom sha256 function and save the result in a file. """
from custom_sha256 import custom_sha256
import json
import time
bits = range(1, 9)
for bit in bits:
    print(f"Calculando hash con {bit} bits...")
    start_time = time.time()
    result = custom_sha256("Hola", "0"*32, bit)
    end_time = time.time()
    result["time"] = end_time - start_time
    print(f"---> Intentos: {result['attempts']} - Tiempo: {result['time']} segundos")
    with open("results.json", "a") as f:
        f.write(f"{json.dumps(result, indent=4)}\n")
    
            

            





