function (doc) {
      if (doc.type) {
        if (doc.type == 'Resource')
          emit(doc._id, doc)
      }
    }