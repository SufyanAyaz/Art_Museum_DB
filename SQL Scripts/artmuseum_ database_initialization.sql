DROP DATABASE IF EXISTS artmuseum;
CREATE DATABASE artmuseum;
USE artmuseum;

DROP TABLE IF EXISTS ART_OBJECTS;
CREATE TABLE ART_OBJECTS
( Id_no						VARCHAR(10)		NOT NULL,
  year						INT,
  Title						VARCHAR(120)		NOT NULL,
  Description				VARCHAR(500)	NOT NULL,
  Origin_Country_Culture	VARCHAR(30)		NOT NULL,
  Epoch						VARCHAR(25)		NOT NULL, 
  Artist					VARCHAR (50),
CONSTRAINT AOPK		PRIMARY KEY (Id_no));



DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING
( Id_no					VARCHAR(10)		NOT NULL,
  Paint_Type			VARCHAR(25)		NOT NULL,
  Style					VARCHAR(25)	NOT NULL,
  Material_Drawn_On		VARCHAR(25)		NOT NULL,

CONSTRAINT PPK		PRIMARY KEY (Id_no),
CONSTRAINT PFK		FOREIGN KEY (Id_no)		REFERENCES ART_OBJECTS(Id_no));



DROP TABLE IF EXISTS SCULPTED;
CREATE TABLE SCULPTED
( Id_no				VARCHAR(10)		NOT NULL,
  is_Sculpture		BOOLEAN,
  is_statue			BOOLEAN,
  Material			VARCHAR(25)		NOT NULL,
  Style				VARCHAR(25)		NOT NULL,
  Height			INT				NOT NULL,
  Weight			INT				NOT NULL,

CONSTRAINT SPK		PRIMARY KEY (Id_no),
CONSTRAINT SFK		FOREIGN KEY (Id_no)		REFERENCES ART_OBJECTS(Id_no));



DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER
( Id_no				VARCHAR(10)		NOT NULL,
  Style				VARCHAR(25)		NOT NULL,
  Type				VARCHAR(25)		NOT NULL,

CONSTRAINT OPK		PRIMARY KEY (Id_no),
CONSTRAINT OFK		FOREIGN KEY (Id_no)		REFERENCES ART_OBJECTS(Id_no));



DROP TABLE IF EXISTS PERMANET_COLLECTION;
CREATE TABLE PERMANET_COLLECTION
( Id_no				VARCHAR(10)		NOT NULL,
  Date_Acquired		DATE			NOT NULL,
  Cost				INT				NOT NULL,
  Status				VARCHAR(25)		NOT NULL,

CONSTRAINT PCPK		PRIMARY KEY (Id_no),
CONSTRAINT PCFK		FOREIGN KEY (Id_no)		REFERENCES ART_OBJECTS(Id_no));



DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED
( Id_no					VARCHAR(10)		NOT NULL,
  Date_Borrowed			DATE			NOT NULL,
  Date_returned			DATE			NOT NULL,
  Collection_Name		VARCHAR(80)		NOT NULL,

CONSTRAINT BPK		PRIMARY KEY (Id_no),
CONSTRAINT BFK		FOREIGN KEY (Id_no)		REFERENCES ART_OBJECTS(Id_no));



DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST
( Name					VARCHAR(50),
  Date_Born				DATE,
  Date_Died				DATE,
  Description			VARCHAR(500),
  Origin_Country		VARCHAR(30),
  Main_Style			VARCHAR(25),

CONSTRAINT APK		PRIMARY KEY (Name));



DROP TABLE IF EXISTS COLLECTION;
CREATE TABLE COLLECTION
( Name							VARCHAR(80)		NOT NULL,
  Type							VARCHAR(25)		NOT NULL,
  Description					VARCHAR(500)	NOT NULL,
  Current_Contact_Point			VARCHAR(50)		NOT NULL,
  Address						VARCHAR(50)		NOT NULL,
  Phone							VARCHAR(20)		NOT NULL,

CONSTRAINT CPK		PRIMARY KEY (Name));



DROP TABLE IF EXISTS EXHIBIT;
CREATE TABLE EXHIBIT
( Name					VARCHAR(80)		NOT NULL,
  Start_Date			DATE			NOT NULL,
  End_Date				DATE			NOT NULL,

CONSTRAINT EPK		PRIMARY KEY (Name));



DROP TABLE IF EXISTS DISPLAYED_AT;
CREATE TABLE DISPLAYED_AT
( Id_no				VARCHAR(10)			NOT NULL  ,
  Name				VARCHAR(80)			NOT NULL  ,

CONSTRAINT EPK		PRIMARY KEY (Id_no, Name),
CONSTRAINT EIFK		FOREIGN KEY (Id_no)		REFERENCES ART_OBJECTS(Id_no), 
CONSTRAINT ENFK		FOREIGN KEY (Name)		REFERENCES EXHIBIT(Name));



INSERT INTO ART_OBJECTS 
VALUES 
('000000001',1527,'Sir Thomas More','Portrait of Sir Thomas More is an oak panel painting commissioned in 1527 of Thomas More by the German artist and printmaker Hans Holbein','England','Northern Renaissance','Hans Holbein the Younger'),
('000000002',1583,'Elizabeth I (The Sieve Portrait)','Known as the Sieve Portrait because the queen holds a large sieve in her left hand which is a traditional symbol of chastity.','England','Elizabethan Era','Quentin Metsys the Younger'),
('000000003',1529,'Angel Bearing Candlestick','This statue represents a candle-bearing angel stepping forward, knees slightly bent, portraying a sense of movement and energy.','Italy','Renaissance England','Benedetto da Rovezzano'),
('000000004',1505,'Unidentified Saint','The statue of Unidentified Saint was made in the early 16th century.','England','Renaissance England',NULL),
('000000005',1520,'Furnishing Textile','Velvets patterned with this fifteenth-sixteenth century version of the palmette were named "pomegranate velvets" in the nineteenth century.','Italy','Renaissance England',NULL),
('000000006',1554,'Portrait Medal of Queen Mary I with Allegory of Peace','The reverse of Queen Marys medal praises the benefits of her reign: a peaceful realm and reconciliation with Rome.','Italy','Elizabethan Era','Jacopo Nizolla da Trezzo'),
('000000013',2019,'Birth and Rebirth and Rebirth','This consists of three large scale banners, each printed with reproductions of original drawings front and back.','America','Modern','Robert Pruitt'),
('000000014',1885,'Face jug','Face jugs were made by African American slaves and freedmen working in potteries in the Edgefield District of South Carolina','America','Neoclassicism movement',NULL),
('000000015',1858,'Storage jar','This monumental storage jar, by the enslaved African American potter David Drake, reveals his unmatched technical facility and command of language.','America','Neoclassicism movement','David Drake'), 
('000000016',1850,'Power figure','Power figures are among the ubiquitous genres identified with African art.','Kongo','colonial era',NULL),
('000000017',2021,'K.S.','Created using human hair sourced from people of the African diaspora.','America','Modern','Adebunmi Gbadebo'),
('000000018',2021,'Applying Pressure','Clay sculpture that takes the shape of household objects that appear to melt, sigh, and twist themselves into knots.','America','Modern','Woody de Othello'),
('000000019',1503, 'Mona Lisa', 'The Mona Lisa is a half-length portrait painting by Italian artist Leonardo da Vinci.', 'Italian', 'Renaissance', 'Leonardo Da Vinci'),
('000000020',1636, 'Still Life with Four Bunches of Grapes','Still life painitng of grapes hanging in a dark chamber', 'Spanish','Renaissance', 'Juan Fernández'),
('000000021',1665, 'The Attributes of the Painter', 'A studio wall displaying the tools of the artists trade.', 'Flemish', 'Renaissance', 'Cornelius Norbertus Gijsbrechts'),
('000000022',1914, 'Glass and Checkerboard', 'The trompe loeil motif of a print attached to wood planking by nails or sealing wax.', 'Spanish', 'Synthetic Cubism', 'Juan Gris'),
('000000023',1914,'Still Life with a Bottle', 'Playing Cards, and a Wineglass on a Table', 'Spanish', 'Synthetic Cubism', 'Pablo Picasso'),
('000000024', 1914, 'The Absinthe Glass', 'Picassos life-size rendering of a glass of alcohol.', 'Spanish', 'Synthetic Cubism', 'Pablo Picasso'),
('000000025', 1914, 'Glass and Die','The carved and marbleized piece of wood fixed to the backboard may represent a curtain or a screen.', 'Spanish', 'Synthetic Cubism', 'Pablo Picasso'),
('000000026', 1881,'Marbles Plate XXII,Album du peintre en bâtiment: Travaux élémentaires. Deuxième partie, Bois, marbres, lettres','Imitates varieties of wood, the veining of marble, and the convex and concave profiles of architectural moldings.', 'French', 'Industrial Revolution', 'Eugène Berthelon'),
('000000027', 1780, 'Coffeepot','The trompe loeil motif of a print attached to wood coffee pot by sealing wax', 'Belgian', 'Industrial Revolution', 'Tournai Facotry');

INSERT INTO PAINTING 
VALUES 
('000000001','Oil Paint','Portrait','Oak'),
('000000002','Oil Paint','Portrait','Canvas'),
('000000013','Conte','Contemporary','Paper'),
('000000019', 'Oil', 'Portrait', 'Wood'),
('000000020','Oil', 'Still Life', 'Canvas'),
('000000021', 'Oil', 'Trope LOeil', 'Canvas'),
('000000022', 'Watercolour', 'Still Life', 'Canvas'),
('000000023', 'Oil', 'Still Life', 'Paperboard');

INSERT INTO SCULPTED 
VALUES 
('000000003',null,true,'Bronze','representational',103,177),
('000000004',true,null,'Terracotta','representational',52,74),
('000000016',true,null,'Iron','anthropomorphic',103.5,18),
('000000018',true,null,'Ceramic','Contemporary',48,15),
('000000024', true, null, 'Bronze', 'Abstract', 22.5, 15),
('000000025',	true, null,	'Wood',	'Abstract', 23.5, 7);

INSERT INTO OTHER 
VALUES 
('000000005','Heraldic pattern','Textile'),
('000000006','Portrait medal','Medal'),
('000000014','Impressionism','Pottery'),
('000000015','Impressionism','Pottery'),
('000000017','Contemporary','Pottery'),
('000000026', 'Chromolithograph', 'Print'),
('000000027', 'Cubism', 'Ceramics');

INSERT INTO PERMANET_COLLECTION 
VALUES 
('000000019', '1804-01-01', 870000000, 'Storage');


INSERT INTO BORROWED 
VALUES 
('000000001','2022-10-10','2023-01-08','The Met Collection: European Sculpture and Decorative Arts'),
('000000002','2022-10-10','2023-01-08','The Met Collection: European Sculpture and Decorative Arts'),
('000000003','2022-10-10','2023-01-08','The Met Collection: European Sculpture and Decorative Arts'),
('000000004','2022-10-10','2023-01-08','The Met Collection: European Sculpture and Decorative Arts'),
('000000005','2022-10-10','2023-01-08','The Met Collection: European Sculpture and Decorative Arts'),
('000000006','2022-10-10','2023-01-08','The Met Collection: European Sculpture and Decorative Arts'),
('000000013','2022-09-09','2023-02-05','The Met Collection: The American Wing'),
('000000014','2022-09-09','2023-02-05','The Met Collection: The American Wing'),
('000000015','2022-09-09','2023-02-05','The Met Collection: The American Wing'),
('000000016','2022-09-09','2023-02-05','The Met Collection: The American Wing'),
('000000017','2022-09-09','2023-02-05','The Met Collection: The American Wing'),
('000000018','2022-09-09','2023-02-05','The Met Collection: The American Wing'),
('000000020', '2022-08-20', '2023-02-22', 'The Met Collection: Modern and Contemporary Art'),
('000000021', '2022-08-20', '2023-02-22', 'The Met Collection: Modern and Contemporary Art'),
('000000022', '2022-08-20', '2023-02-22', 'The Met Collection: Modern and Contemporary Art'),
('000000023', '2022-08-20', '2023-02-22', 'The Met Collection: Modern and Contemporary Art'),
('000000024', '2022-08-20', '2023-02-22', 'The Met Collection: Modern and Contemporary Art'),
('000000025', '2022-08-20', '2023-02-22', 'The Met Collection: Modern and Contemporary Art'),
('000000026', '2022-08-20', '2023-02-22', 'The Met Collection: Modern and Contemporary Art');


INSERT INTO ARTIST 
VALUES 
('Hans Holbein the Younger','1597-12-04','1543-10-07','Hans Holbein the Younger was a German-Swiss painter and printmaker who worked in a Northern Renaissance style','Germany','Portraits'),
('Quentin Metsys the Younger',null,null,'Quentin Metsys the Younger (Quinten was a Flemish Renaissance painter, one of several of his countrymen active as artists of the Tudor court in the reign of Elizabeth I of England.','Netherlands','Portraits'),
('Benedetto da Rovezzano',null,null,'Benedetto Grazzini was an Italian architect and sculptor who worked mainly in Florence.','Italy','representational'),
('Jacopo Nizolla da Trezzo',null,null,'Jacopo was trained as a gem engraver, sculptor, and architect.','Italy','Portrait Medals'),
('Robert Pruitt',null,NULL,'Robert Pruitt is known for his figurative drawings and who also works with sculpture, photography, and animation.','America','Contemporary'),
('David Drake',null,'1865-10-28','David Drake was an American potter and enslaved African American who lived in Edgefield, South Carolina.','America','Impressionism'),
('Adebunmi Gbadebo',null,NULL,'Adebunmi Gbadebo is a visual artist who creates sculptures, paintings, prints, and paper.','America','Contemporary'),
('Woody de Othello',null,NULL,'Woody De Othello is an American ceramicist and painter.','America','Contemporary'),
('Juan Fernández', '1526-01-01', '1579-03-28', 'Mute spanish painter also known as El Labrador. Characterized by boldness and freedom in design, and by warm colouring.', 'Spain', 'Altar Art'),
('Cornelius Norbertus Gijsbrechts', '1630-01-01', '1683-01-01', null, null, 'Cubism'),
('Juan Gris','1887-03-23' ,'1927-05-11','Incorporated mathematics into his paintings and became known for his different cubism styles.', 'Spain', 'Cubism'),
('Pablo Picasso', '1881-08-05', '1973-04-08', 'One of the most influential artists of the 20th century he is known for co-founding the Cubist movement and the invention of constructed sculpture', 'Spain', 'Cubism'),
('Eugène Berthelon', '1829-09-17', '1916-08-17', null, 'France', 'Landscape'),
('Tournai Facotry', null, null, null, 'Belgium', 'Ceramics'),
('Leonardo Da Vinci', '1452-04-15', '1519-05-02', 'Italian polymath of the High Renaissance.', 'Italy', 'Anatomical');

INSERT INTO COLLECTION 
VALUES 
('The Met Collection: European Sculpture and Decorative Arts','Tudor Art','European sculpture and decorative arts reflect the development of a number of art forms in Western European countries from the early fifteenth century','Danielle Kisluk-Grosheide','1000 5th Ave, New York, NY 10028, United States','2125357710'),
('The Met Collection: Modern and Contemporary Art','Modern Art','The Modern and Contemporary Art department at The Met is devoted to the study, collection and exhibition of art from 1890 to the present.','Ana Matisse Donefer-Hickie','1000 5th Ave, New York, NY 10028, United States','2125357710'),
('The Met Collection: The American Wing','Pottery','American Wing displays the domestic arts of the seventeenth to early nineteenth centuries opened in 1924.','Elyse Nelson','1000 5th Ave, New York, NY 10028, United States','2125357710'),
('The Louvre Collection', 'Paintings', 'The worlds most visitec museum.', 'Elisabeth Borne','Rue de Rivoli 75001 Paris', '3301402050317');

INSERT INTO EXHIBIT 
VALUES 
('The Tudors: Art and Majesty in Renaissance England','2022-10-10','2023-01-08'),
('Hear Me Now: The Black Potters of Old Edgefield, South Carolina','2022-09-09','2023-02-05'),
('Cubism and the Trompe lOeil Tradition', '2022-08-20', '2023-01-22');

INSERT INTO DISPLAYED_AT 
VALUES 
('000000001','The Tudors: Art and Majesty in Renaissance England'),
('000000002','The Tudors: Art and Majesty in Renaissance England'),
('000000003','The Tudors: Art and Majesty in Renaissance England'),
('000000004','The Tudors: Art and Majesty in Renaissance England'),
('000000005','The Tudors: Art and Majesty in Renaissance England'),
('000000006','The Tudors: Art and Majesty in Renaissance England'),
('000000013','Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('000000014','Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('000000015','Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('000000016','Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('000000017','Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('000000018','Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('000000020', 'Cubism and the Trompe lOeil Tradition'),
('000000021', 'Cubism and the Trompe lOeil Tradition'),
('000000022', 'Cubism and the Trompe lOeil Tradition'),
('000000023', 'Cubism and the Trompe lOeil Tradition'),
('000000024', 'Cubism and the Trompe lOeil Tradition'),
('000000025', 'Cubism and the Trompe lOeil Tradition'),
('000000026', 'Cubism and the Trompe lOeil Tradition'),
('000000027', 'Cubism and the Trompe lOeil Tradition');


ALTER TABLE ART_OBJECTS
	ADD CONSTRAINT AFK		FOREIGN KEY (Artist)			REFERENCES ARTIST(Name)			ON DELETE SET NULL		ON UPDATE CASCADE;

ALTER TABLE BORROWED
	ADD CONSTRAINT BCFK		FOREIGN KEY (Collection_Name)	REFERENCES COLLECTION(NAME)		ON DELETE CASCADE		ON UPDATE CASCADE;


DROP ROLE IF EXISTS db_admin@localhost, read_access@localhost, entry_access@localhost;
CREATE ROLE db_admin@localhost, read_access@localhost, entry_access@localhost;
GRANT ALL PRIVILEGES ON ARTMUSEUM.* TO db_admin@localhost;
grant create user on *.* to db_admin@localhost with grant option;
GRANT Select ON ARTMUSEUM.* TO read_access@localhost;
GRANT UPDATE ON ARTMUSEUM.* TO entry_access@localhost;
GRANT ALTER ON ARTMUSEUM.* TO entry_access@localhost;
GRANT DELETE ON ARTMUSEUM.* TO entry_access@localhost;
GRANT SELECT ON ARTMUSEUM.* TO entry_access@localhost;

DROP USER IF EXISTS adm@localhost;
DROP USER IF EXISTS guest@localhost;
DROP USER IF EXISTS enduser@localhost;
DROP USER IF EXISTS entry@localhost;

CREATE USER adm@localhost IDENTIFIED WITH mysql_native_password BY 'Admin_Password';
CREATE USER entry@localhost IDENTIFIED WITH mysql_native_password BY 'Entry_User_Password';
CREATE USER enduser@localhost IDENTIFIED WITH mysql_native_password BY 'End_User_Password';

CREATE USER guest@localhost; 
GRANT db_admin@localhost TO adm@localhost;
GRANT entry_access@localhost TO entry@localhost;
GRANT read_access@localhost TO enduser@localhost;
GRANT read_access@localhost TO guest@localhost;

SET DEFAULT ROLE ALL TO adm@localhost;
SET DEFAULT ROLE ALL TO entry@localhost;
SET DEFAULT ROLE ALL TO enduser@localhost;
SET DEFAULT ROLE ALL TO guest@localhost;
