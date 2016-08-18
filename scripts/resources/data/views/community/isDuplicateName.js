function (doc) {
            if (doc.Name) {
                emit(doc.Name, true);
            }
        }