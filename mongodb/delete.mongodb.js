// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("mongo_stories");

// Find a document in a collection.
db.stories.deleteOne({ author: "Suzie Wolfgang" });
