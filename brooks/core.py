import sys
import random

_LOCKED = False  # this seems secure, right?


class LockedError(Exception): pass


def lock():
    global _LOCKED

    _LOCKED = '12345'


def unlock(code):
    global _LOCKED

    if _LOCKED:
        if str(code) == _LOCKED:
            _LOCKED = False
        else:
            raise ValueError('Wrong code')


def _check_lock():
    if _LOCKED:
        raise LockedError("The air shield is up!")


def self_destruct():
    _check_lock()
    print("Thank you for pressing the self destruct button!")
    sys.exit(0)


_TOWNS_GRABBED = []
def land_grab(town='Rock Ridge', sheriff_bart=True):
    _check_lock()

    if sheriff_bart:
        threshold = .01
    else:
        threshold = .5

    success = random.random() < threshold

    _TOWNS_GRABBED.append(town)

    if success:
        print("Go do that voodoo that you do... so well!")
    else:
        print("To tell the truth, I'm getting a bit bored...")

    return success


def towns():
    return tuple(_TOWNS_GRABBED)
