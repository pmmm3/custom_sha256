import hashlib
import random

def custom_sha256(texto, hex, bits):
    """
    Función que calcula el hash SHA256 de un texto dado, concatenado con una cadena dada, y 
    que cumpla con la condición de que los primeros b bits del hash sean cero.

    Parameters:
    ----------
    texto: str
        Texto a utilizar para calcular el hash.
    hex: str
        Cadena a concatenar con el texto.
    bits: int
        Número de bits a verificar del hash.

    Returns:
    --------
    dict
        Diccionario con la información del hash calculado.
    """

    datos = texto + hex

    intentos = 0

    while True:
        random_x = format(random.getrandbits(256), '0256x')

        data_to_hash = datos + random_x

        # Calcular el hash SHA256
        hash_value = hashlib.sha256(data_to_hash.encode()).hexdigest()

        # Verificar si los primeros b bits del hash son cero
        if hash_value[:b] == '0' * b:
            # Si es así, devolver la información
            return {
                'id': concatenated_data,
                'x': random_x,
                'hash': hash_value,
                'attempts': attempts
            }

        # Incrementar el número de intentos
        attempts += 1

# Ejemplo de uso:
text_input = "Ejemplo"
hex_string_input = "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f"
b_input = 4

result = custom_sha256(text_input, hex_string_input, b_input)
print(result)
