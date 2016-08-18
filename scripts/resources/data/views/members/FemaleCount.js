function (doc) {
            if (doc.Gender == "Female") {
                emit(doc._id, 1);
            }
        }