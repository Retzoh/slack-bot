"""Functions so that the user may input config elements

"""

from functools import wraps

from slack_bot.config import validate


def with_default(message: str, default_value):
    """Prompt the user, replace empty inputs with default values

    Args:
        message (str): Message to prompt the user with
        default_value (str): Default value to use

    Returns:
        User input if not empty, else the default value
    """
    input_result = input(message + f'\n[{default_value}]: ')
    if input_result == '':
        return default_value
    return input_result


def repeat_ask_until_valid(prompter: callable, validator: callable,
                           *prompt_args):
    """Repeatedly call `prompter` until `validator` validates the output

    If the result is not valid, the validator's indication is shown before
    re-prompting.

    Args:
        prompter (callable): Ask the user for input
        validator (callable): validator for the input given by the user in
            response to `prompter`
        *prompt_args: Arguments to give to the prompter

    Returns:
        Valid user input
    """
    user_input, error_message = validator(prompter(*prompt_args))
    while error_message:
        print(error_message),
        user_input, error_message = validator(prompter(*prompt_args))
    return user_input


def repeat_ask_until_valid_decorator(validator):
    """Turn a regular prompter into a repeat-until-valid one (Decorator)

    Args:
        validator (callable): validator for the input given by the user in
            response to `prompter`

    Returns:
        callable: prompter-until-valid
    """
    def decorator(f):
        @wraps(f)
        def helper(*prompt_args):
            return repeat_ask_until_valid(f, validator, *prompt_args)
        return helper
    return decorator


@repeat_ask_until_valid_decorator(validate.bot_user_token)
def bot_user_token(default):
    """Ask for the Bot User token

    Validity: is not empty and starts with "xoxb-"

    Args:
        default (str): a default token

    Returns:
        the token
    """
    return with_default(
        f'Bot User token (starts with "xoxb-")', default_value=default)


@repeat_ask_until_valid_decorator(validate.app_user_token)
def app_user_token(default):
    """Ask for the App User token

    Validity: is not empty and starts with "xoxp-"

    Args:
        default (str): a default token

    Returns:
        the token
    """
    return with_default(
        f'App User token (starts with "xoxp-")', default)
