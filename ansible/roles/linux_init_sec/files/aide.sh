#!/bin/bash
mv -f /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
/sbin/aide -u |tee /var/lib/aide/`hostname`_`date +%Y%m%d`.log |mail -s `hostname`_aide_result ops@synjones.net
