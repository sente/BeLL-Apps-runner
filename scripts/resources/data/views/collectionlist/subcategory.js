function (doc) {
      if (doc.show == true) {
        if (!doc.IsMajor)
          emit(doc._id, doc);
      }
    }