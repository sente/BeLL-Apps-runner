

function reset_couchdb() {
    set -x
    if [ -d /usr/local/var/lib/couchdb/ ]; then
        rm -rf /usr/local/var/lib/couchdb/.*  2>/dev/null
        rm -rf /usr/local/var/lib/couchdb/*.* 2>/dev/null
    fi
    set +x
}

function install_nation() {

    export NAME=stunation
    export PORT=5984

    if [ -z "$OLEPASSWORD" ]; then 
        echo "set and export \$OLEPASSWORD before running this script"
        echo ">> export OLEPASSWORD=<yourpassword"
        echo -ne "\n\n\n\n"
        return 1
    fi

    BELL_APPS_DIRECTORY=/Users/stu/code/ole/BeLL-Apps/

    cd "${BELL_APPS_DIRECTORY}" || exit 1
    chmod +x node_modules/.bin/couchapp


    curl -X DELETE 'http://nation:${OLEPASSWORD}@127.0.0.1:'${PORT}'/_config/admins/'${NAME} 
    curl -X DELETE 'http://nation:${OLEPASSWORD}@127.0.0.1:'${PORT}'/_config/admins/nation' 


    # create install_linux
    echo "node_modules/.bin/couchapp push \$1 \$2" > pushDocToDb.sh
    chmod +x node_modules/.bin/couchapp pushDocToDb.sh
    cp install_windows install_linux
    sed -i "s/pushDocToDb.bat/.\/pushDocToDb.sh/" install_linux
    sed -i 's#databases\\\\#databases/#' install_linux
    sed -i 's/NationBell/'${NAME}'QA/' init_docs/ConfigurationsDoc-Nation.txt
    sed -i 's/nationbell/'${NAME}'/' init_docs/ConfigurationsDoc-Nation.txt
    sed -i 's#Male#Female#' install_linux
    sed -i 's#somalia#'${NAME}'#' install_linux
    sed -i 's#"visits": 0#"visits":0,"bellLanguage":"English","BirthDate":"2010-10-15T04:00:00.000Z","community":"'${NAME}'"#' install_linux

    # install nation
    node install_linux http://127.0.0.1:${PORT}





    # add users
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"English","firstName":"a","lastName":"a","middleNames":"a","login":"a","password":"a","phone":"a","email":"a@a","language":"","BirthDate":"2010-10-15T04:00:00.000Z","visits":0,"Gender":"Male","levels":"1","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell","lastLoginDate":"2015-01-01T04:00:00.000Z","lastEditDate":"2015-01-01T04:00:00.000Z"}'
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"English","firstName":"b","lastName":"b","middleNames":"b","login":"b","password":"b","phone":"b","email":"b@b","language":"","BirthDate":"2010-10-15T04:00:00.000Z","visits":0,"Gender":"Female","levels":"1","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell","lastLoginDate":"2015-01-01T04:00:00.000Z","lastEditDate":"2015-01-01T04:00:00.000Z"}'
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"Spanish","firstName":"c","lastName":"c","middleNames":"c","login":"c","password":"c","phone":"c","email":"c@c","language":"","BirthDate":"2005-10-15T04:00:00.000Z","visits":0,"Gender":"Male","levels":"4","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell"}'
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"Spanish","firstName":"d","lastName":"d","middleNames":"d","login":"d","password":"d","phone":"d","email":"d@d","language":"","BirthDate":"2005-10-15T04:00:00.000Z","visits":0,"Gender":"Female","levels":"4","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell"}'
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"Arabic","firstName":"e","lastName":"e","middleNames":"e","login":"e","password":"e","phone":"e","email":"e@e","language":"","BirthDate":"2000-10-15T04:00:00.000Z","visits":0,"Gender":"Male","levels":"7","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell","lastLoginDate":"2016-01-01T04:00:00.000Z","lastEditDate":"2016-01-01T04:00:00.000Z"}'
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"Arabic","firstName":"f","lastName":"f","middleNames":"f","login":"f","password":"f","phone":"f","email":"f@f","language":"","BirthDate":"2000-10-15T04:00:00.000Z","visits":0,"Gender":"Female","levels":"7","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell","lastLoginDate":"2016-01-01T04:00:00.000Z","lastEditDate":"2016-01-01T04:00:00.000Z"}'
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"Urdu","firstName":"g","lastName":"g","middleNames":"g","login":"g","password":"g","phone":"g","email":"g@g","language":"","BirthDate":"1995-10-15T04:00:00.000Z","visits":0,"Gender":"Male","levels":"10","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell","lastLoginDate":"2015-01-01T04:00:00.000Z","lastEditDate":"2015-01-01T04:00:00.000Z"}'
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"Urdu","firstName":"h","lastName":"h","middleNames":"h","login":"h","password":"h","phone":"h","email":"h@h","language":"","BirthDate":"1995-10-15T04:00:00.000Z","visits":0,"Gender":"Female","levels":"10","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell","lastLoginDate":"2015-01-01T04:00:00.000Z","lastEditDate":"2015-01-01T04:00:00.000Z"}'
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"English","firstName":"i","lastName":"i","middleNames":"i","login":"i","password":"i","phone":"i","email":"i@i","language":"","BirthDate":"1990-10-15T04:00:00.000Z","visits":0,"Gender":"Male","levels":"Higher","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell"}'
    curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:'${PORT}'/members' --data '{"kind":"Member","roles":["Learner"],"bellLanguage":"English","firstName":"j","lastName":"j","middleNames":"j","login":"j","password":"j","phone":"j","email":"j@j","language":"","BirthDate":"1990-10-15T04:00:00.000Z","visits":0,"Gender":"Female","levels":"Higher","status":"active","yearsOfTeaching":null,"teachingCredentials":null,"subjectSpecialization":null,"forGrades":null,"community":"'${NAME}'","region":"","nation":"earthbell"}'

    curl -X PUT 'http://127.0.0.1:'${PORT}'/_config/httpd/allow_jsonp' -d '"true"'
    #curl -X PUT 'http://127.0.0.1:'${PORT}'/_config/httpd/enable_cors' -d '"true"'
    #curl -X PUT 'http://127.0.0.1:'${PORT}'/_config/cors/origins' -d '"*"'

    curl -X PUT 'http://127.0.0.1:'${PORT}'/_config/admins/nation' -d '"${OLEPASSWORD}"'
    curl -X PUT 'http://nation:${OLEPASSWORD}@127.0.0.1:'${PORT}'/_config/admins/'${NAME} -d '"${OLEPASSWORD}"' 

    cd -

}
