bindfunction ()
{
    cat servers.txt | grep ole | while read line; do
        echo $line/apps/_design/bell/MyApp/app/Router.js;
    done | while read foobar; do
        echo -ne "$foobar\t" && curl -s $foobar | md5sum;
    done | vi -
}
