import argparse
import asyncio
from collections import Counter

import aiohttp

from urllib.parse import urljoin
from bs4 import BeautifulSoup

import sys
from typing import NamedTuple

class Job(NamedTuple):
    url: str
    depth: int = 1

    def __lt__(self, other):
        if isinstance(other, Job):
            return len(self.url) < len(other.url)

async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        queue = asyncio.PriorityQueue() # Instantiates an asynchronous Priority Queue
        tasks = [
            asyncio.create_task(
                worker(
                    f"Worker-{i + 1}",
                    session,
                    queue,
                    links,
                    args.max_depth,
                )
            )
            for i in range(args.num_workers)
        ]

        await queue.put(Job(args.url)) # Puts the first job in the queue, which kicks off the crawling
        await queue.join() # Causes the main coroutine to wait until the queue has been drained and there are no more jobs to perform

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-d", "--max-depth", type=int, default=2)
    parser.add_argument("-w", "--num-workers", type=int, default=3)
    return parser.parse_args()

def display(links):
    for url, count in links.most_common():
        print(f"{count:>3} {url}")

async def fetch_html(session, url):
    async with session.get(url) as response:
        if response.ok and response.content_type == "text/html":
            return await response.text()

def parse_links(url, html):
    soup = BeautifulSoup(html, features="html.parser")
    for anchor in soup.select("a[href]"):
        href = anchor.get("href").lower()
        if not href.startswith("javascript:"):
            yield urljoin(url,href)

if __name__ == "__main__":
    asyncio.run(main(parse_args()))