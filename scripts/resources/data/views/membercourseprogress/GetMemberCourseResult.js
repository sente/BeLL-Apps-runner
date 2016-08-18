function (doc) {
      if (doc.memberId && doc.courseId) {
        emit([doc.memberId, doc.courseId], true)
      }
    }