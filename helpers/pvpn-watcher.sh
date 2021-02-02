#!/bin/bash
source /etc/environment
pvpn=protonvpn
log_file=/var/log/pvpn-watcher.log
/bin/date >> $log_file
($pvpn s 2>%1) >> $log_file
if $pvpn s | grep -q Disconnected; then
  echo "Trying to reconnect..." >> $log_file
  ($pvpn c -f 2>%1) >> $log_file
  echo "Done" >> $log_file
fi
echo "------------------------------" >> $log_file
