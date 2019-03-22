"""Functions to validate config elements / user inputs

"""

from slack_bot.config.utilities import log_and_exit


def bot_user_token(candidate: str):
    """Check that given bot_user_token candidate is valid

    Check that it :
      - is not blank
      - starts with "xoxb-" (https://api.slack.com/docs/token-types)

    Args:
        candidate (str): the bot_user_token candidate

    Returns:
        if valid:
          candidate, False
        if not:
           candidate, indication
    """
    if candidate == '':
        return candidate, (
            f'The slack Bot User token cannot be blank.')
    if not candidate.startswith("xoxb-"):
        return candidate, (
            f'The slack Bot User token should start with "xoxb-".')
    return candidate, False


def app_user_token(candidate: str):
    """Check that given app_user_token candidate is valid

    Check that it :
      - is not blank
      - starts with "xoxp-" (https://api.slack.com/docs/token-types)

    Args:
        candidate (str): the app_user_token candidate

    Returns:
        if valid:
          candidate, False
        if not:
           candidate, indication
    """
    if candidate == '':
        return candidate, (
            f'The slack App User token cannot be blank.')
    if not candidate.startswith("xoxp-"):
        return candidate, (
            f'The slack App User token should start with "xoxp-".')
    return candidate, False


def config(candidate: dict, context_msg: str= '')->dict:
    """Validate a config candidate

    A valid config should contain:

    * A slack `bot_user_token`
    * A slack `app_user_token`

    Args:
        candidate (dict): the config candidate to validate
        context_msg (str): context message to append before raising errors

    Raises:
        ValueError if a config element is invalid

    Returns:
        the config: dict containing the saved/default values
    """

    _, error_msg = bot_user_token(candidate['bot_user_token'])
    log_and_exit(error_msg + context_msg) if error_msg else ''

    _, error_msg = app_user_token(candidate['app_user_token'])
    log_and_exit(error_msg + context_msg) if error_msg else ''

    return candidate
