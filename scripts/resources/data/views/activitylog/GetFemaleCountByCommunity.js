function (doc) {
            if (doc && doc.community) {
                emit(doc.community, doc.female_new_signups)
            }
        }