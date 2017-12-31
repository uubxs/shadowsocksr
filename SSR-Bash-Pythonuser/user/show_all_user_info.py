# -*- coding:utf-8 -*-  
import json

f = file("/usr/local/shadowsocksr/mudb.json");

json = json.load(f);

print "用户名\t端口\t密码\t加密方式"

for x in json:
  print "%s\t%s\t%s\t%s" %(x[u"user"],x[u"port"],x[u"passwd"],x[u"method"])
f.close();

