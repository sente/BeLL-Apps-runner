function (doc) {
      if (doc.kind == 'Assignment' && doc.context.groupId) {
        emit(doc.context.groupId, true)
      }
    }