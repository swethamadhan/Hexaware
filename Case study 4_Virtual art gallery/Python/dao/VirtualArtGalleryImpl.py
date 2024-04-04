import pyodbc
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.ivirtualartgallery import IVirtualArtGallery
from entity.artwork import Artwork
from exception.exceptions import ArtWorkNotFoundException

class virtualartgallery_impl (IVirtualArtGallery):
    def __init__(self):
        self.connection_string = self.get_connection_string()
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()
        
    def get_connection_string(self):
        # Define the connection string based on your database configuration
        server_name = "DESKTOP-GM6QDGG\\SQLEXPRESS"
        database_name = "Virtual_Art_Gallery"
        trusted_connection = "yes"
        return f"Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};"

    def add_artwork(self, artwork: Artwork) -> bool:
        try:
            self.cursor.execute("INSERT INTO Artwork (Title, ArtistID, Description, CreationDate, Medium, ImageURL) VALUES (?,?, ?, ?, ?, ?)",
                                (artwork.title, artwork.artist_id,artwork.description, artwork.creation_date, artwork.medium, artwork.image_url))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def update_artwork(self, artwork: Artwork) -> bool:
        try:
            self.cursor.execute("UPDATE Artwork SET Title = ?, ArtistID = ? , Description = ?, CreationDate = ?, Medium = ?, ImageURL = ? WHERE ArtworkID = ?",
                                (artwork.title, artwork.artist_id, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artwork_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def remove_artwork(self, artwork_id: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM Artwork WHERE ArtworkID = ?", (artwork_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        try:
            self.cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = ?", (artwork_id,))
            row = self.cursor.fetchone()
            if row:
                return Artwork(row[0], row[1], row[2], row[3], row[4], row[5])
            else:
                raise ArtWorkNotFoundException("Artwork with ID {} not found".format(artwork_id))
        except Exception as e:
            print("Error:", e)

    def search_artworks(self, keyword: str) -> list:
        try:
            self.cursor.execute("SELECT * FROM Artwork WHERE Title LIKE ? OR Description LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
            artworks = []
            for row in self.cursor.fetchall():
                artworks.append(Artwork(row[0], row[1], row[2], row[3], row[4], row[5]))
            return artworks
        except Exception as e:
            print("Error:", e)
            return []

    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            self.cursor.execute("INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (?, ?)", (user_id, artwork_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM User_Favorite_Artwork WHERE UserID = ? AND ArtworkID = ?", (user_id, artwork_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def get_user_favorite_artworks(self, user_id: int) -> list:
        try:
            self.cursor.execute("SELECT ArtworkID FROM User_Favorite_Artwork WHERE UserID = ?", (user_id,))
            favorite_artwork_ids = [row[0] for row in self.cursor.fetchall()]

            favorite_artworks = []
            for artwork_id in favorite_artwork_ids:
                artwork = self.get_artwork_by_id(artwork_id)
                if artwork:
                    favorite_artworks.append(artwork)

            return favorite_artworks
        except Exception as e:
            print("Error:", e)
            return []
        
        ## used for testing gallery 
        
    def create_gallery(self, gallery):
        try:
            # Execute SQL INSERT statement to add the gallery to the database
            self.cursor.execute("INSERT INTO Gallery (Name, Description, Location, Curator, Openinghours) VALUES (?, ?, ?, ?, ?)",
                           gallery.name, gallery.description, gallery.location, gallery.curator, gallery.opening_hours)
            self.connection.commit()
            
            print("Gallery created successfully")
            return True
        
        except Exception as e:
            print(f"Error creating gallery: {e}")
            return[]

    def remove_gallery(self, gallery_id):
        try:
        
            # Execute SQL DELETE statement to remove the gallery from the database
            self.cursor.execute("DELETE FROM Gallery WHERE GalleryID = ?", gallery_id)
            self.connection.commit()

            print("Gallery removed successfully")
            return True
        except Exception as e:
            print(f"Error removing gallery: {e}")
            return []

    def search_galleries(self, keyword):
        try:
        
            # Execute SQL SELECT statement to search for galleries in the database
            self.cursor.execute("SELECT * FROM Gallery WHERE Name LIKE ? OR Description LIKE ?", f'%{keyword}%', f'%{keyword}%')
            galleries = self.cursor.fetchall()
            
            return galleries
        except Exception as e:
            print(f"Error searching galleries: {e}")
            return[]

    def update_gallery(self, updated_gallery):
        try:
            
            # Execute SQL UPDATE statement to update the gallery information in the database
            self.cursor.execute("UPDATE Gallery SET Name = ?, Description = ?, Location = ?, Curator = ?, Openinghours = ? WHERE GalleryID = ?",
                           updated_gallery.name, updated_gallery.description, updated_gallery.location,
                           updated_gallery.curator, updated_gallery.opening_hours, updated_gallery.gallery_id)
            self.connection.commit()
            print("Gallery updated successfully")
            return True
        except Exception as e:
            print(f"Error updating gallery: {e}")
            return[]


    def __del__(self):
        # Close database connection and cursor when the object is destroyed
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'connection'):
            self.connection.close()
        