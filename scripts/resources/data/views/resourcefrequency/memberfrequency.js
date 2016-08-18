function (doc) {
      if (doc.memberID) {
        emit(doc.memberID, true)
      }
    }