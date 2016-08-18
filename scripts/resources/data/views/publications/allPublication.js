function (doc) {
      if (doc.IssueNo)
        emit(doc._id, doc);
    }