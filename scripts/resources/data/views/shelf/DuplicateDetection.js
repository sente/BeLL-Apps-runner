function (doc) {
      if (doc.memberId) {
        emit(doc.memberId, true)
      }
    }