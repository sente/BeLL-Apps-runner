function (doc) {
            if (doc.logDate) {
                var datePart = doc.logDate.match(/\d+/g),
                    month = datePart[0], // get only two digits
                    day = datePart[1],
                    year = datePart[2];
                var newdate = year + '/' + month + '/' + day;
                emit(newdate, doc);
            }
        }