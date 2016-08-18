function (doc) {
            if (doc && doc.kind == 'Member') {
                emit(doc._id, true)
            }
        }