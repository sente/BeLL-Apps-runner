function (doc) {
      if (doc.resourceId) {
        emit(doc.resourceId, true)
      }
    }