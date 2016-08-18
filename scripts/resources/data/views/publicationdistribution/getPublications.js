function (doc) {
      if (doc.communityName)
        emit([doc.communityName, doc.Viewed], true);
    }