CREATE DATABASE secretnotes;
use secretnotes;

CREATE TABLE notes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  content VARCHAR(1000),
  creation_time DateTime DEFAULT CURRENT_TIMESTAMP,
  expiration_time DateTime default CURRENT_TIMESTAMP
);

-- INSERT INTO notes
--   (content, creation_time, expiration_time)
-- VALUES
--   ('seed note');