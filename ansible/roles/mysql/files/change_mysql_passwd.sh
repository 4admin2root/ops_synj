#!/bin/bash
passwd=`grep "temporary password" /opt/xzx/log/mysql/mysqld.log|awk '{print $NF}'`

mysql --connect-expired-password -uroot -p$passwd -hlocalhost -e "set password=password('Xzx_Synjones01')"
