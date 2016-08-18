function (doc) {
      if (doc.kind == 'Schedule') {
        emit(doc.courseId, true)
      }
    }