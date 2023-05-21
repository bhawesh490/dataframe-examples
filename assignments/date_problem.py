"""
You have a table with one column, `original_date`, of datatype string
ORIGINAL_DATE
20190825
20190826
20190827
20190828
20190829
20190830
20190831
20190901

Question:
Write a SQL query to calculate two more columns –
    `end_of_week ` - the date of the next Sunday from `original_date`. If `original_date` is already a Sunday, this field should be the same value
    `end_of_month ` - the value of the end of month date

An acceptable solution is one which works for any valid date in the string format of `original_date`.

Expected Output:
20190825	2019-08-25	2019-08-31
20190826	2019-09-01	2019-08-31
20190827	2019-09-01	2019-08-31
20190828	2019-09-01	2019-08-31
20190829	2019-09-01	2019-08-31
20190830	2019-09-01	2019-08-31
20190831	2019-09-01	2019-08-31
20190901	2019-09-01	2019-09-30

Solution in MySQL:
SELECT
  ORIGINAL_DATE,
  DATE(original_date + INTERVAL (6 - WEEKDAY(original_date)) DAY) as END_OF_WEEK,
  last_day(original_date) AS END_OF_MONTH
from
  random_dates;

"""