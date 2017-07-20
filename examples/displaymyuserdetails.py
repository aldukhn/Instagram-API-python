import logging

# Dump everything from InstagramAPI, but suppress detail from Requests
logging.basicConfig(level=logging.ERROR)
logging.getLogger("InstagramAPI").setLevel(logging.DEBUG)

from InstagramAPI import InstagramAPI, credentials


def display():
    api = InstagramAPI(credentials.USERNAME, credentials.PASSWORD)
    _, login_data = api.login()
    _, profile_data = api.getProfileData()
    print("You are logged in as %s." % profile_data[u"user"][u"username"])
    print("Your full name is %s." % profile_data[u"user"][u"full_name"])
    print("Your email address is %s." % profile_data[u"user"][u"email"])
    print("Your account %s private." % ("is" if profile_data[u"user"][u"is_private"] else "is not"))
    print("Your 'pk' is %s." % profile_data[u"user"][u"pk"])
    print("All fields available:\n   %s," % ", ".join(profile_data[u"user"].keys()))

if __name__ == "__main__":
    display()