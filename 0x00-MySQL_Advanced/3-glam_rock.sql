-- Active: 1716468751032@@127.0.0.1@3306@holberton
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan
FROM metal_bands
WHERE `style` LIKE '%Glam rock%'
ORDER BY lifespan DESC;
