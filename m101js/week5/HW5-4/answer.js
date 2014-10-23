use test;

db.zips.aggregate([
  {$match:
    {
      city: /^[0-9]/
    }
  },
  {$group:
    {
      "_id": null,
      "result": {$sum: '$pop'}
    }
  }
])