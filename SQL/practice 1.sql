create database xyz;
create table team(
eid int primary key,
name varchar(50)
);

INSERT INTO team (eid, name) 
VALUES 
(3, 'anant');

SELECT * FROM team;
