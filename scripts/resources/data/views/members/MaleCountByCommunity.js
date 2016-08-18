function (doc) {
            if (doc.community && doc.Gender == "Male") {
                emit(doc.community, 1)
            }
        }