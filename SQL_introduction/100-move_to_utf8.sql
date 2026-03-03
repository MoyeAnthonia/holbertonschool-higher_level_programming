-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) 
-- Step 1: Convert the database default
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 2: Convert the table AND all its character columns in one go
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
