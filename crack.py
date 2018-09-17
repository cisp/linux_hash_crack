#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

def _dict_load(passwordfile,saltstringfile):
    _passwordlist = []
    _saltstringlist = []
    with open(passwordfile,'r') as fr:
        while True:
            line = fr.readline().split("\n")[0].split('\r')[0]
            if line != '':
                _passwordlist.append(line)
            else:
                break
    with open(saltstringfile,'r') as fr:
        while True:
            line = fr.readline().split("\n")[0].split('\r')[0]
            if line != '':
                _saltstringlist.append(line)
            else:
                break
        return (_passwordlist,_saltstringlist)

def crack(pf,sf,value):
    pl,sl = _dict_load(pf,sf)
    for pswd in pl:
        for salt in sl:
            ret = os.popen('./crack %s %s'%(pswd,salt)).read().split('%')[0]
            print "[*] password:%s , salt:%s, result:%s"%(pswd, salt , ret)
            if ret == value:
                print '[+] Carcked OK! Password:%s'%pswd




if __name__ == "__main__":
    pf = sys.argv[1]
    sf = sys.argv[2]
    value = sys.argv[3]
    crack(pf,sf,value)
