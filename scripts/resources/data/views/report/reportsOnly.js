function (doc) {
      if (doc.kind) {
        if (doc.kind == 'report') {
          emit(doc._id, doc);
        }
      }
    }