
# see out/ports_and_versions.csv

echo -ne "Host,Version\n"

ssh root@hammock cat /root/oleproxy/server.js | grep '"http' | cut -f4 -d'"' | sed 's/\/apps.*//' | grep -v 192.168 | while read host; do
    version="$(curl -s ${host}/configurations/_all_docs?include_docs=true| jq  '.rows[] | .doc | .version' | tr -d '"')";

    echo -ne "$host,$version\n"; 
done


