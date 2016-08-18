function (doc) {
      if (doc.userId) {
        emit(doc.userId, true)
      }
    }