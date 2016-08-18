function (doc) {
            if (doc.isWelcomeVideo) {
                emit(doc._id, true)
            }
        }