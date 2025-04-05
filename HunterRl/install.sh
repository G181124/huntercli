#!/bin/bash

echo "🔧 Menginstal HunterCLI..."

# Lokasi target instalasi
INSTALL_DIR="$HOME/.huntercli"

# Buat folder dan copy file
mkdir -p $INSTALL_DIR
cp -r * $INSTALL_DIR

# Tambah alias ke .bashrc (kalau belum ada)
if ! grep -Fxq "alias huntercli='python3 $INSTALL_DIR/huntercli.py'" $HOME/.bashrc; then
  echo "alias huntercli='python3 $INSTALL_DIR/huntercli.py'" >> $HOME/.bashrc
  echo "✅ Alias 'huntercli' ditambahkan ke .bashrc"
else
  echo "ℹ️ Alias sudah ada di .bashrc"
fi

# Apply alias sekarang juga
source $HOME/.bashrc

echo "✅ Instalasi selesai! Jalankan dengan perintah: huntercli --help"
