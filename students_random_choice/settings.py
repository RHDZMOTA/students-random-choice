import os
import posixpath

RANDOM_STUDENTS_SECRET_KEY = os.environ.get(
    "RANDOM_STUDENTS_SECRET_KEY",
    default=""
).strip() or None

RANDOM_STUDENTS_DECRYPTION_KEY = os.environ.get(
    "RANDOM_STUDENTS_DECRYPTION_KEY",
    default=""
).strip() or None

# Gist Config

RANDOM_STUDENTS_GIST_ID = os.environ.get(
    "RANDOM_STUDENTS_GIST_ID",
    default=""
).strip() or None

RANDOM_STUDENTS_GIST_FILENAME = os.environ.get(
    "RANDOM_STUDENTS_GIST_FILENAME",
    default="students.csv"
).strip() or None

RANDOM_STUDENTS_GIST_USERNAME = os.environ.get(
    "RANDOM_STUDENTS_GIST_USERNAME",
    default="rhdzmota"
).strip() or None

RANDOM_STUDENTS_GIST_ENDPOINT_PATH = posixpath.join(
    RANDOM_STUDENTS_GIST_USERNAME,
    RANDOM_STUDENTS_GIST_ID,
    "raw",
    RANDOM_STUDENTS_GIST_FILENAME
)
RANDOM_STUDENTS_GIST_URL_TEMPLATE = "https://gist.githubusercontent.com/{endpoint}"
RANDOM_STUDENTS_GIST_URL = RANDOM_STUDENTS_GIST_URL_TEMPLATE.format(
    endpoint=RANDOM_STUDENTS_GIST_ENDPOINT_PATH
)
