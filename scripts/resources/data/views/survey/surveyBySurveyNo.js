function (doc) {
            if (doc.SurveyNo && doc.kind == 'survey') {
                emit(doc.SurveyNo, doc);
            }
        }