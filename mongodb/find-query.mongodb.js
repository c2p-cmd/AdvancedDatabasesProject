// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("mongo_stories");

// Find all documents.
use("mongo_stories");
db.stories.find();

// Find all documents with the title "The Fox and The Grapes".
use("mongo_stories");
db.stories.find({ title: "The Fox and The Grapes" });

// Find recent stories.
use("mongo_stories");
db.stories.find().sort({ datetime: -1 }).limit(5);

// Find stories before 18 April 2024
use("mongo_stories");
db.stories.find({ datetime: { $lt: "2024-04-18" } });

// Find stories after 18 April 2024
use("mongo_stories");
db.stories.find({ datetime: { $gt: "2024-04-18" } });

// Find random one story between 15 Jan 2024 and 18 April 2024
use("mongo_stories");
db.stories.aggregate([
  {
    $match: {
      datetime: { $gte: "2024-01-15", $lte: "2024-04-18" },
    },
  },
  { $sample: { size: 1 } },
]);

// Find all authors
use("mongo_stories");
db.stories.distinct("author");

// Find all Stories by author "Rajesh Kumar Verma"
use("mongo_stories");
db.stories.find({ author: "Rajesh Kumar Verma" });
