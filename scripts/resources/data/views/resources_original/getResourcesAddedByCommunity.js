function (doc) {
            if (doc.type && doc.type == "community") {
                emit(true, doc._id);
            }
        }