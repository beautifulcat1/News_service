DROP TABLE IF EXISTS userProfile;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS comments;

CREATE TABLE userProfile (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  userID TEXT,
  addres TEXT,
  NewsImage TEXT,
  NewsTitle TEXT,
  Source TEXT

); 
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  userID TEXT UNIQUE,
  pwd TEXT

);
CREATE TABLE comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  address TEXT,
  comment TEXT
  -- PRAGMA foreign_keys = ON

);
