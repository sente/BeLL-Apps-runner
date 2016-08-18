function (doc) {
      if (doc.publicationId) {

        emit(doc.publicationId, doc);
      }
    }