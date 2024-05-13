# MACS 30112 FINAL PROJECT
# TIGER PARENTING

# Import Libraries for scraping Parental Forum data
import requests
from bs4 import BeautifulSoup
import random
import time
import csv

# Function to scrape comments from What to Expect Forum 
def scrape_comments(url):
    """
    Scrapes comments from the provided URL.
    Inputs:
        url (str): The URL to scrape comments from.
    Returns:
        list: A list of comments scraped from the URL.
    """
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements containing comments
        comment_elements = soup.find_all('div', 
                                class_='group-discussions__list__item__content')
        # Extract text from comment elements
        comments = [comment.get_text().strip() for comment in comment_elements]
        # Return the list of comments
        return comments
    else:
        # If the request was not successful, print an error message & return None
        print(f"Failed to retrieve data from {url}")
        return None
# Main function to visit random pages and scrape comments
def main():
    """
    Visits a random selection of pages on the What to Expect community forum, 
    scrapes comments from each page, and saves them to a CSV file.
    Inputs:
        None
    Returns:
        None. Saves the scraped comments into a CSV file.
    """
    base_url = "https://community.whattoexpect.com/forums/may-2023-babies.html"
    num_pages_to_scrape = 60
    min_page_number = 1
    max_page_number = 1000
    delay_between_requests = 2

    # Dictionary to store scraped comments
    scraped_comments = {}

    for _ in range(num_pages_to_scrape):
        page_number = random.randint(min_page_number, max_page_number)
        # Construct the URL for the random page
        url = f"{base_url}?page={page_number}"  

        print(f"Scraping comments from: {url}")
        
        comments = scrape_comments(url)
        if comments:
            for comment in comments:
                # Add comments to the dictionary
                scraped_comments[f"Headline {len(scraped_comments)+1}"] = comment
        else:
            print("No comments found on this page.")

        time.sleep(delay_between_requests)

   
    # Save the scraped comments to a CSV file
    csv_file = "final_scraped_comments.csv"

    # Open the CSV file in write mode, specifying error handling
    with open(csv_file, "w", newline="", encoding="utf-8", errors="replace") as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        
        # Write the column headers
        writer.writerow(["Headline", "Comment"])
        
        # Iterate over the scraped_comments dictionary
        for headline, comment in scraped_comments.items():
            # Replace problematic characters 
            #write each headline-comment pair as a row in the CSV file
            writer.writerow([headline, comment])

if __name__ == "__main__":
    main()