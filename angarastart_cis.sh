#!/bin/bash

set -euo pipefail

REPO_URL="https://github.com/ovh/debian-cis.git"
REPO_DIR="debian-cis"
CONFIG_FILE="/etc/default/cis-hardening"
AUDIT_FILE="/cis_angarastart.txt"

if ! command -v git &> /dev/null; then
  echo "Git не найден. Пытаемся установить git..."
  if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y git
  else
    echo "Пакетный менеджер apt-get не найден. Установите git вручную."
    exit 1
  fi
else
  echo "Пакеты установлены"
fi

if [ ! -d "$REPO_DIR" ]; then
  echo "Клонируем репозиторий $REPO_URL..."
  git clone "$REPO_URL"
else
  echo "Репозиторий $REPO_DIR уже существует, пропускаем клонирование."
fi

cd "$REPO_DIR"

if [ ! -f "$CONFIG_FILE" ]; then
  echo "Копируем конфигурационный файл в $CONFIG_FILE..."
  sudo cp debian/default "$CONFIG_FILE"
else
  echo "Файл $CONFIG_FILE уже существует, пропускаем копирование."
fi

echo "Обновляем пути в $CONFIG_FILE..."
sudo sed -i "s#CIS_LIB_DIR=.*#CIS_LIB_DIR='$(pwd)'/lib#" "$CONFIG_FILE"
sudo sed -i "s#CIS_CHECKS_DIR=.*#CIS_CHECKS_DIR='$(pwd)'/bin/hardening#" "$CONFIG_FILE"
sudo sed -i "s#CIS_CONF_DIR=.*#CIS_CONF_DIR='$(pwd)'/etc#" "$CONFIG_FILE"
sudo sed -i "s#CIS_TMP_DIR=.*#CIS_TMP_DIR='$(pwd)'/tmp#" "$CONFIG_FILE"

echo "Запускаем скрипт аудита и сохраняем вывод в $AUDIT_FILE..."
./bin/hardening.sh --audit-all > "$AUDIT_FILE"

cd ..

if [ -d "$REPO_DIR" ]; then
  echo "Удаляем каталог $REPO_DIR..."
  rm -rf "$REPO_DIR"
  echo "Удаляем конфигурационный файл $CONFIG_FILE..."
  rm -rf "$CONFIG_FILE"
fi

echo "Скрипт выполнен успешно. Результат: $AUDIT_FILE"
