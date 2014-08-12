use test;

db.zips.aggregate([
    {
        $project: 
        {
           first_c: {$substr : ["$city",0,1]},
           pop: "$pop"
        }
    },
    {
        $match: {'first_c':/\d/}
    },
    {
        $group: 
        {
            _id: null,
            avg_p: {$sum: '$pop'}
        }
    }
]);