function (doc) {
      if (doc.senderId) {
        emit(doc.senderId, true)
      }
    }