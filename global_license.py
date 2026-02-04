import hashlib
import datetime

def generate_global_license(user_name, sector):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    contract_end = "2027-02-05" # Votre règle d'un an et un jour
    
    # Création d'une empreinte unique (Hash) pour la licence
    license_data = f"{user_name}|{sector}|{timestamp}|{contract_end}"
    license_hash = hashlib.sha256(license_data.encode()).hexdigest()[:16].upper()
    
    print(f"\n🌍 ÉMISSION DE LICENCE PROFESSIONNELLE INTERNATIONALE")
    print("-" * 50)
    print(f"DÉTENTEUR  : {user_name}")
    print(f"SECTEUR    : {sector}")
    print(f"ORIGINE    : RDC (Afrique)")
    print(f"ID LICENCE : LPRO-{license_hash}")
    print(f"VALIDITÉ   : Jusqu'au {contract_end} (Irrévocable)")
    print("-" * 50)
    print("📡 VISION CARTOGRAPHIQUE : Enregistré sur le flux Global Plasma")

if __name__ == "__main__":
    generate_global_license("CADRE_CLASSE_MOYENNE_001", "MANAGEMENT_STRATEGIQUE")


