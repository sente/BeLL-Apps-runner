function (doc) {
      if (doc.memberId && doc.kind == 'invitation') {
        emit(doc.memberId, true)
      }
    }