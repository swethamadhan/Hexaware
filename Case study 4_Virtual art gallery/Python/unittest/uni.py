import sys
import os

# Add parent directory of 'dao' to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from dao.VirtualArtGalleryImpl import virtualartgallery_impl
from entity.artwork import Artwork
from entity.gallery import Gallery

class TestArtworkManagement(unittest.TestCase):
    def setUp(self):
        # Initialize the service for testing
        self.service = virtualartgallery_impl()

    def test_add_artwork(self):
        # Test the ability to upload a new artwork
        artwork_id = input("Enter Artwork ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        creation_date = input("Enter Creation Date (YYYY-MM-DD): ")
        medium = input("Enter Medium: ")
        image_url = input("Enter Image URL: ")
        
        artwork = Artwork(artwork_id, title, description, creation_date, medium, image_url)
        result = self.service.add_artwork(artwork)
        print("successfully added:", result)
        self.assertTrue(result)

    def test_update_artwork(self):
        # Verify that updating artwork details works correctly
        artwork_id = input("Enter Artwork ID to update: ")
        title = input("Enter Updated Title: ")
        description = input("Enter Updated Description: ")
        creation_date = input("Enter Updated Creation Date (YYYY-MM-DD): ")
        medium = input("Enter Updated Medium: ")
        image_url = input("Enter Updated Image URL: ")
        
        updated_artwork = Artwork(artwork_id, title, description, creation_date, medium, image_url)
        result = self.service.update_artwork(updated_artwork)
        print("successfully updated:", result)
        self.assertTrue(result)

    def test_remove_artwork(self):
        # Test removing an artwork from the gallery
        artwork_id = input("Enter Artwork ID to remove: ")
        result = self.service.remove_artwork(artwork_id)
        print("successfully removed:", result)
        self.assertTrue(result)

    def test_search_artworks(self):
        # Check if searching for artworks returns the expected results
        keyword = input("Enter Keyword to Search: ")
        artworks = self.service.search_artworks(keyword)
        self.assertIsNotNone(artworks)
        # Add additional assertions based on expected results


class TestGalleryManagement(unittest.TestCase):
    def setUp(self):
        # Initialize the service for testing
        self.service = virtualartgallery_impl()


    ## gallery management 

    def test_create_new_gallery(self):
        # Test creating a new gallery
        gallery_id = input("Enter Gallery ID: ")
        name = input("Enter Name: ")
        description = input("Enter Description: ")
        location = input("Enter Location: ")
        curator = input("Enter Curator: ")
        opening_hours = input("Enter Opening Hours: ")
        
        gallery = Gallery(gallery_id, name, description, location, curator, opening_hours)
        result = self.service.create_gallery(gallery)
        self.assertTrue(result)

    def test_update_gallery(self):
        # Verify that updating gallery information works correctly
        gallery_id = input("Enter Gallery ID to update: ")
        name = input("Enter Updated Name: ")
        description = input("Enter Updated Description: ")
        location = input("Enter Updated Location: ")
        curator = input("Enter Updated Curator: ")
        opening_hours = input("Enter Updated Opening Hours: ")
        
        updated_gallery = Gallery(gallery_id, name, description, location, curator, opening_hours)
        result = self.service.update_gallery(updated_gallery)
        self.assertTrue(result)

    def test_remove_gallery(self):
        # Test removing a gallery from the system
        gallery_id = input("Enter Gallery ID to remove: ")
        result = self.service.remove_gallery(gallery_id)
        self.assertTrue(result)

    def test_search_galleries(self):
        # Check if searching for galleries returns the expected results
        keyword = input("Enter Keyword to Search: ")
        galleries = self.service.search_galleries(keyword)
        self.assertIsNotNone(galleries)
        # Add additional assertions based on expected results

if __name__ == '__main__':
    unittest.main()
