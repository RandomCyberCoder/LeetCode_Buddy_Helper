import requests
import sys
import pandas
import re
from graphql.leetcode_problem import questionTitle, singleQuestionTopicTags

def extractSlug(url):
    # Define the regex pattern to capture the problem slug
    PATTERN = r"https://leetcode\.com/problems/([^/?]+)"

    # Search for the problem slug
    match = re.search(PATTERN, url)

    # Extract the problem slug if found
    if match:
        return match.group(1)  #capture problem slug
    else:
        return None

def extract(filePath):
    df = pandas.read_csv(filePath)
    if "url" not in df.columns:
        print("url must be present in the csv file")
        return
    for url in df["url"]:
        slug = extractSlug(url);
        if slug is None:
            print(f"no slug found for url: {url}")
            continue
        print(questionTitle(slug))
        print(singleQuestionTopicTags(slug))
        break


        

def main():
    if len(sys.argv) != 2:
        print("you must provide a file name")
        return
    extract(sys.argv[1])


    # Test URL
    url = "https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150"
    extractSlug(url)
        


if __name__ == "__main__":
    main()