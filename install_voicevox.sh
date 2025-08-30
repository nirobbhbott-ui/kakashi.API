---

### **4. install_voicevox.sh**
- Your Linux installer script for VOICEVOX (from your first script).

```bash
#!/usr/bin/env bash
set -euo pipefail

if ! command -v curl &>/dev/null; then
    echo "Install curl first!"
    exit 1
fi

curl -fsSL https://raw.githubusercontent.com/VOICEVOX/voicevox/0.24.2/build/installer_linux.sh >tmp_voicevox_installer.sh
VERSION=0.24.2 NAME=linux-nvidia-appimage bash tmp_voicevox_installer.sh
rm tmp_voicevox_installer.sh
