function (doc) {
      if (doc.CollectionName) {
        emit(doc.CollectionName, true)
      }
    }