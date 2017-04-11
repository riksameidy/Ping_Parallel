import os
import re
import time

start = time.time()
received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")
sfx = ["8.8.8.8", "8.8.4.4", "68.180.230.248", "41.79.93.185"]

for suffix in sfx:
    #ip = "192.168.43." + str(suffix)
    ip = suffix
    ping_out = os.popen("ping -q -c2 " + ip, "r")
    print("... pinging ", ip)

    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])

end = time.time()
print(end - start)


"""
received_packages = re.compile(r"(\d) received")

$ ping -q -c2 192.168.178.26
PING 192.168.178.26 (192.168.178.26) 56(84) bytes of data.

--- 192.168.178.26 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 999ms
rtt min/avg/max/mdev = 0.022/0.032/0.042/0.010 ms


$ ping -q -c2 192.168.178.23
PING 192.168.178.23 (192.168.178.23) 56(84) bytes of data.

--- 192.168.178.23 ping statistics ---
2 packets transmitted, 0 received, +2 errors, 100% packet loss, time 1006ms
"""
