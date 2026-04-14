# Réseau Distribué ZPUCE — NetSecurePro IA
# Fondateur : Mohammed Ilyes Zoubirou

import datetime

class ZPUCE_Network:
    def __init__(self):
        self.nodes = {}
        self.sovereignty = "LOCAL_ONLY"

    def register(self, zpuce_id):
        self.nodes[zpuce_id] = {"id": zpuce_id, "status": "ACTIVE", "joined": str(datetime.datetime.now())}
        print(f"📡 ZPUCE enregistrée : {zpuce_id}")

    def broadcast(self, message, sender_id):
        if message.get("source") != "LOCAL":
            print("🔴 Broadcast rejeté")
            return False
        print(f"📡 Broadcast LOCAL de {sender_id} → {len(self.nodes)} nœuds")
        return True

    def topology(self):
        print(f"🌐 Réseau P2P : {len(self.nodes)} nœuds actifs")
        for nid, info in self.nodes.items():
            print(f"   [{nid}] {info['status']}")
