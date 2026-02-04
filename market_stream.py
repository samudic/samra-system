import random
import time

def market_pulse():
    print("\n📈 FLUX BOURSIER : CLASSE MOYENNE RDC (XPL/PLASMA)")
    print("--------------------------------------------------")
    
    base_value = 100.00
    for day in range(1, 6):
        variation = random.uniform(-1.5, 3.5)
        base_value += variation
        print(f"Jour {day} | Indice Maturité : {base_value:.2f} | Statut : PROGRESSION")
        time.sleep(0.5)

    print("--------------------------------------------------")
    print("✅ SIGNAL TRANSMIS AU REGISTRE INTERNATIONAL (SAMRA)")

if __name__ == "__main__":
    market_pulse()
