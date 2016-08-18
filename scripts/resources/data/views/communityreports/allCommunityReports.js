function (doc) {
      if (doc.kind && doc._id) {
        if (doc.kind == 'CommunityReport') {
          emit(doc._id, doc)
        }
      }
    }