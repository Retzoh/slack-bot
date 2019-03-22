"""Manage sync configuration:

Which file to sync, with which google account, with which file on the drive.

See https://github.com/Retzoh/google_services_wrapper for the google-api SSO
integration
"""

import json
import pprint

from slack_bot.config.utilities import logger, sanitize_path, \
    create_folder_if_needed
from slack_bot.config import ask_user
from slack_bot.config.validate import config as validate_config

default_config_path = '~/.slack_bot/'


def get_config_file_path(version):
    return sanitize_path(default_config_path) / version


def _read(version: str= 'default')->dict:
    """Load desired config fom the filesystem

    The config should contain:

    * A slack `bot_user_token`
    * A slack `app_user_token`

    Args:
        version (str): version of the configuration to use

    Returns:
        dict containing the saved/default values
    """
    logger.info('loading config')
    logger.debug(f'version: {version}')
    # Setting default values
    config = dict(
        bot_user_token='',
        app_user_token='')

    # Update them with saved ones
    config_file_path = get_config_file_path(version)
    logger.debug(f'config path: {config_file_path}')
    if config_file_path.exists():
        with config_file_path.open("r") as config_file:
            saved_config = json.load(config_file)
        config.update(saved_config)

    logger.debug(f'Loaded config: {pprint.pformat(config)}')
    return config


def load(version: str='')->tuple:
    """Load, validate and process the config for the specified version

    The processing consists of:

    * Return the config elements, ready to be fed to the other scripts (e.g.
      sync, ...)

    Args:
        version(str): version of the configuration to use

    Returns:
        (bot_user_token: str, app_user_token: str)
    """
    if version == '':
        version = 'default'

    config = validate_config(_read(version), context_msg=(
            f' Please make sure that you have run `python -m slack_bot init`. '
            f'Config version: {version}.'))

    return (config['bot_user_token'],
            config['app_user_token'],)


def _write(config: dict, version: str= 'default')->dict:
    """Save a config

    The config should contain:

    * A slack `bot_user_token`
    * A slack `app_user_token`

    Args:
        config (dict): the config elements to _write
        version (str): version of the configuration to use

    Returns:
        the config, dict containing the saved/default values
    """
    logger.info('saving config')

    logger.debug(f'version: {version}')

    create_folder_if_needed(get_config_file_path(version).parent)
    with get_config_file_path(version).open("w") as config_file:
        json.dump(config, config_file)

    logger.debug(f'Saved config: {pprint.pformat(config)}')
    return config


def init(version: str='')->None:
    """Setup everything to be able to sync a file

    The setup steps are:

    * Ask the user for the config elements
    * Validate the config elements
    * Save the config

    Args:
        version (str): version of the configuration to use
    """

    if version == '':
        version = 'default'
    config = _read(version)

    print('Setting up the configuration for the slack-bot.')
    _ = input('Please make sure that you have:\n'
              '- created your slack app (https://api.slack.com/apps)\n'
              '- activated the `Bot User` feature for your app\n'
              '- access to the `OAuth & Permissions` feature of you app\n'
              '[Ok]')

    config["bot_user_token"] = ask_user.bot_user_token(config['bot_user_token'])

    config["app_user_token"] = ask_user.app_user_token(config['app_user_token'])

    _write(validate.config(config, version), version)
