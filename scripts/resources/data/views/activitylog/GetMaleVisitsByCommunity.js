function (doc) {
            if (doc && doc.community) {
                emit(doc.community, doc.male_visits)
            }
        }