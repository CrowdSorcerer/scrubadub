import re

from .base import RegexDetector
from ..filth import TwitterFilth


class TwitterDetector(RegexDetector):
    """Use regular expression magic to remove email addresses from dirty
    dirty ``text``. This method also catches email addresses like ``john at
    gmail.com``.
    """
    filth_cls = TwitterFilth
    name = 'twitter'

    # https://help.twitter.com/en/managing-your-account/twitter-username-rules#error
    # Twitter user names must be 15 or less charachtors and only contain a-zA-Z0-9_
    # Twitter and admin are not allowed in user names
    # (?<!\w) prevents it matching email addresses
    regex = re.compile((
        r"(?<!\w)@((?!((admin)|(twitter)))[a-z0-9_]){2,15}\b"
    ), re.VERBOSE | re.IGNORECASE)
