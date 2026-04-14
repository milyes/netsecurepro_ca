# Perception Fusion — NetSecurePro IA
# Fondateur : Mohammed Ilyes Zoubirou

class PerceptionFusion:
    def __init__(self):
        self.sensors = ["detections", "sovereign_state", "fusion_sync"]
        self.mode = "ALERTE"

    def fuse(self, inputs):
        print(f"🔵 Perception Fusion : {len(inputs)} entrées traitées")
        return {"source": "LOCAL", "sensors": self.sensors, "mode": self.mode, "data": inputs}
