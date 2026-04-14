# NetSecurePro IA — Shield Cognitif
# Fondateur : Mohammed Ilyes Zoubirou
# MILYES@NETSECUREPRO.CA

import hashlib, datetime

class NetSecurePro:
    def __init__(self):
        self.name = "NetSecurePro IA"
        self.level = "MAXIMUM"
        self.domain = "SECURITY"
        self.log = []

    def check(self, source):
        if source != "LOCAL":
            self.lock("EXTERNAL_CLOUD_ATTEMPT")
            return False
        return True

    def lock(self, reason):
        event = {"timestamp": str(datetime.datetime.now()), "action": "VERROUILLAGE_URGENCE", "reason": reason, "hash": self._seal(reason)}
        self.log.append(event)
        print(f"🔴 ACTION REJETÉE — {reason}")
        return event

    def _seal(self, data):
        return hashlib.sha256(data.encode()).hexdigest()[:12]

    def audit(self):
        print(f"🔒 Audit : {len(self.log)} événements")
        for e in self.log:
            print(f"  [{e['timestamp']}] {e['reason']} — {e['hash']}")
