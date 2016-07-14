#!/bin/bash

PORT=5984
BELL_APPS_DIRECTORY=/Users/stu/code/ole/BeLL-Apps/

cd "${BELL_APPS_DIRECTORY}" || exit 1
chmod a+x node_modules/.bin/couchapp

## create databases & push design docs into them
for database in databases/*.js; do

    dname=$(basename $database .js)
    echo curl -X PUT http://127.0.0.1:$PORT/$dname
    curl -X PUT http://127.0.0.1:$PORT/$dname

    case $dname in
      "communities" | "languages" | "configurations" ) ;;
      * ) 
          echo node_modules/.bin/couchapp push $database http://127.0.0.1:$PORT/$dname
          node_modules/.bin/couchapp push $database http://127.0.0.1:$PORT/$dname 
      ;;
    esac
done


## add bare minimal required data to couchdb for launching bell-apps smoothly
for filename in init_docs/languages/*.txt; do
    echo curl -d @$filename -H "Content-Type: application/json" -X POST http://127.0.0.1:$PORT/languages;
    curl -d @$filename -H "Content-Type: application/json" -X POST http://127.0.0.1:$PORT/languages;
done

echo curl -d @init_docs/ConfigurationsDoc-Community.txt -H "Content-Type: application/json" -X POST http://127.0.0.1:$PORT/configurations
curl -d @init_docs/ConfigurationsDoc-Community.txt -H "Content-Type: application/json" -X POST http://127.0.0.1:$PORT/configurations

echo curl -d @init_docs/admin.txt -H "Content-Type: application/json" -X POST http://127.0.0.1:$PORT/members
curl -d @init_docs/admin.txt -H "Content-Type: application/json" -X POST http://127.0.0.1:$PORT/members

echo -e "\n\n\n"
echo "****************"
echo "** setup done **"
echo "****************"
echo -e "\n\n\n"
echo "http://localhost:${PORT}/apps/_design/bell/MyApp/index.html"
echo -e "\n\n\n"
