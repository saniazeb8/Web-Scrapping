
# MACS 30112 FINAL PROJECT
# TIGER PARENTING

# Import Libraries for scraping Reddit data
import praw #Python Reddit API Wrapper
#Openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
from openpyxl import Workbook 


def reddit_scraper(subreddit_name, flair_text, num_posts=10):
    """
    Scrapes Reddit submissions and comments from a subreddit Parenting 
    based on tags of child age, then saves the data into an Excel file.
    
    Inputs:
        subreddit_name (str): The name of the subreddit to scrape.
        flair_text (str): The flair text to filter submissions.
        keywords (list of str): List of keywords to filter submissions.
        num_posts (int): Number of top posts to scrape (default is 10).
    
    Returns:
        None, saves excel_filename (str): "reddit_discussions.xlsx".
    """

    # Initialize PRAW with your Reddit API credentials
    reddit = praw.Reddit(client_id='ENTER YOUR CLIENT ID HERE',

                         client_secret='ENTER YOUR CLIENT SECRET HERE/API KEY',

                         user_agent='parentingadvice')

    # Get the subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Write headers to the Excel file
    headers = ['Title', 'Tags', 'Headlines', 'Comment']
    ws.append(headers)

    # Get the top 'num_posts' hot submissions from the subreddit
    hot_submissions = subreddit.search(f'flair:"{flair_text}"', sort='hot', 
                                       time_filter='all', limit=num_posts)

    # Iterate through each submission with its index
    for index, submission in enumerate(hot_submissions, start=1):
        # Iterate through each comment in the submission
        submission.comments.replace_more(limit=None)
        comment_data = [submission.title, submission.link_flair_text, submission.selftext]

        print(index,": ",submission.link_flair_text," => ", submission.title)

        for comment in submission.comments.list():
            # Append each comment to the data
            comment_data.append(comment.body)

        # Append the row to the Excel sheet
        ws.append(comment_data)

    # Save the Excel file
    wb.save(excel_filename)

    print(f"Data written to {excel_filename}")


# Example usage
"""
It demonstrates how to employ the reddit_scraper function to gather discussions 
Focuses on "Parenting" subreddit focusing on teenagers aged 13-19 years. 
specifies relevant keywords such as "parenting," "children," and "activities," 
thus function filters submissions to extract valuable insights. 
The flexibility to adjust parameters like the number of posts to scrape, 
We can tailor the scraping process to their specific requirements, 
facilitates in-depth analysis and informed decision-making in parenting discussions.
"""

subreddit_name = 'Parenting'
keywords = ['parenting', 'children', 'time spent', 'homework', 'activities', 'feeling']
num_posts = 300 #increase this number to change the total amount of posts 
# Scrape based on the given flair text
# Repaet the process for different age groups and save the data into different excel files
flair_text='Teenager 13-19 Years'
excel_filename = 'reddit_discussions Teenager 13-19 Years.xlsx'
reddit_scraper(subreddit_name,flair_text, keywords, num_posts)

