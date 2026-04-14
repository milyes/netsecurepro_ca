# ==================================================
# z-_vm_ZPUCE_.ESP32 - Module Physique Souverain
# NetSecurePro IA - ROBOOX ULTRA
# Fondateur : Mohammed Ilyes Zoubirou
# Site : https://netsecurepro.ca
# Mode : LOCAL_ONLY
# ==================================================

import bluetooth
import time
import machine

print("=== z-_vm_ZPUCE_.ESP32 démarré ===")
print("Nom du module     : ZPUCE_001_MILYES")
print("Souveraineté      : LOCAL_ONLY")
print("Communication     : Bluetooth Local")
print("Fondateur         : Mohammed Ilyes Zoubirou")
print("https://netsecurepro.ca")
print("========================================")

# Activation Bluetooth
ble = bluetooth.BLE()
ble.active(True)

# Nom visible en Bluetooth
ble.config(gap_name="ZPUCE_001_MILYES")

# UUID pour communication simple (comme un port série Bluetooth)
UART_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
TX = (bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E"), bluetooth.FLAG_NOTIFY)
RX = (bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"), bluetooth.FLAG_WRITE)

uart_service = (UART_UUID, (TX, RX))
ble.gatts_register_services((uart_service,))

conn_handle = None

def on_rx(conn_handle, value_handle, data):
    try:
        msg = data.decode('utf-8')
        print("Perception reçue de ROBOOX ULTRA :", msg)
        
        # Réponse souveraine
        response = f"ZPUCE_001: ACCEPTED - LOCAL_ONLY - {time.ticks_ms()}"
        ble.gatts_notify(conn_handle, 1, response.encode())
        
        print("Réponse envoyée à ROBOOX ULTRA")
    except:
        print("Erreur de décodage")

# Callback simplifié
ble.irq(lambda event, data: None)

# Publicité Bluetooth (visible par ROBOOX ULTRA)
ble.gap_advertise(100000, b'\x02\x01\x06' + b'\x0F\x09ZPUCE_001_MILYES')

print("Module prêt - En attente de connexion Bluetooth...")

while True:
    time.sleep(2)
    # On peut ajouter ici des capteurs physiques plus tard (température, mouvement, etc.)
