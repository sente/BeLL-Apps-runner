function (doc) {
			if (doc.meetupId && doc.memberId) {
				emit([doc.memberId, doc.meetupId], true)
			}
		}