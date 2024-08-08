-- Active: 1716468751032@@127.0.0.1@3306@holberton

SELECT origin, SUM(fans) as nb_fans
from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
