function (doc) {
            if (doc.Type && doc.kind == 'surveyquestions') {
                emit(doc.Type, doc);
            }
        }