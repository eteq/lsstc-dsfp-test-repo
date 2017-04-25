import sys
import random

_LOCKED = False  # this seems secure, right?


class LockedError(Exception): pass


def lock():
    """
    Lock the air shield!
    """
    global _LOCKED

    _LOCKED = '12345'


def unlock(code):
    """
    It should be the same combination as my luggage...

    Parameters
    ----------
    code
        The unlock code to try to use to unlock
    """
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
    """
    The final win of the up side of the Schwartz against Dark Helmet...
    """
    _check_lock()
    print("Thank you for pressing the self destruct button!")
    sys.exit(0)


_TOWNS_GRABBED = []
def land_snatch(town='Rock Ridge', sheriff_bart=True):
    """
    Land snatching!

    Parameters
    ----------
    town : str
        The town we want
    sheriff_bart : bool
        Whether or not Bart is the sheriff_bart

    Returns
    -------
    bool
        Whether or not the snatch was sucessful
    """
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
    """
    Get the towns that have been snatched.

    Returns
    -------
    tuple of strings
        The names of all the towns that have been snatched.
    """
    return tuple(_TOWNS_GRABBED)
