thonpython
import logging
import time

class QuoraParser:
    """
    Fake parser that simulates extraction.
    Replace with real scraping logic if needed.
    """

    def parse(self, resolved_query: dict) -> dict:
        logging.info(f"Parsing resolved query: {resolved_query}")

        # Simulated extracted result
        return {
            "query": resolved_query["original"],
            "type": resolved_query["type"],
            "title": f"Sample title for {resolved_query['original']}",
            "url": resolved_query["url"],
            "content": "This is simulated scraped content.",
            "author": "@demo_user",
            "upvotes": 42,
            "comments": 3,
            "followers": 100,
            "metadata": {
                "timestamp": int(time.time() * 1000),
                "language": "en",
                "section": "answers",
            },
        }