use test;

db.zips.aggregate([
  {$match:
    {
      state: { $in: ["CA", "NY"] }
    }
  },
  {$group:
    {
      "_id":
      {
        "city": "$city",
        "state": "$state"
      },
      "total_pop_by_city" : { $sum : "$pop" }
    }
  },
  {$match :
    {
      total_pop_by_city : { $gt : 25000 }
    }
  },
  {$group :
    {
      "_id" : null,
      "avg" : { $avg : "$total_pop_by_city" }
    }
  }
]);