
function reset_couchdb() {

    if [ -d /usr/local/var/lib/couchdb/ ]; then
        rm -rf /usr/local/var/lib/couchdb/.* 
        rm -rf /usr/local/var/lib/couchdb/*.*
    fi
}

