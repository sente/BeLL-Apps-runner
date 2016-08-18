function (doc) {
      if (doc.kind && doc.NationReportId) {
        if (doc.kind == 'NationReportComment') {
          emit(doc.NationReportId, doc)
        }
      }
    }