function (doc) {
            if (doc.community && doc.Gender == "Female") {
                emit(doc.community, 1)
            }
        }