function (doc) {
            if (doc.Url) {
                emit(doc.Url, true);
            }
        }