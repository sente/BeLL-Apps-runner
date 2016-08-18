function (doc) {
            if (doc.memberId && doc.kind == 'survey'){
                emit(doc.memberId, doc);
            }
        }