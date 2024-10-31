CREATE TABLE reports

(

    id int PRIMARY KEY,

    user_id int,

    reward int,

    created_at timestamp without time zone

);


SELECT
    r.user_id,
    SUM(r2.reward) AS total_reward_2022
FROM
    reports r
JOIN
    (SELECT user_id, MIN(created_at) AS first_report_date
     FROM reports
     GROUP BY user_id) AS first_reports
ON
    r.user_id = first_reports.user_id
AND
    EXTRACT(YEAR FROM first_reports.first_report_date) = 2021
JOIN
    reports r2
ON
    r.user_id = r2.user_id
AND
    EXTRACT(YEAR FROM r2.created_at) = 2022
GROUP BY
    r.user_id;
