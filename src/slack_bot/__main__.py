"""Cli-usage entry-point

"""

import sys
import pprint
from slack_bot.config.utilities import logger
from slack_bot import config


if __name__ == "__main__":
    logger.info('Start of the main slack-bot program.')
    logger.debug(f'Program argument: {pprint.pformat(sys.argv)}')

    if len(sys.argv) > 1 and (sys.argv[1] == 'help' or sys.argv[1] == '-h'):
        print('\n'
              'Slack bot program.\n\n'
              'Usage:\n\n'
              'python -m slack_bot init -> setup tokens.\n\n'
              '\n'
              'All commands can be followed with a `name` argument to '
              'choose between multiple files to sync:\n'
              'python -m slack_bot init [name]\n')
        exit(0)

    if len(sys.argv) > 1 and sys.argv[1] == 'init':
        version = '_'.join(sys.argv[2:])
        config.init(version)
        exit(0)
