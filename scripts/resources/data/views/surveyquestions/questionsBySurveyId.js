function (doc) {
            if (doc.surveyId && doc.kind == 'surveyquestions') {
                emit(doc.surveyId, doc);
            }
        }