// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("mongo_stories");

// Update the story with title "Belling the Cat" to "Belling the Cat (Updated)"
db.stories.updateOne(
  { title: "Belling the Cat" },
  { $set: { author: "Suzie Wolfgang" } }
);

// Find the updated story
// db.stories.find({ title: "Belling the Cat" });
