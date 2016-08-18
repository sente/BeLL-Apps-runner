function (doc) {
            if (doc.title) {
                emit(doc.Tag, true)
            }
        }