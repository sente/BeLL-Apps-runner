function (doc) {
      if (doc.receiverId && doc.status == '0') {
        emit(doc.receiverId, doc);
      }
    }