class Gallery:
    def __init__(self, gallery_id, name, description, location, curator, opening_hours):
        self.gallery_id = gallery_id
        self.name = name
        self.description = description
        self.location = location
        self.curator = curator
        self.opening_hours = opening_hours

    def get_gallery_id(self):
        return self.gallery_id

    def set_gallery_id(self, gallery_id):
        self.gallery_id = gallery_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_curator(self):
        return self.curator

    def set_curator(self, curator):
        self.curator = curator

    def get_opening_hours(self):
        return self.opening_hours

    def set_opening_hours(self, opening_hours):
        self.opening_hours = opening_hours

    def __str__(self):
        return f"Gallery ID: {self.gallery_id}\nName: {self.name}\nDescription: {self.description}\nLocation: {self.location}\nCurator: {self.curator}\nOpening Hours: {self.opening_hours}"


