function (doc) {
            if (doc.community && doc.kind == 'Member') {
                emit(doc.community, doc)
            }
        }