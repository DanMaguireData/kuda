import asyncio
from typing import Callable, Dict, List

import aiohttp


async def scrape_page(
    session: aiohttp.ClientSession, url: str, data_parser: Callable
):
    """
    Scrape a single page and return the parsed data.
    Args:
        session: (aiohttp.ClientSession) Session to use for the request.
        url: (str) Url to scrape.
        data_parser: (Callable) Function to parse the data.
    Returns:
        Dict: Parsed data.
    """

    async with session.get(url) as response:
        data = await response.text()
        # We include the url for tracking purposes.
        return data_parser(url, data)


async def scrape_in_batches(
    urls: List[str], batch_size: int, data_parser: Callable
) -> List[Dict]:
    """
    Scrape a list of pages in batches and return the parsed data.
    We create the session outside of the function so that we can
    reuse it for all the requests.
    Args:
        urls: (List[str]) List of urls to scrape.
        batch_size: (int) Number of urls to scrape in each batch.
        data_parser: (Callable) Function to parse the data.
    Returns:
        List[Dict]: List of parsed data.
    """

    async with aiohttp.ClientSession() as session:
        scraped_data = []
        for i in range(0, len(urls), batch_size):
            batch = urls[i : i + batch_size]
            tasks = [
                scrape_page(session=session, url=url, data_parser=data_parser)
                for url in batch
            ]
            batch_data = await asyncio.gather(*tasks)
            scraped_data.extend(batch_data)
        return scraped_data


def scrape_urls(
    urls: List[str], data_parser: Callable, batch_size: int = 1
) -> List[Dict]:
    """
    Scrape a list of urls and return the parsed data.
    Args:
        urls: (List[str]) List of urls to scrape.
        data_parser: (Callable) Function to parse the data.
        batch_size: (int) Number of urls to scrape in each batch.
    Returns:
        List[Dict]: List of parsed data.
    """

    return asyncio.run(
        scrape_in_batches(
            urls=urls,
            batch_size=batch_size,
            data_parser=data_parser,
        )
    )
