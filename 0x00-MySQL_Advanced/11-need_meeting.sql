-- Active: 1716468751032@@127.0.0.1@3306@holberton
DROP VIEW need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE
    students.score < 80
    AND students.last_meeting IS NULL
    OR last_meeting < SUBDATE(
        CURRENT_DATE(),
        INTERVAL 1 MONTH
    );
;
