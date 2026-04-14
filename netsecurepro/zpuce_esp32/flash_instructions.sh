#!/bin/bash
# Flash ESP32 — NetSecurePro IA
echo "=================================="
echo "  IA_ZPUCE_CORE — Flash ESP32"
echo "  Fondateur : Mohammed Ilyes Zoubirou"
echo "=================================="
pip install esptool mpremote --break-system-packages
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 micropython.bin
mpremote connect /dev/ttyUSB0 cp main.py :main.py
echo "✅ ZPUCE_001 prête !"
