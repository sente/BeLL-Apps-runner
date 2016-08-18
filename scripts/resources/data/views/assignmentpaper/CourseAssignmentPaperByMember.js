function (doc) {
      if (doc.senderId && doc.courseId) {
        emit([doc.senderId, doc.courseId], true)
      }
    }