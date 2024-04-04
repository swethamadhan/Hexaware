class Artist:
    def __init__(self, artist_id, name, biography, birth_date, nationality, website, contact_information):
        self.artist_id = artist_id
        self.name = name
        self.biography = biography
        self.birth_date = birth_date
        self.nationality = nationality
        self.website = website
        self.contact_information = contact_information

    def get_artist_id(self):
        return self.artist_id

    def set_artist_id(self, artist_id):
        self.artist_id = artist_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_biography(self):
        return self.biography

    def set_biography(self, biography):
        self.biography = biography

    def get_birth_date(self):
        return self.birth_date

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def get_nationality(self):
        return self.nationality

    def set_nationality(self, nationality):
        self.nationality = nationality

    def get_website(self):
        return self.website

    def set_website(self, website):
        self.website = website

    def get_contact_information(self):
        return self.contact_information

    def set_contact_information(self, contact_information):
        self.contact_information = contact_information

    def __str__(self):
        return f"Artist ID: {self.artist_id}\nName: {self.name}\nBiography: {self.biography}\nBirth Date: {self.birth_date}\nNationality: {self.nationality}\nWebsite: {self.website}\nContact Information: {self.contact_information}"

