# free-paywall


f-paywall takes advantage of a javascript loophole in Google chrome (also present in other browsers) to make content behind paywall accessible for a period of one hour in a new window. 

The `f`'s a variable.

* `f` stands for **free**: Are you a low-income or young writer tired of running into the paywall to access the wealth of stories (once you've finished the meagre `n` free articles per month limit)? This is a tool that will help you get up-to-date.
* `f` stands for **fair**: Understand your responsiblity in using this tool only for your personal, educational use. Mass media outlets rely increasingly on subscriber support to maintain their independent journalism standards and avoid advertizer enroachment/influence. If you can, like me, please subscribe to at least one or few media outlets of your choice. 

## Current repository:

* fpaywall.py: Navigate around paywall for most media outlet links. Compatible with the latest version of Google chrome; opens a new window with the linked article and keeps it running for an hour.

## Setup:
Install the `selenium` and `webdriver_manager` python libraries:
- `pip install selenium, webdriver_manager`

## Usage:

`python fpaywall.py https://link/to/article`

### Troubleshooting:
Ensure current version of chrome is updated to the latest one and the above python libraries are correctly installed.
