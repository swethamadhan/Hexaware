/*CODING CHALLENGE - 5 Virtual art gallery*/

CREATE DATABASE virtualartgallery;
use virtualartgallery;
-- Create the Artists table
CREATE TABLE Artists (
 ArtistID INT PRIMARY KEY,
 Name VARCHAR(255) NOT NULL,
 Biography TEXT,
 Nationality VARCHAR(100));

-- Create the Categories table
CREATE TABLE Categories (
 CategoryID INT PRIMARY KEY,
 Name VARCHAR(100) NOT NULL);

-- Create the Artworks table
CREATE TABLE Artworks (
 ArtworkID INT PRIMARY KEY,
 Title VARCHAR(255) NOT NULL,
 ArtistID INT,
 CategoryID INT,
 Year INT,
 Description TEXT,
 ImageURL VARCHAR(255),
 FOREIGN KEY (ArtistID) REFERENCES Artists (ArtistID),
 FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID));

-- Create the Exhibitions table
CREATE TABLE Exhibitions (
 ExhibitionID INT PRIMARY KEY,
 Title VARCHAR(255) NOT NULL,
 StartDate DATE,
 EndDate DATE,
 Description TEXT);

-- Create a table to associate artworks with exhibitions
CREATE TABLE ExhibitionArtworks (
 ExhibitionID INT,
 ArtworkID INT,
 PRIMARY KEY (ExhibitionID, ArtworkID),
 FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions (ExhibitionID),
 FOREIGN KEY (ArtworkID) REFERENCES Artworks (ArtworkID));


-- Insert sample data into the Artists table
INSERT INTO Artists (ArtistID, Name, Biography, Nationality) VALUES
(1, 'Pablo Picasso', 'Renowned Spanish painter and sculptor.', 'Spanish'),
(2, 'Vincent van Gogh', 'Dutch post-impressionist painter.', 'Dutch'),
(3, 'Leonardo da Vinci', 'Italian polymath of the Renaissance.', 'Italian'),
(4, 'Claude Monet', 'A French painter and founder of Impressionist painting.', 'French'),
(5, 'Pablo Picasso', 'An American artist known for her large-scale paintings of natural forms.', 'Spanish'),
(6, 'Michelangelo', 'An Italian sculptor, painter, architect, and poet of the High Renaissance.', 'Italian'),
(7, 'Frida Kahlo', 'A Mexican painter known for her self-portraits and works inspired by nature and artifacts of Mexico.', 'Mexican'),
(8, 'Rembrandt', 'A Dutch draughtsman, painter, and printmaker of the Dutch Golden Age.', 'Dutch'),
(9, 'Henri Matisse', 'A French artist, known for his use of color and his fluid and original draughtsmanship.', 'French'),
(10, 'Salvador Dalí', 'A Spanish surrealist painter.', 'Spanish'),
(11, 'Andy Warhol', 'An American artist, director, and producer who was a leading figure in the visual art movement known as pop art.', 'American'),
(12, 'Edvard Munch', 'A Norwegian painter whose best known work, The Scream, has become one of the most iconic images of world art.', 'Norwegian'),
(13, 'Gustav Klimt', 'An Austrian symbolist painter and one of the most prominent members of the Vienna Secession movement.', 'Austrian'),
(14, 'Paul Cézanne', 'A French artist and Post-Impressionist painter whose work laid the foundations of the transition', 'French');

-- Insert sample data into the Categories table
INSERT INTO Categories (CategoryID, Name) VALUES
 (1, 'Painting'),
 (2, 'Sculpture'),
 (3, 'Photography'),
 (4, 'Drawing'),
 (5, 'Printmaking'),
 (6, 'Installation Art'),
 (7, 'Performance Art'),
 (8, 'Ceramics'),
 (9, 'Textile Art'),
 (10, 'Digital Art');


-- Insert sample data into the Artworks table
INSERT INTO Artworks (ArtworkID, Title, ArtistID, CategoryID, Year, Description, ImageURL) VALUES
(1, 'Starry Night', 2, 1, 1889, 'A famous painting by Vincent van Gogh.', 'starry_night.jpg'),
(2, 'Mona Lisa', 3, 1, 1503, 'The iconic portrait by Leonardo da Vinci.', 'mona_lisa.jpg'),
(3, 'Guernica', 1, 1, 1937, 'Pablo Picassos powerful anti-war mural.', 'guernica.jpg'),
(4, 'Horse and Rider', 3, 1, 1500, 'A sculpture depicting the knights', 'horse_rider.jpg'),
(5, 'Red Poppy', 5, 1, 1927, 'A painting by Georgia O''Keeffe representing a close-up view of a red poppy.', 'red_poppy.jpg'),
(6, 'David', 6, 2, 1504, 'A marble sculpture by Michelangelo representing the biblical hero David.', 'david.jpg'),
(7, 'The Two Fridas', 7, 2, 1939, 'A sculpture by Frida Kahlo depicting two versions of herself sitting together.', 'two_fridas.jpg'),
(8, 'The Night Watch', 8, 3, 1642, 'A photograph by Rembrandt depicting a company of civic guardsmen.', 'night_watch.jpg'),
(9, 'The anatomy lesson', 8, 1, 1632, 'A painting depicting Dr. Tulp','anatomy.jpg'),
(10, 'Bust of old man', 8, 2, 1630, 'a sculpture of an old man', 'bust.jpg'),
(11, 'Self potrait of circles', 8, 1, 1634, 'A painting of circles', 'circle.jpg'),
(12, 'Virtuvian man', 3, 1, 1490, 'A male figure', 'man.jpg'),
(13, 'The Scream', 12, 1, 1893, 'A painting by Edvard Munch depicting an anguished figure against a blood-red sky.', 'scream.jpg'),
(14, 'The Kiss', 13, 2, 1907, 'A painting by Gustav Klimt depicting a couple embracing each other.', 'kiss.jpg'),
(15, 'Mont Sainte-Victoire', 14, 1, 1904, 'A series of paintings by Paul Cézanne depicting Mont Sainte-Victoire in southern France.', 'mont_sainte_victoire.jpg'),
(16, 'Campbells Soup Cans', 11, 1, 1962, 'A series of paintings by Andy Warhol depicting Campbells Soup cans.', 'soup_cans.jpg');

-- Insert sample data into the Exhibitions table
INSERT INTO Exhibitions (ExhibitionID, Title, StartDate, EndDate, Description) VALUES
 (1, 'Modern Art Masterpieces', '2023-01-01', '2023-03-01', 'A collection of modern art masterpieces.'),
 (2, 'Renaissance Art', '2023-04-01', '2023-06-01', 'A showcase of Renaissance art treasures.'),
 (3, 'Impressionist Landscapes', '2023-07-01', '2023-09-01', 'Exhibition featuring impressionist landscapes.'),
 (4, 'Surrealist Dreams', '2023-10-01', '2023-12-01', 'Exploring the world of surrealist art.'),
 (5, 'Baroque Brilliance', '2024-01-01', '2024-03-01', 'A celebration of baroque art and architecture.'),
 (6, 'Abstract Expressionism', '2024-04-01', '2024-06-01', 'An exploration of abstract expressionist works.'),
 (7, 'Ancient Civilizations in Art', '2024-07-01', '2024-09-01', 'Artworks inspired by ancient civilizations.'),
 (8, 'Contemporary Photography', '2024-10-01', '2024-12-01', 'A showcase of contemporary photography.'),
 (9, 'Asian Art Treasures', '2025-01-01', '2025-03-01', 'Exhibition featuring treasures from Asian art history.'),
 (10, 'Women in Art', '2025-04-01', '2025-06-01', 'Highlighting the contributions of women artists throughout history.');


-- Insert artworks into exhibitions
INSERT INTO ExhibitionArtworks (ExhibitionID, ArtworkID) VALUES
 (1, 1),
 (1, 2),
 (1, 3),
 (2, 2),
 (3, 4),
 (3, 5),
 (2, 6),
 (1, 6),
 (3, 7),
 (1, 8),
 (2, 7),
 (9, 7);

 select * from Artists
 select * from Artworks
 select * from Categories
 select * from Exhibitions

 /* 1.Retrieve the names of all artists along with the number of 
 artworks they have in the gallery, and list them in descending 
 order of the number of artworks. */

select artists.name as artist_name, count(*) as number
from artists
join artworks on artists.artistid = artworks.artistid
group by name
order by number DESC;

/* 2. List the titles of artworks created by artists from 'Spanish' 
and 'Dutch' nationalities, and order them by the year in ascending order*/

select Title from Artworks
join Artists on Artworks.ArtistID = Artists.ArtistID
where Nationality ='Spanish' OR Nationality = 'Dutch'
order by Year ASC;

/* 3. Find the names of all artists who have artworks in the
'Painting' category, and the number of artworks they have in 
this category.*/

select artists.name as artist_name, count(*) as number
from artists
join artworks on artists.artistid = artworks.artistid
join categories on artworks.categoryid = categories.categoryid
where categories.name = 'Painting'
group by artists.name;

/* 4. List the names of artworks from the 'Modern Art Masterpieces'
exhibition, along with their artists and categories.*/

select a.title as title, artists.name as artist, categories.name as category
from artworks a
join artists on a.artistid = artists.artistid
join categories on a.categoryid = categories.categoryid
join exhibitionartworks ea on a.artworkid = ea.artworkid
join exhibitions e on ea.exhibitionid = e.exhibitionid
where e.title = 'Modern Art Masterpieces';

/* 5. Find the artists who have more than two artworks in the gallery. */

select artists.name as artist
from artists
join artworks on artists.artistid = artworks.artistid
group by artists.name
having count(*) > 2;

/* 6. Find the titles of artworks that were exhibited in both 'Modern Art Masterpieces' 
and 'Renaissance Art' exhibitions */

select a.title
from artworks a
join exhibitionartworks ea on a.artworkid = ea.artworkid
join exhibitions e on ea.exhibitionid = e.exhibitionid
where e.title = 'modern art masterpieces' or e.title = 'renaissance art'
group by a.title
having count(distinct e.title) = 2;

/* 7. Find the total number of artworks in each category */

SELECT Categories.Name AS Category, COUNT(Artworks.ArtworkID) AS TotalArtworks
FROM Categories
LEFT JOIN Artworks ON Categories.CategoryID = Artworks.CategoryID
GROUP BY Categories.Name;

/* 8. List artists who have more than 3 artworks in the gallery. */

select a.name as artist_name
from artists a
join artworks aw on a.artistid = aw.artistid
group by a.name
having count(*) > 3;

/* 9. Find the artworks created by artists from a specific nationality (e.g., Spanish).*/

SELECT Artworks.Title, Artists.Name AS Artist, Artists.Nationality
FROM Artworks
JOIN Artists ON Artworks.ArtistID = Artists.ArtistID
WHERE Artists.Nationality = 'Spanish';

/* 10. List exhibitions that feature artwork by both Vincent van Gogh and Leonardo da Vinci.*/

select e.title
from exhibitions e
join exhibitionartworks ea on e.exhibitionid = ea.exhibitionid
join artworks art on ea.artworkid = art.artworkid
join artists a on art.artistid = a.artistid
where a.name = 'vincent van gogh' or a.name = 'leonardo da vinci'
group by e.title
having count(distinct a.name) = 2;

/* 11. Find all the artworks that have not been included in any exhibition.*/

select title
from artworks
where artworkid not in (select artworkid from exhibitionartworks);

/* 12. List artists who have created artworks in all available categories.*/

select name as artist_name
from artists
where artistid in (
select artistid from artworks
group by artistid
having count(distinct categoryid) = (select count(*) from categories));

/* 13. List the total number of artworks in each category.*/

select c.name as category_name, count(*) as total_artworks
from categories c
join artworks a on c.categoryid = a.categoryid
group by c.name;

/* 14. Find the artists who have more than 2 artworks in the gallery.*/

select name as artist_name
from artists
where artistid in (
select artistid from artworks
group by artistid
having count(*) > 2);

/* 15. List the categories with the average year of artworks they contain, only for categories with more
than 1 artwork.*/

select c.name as category_name, avg(a.year) as average_year
from categories c
join artworks a on c.categoryid = a.categoryid
group by c.name
having count(*) > 1;

/* 16. Find the artworks that were exhibited in the 'Modern Art Masterpieces' exhibition. */

select a.title
from artworks a
join exhibitionartworks ea on a.artworkid = ea.artworkid
join exhibitions e on ea.exhibitionid = e.exhibitionid
where e.title = 'modern art masterpieces';

/* 17. Find the categories where the average year of artworks is greater than the average year of all 
artworks.*/

select c.name as category_name
from categories c
join artworks a on c.categoryid = a.categoryid
group by c.name
having avg(a.year) > (select avg(year) from artworks);

/* 18. List the artworks that were not exhibited in any exhibition.*/

select title from artworks
where artworkid not in (select artworkid from exhibitionartworks);

/* 19. Show artists who have artworks in the same category as "Mona Lisa."*/
select distinct a.name as artist_name
from artists a
join artworks art on a.artistid = art.artistid
join categories c on art.categoryid = c.categoryid
where c.name = (select c.name from categories c join artworks art on c.categoryid = art.categoryid where art.title = 'mona lisa');

/* 20. List the names of artists and the number of artworks they have in the gallery*/
select a.name as artist_name, count(*) as num_artworks
from artists 
join artworks art on a.artistid = art.artistid
group by a.name;


