# IA_ZPUCE_CORE — ZCore Principal
# Fondateur : Mohammed Ilyes Zoubirou
# MILYES@NETSECUREPRO.CA | Version 1.1.0

import json, hashlib, datetime

class ZCore:
    def __init__(self):
        self.name = "IA_ZPUCE_CORE"
        self.founder = "Mohammed Ilyes Zoubirou"
        self.email = "MILYES@NETSECUREPRO.CA"
        self.site = "https://netsecurepro.ca"
        self.sovereignty = "LOCAL_ONLY"
        self.status = "STANDBY"
        self.version = "1.1.0"

    def boot(self):
        print("=" * 50)
        print("  IA_ZPUCE_CORE — BOOT SOUVERAIN")
        print(f"  Fondateur  : {self.founder}")
        print(f"  Email      : {self.email}")
        print(f"  Souveraineté : {self.sovereignty}")
        print("=" * 50)
        self.status = "ACTIVE"
        return True

    def perceive(self, data):
        source = data.get("source", "UNKNOWN")
        if source != "LOCAL":
            return {"status": "REJECTED", "reason": "EXTERNAL_CLOUD_ATTEMPT", "action": "PROTOCOLE_VERROUILLAGE_URGENCE"}
        return {"status": "ACCEPTED", "source": source, "data": data}

    def decide(self, perception):
        if perception["status"] == "REJECTED":
            return perception
        return {"action": "EXECUTE", "confidence": 100.0, "sovereignty": self.sovereignty, "timestamp": str(datetime.datetime.now())}

    def execute(self, decision):
        if decision.get("confidence", 0) >= 95.0:
            self.status = "ACTIVE"
            print(f"✅ Exécution : {decision['action']}")
        else:
            self.status = "WAITING"
