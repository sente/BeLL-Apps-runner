function (doc) {
            if (doc.CourseTitle) {
                emit(doc.CourseTitle, doc._id);
            }
        }