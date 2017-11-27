#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import re
import shutil

# the list of doctor studient names that need to check
LD =[];
LM =[];
# getting the sorted name list 
# L.sort();
# print(LD);
# print(LM);
ND = len(LD);
NM = len(LM);

ldcut = [None] * ND;
lmcut = [None] * NM;

lsearch = os.listdir('/home/sarah/Documents/wstmp');
jd = 0;
jm = 0;

for i in lsearch:
    strcmp = i;
    strcpart = re.split('\_|\.',strcmp);
    attri = strcpart[0];
    if attri == 'rr':
       ldcut[jd] = strcpart[2];
       jd = jd+1;
    elif attri == '本周小结':
       lmcut[jm] = strcpart[2];
       jm = jm+1;
    else:
       continue; 

LDd = set(LD);
LMm = set(LM);
ldcutt = set(ldcut);
lmcutt = set(lmcut);

dmiss = LDd - LDd.intersection(ldcutt);
mmiss = LMm - LMm.intersection(lmcutt);

if (len(dmiss)>0 and len(mmiss)>0):
    print('Research report missing: ');
    print(dmiss);
    print('weekly summaries missing: '); 
    print(mmiss);
elif len(dmiss)>0 and len(mmiss)==0:
    print('Research report missing: ');
    print(dmiss);
elif len(dmiss)==0 and len(mmiss)>0:
    print('weekly summaries missing: '); 
    print(mmiss);
else:
    now = datetime.datetime.now();
    rrdir = 'researchreport'+str(now.year)+str(now.month)+str(now.day);
    wsdir = '小组本周小结'+str(now.year)+str(now.month)+str(now.day);
    if not os.path.isdir(rrdir):
        os.makedirs(rrdir);
    if not os.path.isdir(wsdir):
        os.makedirs(wsdir);
    for i in lsearch:
        strcmp = i;
        strcpart = re.split('\_|\.',strcmp);
        attri = strcpart[0];
        if attri == 'rr':
            shutil.move(strcmp,rrdir);
        if attri == '本周小结':
            shutil.move(strcmp,wsdir);




