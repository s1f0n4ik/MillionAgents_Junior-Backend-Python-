CREATE TABLE pos

(

    id int PRIMARY KEY,

    title character varying

);

CREATE TABLE reports

(

    id int PRIMARY KEY,

    barcode character varying,

    price float,

    pos_id int

);


SELECT
    r.barcode,
    r.price
FROM
    reports r
JOIN
    (SELECT pos_id
     FROM reports
     GROUP BY pos_id
     HAVING COUNT(DISTINCT barcode) > 1) AS duplicate_barcodes
ON
    r.pos_id = duplicate_barcodes.pos_id
JOIN
    pos p
ON
    r.pos_id = p.id;
