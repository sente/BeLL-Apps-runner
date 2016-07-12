var fs = require('fs')

var args = process.argv.slice(1);
var LogParse = require('./couchdb-log-parse')
var parser = new LogParse()

fs.createReadStream(args[1]).pipe(parser)

console.warn("reading ", args[1]);
    parser.on('data', function (c) {
})

var lines = []

parser.on('message', function (message) {
    lines.push(message);
    if (lines.length % 1000 == 0){
        console.warn(lines.length);
    }
})

parser.on('end', function (message) {
    console.warn("writing json...");
    console.log(JSON.stringify(lines))
})
