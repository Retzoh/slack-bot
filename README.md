Slack bot
=========

This repository contains a python pip package providing tools to
create a slack-bot app.

It includes a command-line tool and the necessary functions for
in-script use.

### Usage

###### From a terminal:

> `python -m slack_bot -h` -- display the command line interface man
page

> `python -m slack_bot init` -- setup the bot

You will be asked for:

- A slack Bot User token
- A slack App User token

###### From python:

> `import slack_bot`.

### Installation

- Stet up a slack app with a Bot user and get its tokens.
  - Optional: from the slack app, click on `Customize Slack` in your
  team drop-down-menu (top left of the screen on the PC app). This
  will sign you up in your browser.
  - Go to [Your Apps](https://api.slack.com/apps).
  - Sign in if needed.
  - Create or select your app.
  - Make sure the `Bot User` feature is activated.
  - Head to the `OAuth & Permissions` feature page. It lists the token
  of you app.
- Install this package
  - Clone [this repository](https://github.com/Retzoh/slack-bot.git)
  - Install the dependencies
    - I recommend using
    [anaconda](https://www.anaconda.com/distribution/#download-section)
    (python 3.7)
    - run `conda env update -n base` from the repository folder
  - Install the package by running `pip install .` from the repository
  folder

#### git.sh.ht repository

[https://git.sr.ht/~retzoh/slack-bot](https://git.sr.ht/~retzoh/slack-bot)

#### github repository

[https://github.com/Retzoh/slack-bot.git](https://github.com/Retzoh/slack-bot.git)

#### Contacts

comptes.hb@gmail.com
