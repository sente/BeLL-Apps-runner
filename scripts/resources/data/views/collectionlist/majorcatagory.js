function (doc) {
      if (doc.show == true) {
        if (doc.IsMajor == true)
          emit(doc._id, doc);
      }
    }