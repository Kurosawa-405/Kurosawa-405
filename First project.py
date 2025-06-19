class WebScraper:
    def __init__(self, url):
        self.url = url
        self.page_content = None

    def fetch_page(self):
        """Fetches the page content from the URL."""
        import requests
        try:
            print(f"Fetching page: {self.url}")
            response = requests.get(self.url, timeout=10)  # Set timeout to avoid hanging
            response.raise_for_status()  # Raise an exception for HTTP errors
            self.page_content = response.text
            print("Page fetched successfully!") 
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.ConnectionError:
            print("Connection error. Please check your internet or the URL.")
        except requests.exceptions.Timeout:
            print("The request timed out.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    def parse_html(self):
        """Parses the HTML content."""
        if not self.page_content:
            print("No content to parse. Please fetch the page first.")
            return None
        from bs4 import BeautifulSoup
        try:
            soup = BeautifulSoup(self.page_content, "html.parser")
            print("HTML parsed successfully!")
            return soup
        except Exception as e:
            print(f"Error parsing HTML: {e}")
            return None

    def find_elements(self, tag, attributes=None):
        """Finds elements by tag and optional attributes."""
        soup = self.parse_html()
        if not soup:
            print("Cannot find elements without a valid parsed HTML document.")
            return []
        try:
            elements = soup.find_all(tag, attributes)
            if not elements:
                print(f"No elements found for tag: {tag} with attributes: {attributes}")
            return elements
        except Exception as e:
            print(f"Error finding elements: {e}")
            return []

    def extract_text(self, elements):
        """Extracts and returns text from elements."""
        if not elements:    
            print("No elements provided for text extraction.")
            return []
        try:
            text_data = [element.get_text(strip=True) for element in elements]
            return text_data
        except Exception as e:
            print(f"Error extracting text: {e}")
            return []

    def save_to_file(self, data, file_name):
        """Saves extracted data to a file."""
        if not data:
            print("No data to save.")
            return
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                for line in data:
                    file.write(line + "\n")
            print(f"Data saved to {file_name}")
        except Exception as e:
            print(f"Error saving to file: {e}")


# Example Usage
if __name__ == "__main__":
    url = "https://example.com"
    scraper = WebScraper(url)
    
    # Fetch the page
    scraper.fetch_page()
    
    # Find all <h1> tags
    elements = scraper.find_elements("h1")
    if elements:
        # Extract text content
        text_data = scraper.extract_text(elements)
        print("Extracted Text:", text_data)
        
        # Save to a file
        scraper.save_to_file(text_data, "output.txt")
