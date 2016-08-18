function (doc) {
      if (doc.kind && doc.CommunityReportId) {
        if (doc.kind == 'CommunityReportComment') {
          emit(doc.CommunityReportId, doc)
        }
      }
    }