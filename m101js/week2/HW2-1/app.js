var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/weather', function(err, db) {
  if (err) throw err;

  var query    = {"Wind Direction": {"$gte": 180, "$lte": 360}},
      state    = "";
      min_temp = Infinity;

  db.collection('data').find(query).each(function(err, doc) {
    if (err) throw err;

    if (doc === null) {
      console.dir(state);
      return db.close();
    }

    if (doc['Temperature'] < min_temp) {
      min_temp = doc['Temperature'];
      state    = doc['State'];
    }

  });
});

