import hashlib
import random
from pprint import pprint


def custom_sha256(texto: str, cadena_hex: str, bits: int) -> dict:
    """
    Función que calcula el hash SHA256 de un texto dado, concatenado con una cadena dada, y
    que cumpla con la condición de que los primeros b bits del hash sean cero.

    Parameters:
    ----------
    texto: str
        Texto a utilizar para calcular el hash.
    cadena_hex: str
        Cadena a concatenar con el texto, minimo 32 caracteres.
    bits: int
        Número de bits a verificar del hash.

    Returns:
    --------
    dict
        Diccionario con la información del hash calculado.
    """
    if len(cadena_hex) < 32:
        raise ValueError("La cadena debe tener al menos 32 caracteres")
    id = texto + cadena_hex
    intentos = 0
    while True:
        x = random.randbytes(32).hex()
        data_to_hash = id + x
        hash_value = hashlib.sha256(data_to_hash.encode()).hexdigest()
        if hash_value.startswith("0" * bits):
            return {"id": id, "x": x, "hash": hash_value, "attempts": intentos, "bits": bits}
        intentos += 1
