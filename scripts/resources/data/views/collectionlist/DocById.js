function (doc) {
      if (doc._id) {
        if (doc.show == true)
          emit(doc._id, doc.CollectionName);
      }
    }