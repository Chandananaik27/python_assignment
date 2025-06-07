import re
import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$'
    return re.match(pattern, email) is not None


def fun():
    # Take user input for n
    n = int(input("Enter the number of email addresses: "))

    # Take user input for s
    logging.debug("Enter the email addresses:")
    s = ''
    for _ in range(n):
        s += input().strip() + '\n'

    # Extract email addresses
    emails = s.split('\n')[1:]

    # Filter and sort valid email addresses
    valid_emails = sorted(filter(is_valid_email, emails))

    return valid_emails


    logging.debug("Valid email addresses in lexicographical order:")