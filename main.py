import subprocess
import os
import requests
import time
import wget
#下载MMDB
wget("https://github.com/ssrlive/proxypool/blob/master/assets/GeoLite2-City.mmdb?raw=true","./assets/GeoLite2-City.mmdb")
#清理并运行Proxypool
os.remove("./sub.yaml")
p = subprocess.Popen('./proxypool -c ./config/config.yaml', shell=True)
#持续监测运行并检测是否完成
while 1:
    if p.returncode != 0:
        p = subprocess.Popen('sudo ./proxypool -c ./config/config.yaml', shell=True)
    try:
        sub = requests.get("http://localhost:8080/clash/proxies")
    except:
        continue
    sub = sub.content.decode("utf-8")
    if "NULL" not in sub:
        break
    time.sleep(5)
#获取订阅
proxies = requests.get("http://localhost:8080/clash/proxies").content.decode("utf-8")
#写入
f = open("config.yaml", "x")
f.write(proxies)
f.close()
#清理
os.remove("./assets/GeoLite2-City.mmdb")






