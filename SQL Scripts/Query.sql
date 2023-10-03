#1
SHOW TABLES;

# The tables are related to each other in vairous ways. The PAINTING, SCULPTED, OTHER, PERMANENT_COLLECTION, BORROWED 
# and DISPLAYED_AT tables all consist of the foriegn key called Id_no. ALL these foreign keys relate back to the Primary 
# key In the ART_OBJECT table where the primary key is called Id_no. The attribute in the ART_OBJECT table called Artist, 
# relates to the primary key in the table ARTIST. The attribute in the tablled BORROWED called Collection_Name, relates to 
# the Primary key of the table Collection. And finally the attribute in the table DISPLAYED_AT related to the Primary key 
# in the table EXHIBIT.

#2
SELECT *
FROM ART_OBJECTS;

#3
SELECT (Name)
FROM EXHIBIT AS E
ORDER BY E.Start_Date ASC;

#4
SELECT (Current_Contact_Point)
FROM COLLECTION AS C
WHERE C.Name IN (SELECT B.Collection_Name FROM BORROWED AS B);

#5
SELECT Name, AO.Id_no, AO.year, AO.Title, AO.Description
FROM ARTIST AS A LEFT JOIN ART_OBJECTS AS AO ON AO.Artist=A.Name
WHERE A.Origin_Country = 'Spain';

#6
UPDATE ART_OBJECTS SET Origin_Country_Culture = 'England'
WHERE Id_no = '000000005';

#7
DELETE FROM ARTIST
WHERE NAME = 'Robert Pruitt';
