# Advanced Databases Project

A comprehensive project showcasing database operations, and data modeling across MongoDB and MySQL. This project demonstrates practical applications of advanced database concepts through two distinct implementations.

## Overview

This repository contains two sub-projects:

- **MongoDB Implementation**: A collection of scripts for working with a story database (completed)
- **MySQL Implementation**: SQL database component (in progress)

## MongoDB Implementation

The MongoDB portion of the project is fully implemented and includes various examples of:

- Basic CRUD operations
- Aggregation pipelines

### Key Features

- **Query Operations**: Find operations with various filters
- **Aggregation Framework**: Data analysis using MongoDB's aggregation pipelines

### Directory Structure

```
/mongodb
├── initialize-db.mongodb.js   # Script to initiliaze db with sample data
├── find-query.mongodb.js      # All find operations
├── update.mongodb.js          # Update operation
├── delete.mongodb.js          # Delete operation
├── aggregation.mongodb.js     # Aggregation pipeline examples
└── Short_Stories.json         # Sample data
```

### Queries

The implementation includes queries for:

- Finding stories by author, date range, and title
- Sorting and limiting results
- Random document selection
- Complex data transformations and analysis

## MySQL Implementation (Coming Soon)

The MySQL portion of the project is currently under development and will include:

- Table creation and schema design
- Advanced SQL queries
- Stored procedures and functions
- Transaction management
- Performance optimization

## Getting Started

### Prerequisites

- MongoDB 8+ installed
- MySQL 8.0+ installed

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

## Acknowledgments

- MongoDB documentation and best practices
- Advanced database design principles
