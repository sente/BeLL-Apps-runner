function (doc) {
            if (doc.communityName && doc.kind == 'survey'){
                emit(doc.communityName, doc.SurveyNo);
            }
        }