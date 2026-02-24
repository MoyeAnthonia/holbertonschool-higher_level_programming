#!/usr/bin/python3
import requests
import csv
"""Print JSON content"""


def fetch_and_print_posts():
    """Fetch and print posts"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        print(f"Status Code: {r.status_code}")
        raw_data = r.json()
        for details in raw_data:
            print(details)
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """Fetch and save posts"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        raw_data = r.json()
        posts = [
            {
                "id": item.get("id"),
                "title": item.get("title"),
                "body": item.get("body")
            }
            for item in raw_data
        ]

        # Write to CSV
        with open("posts.csv", "w", encoding="utf-8", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in posts:
                writer.writerow(post)

        print("Posts saved to posts.csv successfully!")
    else:
        print("Failed to fetch posts.")