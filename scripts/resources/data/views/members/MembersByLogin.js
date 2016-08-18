function (doc) {
            if (doc.kind == 'Member') {
                emit(doc.login, true)
            }
        }