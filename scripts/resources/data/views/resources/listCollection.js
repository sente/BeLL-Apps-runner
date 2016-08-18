function (doc) {
            if (doc.Tag && doc.kind == 'Resource') {
                if (Array.isArray(doc.Tag)) {
                    if (doc.Tag.length > 0) {
                        for (var idx in doc.Tag) {
                            emit(doc.Tag[idx], doc._id);
                        }
                    }
                } else {
                    emit(doc.Tag, doc._id)
                }
            }
            if (doc.subject && doc.kind == 'Resource') {
                if (Array.isArray(doc.subject)) {
                    if (doc.subject.length > 0) {
                        for (var idx in doc.subject) {
                            emit(doc.subject[idx], doc._id);
                        }
                    }
                } else {
                    emit(doc.subject, doc._id)
                }
            }
            if (doc.Level && doc.kind == 'Resource') {
                if (Array.isArray(doc.Level)) {
                    if (doc.Level.length > 0) {
                        for (var idx in doc.Level) {
                            emit(doc.Level[idx], doc._id);
                        }
                    }
                } else {
                    emit(doc.Level, doc._id)
                }
            }
            if (doc.Medium && doc.kind == 'Resource') {
                emit(doc.Medium, doc._id)
            }
            if (doc.sum && doc.timesRated >= 1 && doc.kind == 'Resource') {
                emit(Math.ceil(doc.sum / doc.timesRated), doc._id)
            }
            if (doc.title) {
                var txt = doc.title;
                var prefix = txt.replace(/[!(.,;):]+/g, "").toLowerCase().split(" ");
                if (prefix.length > 0) {
                    for (var idx in prefix) {
                        if (prefix[idx] != ' ' && prefix[idx] != "" && prefix[idx] != "the" && prefix[idx] != "an" && prefix[idx] != "a")
                            emit(prefix[idx], doc._id);
                    }
                }
            }
            if (doc.author && doc.kind == 'Resource') {
                if (Array.isArray(doc.author)) {
                    auth = doc.author
                    for (var idnx in auth) {
                        var prefix = auth[idnx].replace(/[!(.,;):]+/g, "").toLowerCase().split(" ");
                        if (prefix.length > 0) {
                            for (var idx in prefix) {
                                if (prefix[idx] != ' ' && prefix[idx] != "" && prefix[idx] != "the" && prefix[idx] != "an" && prefix[idx] != "a")
                                    emit(prefix[idx], doc._id);
                            }
                        }
                    }
                } else {
                    var authr = doc.author.replace(/[!(.,;):]+/g, "").toLowerCase().split(" ");
                    if (authr.length > 0) {
                        for (var idx in authr) {
                            if (authr[idx] != ' ' && authr[idx] != "" && authr[idx] != "the" && authr[idx] != "an" && authr[idx] != "a")
                                emit(authr[idx], doc._id);
                        }
                    }
                }
            }
        }