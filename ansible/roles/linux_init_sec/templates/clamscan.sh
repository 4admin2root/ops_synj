#!/bin/bash
mkdir /tmp/av
LOG=/tmp/av/`hostname`_`date +%Y%m%d`_av.log
clamscan --infected  --recursive /usr/lib64 /usr/local/lib /usr/local/sbin /usr/local/bin /usr/sbin /usr/bin /root/bin /etc /home /opt /data /data1 >> $LOG
if [ `grep Infected $LOG |awk '{print $3}'` -gt 0 ]
then
cat $LOG | mail -s `hostname`_antivirus_result {{ smtp_send_to }}
fi
