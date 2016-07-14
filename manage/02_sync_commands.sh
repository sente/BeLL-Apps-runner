#!/bin/bash

PORT=5984
BELL_APPS_DIRECTORY=/Users/stu/code/ole/BeLL-Apps/

cd "${BELL_APPS_DIRECTORY}" || exit 1

node_modules/.bin/couchapp sync databases/activitylog.js http://127.0.0.1:${PORT}/activitylog &
node_modules/.bin/couchapp sync databases/apps.js http://127.0.0.1:${PORT}/apps &
node_modules/.bin/couchapp sync databases/assignmentpaper.js http://127.0.0.1:${PORT}/assignmentpaper &
node_modules/.bin/couchapp sync databases/assignments.js http://127.0.0.1:${PORT}/assignments &
node_modules/.bin/couchapp sync databases/calendar.js http://127.0.0.1:${PORT}/calendar &
node_modules/.bin/couchapp sync databases/collectionlist.js http://127.0.0.1:${PORT}/collectionlist &
node_modules/.bin/couchapp sync databases/community.js http://127.0.0.1:${PORT}/community &
node_modules/.bin/couchapp sync databases/communityreports.js http://127.0.0.1:${PORT}/communityreports &
node_modules/.bin/couchapp sync databases/courseschedule.js http://127.0.0.1:${PORT}/courseschedule &
node_modules/.bin/couchapp sync databases/coursestep.js http://127.0.0.1:${PORT}/coursestep &
node_modules/.bin/couchapp sync databases/feedback.js http://127.0.0.1:${PORT}/feedback &
node_modules/.bin/couchapp sync databases/groups.js http://127.0.0.1:${PORT}/groups &
node_modules/.bin/couchapp sync databases/invitations.js http://127.0.0.1:${PORT}/invitations &
node_modules/.bin/couchapp sync databases/mail.js http://127.0.0.1:${PORT}/mail &
node_modules/.bin/couchapp sync databases/meetups.js http://127.0.0.1:${PORT}/meetups &
node_modules/.bin/couchapp sync databases/membercourseprogress.js http://127.0.0.1:${PORT}/membercourseprogress &
node_modules/.bin/couchapp sync databases/members.js http://127.0.0.1:${PORT}/members &
node_modules/.bin/couchapp sync databases/nationreports.js http://127.0.0.1:${PORT}/nationreports &
node_modules/.bin/couchapp sync databases/publicationdistribution.js http://127.0.0.1:${PORT}/publicationdistribution &
node_modules/.bin/couchapp sync databases/publications.js http://127.0.0.1:${PORT}/publications &
node_modules/.bin/couchapp sync databases/report.js http://127.0.0.1:${PORT}/report &
node_modules/.bin/couchapp sync databases/requests.js http://127.0.0.1:${PORT}/requests &
node_modules/.bin/couchapp sync databases/resourcefrequency.js http://127.0.0.1:${PORT}/resourcefrequency &
node_modules/.bin/couchapp sync databases/resources.js http://127.0.0.1:${PORT}/resources &
node_modules/.bin/couchapp sync databases/shelf.js http://127.0.0.1:${PORT}/shelf &
node_modules/.bin/couchapp sync databases/survey.js http://127.0.0.1:${PORT}/survey &
node_modules/.bin/couchapp sync databases/surveyanswers.js http://127.0.0.1:${PORT}/surveyanswers &
node_modules/.bin/couchapp sync databases/surveyquestions.js http://127.0.0.1:${PORT}/surveyquestions &
node_modules/.bin/couchapp sync databases/surveyresponse.js http://127.0.0.1:${PORT}/surveyresponse &
node_modules/.bin/couchapp sync databases/usermeetups.js http://127.0.0.1:${PORT}/usermeetups &
