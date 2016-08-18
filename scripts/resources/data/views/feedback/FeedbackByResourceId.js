function (doc) {
      if (doc.kind == 'Feedback' && doc.resourceId) {
        emit(doc.resourceId, true)
      }
    }