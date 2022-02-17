import time
import textwrap
import logging

from students_random_choice.helpers import get_random_students
from students_random_choice.utils.misc import get_hash
from students_random_choice.settings import RANDOM_STUDENTS_SECRET_KEY

import streamlit as st


logger = logging.getLogger(__name__)


def random_selector():
    markdown_layout = textwrap.dedent(
        """
        ## Results
        
        {students}
        
        """
    )
    with st.form("random-selector", clear_on_submit=False):
        lecture = st.text_input(label="Lecture Name")
        size = int(st.text_input(label="Sample Size", value="1"))
        passcode = st.text_input(label="Passcode", type="password")
        submitted = st.form_submit_button("Random")
    if not submitted:
        return
    if get_hash(passcode) != RANDOM_STUDENTS_SECRET_KEY:
        return st.warning("Invalid Passcode")
    content = st.empty()
    content.empty()
    bullet = "\n1. "
    with st.spinner("Fetching results..."):
        students = get_random_students(lecture=lecture.strip(), size=size)
        time.sleep(1)
        content.markdown(markdown_layout.format(students=bullet + bullet.join(students)))


def main():
    random_selector()


if __name__ == "__main__":
    main()
