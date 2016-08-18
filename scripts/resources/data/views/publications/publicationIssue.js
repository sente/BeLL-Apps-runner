function (doc) {
      if (doc.IssueNo)
        emit(doc.IssueNo, doc);
    }