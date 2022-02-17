import json
from typing import List, Optional

from .utils.misc import get_random_subset
from .utils.gist import get_gist_content
from .utils.rsa_tools import KeyWrapper, rsa_decrypt
from .settings import RANDOM_STUDENTS_DECRYPTION_KEY


def get_random_students(
        lecture: str,
        size: int = -1,
        decryption_key: Optional[str] = RANDOM_STUDENTS_DECRYPTION_KEY
) -> List[str]:
    # Setup decryption function
    decrypt = lambda message: message
    if decryption_key:
        decryption_payload = json.loads(bytes.fromhex(decryption_key).decode("utf-8"))
        private_key_wrapper = KeyWrapper.from_privdict(dictionary=decryption_payload)
        decrypt = lambda message: rsa_decrypt(message=message, privkey=private_key_wrapper)
    # Retrieve content from gist
    content = get_gist_content()
    # List of decrypted students
    students = [
        student["student"]
        for line in content.splitlines()
        for curated_line in [line.strip()]
        for student in [
            json.loads(curated_line if curated_line.startswith("{") else decrypt(curated_line))
        ]
        if student["lecture"].lower() == lecture.lower()
    ]
    # Random subset
    subset = get_random_subset(population=students, size=size) if size > 0 else students
    return subset
