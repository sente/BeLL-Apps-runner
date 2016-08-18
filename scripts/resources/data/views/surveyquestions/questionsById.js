function (doc) {
            if (doc._id && doc.kind == 'surveyquestions') {
                emit(doc._id, doc);
            }
        }