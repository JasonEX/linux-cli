#!/bin/bash
source /etc/environment
pvpn=protonvpn
log_file=/var/log/pvpn-watcher.log
/bin/date >> $log_file
($pvpn s 2>&1) >> $log_file
if $pvpn s | grep -q Disconnected; then
  echo "[Watcher] Disconnected, trying to reconnect..." >> $log_file
  ($pvpn d)
  ($pvpn c -f 2>&1) >> $log_file
  echo "[Watcher] Done" >> $log_file
elif $pvpn s | grep -q error; then
  echo "[Watcher] Error detected, trying to reconnect..." >> $log_file
  ($pvpn d)
  ($pvpn c -f 2>&1) >> $log_file
  echo "[Watcher] Done" >> $log_file
fi
echo "------------------------------" >> $log_file
