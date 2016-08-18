function (doc) {
            if (doc._id && doc.kind == 'survey') {
                emit(doc._id, doc);
            }
        }