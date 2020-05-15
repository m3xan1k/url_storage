from urllib.parse import urlparse
from typing import List
import json


def clean_data(stored_data: List[list]) -> List[str]:
    flat_stored_data = [link for links in stored_data
                        for link in json.loads(links)]
    domains = [urlparse(url).netloc if urlparse(url).netloc
               else urlparse(url).path
               for url in flat_stored_data]
    cleaned_domains = list(set(domains))
    return cleaned_domains


def valid_params(_from: str, to: str) -> bool:
    valid = True
    if _from is None or to is None:
        print(1)
        valid = False
    elif _from > to:
        print(2)
        valid = False
    elif not all((_from.isnumeric(), to.isnumeric())):
        print(3)
        valid = False
    return valid
