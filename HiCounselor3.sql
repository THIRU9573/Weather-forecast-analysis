CREATE DATABASE HICOUNSELOR2;
USE HICOUNSELOR2;
SELECT * FROM hicounselor2.weather_dataset_stage;
DROP TABLE weather_dataset_stage;
DROP TABLE hicounselor2.weather_table2;

DESCRIBE weather_dataset_stage;

-- 1.Give the count of the minimum number of days for the time when temperature reduced ---

SELECT COUNT(DISTINCT Date)
FROM (
  SELECT Date, Temperature,
         LAG(Temperature) OVER (ORDER BY Date) AS Prev_Temp
  FROM weather_dataset_stage
) AS subq
WHERE Temperature < Prev_Temp;

-- 2.Find the temperature as Cold / hot by using the case and avg of values of the given data set --

SELECT Date, Temperature, 
       CASE 
         WHEN Temperature < AVG(Temperature) OVER () THEN 'COLD'
         ELSE 'HOT'
       END AS Temperature_Category
FROM weather_dataset_stage;

-- 3.	Can you check for all 4 consecutive days when the temperature was below 30 Fahrenheit

    CREATE TEMPORARY TABLE t1 SELECT Date, Temperature,
SUM(CASE WHEN Temperature < 30 THEN 1 ELSE 0 END)
OVER (ORDER BY Date ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS below_30_count
FROM weather_dataset_stage ;
SELECT date, temperature FROM t1 WHERE below_30_count = 4;
    
  --   4.Can you find the maximum number of days for which temperature dropped --
SELECT MAX(count_days) FROM (
   SELECT
      t1.Date,
      t1.Temperature,
      (
         SELECT COUNT(*)
         FROM weather_dataset_stage t2
         WHERE t2.Date < t1.Date AND t2.Temperature < t1.Temperature
      ) AS count_days
   FROM weather_dataset_stage t1
) AS temp_diff 
WHERE Temperature < (
   SELECT Temperature FROM weather_dataset_stage t2
   WHERE t2.Date < temp_diff.Date
   ORDER BY Date DESC 
   LIMIT 1
);

-- 5.	Can you find the average of average humidity from the dataset 

-- ( NOTE: should contain the following clauses: group by, order by, date ) ---

SELECT `Date`, AVG(`Average humidity (%`) AS avg_humidity
FROM weather_dataset_stage
GROUP BY `Date`
ORDER BY `Date` ASC;


-- 6.Use the GROUP BY clause on the Date column and make a query to fetch details for average windspeed ( which is now windspeed done in task 3 )
SELECT Date, AVG(`Average windspeed (mph`) AS Average_windspeed
FROM weather_dataset_stage 
GROUP BY Date
ORDER BY Date;

-- 7.Please add the data in the dataset for 2034 and 2035 as well as forecast predictions for these years 

-- ( NOTE: data consistency and uniformity should be maintained )   ------



-- 8.If the maximum gust speed increases from 55mph, fetch the details for the next 4 days --
SELECT * 
FROM weather_dataset_stage 
WHERE Date > (
    SELECT Date 
    FROM weather_dataset_stage 
    WHERE `Average gustspeed (mph` > 55 
    ORDER BY Date ASC 
    LIMIT 1
) 
ORDER BY Date ASC 
LIMIT 4;

-- 9.Find the number of days when the temperature went below 0 degrees Celsius  --

SELECT COUNT(*) AS days_below_0 
FROM weather_dataset_stage 
WHERE (`Minimum temperature (Â°F` - 32) * 5/9 < 0;

-- 10.Create another table with a “Foreign key” relation with the existing given data set.-----
ALTER TABLE weather_dataset_stage ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST ;

CREATE TABLE weather_table2 (
   id INT PRIMARY KEY AUTO_INCREMENT,
   Date VARCHAR(50) NOT NULL,
   Temperature FLOAT NOT NULL,
   `Average humidity (%` DOUBLE NOT NULL,
   `Average barometer (in` DOUBLE NOT NULL,
   `Average windspeed (mph` DOUBLE NOT NULL,
   `Rainfall for month (in` DOUBLE NOT NULL,
   `Rainfall for year (in` DOUBLE NOT NULL,
   Month INT NOT NULL,
   diff_pressure DOUBLE NOT NULL,
   FOREIGN KEY (id)
     REFERENCES weather_dataset_stage (id)
     ON DELETE CASCADE
);

INSERT INTO weather_table2
(id,
   Date,
   Temperature ,
   `Average humidity (%`,
   `Average barometer (in`,
   `Average windspeed (mph` ,
   `Rainfall for month (in`,
   `Rainfall for year (in`,
   Month ,
   diff_pressure) 
SELECT DISTINCT
id,
   Date,
   Temperature ,
   `Average humidity (%`,
   `Average barometer (in`,
   `Average windspeed (mph` ,
   `Rainfall for month (in`,
   `Rainfall for year (in`,
   Month ,
   diff_pressure FROM hicounselor2.weather_dataset_stage;

DESCRIBE weather_dataset_stage;






