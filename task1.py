import csv
from bs4 import BeautifulSoup
import requests


def scrape_quotes():
  url = "http://quotes.toscrape.com/"
  response = requests.get(url)
  if response.status_code != 200:
    print("Failed to retrieve webpage")
    return

  soup = BeautifulSoup(response.text, "html.parser")
  quotes_data = []

  # Extract quote details
  quote_divs = soup.find_all("div", class_="quote")
  for q in quote_divs:
    text = q.find("span", class_="text").get_text()
    author = q.find("small", class_="author").get_text()
    tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
    quotes_data.append(
        {"Quote": text, "Author": author, "Tags": ", ".join(tags)}
    )

  # Save to CSV file
  filename = "scraped_quotes.csv"
  with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Quote", "Author", "Tags"])
    writer.writeheader()
    writer.writerows(quotes_data)

  print(
      f"Successfully scraped {len(quotes_data)} quotes and saved to"
      f" {filename}"
  )


if __name__ == "__main__":
  scrape_quotes()