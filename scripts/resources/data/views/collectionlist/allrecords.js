function (doc) {
      if (doc.CollectionName)
        emit(doc._id, doc);
    }