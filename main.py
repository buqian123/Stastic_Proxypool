import subprocess
import os
import requests
import time
import wget
#下载MMDB
link = 'https://github.com/ssrlive/proxypool/blob/master/assets/GeoLite2-City.mmdb?raw=true'
mymmdb = requests.get(link, stream=True, allow_redirects=True)
open('./assets/GeoLite2-City.mmdb', 'wb').write(mymmdb.content)
#清理并运行Proxypool
os.remove("./sub.yaml")
p = subprocess.Popen('./proxypool -c ./config/config.yaml', shell=True)
time.sleep(10)
#持续监测运行并检测是否完成或错误
while 1:
    if p.poll() is not None:
        print("Proxypool Error Or Died,return code:"+ str(p.returncode))
        try:
          p.kill()
          p.terminate()
        except: print("Kill Error")
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
f = open("sub.yaml", "x")
f.write(proxies)
f.close()
#清理
try:
  p.kill()
  p.terminate()
except: print("Kill Error")
os.remove("./assets/GeoLite2-City.mmdb")





