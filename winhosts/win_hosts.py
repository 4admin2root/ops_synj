#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
winhosts  main
~~~~~~~~~~~~~~~~~~~~~
@time: 2017/6/29 13:48
@contact: a@b.com
usage:


links:

:copyright: 
:license: BSD 3-Clause License
"""
import shutil
import requests
import  datetime

__title__ = 'main'
__version__ = '0.0.1'
__author__ = 'adminroot'
__license__ = 'BSD 3-Clause License'




def get_hosts():
    """ get hosts from git"""
    url = "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"
    try:
        hosts = requests.get(url, timeout=10)
    except Exception as e:
        print(e)

    return hosts.text


if __name__ == '__main__':
    """ copy old hosts file and create new one"""
    shutil.copyfile('C:\Windows\System32\drivers\etc\hosts', 'C:\hosts'+datetime.datetime.now().strftime('%Y-%m-%d'))
    f = open('C:\Windows\System32\drivers\etc\hosts', 'w')
    hosts_con = get_hosts()
    if hosts_con:
        f.write(hosts_con)



