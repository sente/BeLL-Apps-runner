ssh root@hammock cat /root/oleproxy/server.js  | grep '"http' |cut -f4 -d'"' | sed 's/\/apps.*//' | grep -v 192.168
