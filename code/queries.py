# PROBLEM 1
# How many artists are there?
# Return a single column called "count" with a single row containing the count.

query_1 = """
SELECT COUNT(*) AS "count"
FROM public."Artist";
"""


# PROBLEM 2
# How many Artists do not have an Album associated with them?
# Return a single column called "count" with a single row containing the count.
query_2 = """
SELECT COUNT(*) AS "count"
FROM public."Artist" AS a
LEFT JOIN public."Album" AS al ON a."ArtistId" = al."ArtistId"
WHERE al."AlbumId" IS NULL;
"""


# PROBLEM 3
# How many Albums do not have an artist in the Artist table associated with them?
# Return a single column called "count" with a single row containing the count.
query_3 = """
SELECT COUNT(*) AS "count"
FROM public."Album" AS al
LEFT JOIN public."Artist" AS a ON al."ArtistId" = a."ArtistId"
WHERE a."ArtistId" IS NULL;
"""


# PROBLEM 4
# List the tracks by "AC/DC"
# Return a single column called "AC/DC Tracks",
# in any order.
query_4 = """
SELECT t."Name" AS "AC/DC Tracks"
FROM public."Track" AS t
JOIN public."Album" AS al ON t."AlbumId" = al."AlbumId"
JOIN public."Artist" AS a ON al."ArtistId" = a."ArtistId"
WHERE a."Name" = 'AC/DC';
"""


# PROBLEM 5
# Find the total sales of AC/DC Tracks.
# Return a single column called "Total Sales" with a single row containing the total.

query_5 = """
SELECT SUM(il."UnitPrice" * il."Quantity") AS "Total Sales"
FROM public."InvoiceLine" AS il
JOIN public."Track" AS t ON il."TrackId" = t."TrackId"
JOIN public."Album" AS al ON t."AlbumId" = al."AlbumId"
JOIN public."Artist" AS a ON al."ArtistId" = a."ArtistId"
WHERE a."Name" = 'AC/DC';
"""


# PROBLEM 6
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# for the artists with less than or equal to $5 in sales,
# in any order.

query_6 = """
SELECT a."Name" AS "Artist", SUM(il."UnitPrice" * il."Quantity") AS "Total Sales"
FROM public."InvoiceLine" AS il
JOIN public."Track" AS t ON il."TrackId" = t."TrackId"
JOIN public."Album" AS al ON t."AlbumId" = al."AlbumId"
JOIN public."Artist" AS a ON al."ArtistId" = a."ArtistId"
GROUP BY a."Name"
HAVING SUM(il."UnitPrice" * il."Quantity") <= 5;
"""


# PROBLEM 7
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# in descending order of "Total Sales".

query_7 = """
SELECT a."Name" AS "Artist", SUM(il."UnitPrice" * il."Quantity") AS "Total Sales"
FROM public."InvoiceLine" AS il
JOIN public."Track" AS t ON il."TrackId" = t."TrackId"
JOIN public."Album" AS al ON t."AlbumId" = al."AlbumId"
JOIN public."Artist" AS a ON al."ArtistId" = a."ArtistId"
GROUP BY a."Name"
ORDER BY "Total Sales" DESC;
"""


# PROBLEM 8
# Find all of "Michael Mitchell"'s direct reports.
# Return 2 columns called "Name" and "Title".
# "Name" should have the employee's name in the form "last name, first name",
# for example, someone with the last name "Smith" and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_8 = """
SELECT CONCAT(e."LastName", ', ', e."FirstName") AS "Name", e."Title"
FROM public."Employee" AS e
JOIN public."Employee" AS m ON e."ReportsTo" = m."EmployeeId"
WHERE m."FirstName" = 'Michael' AND m."LastName" = 'Mitchell';
"""


# PROBLEM 9
# Make a reporting chart. For each employee, find their name, title, manager's name and manager's title.
# Return 4 columns called "Employee Name" and "Employee Title", "Manager Name" and "Manager Title",
# "Employee Name" and "Manager Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_9 = """
SELECT 
    CONCAT(e."LastName", ', ', e."FirstName") AS "Employee Name",
    e."Title" AS "Employee Title",
    CONCAT(m."LastName", ', ', m."FirstName") AS "Manager Name",
    m."Title" AS "Manager Title"
FROM public."Employee" AS e
LEFT JOIN public."Employee" AS m ON e."ReportsTo" = m."EmployeeId";
"""


# PROBLEM 10
# Find the most recently hired employee(s) and their hire date(s)
# Return two columns called "Name" and "Hire Date",
# in any order.
# "Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Smith, Bob"

query_10 = """
SELECT CONCAT("LastName", ', ', "FirstName") AS "Name", "HireDate" AS "Hire Date"
FROM public."Employee"
WHERE "HireDate" = (SELECT MAX("HireDate") FROM public."Employee");
"""


# PROBLEM 11
# Assume today is "2010-01-01", find every employee's tenure.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in any order.


query_11 = """
SELECT "FirstName" AS "First Name", 
       "LastName" AS "Last Name",
       (DATE '2010-01-01' - "HireDate") AS "Tenure"
FROM public."Employee";
"""



# PROBLEM 12
# Assume today is 2010-01-01, find every employee with a tenure of less than 7 365-day years.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in ascending order of tenure.

query_12 = """
SELECT 
       e."FirstName" AS "First Name", 
       e."LastName" AS "Last Name",
       (DATE '2010-01-01' - e."HireDate") AS "Tenure"
FROM "Employee" e
WHERE (DATE '2010-01-01' - e."HireDate") < INTERVAL '7 years'
ORDER BY "Tenure" ASC;
"""

