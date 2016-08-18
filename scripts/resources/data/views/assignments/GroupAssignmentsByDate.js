function (doc) {
      if (doc.kind == 'Assignment' && doc.context.groupId && doc.startDate && doc.endDate) {
        emit([doc.context.groupId, doc.startDate, doc.endDate], true)
      }
    }