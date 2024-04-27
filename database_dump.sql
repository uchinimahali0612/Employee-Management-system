BEGIN TRANSACTION;
CREATE TABLE Employees (
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   role TEXT,
                   gender TEXT,
                   status TEXT, gmail VARCHAR(255), age INTEGER, department TEXT);
INSERT INTO "Employees" VALUES('1','Moopanar  Uchinimahali Esakki','Developer','Female','Active','uchi@gmail.com',21,'IT');
INSERT INTO "Employees" VALUES('2','Sanika bhojane','Data Science','Female','Active','sanikabhojane@gmail.com',21,'IT');
INSERT INTO "Employees" VALUES('3','Maithily Kedare','Data Science','Female','Default','maithilykedare@gmail.com',22,'IT');
INSERT INTO "Employees" VALUES('4','Manasi Shejwal','UX Designer','Female','Active','manasishejwal@gmail.com',22,'IT');
INSERT INTO "Employees" VALUES('5','Athira','Manager','Female','Absent','athira@gmail.com',23,'NON-IT');
INSERT INTO "Employees" VALUES('6','Priti Prajapati','Manager','Female','Absent','priti@gmail.com',23,'NON-IT');
COMMIT;
