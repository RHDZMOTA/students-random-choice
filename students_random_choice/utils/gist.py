import requests
from typing import Optional

from ..settings import RANDOM_STUDENTS_GIST_URL


def get_gist_content() -> Optional[str]:
    response = requests.get(RANDOM_STUDENTS_GIST_URL)
    if not response.ok:
        return
    return response.text
