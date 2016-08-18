function (doc) {
            var txt = doc.lastName;
            var words = txt.replace(/[!.,;]+/g, "").toLowerCase().split(" ");
            for (var word in words) {
                emit(words[word], doc._id);
            }
        }