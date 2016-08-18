function (doc) {
      if (doc.courseId) {
        emit(doc.courseId, true)
      }
    }