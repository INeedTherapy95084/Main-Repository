import feedparser

def google_news_search(query):
    url = f"https://news.google.com/rss/search?q={query}"
    feed = feedparser.parse(url)
    if not feed.entries:
        return "No news found."
    results = []
    for entry in feed.entries[:3]:
        results.append(f"{entry.title} ({entry.link})")
    return "\n".join(results)

print(google_news_search("cybersecurity"))

