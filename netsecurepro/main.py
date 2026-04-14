# NetSecurePro IA — Point d'entrée principal
# Fondateur : Mohammed Ilyes Zoubirou
# MILYES@NETSECUREPRO.CA | https://netsecurepro.ca

from zcore.core import ZCore
from security.netsecurepro import NetSecurePro
from memory.ledger import Ledger
from perception.fusion import PerceptionFusion
from distributed.zpuce import ZPUCE_Network

def main():
    print("=" * 50)
    print("  NETSECUREPRO IA — IA_ZPUCE_CORE")
    print("  Fondateur : Mohammed Ilyes Zoubirou")
    print("  MILYES@NETSECUREPRO.CA")
    print("  https://netsecurepro.ca")
    print("  Mode : LOCAL AUTONOME")
    print("=" * 50)

    zcore = ZCore()
    shield = NetSecurePro()
    ledger = Ledger()
    fusion = PerceptionFusion()
    network = ZPUCE_Network()

    zcore.boot()
    network.register("ZPUCE_MAIN")

    # Test local
    fused = fusion.fuse([{"source": "LOCAL", "msg": "boot_test"}])
    perception = zcore.perceive(fused)
    decision = zcore.decide(perception)
    zcore.execute(decision)
    ledger.save(decision)

    # Test rejet cloud
    perception2 = zcore.perceive({"source": "CLOUD", "msg": "hack"})
    if perception2["status"] == "REJECTED":
        shield.lock("EXTERNAL_CLOUD_ATTEMPT")

    shield.audit()
    ledger.history()

    print("\n" + "=" * 50)
    print("  ✅ NETSECUREPRO IA — OPÉRATIONNELLE")
    print("  Souveraineté : LOCAL_ONLY garantie")
    print("  Prêt pour Phase 2 — ZPUCE ESP32")
    print("=" * 50)

if __name__ == "__main__":
    main()
