import json
import os

settings = os.getenv('BIGBOSS_SETTINGS', 'settings/bigboss.json')
try:
    with open(settings) as f:
        settings = json.load(f)
except IOError:
    raise IOError('Couldnt find settings file {}'.format(settings))
except ValueError:
    raise ValueError('Unable to parse JSON in settings file {}'.format(settings))


def load_settings():
    minion_settings = os.getenv('MINION_SETTINGS', 'minion.json')
    try:
        with open(minion_settings) as f:
            minion_settings = json.load(f)
    except IOError:
        # Must be new
        minion_settings = {
            'nerve': None,
            'commands': [],
            'sensors': [],
            'actuators': []
        }
    except ValueError:
        raise ValueError('Unable to parse JSON in settings file {}'.format(settings))

    return minion_settings


def save(key, value):
    old_settings = load_settings()
    old_settings[key] = value
    minion_settings = os.getenv('MINION_SETTINGS', 'minion.json')
    # TODO Error handling, although we probably wouldn't have made it this far if problem?
    with open(minion_settings, 'w') as f:
        json.dump(old_settings, f, indent=2)
