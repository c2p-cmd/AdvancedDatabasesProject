// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("mongo_stories");


// Count stories by author
db.stories.aggregate([
  { $group: { _id: "$author", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
]);

// Stories published per month
db.stories.aggregate([
  { 
    $addFields: {
      monthYear: { 
        $substr: ["$datetime", 0, 7]
      }
    }
  },
  { $group: { _id: "$monthYear", count: { $sum: 1 } } },
  { $sort: { _id: -1 } }
]);

// Average story length by author
db.stories.aggregate([
  { 
    $addFields: { 
      storyLength: { $strLenCP: "$story" } 
    } 
  },
  { 
    $group: { 
      _id: "$author", 
      averageLength: { $avg: "$storyLength" },
      totalStories: { $sum: 1 }
    } 
  },
  { $sort: { averageLength: -1, totalStories: -1 } }
]);

// Story counts by time period
db.stories.aggregate([
  {
    $facet: {
      "last30Days": [
        { $match: { datetime: { $gte: "2024-02-15" } } },
        { $count: "count" }
      ],
      "last90Days": [
        { $match: { datetime: { $gte: "2023-12-15" } } },
        { $count: "count" }
      ],
      "last365Days": [
        { $match: { datetime: { $gte: "2023-03-15" } } },
        { $count: "count" }
      ]
    }
  }
]);

// Stories by length categories
db.stories.aggregate([
  {
    $addFields: {
      storyLength: { $strLenCP: "$story" },
      lengthCategory: {
        $switch: {
          branches: [
            { case: { $lt: [{ $strLenCP: "$story" }, 1000] }, then: "Short" },
            { case: { $lt: [{ $strLenCP: "$story" }, 5000] }, then: "Medium" },
          ],
          default: "Long"
        }
      }
    }
  },
  { $group: { _id: "$lengthCategory", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
]);