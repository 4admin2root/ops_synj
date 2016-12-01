#!/bin/bash
/bin/rkhunter --cronjob --quiet --noappend-log
if [ $? -ne 0 ]
then
cat /var/log/rkhunter/rkhunter.log |mail -s "Rkhunter daily run on `uname -n` has produced warning messages" lvzhijun@synjones.net
fi
