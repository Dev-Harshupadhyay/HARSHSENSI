#!/data/data/com.termux/files/usr/bin/bash
# HARSH SENSI - Auto Install & Run Script
# WELCOME HARSH SENSI • Exit par JAI SHREE RAM
set -euo pipefail

bye() {
  echo ""
  echo "╔════════════════════════════════════════════════════╗"
  echo "║          🙏  J A I   S H R E E   R A M  🙏          ║"
  echo "╚════════════════════════════════════════════════════╝"
  echo "  Thanks for using HARSH SENSI! - Developer HARSH"
  echo ""
}
trap bye EXIT

cd "$(dirname "$0")"

echo "╔════════════════════════════════════════════════════╗"
echo "║            ★ WELCOME HARSH SENSI ★                 ║"
echo "║        HARSH SENSI - Sensitivity Engine            ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

pkg install -y python 2>/dev/null || true
mkdir -p o0x
chmod +x z_run.py 2>/dev/null || true
python z_run.py
