var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/weather', function(err, db) {
  if (err) throw err;

  var query    = {}
      options  = {'sort': [["State", 1], ["Temperature", -1]]},
      operator = {'$set': {'month_high': true}},
      state    = '';

  var cursor = db.collection('data').find(query, {}, options);

  cursor.each(function(err, doc) {
    if (err) throw err;

    if (doc === null)
      return db.close();

    else if (doc['State'] !== state) {
      state = doc['State'];
      db.collection('data').update({'_id': doc._id}, operator, function(err, updated) {
        if (err) throw err;
        console.dir('Document updated successfully!');
      });
    }
  });
});
