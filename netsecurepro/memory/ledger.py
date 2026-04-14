# Ledger Immuable — NetSecurePro IA
# Fondateur : Mohammed Ilyes Zoubirou

import json, hashlib, os, datetime

class Ledger:
    def __init__(self):
        self.path = os.path.expanduser("~/netsecurepro/memory/ledger.json")
        self.data = self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return {"events": [], "organisation": "NetSecurePro IA"}

    def save(self, event):
        event["timestamp"] = str(datetime.datetime.now())
        event["hash"] = hashlib.sha256(str(event).encode()).hexdigest()[:12]
        self.data["events"].append(event)
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)
        print(f"🔐 Ledger scellé : {event['hash']}...")

    def history(self):
        print(f"📋 {len(self.data['events'])} événements dans le ledger")
        for e in self.data["events"]:
            print(f"  [{e.get('timestamp','')}] {e.get('action','?')} — {e.get('hash','?')}")
