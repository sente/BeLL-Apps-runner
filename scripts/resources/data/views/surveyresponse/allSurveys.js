function (doc) {
            if (doc.SurveyNo && doc.kind == 'survey') {
                emit(doc._id, doc);
            }
        }