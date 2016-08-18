function (doc) {
            if (doc.kind == 'Member' && doc._id) {
                emit(doc._id, doc)
            }
        }