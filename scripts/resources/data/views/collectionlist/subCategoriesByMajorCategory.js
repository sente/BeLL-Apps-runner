function (doc) {
      if (doc.show == true) {
        if (!doc.IsMajor)
          emit(doc.NesttedUnder, doc._id);
      }
    }