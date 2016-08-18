function (doc) {

      /*if (doc.CollectionName && doc.kind == 'CollectionList') {
       var prefix= doc.CollectionName.replace(/[!(.,-;):]+/g, "").toLowerCase();
       prefix = prefix.replace(/[-]+/gi, " ").split(" ")
       if (prefix.length > 0) {
       for (var idx in prefix) {
       if (prefix[idx] != ' ' && prefix[idx] != "" && prefix[idx] != "the" && prefix[idx] != "an" && prefix[idx] != "a")
       emit(prefix[idx], doc._id);
       }
       }
       emit(doc.CollectionName.toLowerCase(), doc);
       emit(doc.CollectionName.replace(/[-]+/gi, " ").toLowerCase(), doc);

       } */
      if (doc.CollectionName && doc.kind == 'CollectionList') {
        var txt = doc.CollectionName;
        var pref = txt.replace(/[-]+/g, " ").toLowerCase().split(" ");

        // prefix = prefix.replace(/[-]+/gi, " ").split(" ")
        if (pref.length > 0) {
          for (var idx in pref) {
            if (pref[idx] != ' ' && pref[idx] != "" && pref[idx] != "the" && pref[idx] != "an" && pref[idx] != "a")
              emit(pref[idx], doc._id);
          }
        }

        var prefix = txt.replace(/[!(.,-;):]+/g, "").toLowerCase().split(" ");
        // prefix = prefix.replace(/[-]+/gi, " ").split(" ")
        if (prefix.length > 0) {
          for (var idx in prefix) {
            if (prefix[idx] != ' ' && prefix[idx] != "" && prefix[idx] != "the" && prefix[idx] != "an" && prefix[idx] != "a")
              emit(prefix[idx], doc._id);
          }
        }
        emit(doc.CollectionName.toLowerCase(), doc);
        emit(doc.CollectionName.replace(/[-]+/gi, " ").toLowerCase(), doc);

      }
    }