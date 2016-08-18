function (doc) {
      if (doc.kind == 'Assignment' && doc.startDate && doc.endDate) {
        emit([doc.startDate, doc.endDate], true)
      }
    }