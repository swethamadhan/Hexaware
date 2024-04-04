class Artwork:
    def __init__(self, artwork_id, artist_id, title, description, creation_date, medium, image_url):
        self.artwork_id = artwork_id
        self.artist_id = artist_id
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.medium = medium
        self.image_url = image_url

    def get_artwork_id(self):
        return self.artwork_id

    def set_artwork_id(self, artwork_id):
        self.artwork_id = artwork_id
        
    def get_artist_id(self):
        return self.artist_id

    def set_artist_id(self, artist_id):
        self.artist_id = artist_id
        
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_creation_date(self):
        return self.creation_date

    def set_creation_date(self, creation_date):
        self.creation_date = creation_date

    def get_medium(self):
        return self.medium

    def set_medium(self, medium):
        self.medium = medium

    def get_image_url(self):
        return self.image_url

    def set_image_url(self, image_url):
        self.image_url = image_url

    def __str__(self):
        return f"Artwork ID: {self.artwork_id}\nArtist ID: {self.artist_id}Title: {self.title}\nDescription: {self.description}\nCreation Date: {self.creation_date}\nMedium: {self.medium}\nImage URL: {self.image_url}"
