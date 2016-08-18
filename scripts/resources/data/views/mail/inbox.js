function (doc) {
      if (doc.receiverId) {
        emit(doc.receiverId, true)
      }
    }