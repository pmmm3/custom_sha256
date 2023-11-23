# Dados estos datos quiero hacer una grafica  que muestre el número de intentos que se hacen por cada valor de bits
from matplotlib import pyplot as plt
import json
import numpy as np


def estimate(b):
        result = np.floor((np.log(1/2)/(np.log( 1-(1/(2**b))))))
        print(b,result)
        return result


with open("results.json", "r") as f:
        data = json.load(f)
        bits = []
        attempts = []
        for i in data:
            bits.append(i["bits"])
            attempts.append(i["attempts"])
            print(i["bits"],i["attempts"])
        plt.plot (bits,attempts, color="blue")
        plt.xlabel("Intentos")
        plt.ylabel("Bits")
        plt.title("Intentos vs Bits")
        plt.savefig("attempts_vs_bits_separate.png")
        plt.close()
        # estimated attempts in a graph to the right with red color
        
        
        estimated_attempts = []
        for i in bits:
            estimated_attempts.append(estimate(i))
        
        plt.plot(bits,estimated_attempts, color="red")
        # Add labels
        plt.xlabel("Intentos esperados")
        plt.ylabel("Bits")
        plt.title("Intentos esperados vs Bits")
        plt.savefig("attempts_estimated_vs_bits_separated.png")
        plt.close()