create database Virtual_Art_Gallery;
use Virtual_Art_Gallery;

create table Artist (
ArtistID int primary key identity,
Name varchar(200),
Biography varchar(500),
BirthDate date,
Nationality varchar(100),
Website varchar(500),
ContactInformation varchar(500));

create table Artwork(
ArtworkID int primary key identity,
ArtistID int,
Title varchar(200),
Description varchar(500),
CreationDate date,
Medium varchar(100),
Imageurl varchar(500),
Foreign key(ArtistID) references Artist(ArtistID));

create table User_table(
UserID int primary key identity,
Username varchar(50),
Password varchar(50),
Email varchar(200),
Firstname varchar(100),
Lastname varchar(100),
Dateofbirth date,
Profilepicture varchar(500)
);

create table User_Favorite_Artwork (
UserID int,
ArtworkID int,
foreign key (UserID) references user_table(userid),
foreign key (ArtworkID) references artwork(artworkid)
);

create table Gallery (
GalleryID int primary key identity,
Name varchar(255),
Description text,
Location varchar(255),
Curator int,
Openinghours varchar(255),
foreign key (curator) references artist(artistid));

create table artwork_gallery (
ArtworkID int,
GalleryID int,
foreign key (artworkid) references artwork(artworkid),
foreign key (galleryid) references gallery(galleryid));

SET IDENTITY_INSERT Artist ON;

INSERT INTO Artist (ArtistID, Name, Biography, BirthDate, Nationality, Website, ContactInformation)
VALUES
(1, 'Leonardo da Vinci', 'Italian polymath of the High Renaissance', '1452-04-15', 'Italian', 'https://www.leonardodavinci.net/', 'contact@leonardodavinci.net'),
(2, 'Vincent van Gogh', 'Dutch post-impressionist painter', '1853-03-30', 'Dutch', 'https://www.vangoghgallery.com/', 'contact@vangoghgallery.com'),
(3, 'Pablo Picasso', 'Spanish painter, sculptor, printmaker, ceramicist, and stage designer', '1881-10-25', 'Spanish', 'https://www.picasso.fr/', 'contact@picasso.fr'),
(4, 'Michelangelo Buonarroti', 'Italian sculptor, painter, architect, and poet', '1475-03-06', 'Italian', 'https://www.michelangelo.com/', 'contact@michelangelo.com'),
(5, 'Rembrandt van Rijn', 'Dutch draughtsman, painter, and printmaker', '1606-07-15', 'Dutch', 'https://www.rembrandt.com/', 'contact@rembrandt.com'),
(6, 'Claude Monet', 'French painter and founder of French Impressionist painting', '1840-11-14', 'French', 'https://www.claudemonet.org/', 'contact@claudemonet.org'),
(7, 'Georgia O\Keeffe', 'American artist known for her paintings of enlarged flowers', '1887-11-15', 'American', 'https://www.okeeffemuseum.org/', 'contact@okeeffemuseum.org'),
(8, 'Frida Kahlo', 'Mexican painter known for her self-portraits and works inspired by Mexican culture', '1907-07-06', 'Mexican', 'https://www.fridakahlo.org/', 'contact@fridakahlo.org'),
(9, 'Salvador Dalí', 'Spanish surrealist artist known for his bizarre and striking images', '1904-05-11', 'Spanish', 'https://www.salvadordali.com/', 'contact@salvadordali.com'),
(10, 'Jackson Pollock', 'American painter known for his unique style of drip painting', '1912-01-28', 'American', 'https://www.jacksonpollock.org/', 'contact@jacksonpollock.org'),
(11, 'Andy Warhol', 'American artist, director, and producer who was a leading figure in the visual art movement known as pop art', '1928-08-06', 'American', 'https://www.warhol.org/', 'contact@warhol.org'),
(12, 'Vincent van Gogh', 'Dutch post-impressionist painter', '1853-03-30', 'Dutch', 'https://www.vangoghgallery.com/', 'contact@vangoghgallery.com'),
(13, 'Edvard Munch', 'Norwegian painter, whose best-known work, The Scream, has become one of the most iconic images of world art', '1863-12-12', 'Norwegian', 'https://www.munchmuseum.no/', 'contact@munchmuseum.no'),
(14, 'Paul Cézanne', 'French artist and Post-Impressionist painter whose work laid the foundations of the transition from the 19th-century conception of artistic endeavor to a new and radically different world of art in the 20th century', '1839-01-19', 'French', 'https://www.cezanne.org/', 'contact@cezanne.org'),
(15, 'Henri Matisse', 'French artist, known for both his use of color and his fluid and original draughtsmanship', '1869-12-31', 'French', 'https://www.matisse.com/', 'contact@matisse.com');

SET IDENTITY_INSERT Artist OFF;

SET IDENTITY_INSERT Artwork ON;

INSERT INTO Artwork (ArtworkID, ArtistID, Title, Description, CreationDate, Medium, Imageurl)
VALUES
(1, 1, 'Mona Lisa', 'Famous portrait by Leonardo da Vinci', '1503-01-01', 'Oil on wood panel', 'https://cdn.britannica.com/24/189624-050-F3C5BAA9/Mona-Lisa-oil-wood-panel-Leonardo-da.jpg?w=300'),
(2, 1, 'The Last Supper', 'Iconic mural painting by Leonardo da Vinci', '1495-01-01', 'Fresco', 'https://upload.wikimedia.org/wikipedia/commons/6/69/DaVinci_Last_Supper_high_res.jpg'),
(3, 2, 'The Starry Night', 'Famous painting by Vincent van Gogh depicting the night sky', '1889-06-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1024px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg'),
(4, 2, 'Sunflowers', 'Series of paintings by Vincent van Gogh', '1888-01-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Vincent_Willem_van_Gogh_127.jpg/800px-Vincent_Willem_van_Gogh_127.jpg'),
(5, 3, 'Guernica', 'Iconic anti-war painting by Pablo Picasso', '1937-01-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/en/thumb/7/74/PicassoGuernica.jpg/1024px-PicassoGuernica.jpg'),
(6, 4, 'David', 'Famous sculpture by Michelangelo', '1504-01-01', 'Marble', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Michelangelo%27s_David_2015.jpg/400px-Michelangelo%27s_David_2015.jpg'),
(7, 5, 'The Night Watch', 'Famous painting by Rembrandt van Rijn', '1642-01-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/The_Nightwatch_by_Rembrandt_-_Rijksmuseum.jpg/800px-The_Nightwatch_by_Rembrandt_-_Rijksmuseum.jpg'),
(8, 6, 'Water Lilies', 'Series of paintings by Claude Monet', '1916-01-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Claude_Monet_-_Water_Lilies_1916.jpg/800px-Claude_Monet_-_Water_Lilies_1916.jpg'),
(9, 7, 'Red Canna', 'Painting by Georgia O''Keeffe', '1923-01-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Georgia_O%27Keeffe_-_Red_Canna.jpg/800px-Georgia_O%27Keeffe_-_Red_Canna.jpg'),
(10, 8, 'The Two Fridas', 'Painting by Frida Kahlo', '1939-01-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Las_dos_fridas%2C_por_Frida_Kahlo.jpg/800px-Las_dos_fridas%2C_por_Frida_Kahlo.jpg'),
(11, 9, 'The Persistence of Memory', 'Iconic painting by Salvador Dalí', '1931-01-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/1a/The_Persistence_of_Memory.jpg/1024px-The_Persistence_of_Memory.jpg'),
(12, 10, 'Number 1A', 'Famous painting by Jackson Pollock', '1948-01-01', 'Oil and enamel on canvas', 'https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/No._5%2C_1948.jpg/1024px-No._5%2C_1948.jpg'),
(13, 11, 'Campbell''s Soup Cans', 'Series of paintings by Andy Warhol', '1962-01-01', 'Silkscreen ink on synthetic polymer paint on canvas', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Campbells_Soup_Cans_MOMA.jpg/1024px-Campbells_Soup_Cans_MOMA.jpg'),
(14, 12, 'Starry Night Over the Rhône', 'Painting by Vincent van Gogh', '1888-01-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Van_Gogh_-_Starry_Night_Over_the_Rh%C3%B4ne.jpg/1024px-Van_Gogh_-_Starry_Night_Over_the_Rh%C3%B4ne.jpg'),
(15, 13, 'The Scream', 'Famous expressionist painting by Edvard Munch', '1893-01-01', 'Oil, tempera, and pastel on cardboard', 'https://www.munchmuseum.no/the-scream.jsp');

SET IDENTITY_INSERT Artwork OFF;

SET IDENTITY_INSERT Gallery ON;

INSERT INTO Gallery (GalleryID, Name, Description, Location, Curator, Openinghours)
VALUES
(1, 'Louvre Museum', 'World\s largest art museum and a historic monument in Paris, France', 'Paris, France', 1, '9:00 AM - 6:00 PM'),
(2, 'National Gallery', 'Art museum in London, England', 'London, England', 2, '10:00 AM - 6:00 PM'),
(3, 'Museum of Modern Art', 'Art museum located in New York City', 'New York City, USA', 3, '10:30 AM - 5:30 PM'),
(4, 'The Metropolitan Museum of Art', 'Art museum in New York City', 'New York City, USA', 4, '10:00 AM - 5:00 PM'),
(5, 'Tate Modern', 'Modern art gallery in London', 'London, England', 5, '10:00 AM - 6:00 PM'),
(6, 'Centre Pompidou', 'Multicultural complex in Paris', 'Paris, France', 6, '11:00 AM - 9:00 PM'),
(7, 'Art Institute of Chicago', 'Art museum in Chicago, Illinois', 'Chicago, USA', 7, '10:30 AM - 5:00 PM'),
(8, 'Uffizi Gallery', 'Art museum in Florence, Italy', 'Florence, Italy', 8, '8:15 AM - 6:50 PM'),
(9, 'Museum of Fine Arts', 'Art museum in Boston, Massachusetts', 'Boston, USA', 9, '10:00 AM - 5:00 PM'),
(10, 'State Hermitage Museum', 'Art and culture museum in Saint Petersburg, Russia', 'Saint Petersburg, Russia', 10, '10:30 AM - 6:00 PM'),
(11, 'Rijksmuseum', 'National museum of the Netherlands', 'Amsterdam, Netherlands', 11, '9:00 AM - 5:00 PM'),
(12, 'Victoria and Albert Museum', 'Art and design museum in London', 'London, England', 12, '10:00 AM - 5:45 PM'),
(13, 'Guggenheim Museum', 'Art museum in New York City', 'New York City, USA', 13, '10:00 AM - 5:30 PM'),
(14, 'Prado Museum', 'Art museum in Madrid, Spain', 'Madrid, Spain', 14, '10:00 AM - 8:00 PM'),
(15, 'Musée d\Orsay', 'Art museum in Paris, France', 'Paris, France', 15, '9:30 AM - 6:00 PM');

SET IDENTITY_INSERT Gallery OFF;

SET IDENTITY_INSERT User_table ON;

INSERT INTO User_table (UserID, Username, Password, Email, Firstname, Lastname, Dateofbirth, Profilepicture)
VALUES
(1, 'user1', 'password1', 'user1@example.com', 'John', 'Doe', '1980-01-01', 'https://example.com/profiles/user1.jpg'),
(2, 'user2', 'password2', 'user2@example.com', 'Jane', 'Smith', '1990-05-15', 'https://example.com/profiles/user2.jpg'),
(3, 'user3', 'password3', 'user3@example.com', 'Michael', 'Johnson', '1985-09-20', 'https://example.com/profiles/user3.jpg'),
(4, 'user4', 'password4', 'user4@example.com', 'Emily', 'Brown', '1977-03-12', 'https://example.com/profiles/user4.jpg'),
(5, 'user5', 'password5', 'user5@example.com', 'David', 'Taylor', '1995-07-08', 'https://example.com/profiles/user5.jpg'),
(6, 'user6', 'password6', 'user6@example.com', 'Sarah', 'Anderson', '1988-11-25', 'https://example.com/profiles/user6.jpg'),
(7, 'user7', 'password7', 'user7@example.com', 'Jessica', 'Martinez', '1992-04-30', 'https://example.com/profiles/user7.jpg'),
(8, 'user8', 'password8', 'user8@example.com', 'Christopher', 'Garcia', '1982-06-17', 'https://example.com/profiles/user8.jpg'),
(9, 'user9', 'password9', 'user9@example.com', 'Amanda', 'Wilson', '1979-10-03', 'https://example.com/profiles/user9.jpg'),
(10, 'user10', 'password10', 'user10@example.com', 'Daniel', 'Lopez', '1983-12-22', 'https://example.com/profiles/user10.jpg'),
(11, 'user11', 'password11', 'user11@example.com', 'Ashley', 'Hernandez', '1998-02-14', 'https://example.com/profiles/user11.jpg'),
(12, 'user12', 'password12', 'user12@example.com', 'Matthew', 'Young', '1974-08-05', 'https://example.com/profiles/user12.jpg'),
(13, 'user13', 'password13', 'user13@example.com', 'Emma', 'Scott', '1991-01-18', 'https://example.com/profiles/user13.jpg'),
(14, 'user14', 'password14', 'user14@example.com', 'Justin', 'King', '1987-05-27', 'https://example.com/profiles/user14.jpg'),
(15, 'user15', 'password15', 'user15@example.com', 'Olivia', 'Lewis', '1980-09-10', 'https://example.com/profiles/user15.jpg');

SET IDENTITY_INSERT User_table OFF;

SELECT*FROM Artwork;





