// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("mongo_stories");
db.stories.find({ title: "The Cock and the Fox" });

// Update the story with title "The Cock and the Fox" to "Belling the Cat (Updated)"
use("mongo_stories");
db.stories.updateOne(
  { title: "The Cock and the Fox" },
  { $set: { author: "Suzie Wolfgang" } }
);
