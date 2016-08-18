function (doc) {
            if (doc.receiverIds && doc.kind == 'survey') {
                if (Array.isArray(doc.receiverIds)) {
                    if (doc.receiverIds.length > 0) {
                        for (var idx in doc.receiverIds) {
                            emit(doc.receiverIds[idx], doc);
                        }
                    }
                } else {
                    emit(doc.receiverIds, doc)
                }
            }
        }