# Dados estos datos quiero hacer una grafica  que muestre el número de intentos que se hacen por cada valor de bits
from matplotlib import pyplot as plt
import json
import numpy as np
def estimate(b):
        result = np.floor((np.log(1/2)/(np.log(1-(1/(2**b))))))
        print(b,result)
        return result


with open("results.json", "r") as f:
        data = json.load(f)
        bits = []
        attempts = []
        for i in data:
            bits.append(i["bits"])
            attempts.append(i["data"]["attempts"])
            print(i["bits"],i["data"]["attempts"])
        plt.plot (bits,attempts, color="blue")
        
        # estimated attempts in the same graph with red color
        estimated_attempts = []
        for i in bits:
            estimated_attempts.append(estimate(i))
        
        plt.plot(bits,estimated_attempts, color="red")
        # Add legend for each line
        plt.legend(["Attempts", "Estimated attempts"])
        # Add labels
        plt.xlabel("Attempts")
        plt.ylabel("Bits")
        plt.title("Attempts vs Bits with estimated attempts")
        plt.savefig("attempts_vs_bits2.png")
        plt.close()        
        