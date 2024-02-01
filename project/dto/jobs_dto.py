class JobsDTO:
    def __init__(self, title: str, shortcode: str):
        self.title = title
        self.shortcode = shortcode
        
    def __str__(self) -> str:
        return f"Title: {self.title}, Shortcode: {self.shortcode}"
