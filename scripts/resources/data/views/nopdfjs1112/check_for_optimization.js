function (doc) {
            if ((doc.need_optimization === true) && (doc.openWith == 'PDF.js')) {
                emit(doc._id, doc);
            }
        }