import logging
import requests
from requests.exceptions import RequestException

logging.basicConfig(level=logging.INFO)

success_logger = logging.getLogger('success')
success_handler = logging.FileHandler('success_responses.log')
success_handler.setLevel(logging.INFO)
success_logger.addHandler(success_handler)

bad_logger = logging.getLogger('bad')
bad_handler = logging.FileHandler('bad_responses.log')
bad_handler.setLevel(logging.WARNING)
bad_logger.addHandler(bad_handler)

blocked_logger = logging.getLogger('blocked')
blocked_handler = logging.FileHandler('blocked_responses.log')
blocked_handler.setLevel(logging.ERROR)
blocked_logger.addHandler(blocked_handler)

sites = [
    'https://www.youtube.com/',
    'https://wikipedia.org',
    'https://yahoo.com',
    'https://yandex.ru',
    'https://whatsapp.com',
    'https://amazon.com',
    'https://www.ozon.ru',
    'https://instagram.com',
    'https://twitter.com'
]


def check_sites(sites):
    for site in sites:
        try:
            response = requests.get(site)
            if response.status_code == 200:
                success_logger.info(f"'{site}', response - {response.status_code}")
            else:
                bad_logger.warning(f"'{site}', response - {response.status_code}")
        except RequestException:
            blocked_logger.error(f"'{site}', NO CONNECTION")


if __name__ == "__main__":
    check_sites(sites)