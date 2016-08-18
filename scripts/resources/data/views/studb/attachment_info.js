function(doc) {
  var json = JSON.stringify(doc);
  var len = json.length;
  var ct = 0;
  if (doc._attachments) {
    for (var attachmentKey in doc._attachments) {
      ct+=1;
	var attachment = doc._attachments[attachmentKey];
      len += attachment.length;
    }
  }
  emit([len,ct,doc.openWith,doc.title], [ct,len]);
}
