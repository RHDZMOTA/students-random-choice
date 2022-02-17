import random
import hashlib
from typing import List, Sequence


def get_random_subset(population: Sequence[str],  size: int) -> List[str]:
    return random.choices(population, k=size)


def get_hash(string: str) -> str:
    return hashlib.sha256(string.encode("utf-8")).hexdigest()
