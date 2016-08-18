function (doc) {
      if (doc.kind && doc.reportId) {
        if (doc.kind == 'reportComment' && doc.reportId) {
          emit(doc.reportId, doc);
        }
      }
    }