use m101;

db.profile.find({'ns': /^school2/}, {millis: true}).sort({millis: -1}).limit(1)