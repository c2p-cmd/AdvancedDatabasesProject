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

## MySQL Implementation

The MySQL portion implements a video game store database with comprehensive functionality:

### Database Schema

![ERD](./mysql/ERD.svg)

The gaming database includes the following tables:

- Gamers: Users who purchase games
- GamePublishers: Companies that publish video games
- VideoGames: Game titles with details and pricing
- Purchases: Records of game purchases by gamers

### Key Features

- Database Design: Well-structured tables with primary and foreign keys
- Stored Procedures: Implement key business logic like purchasing games
- Triggers: Ensure data integrity and business rules
- Data Analysis: SQL queries for business intelligence and analytics
- Joins: Demonstrate relationships between database entities

### Directory Structure

```
/mysql
├── CREATE.sql               # Database and table creation script
├── INSERT.sql               # Sample data for all tables
├── CREATE_PROCEDURES.sql    # Stored procedures implementation
├── TRIGGERS.sql             # Database triggers
├── Analytics.sql            # Business intelligence queries
└── PROCEDURE_EXAMPLE.sql    # Examples of procedure calls
```

## Getting Started

### Prerequisites

- MongoDB 8+ installed
- MySQL 8.0+ installed

### Running MongoDB Scripts

- Start your MongoDB server
- Open MongoDB Shell or MongoDB Compass
- Load and execute the scripts in the mongodb directory

### Running MySQL Implementation

- Start your MySQL server
- Run the scripts in the following order:
  - `CREATE.sql` - Creates database schema
  - `INSERT.sql` - Populates tables with sample data
  - `CREATE_PROCEDURES.sql` - Adds stored procedures
  - `CREATE_TRIGGERS.sql` - Sets up database triggers
- Execute example procedures with `PROCEDURE_EXAMPLE.sql`
- Execute examples for the trigger with `TRIGGER_EXAMPLE.sql`
- Run analytics queries from `ANALYTICS.sql`

## Data Visualization Dashboard

The project includes an optional interactive Dash web application that visualizes the MySQL gaming database analytics:

### Dashboard Features

- **Interactive Visualizations**: Charts and graphs providing insights into game popularity, pricing, and purchasing patterns
- **Multi-tab Interface**: Organized views for Game Analytics, Gamer Analytics, Publisher Analytics, and more
- **Live Database Connection**: Direct connection to the MySQL database for real-time data
- **Email Domain Analysis**: Visual comparison between Gmail and iCloud users' gaming preferences
- **Stored Procedure Integration**: Execute and visualize results from database stored procedures

### Dashboard Components

- Game popularity and pricing trends
- Gamer spending patterns and activity levels
- Publisher performance metrics
- Interactive query selector for custom analysis
- Gamer library lookup functionality

### Running the Dashboard

1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure database connection:

- Create a .env file in the root directory
- Add your database connection string: `DB_CONNECTION_STR=mysql+pymysql://username:password@localhost/gaming_db`

3. Start the dashboard:

```
python dashboard/app.py
```

4. Open your browser to http://127.0.0.1:8050/

![App Screenshot](./dashboard/dahs_app.png)

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

## Acknowledgments

- MongoDB documentation and best practices
- Advanced database design principles
