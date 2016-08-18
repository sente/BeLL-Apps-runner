function (doc) {
            if (doc && doc.Name) {
                emit(doc.Name, doc.Code);
            }
        }