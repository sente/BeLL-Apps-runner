function (doc) {
      if (doc.memberId && doc.courseId) {
        emit(doc.courseId, true)
      }
    }