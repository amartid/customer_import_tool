class JobsDTO:
    def __init__(self, title, shortcode):
        self.title = title
        self.shortcode = shortcode
        
    def __str__(self):
        return f"Title: {self.title}, Shortcode: {self.shortcode}"