use test;

db.zips.aggregate([
	{
	 	$match: 
	  	{
	  		$or : [{state: "CA"}, {state:"NY"}] 
	  	}
	},  
	{
    	$group: 
    	{
	  		"_id" : {
	  		"city" : "$city",
	  		"state" : "$state"
	  		},
	  		"total_pop_by_city" : { $sum : "$pop" }
  		}
	},  
	{
	  	$match: 
	  	{
	  		total_pop_by_city : { $gt : 25000 }
	    }
	},
	{
  		$group: 
  		{
  			"_id" : 0,
  			"avg" : { $avg : "$total_pop_by_city" }
  		}
	}
]);