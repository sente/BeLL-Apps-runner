function (doc) {
      if (doc.type) {
        if (doc.type == 'Course')
          emit(doc._id, doc)
      }
    }