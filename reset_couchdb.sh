
function reset_couchdb() {
    set -x
    if [ -d /usr/local/var/lib/couchdb/ ]; then
        rm -rf /usr/local/var/lib/couchdb/.*  2>/dev/null
        rm -rf /usr/local/var/lib/couchdb/*.* 2>/dev/null
    fi
    set +x
}

