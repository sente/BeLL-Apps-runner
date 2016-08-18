function (doc) {
            if (doc.Gender == "Male") {
                emit(doc._id, 1);
            }
        }