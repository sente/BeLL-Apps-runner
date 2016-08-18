function (doc) {
            if (doc.CourseTitle) {
                var txt = doc.CourseTitle;
                var prefix = txt.replace(/[!(.,;):]+/g, "").toLowerCase().split(" ");
                if (prefix.length > 0) {
                    for (var idx in prefix) {
                        if (prefix[idx] != ' ' && prefix[idx] != "" && prefix[idx] != "the" && prefix[idx] != "an" && prefix[idx] != "a")
                            emit(prefix[idx], doc._id);
                    }
                }
            }
        }