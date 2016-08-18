function (doc) {
            if(doc.Tag){
                if (Array.isArray(doc.Tag)) {
                    if (doc.Tag.length > 0) {
                        for (var idx in doc.Tag) {
                            emit(doc.Tag[idx], doc);
                        }
                    }
                }
            }

        }