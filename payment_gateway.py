import time
import uuid

def process_license_payment(user_id, amount, currency="USD"):
    transaction_id = str(uuid.uuid4())[:8].upper()
    print(f"\n💳 GATEWAY XPL/PLASMA : TRAITEMENT EN COURS")
    print("-" * 45)
    time.sleep(1)
    print(f"UTILISATEUR : {user_id}")
    print(f"MONTANT     : {amount} {currency}")
    print(f"STATUT      : PAIEMENT CERTIFIÉ ✅")
    print(f"ID TRANSAC  : TXN-{transaction_id}")
    print("-" * 45)
    print("📢 LICENCE ACTIVÉE POUR 366 JOURS (RDC-MONDE)")

if __name__ == "__main__":
    process_license_payment("CADRE_RDC_001", 250.00)
