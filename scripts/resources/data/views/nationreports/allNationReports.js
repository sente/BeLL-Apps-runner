function (doc) {
      if (doc.kind && doc._id) {
        if (doc.kind == 'NationReport') {
          emit(doc._id, doc)
        }
      }
    }