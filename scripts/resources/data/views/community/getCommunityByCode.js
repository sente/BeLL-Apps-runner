function (doc) {
            if (doc && doc.Code)
                emit(doc.Code, doc);
        }