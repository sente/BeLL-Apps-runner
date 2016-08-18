function (doc) {
            if (doc.Gender && doc.kind == 'Member') {
                emit(doc.Gender, doc)
            }
        }