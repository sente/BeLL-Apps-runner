function (doc) {
      if (doc.memberId && doc.resourceId) {
        emit([doc.memberId, doc.resourceId], true)
      }
    }