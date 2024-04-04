import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entity.artwork import Artwork

# Add parent directory of 'dao' to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.VirtualArtGalleryImpl import virtualartgallery_impl 
from entity import artwork, gallery, artist, user
from exception.exceptions import ArtWorkNotFoundException, UserNotFoundException

class ArtGalleryMenu:
    def __init__(self):
        print("Initializing service...")
        self.service = virtualartgallery_impl()
        print("Service initialized successfully.")
        
    @staticmethod
    def display_menu():
        print("Welcome to the Virtual Art Gallery System")
        print("1. Add Artwork")
        print("2. Update Artwork")
        print("3. Remove Artwork")
        print("4. Search Artworks")
        print("5. Add Artwork to Favorites")
        print("6. Remove Artwork from Favorites")
        print("7. Get User's Favorite Artworks")
        print("8. Exit")
        
    @staticmethod
    def get_artwork_details():
        artwork_id = input("Enter Artwork ID: ")
        artist_id  = input("enter artist ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        creation_date = input("Enter Creation Date: ")
        medium = input("Enter Medium: ")
        image_url = input("Enter Image URL: ")
        return Artwork(artwork_id, artist_id, title, description, creation_date, medium, image_url)
    
    @staticmethod
    def main():
        service = virtualartgallery_impl()
        while True:
            ArtGalleryMenu.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                artwork = ArtGalleryMenu.get_artwork_details()
                print("Adding artwork...")
                service.add_artwork(artwork)
                print("Artwork added successfully.")
            elif choice == '2':
                artwork_id = input("Enter Artwork ID to update: ")
                updated_artwork = ArtGalleryMenu.get_artwork_details()
                print("Updating artwork...")
                service.update_artwork(updated_artwork)
                print("Artwork updated successfully.")
            elif choice == '3':
                artwork_id = input("Enter Artwork ID to remove: ")
                print("Removing artwork...")
                service.remove_artwork(artwork_id)
                print("Artwork removed successfully.")
            elif choice == '4':
                keyword = input("Enter Keyword to Search: ")
                print("Searching artworks...")
                artworks = service.search_artworks(keyword)
                print("Search completed.")
                # Display search results
            elif choice == '5':
                user_id = input("Enter User ID: ")
                artwork_id = input("Enter Artwork ID to add to favorites: ")
                print("Adding artwork to favorites...")
                service.add_artwork_to_favorite(user_id, artwork_id)
                print("Artwork added to favorites successfully.")
            elif choice == '6':
                user_id = input("Enter User ID: ")
                artwork_id = input("Enter Artwork ID to remove from favorites: ")
                print("Removing artwork from favorites...")
                service.remove_artwork_from_favorite(user_id, artwork_id)
                print("Artwork removed from favorites successfully.")
            elif choice == '7':
                user_id = input("Enter User ID: ")
                print("Getting user's favorite artworks...")
                favorite_artworks = service.get_user_favorite_artworks(user_id)
                print("Favorite artworks retrieved successfully.")
                # Display user's favorite artworks
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    ArtGalleryMenu.main()
