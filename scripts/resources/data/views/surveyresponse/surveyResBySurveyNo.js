function (doc) {
            if (doc.SurveyNo && doc.kind == 'survey' && doc.memberId!='') {
                emit(doc.SurveyNo, doc);
            }
        }