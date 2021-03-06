# Instagram-API-python

Unofficial Instagram API library.

Provides access to Instagrams features, including the unpublished
ones, such as uploading photos and video.

### History

* Instagram provides a published API, but it doesn't include many features.

* There's a PHP project [Instagram-API](https://github.com/mgp25/Instagram-API) to reverse-engineer the
interface used by the Instagram App on your phone. It is a useful resource, and a result of careful work.

* There's an initial Python port of that project, [LevPasha/Instagram-API-python](https://github.com/LevPasha/Instagram-API-python). It doesn't have a complete set of "endpoints" (Instagram methods).

* This is a fork of that project. This is an attempt to improve it in
  several areas including:

    * Robustness
      * Errors are handled with exceptions, not return codes.
      * Runtime issues are reported with logging, rather than print statements.
    * Cleanliness
      * Interfaces are simplified.
      * Introduction of iterators to make accessing lists more pythonic.
      * More compliant with coding standards.
      * Examples have been fleshed out, and are easier to run.
    * Some limited extensions to functionality.
      * Support for Two Factor Authentication has been added.

  To achieve these improvements, sacrifices have been made in backwards compatibility. There have been
  several breaking changes to the API. There may be more. However, clients of Lev Pasha's project will find the changes required to
  use this library are minor.
  
### Known Deficiencies

  * It will never be complete:
     * If a change happens to the Instagram API, it may take time for the change to be noticed andbe  included in the PHP project.
     * Then it may take time to be noticed and included in the base project.
     * Then it may take time to be noticed and included into this fork.
    As a result, it will always be behind and not complete.

  * Unit-testing remains deficient.
  
  * Instagram does not approve of the usage of these ported APIs. It may violate the Terms of Use. If they are able to detect that you are using them, they may take steps to silently block some functionality or block your account.


### Installation Instructions

1. Fork/Clone/Download this repo

    `git clone https://github.com/Julian-O/Instagram-API-python.git`


2. Navigate to the directory

    `cd Instagram-API-python`


3. Install the dependencies

    `pip install -r requirements.txt`


4. If you want to run the examples or tests:

  * Create a file in the
   InstagramAPI directory called `credentials.py`, which contains:

   ````
   USERNAME = "your_instagram_user_name"
   PASSWORD = "your_instagram_password"
   ````

  The test account should **not** have two-factor authentication turned on.

  * Run the test script.

    `python test.py`
    
### Usage Instructions

1. Import the `InstagramAPI` package.

2. Optionally, if you want to see information about the requests sent to Instagram, configure the logging module.

2. Create an instance of the `InstagramAPI` class. The constructor takes your Instagram username and password as parameters. (See below if you need Two-Factor authentication.)

3. Call the `login()` method. Your InstagramAPI instance is ready to go.

#### "Endpoints"

You now have a large list of methods you can call on the InstagramAPI instance, that are directly derived from the commands Instagram accepts. (Check out `endpoints.py` for a list of the methods available.) For example, `get_profile_data` will return a dictionary of information about the currently logged in user - including their full name and email address. (See `examples/display_my_user_details.py` to see this in action.)

#### Iterators

Some methods allow you to get a "page" worth of a longer list. Each time you call the method, you provide the starting point from the previous call. To make navigating these easier, the more common methods have be wrapped up in an iterator. (See `instagram_api.py` for a list.) 

For example, `followers_iter()` is an iterator over dictionaries describing each use who follows the logged in user.  See `examples/iterator_examples.py` to see this in action.

To avoid heavily loading the Instagram server (which in turn can lead to your account being throttled or suspended), there is an option with each iterator to slow it down: `delay_between_calls` is the number of seconds to sleep between each call to Instagram.

#### Helper Methods

A few methods can act on any Instagram user, but are typically applied to the current logged in user. Some helper methods in `instagram_api.py` automatically apply to the logged in user, to simplify this common case

For example `get_user_feed()` returns a page of information about itemsabout a specified user's feed, while `self_user_feed()` returns the same information about the *current logged in* user's feed.

#### Two-Factor Authentication

Some Instagram accounts have Two-Factor Authentication (2FA) turned on. For these accounts, a code is sent to the associated phone during the login process, and this is required to complete the login. (Alternatively, preallocated "backup codes" can be used if SMS is not available.)

In order to use 2FA with this API, you will need some mechanism to get the code from the phone. A simple way is to simply ask the user to type it in at the console - but you might need have a GUI, web-server or SMS gateway solution, depending on your application.

If you wish to support 2FA, you need to provide a callback function (`two_factor_callback()`) to the constructor. If the username is associate with an account with 2FA turned on, the provided function will be called with some details about the account name and phone number being called. The function should return the verification string, which will then automatically be used to complete the login call.

For simplicity, most of the example and test code assumes your account does not have 2FA. However, `examples/login.py` contains example code of how to login with 2FA.

