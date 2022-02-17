import json
from typing import List, Optional

from .utils.misc import get_random_subset, get_hash
from .utils.gist import get_gist_content
from .helpers import get_random_students
from .settings import (
    RANDOM_STUDENTS_GIST_URL,
    RANDOM_STUDENTS_GIST_URL_TEMPLATE,
    RANDOM_STUDENTS_GIST_ENDPOINT_PATH,
    RANDOM_STUDENTS_DECRYPTION_KEY
)


class CLI:

    def __init__(self):
        self.gist_url = RANDOM_STUDENTS_GIST_URL
        self.gist_url_temp = RANDOM_STUDENTS_GIST_URL_TEMPLATE
        self.gist_url_endpoint = RANDOM_STUDENTS_GIST_ENDPOINT_PATH

    @staticmethod
    def hash(string: str) -> str:
        return get_hash(string=string)

    @staticmethod
    def hello(name: Optional[str] = None) -> str:
        name = name or "world"
        return f"Hello, {name}!"

    @staticmethod
    def random_subset(size: int, *options: str) -> List[str]:
        return get_random_subset(population=options, size=size)

    @staticmethod
    def gist_content():
        return get_gist_content()

    @staticmethod
    def exec(lecture: str, size: int = -1) -> List[str]:
        return get_random_students(lecture=lecture, size=size, decryption_key=RANDOM_STUDENTS_DECRYPTION_KEY)
