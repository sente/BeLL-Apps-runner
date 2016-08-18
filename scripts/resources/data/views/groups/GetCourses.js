function (doc) {
            if (doc.members) {
                for (var x = 0; x < doc.members.length; x++) {
                    emit(doc.members[x], true)
                }
            }
        }