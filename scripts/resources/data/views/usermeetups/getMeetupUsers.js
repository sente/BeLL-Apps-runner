function (doc) {
			if (doc.meetupId) {
				emit(doc.meetupId, true)
			}
		}