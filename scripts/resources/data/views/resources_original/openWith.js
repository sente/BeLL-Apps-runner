function (doc) {
            if (doc.openWith) {
                emit(doc._id, doc.openWith);
            }
        }