from collections import defaultdict

class NestedDict(defaultdict):
    """defaultdict of defaultdicts. Behold the meta!"""

    def __init__(self):
        defaultdict.__init__(self, NestedDict)

    def to_dict(self):
        return dict(
            (k, v.to_dict() if isinstance(v, NestedDict) else v)
            for k, v, in self.iteritems()
        )


def unflatten(flat):
    nested = NestedDict()

    for k, v in flat.iteritems():
        parts = k.split('.')

        level = nested
        # Climb up to the right level
        for part in parts[:-1]:
            level = level[part]

        level[parts[-1]] = v

    return nested.to_dict()


def is_dict(value):
    return hasattr(value, '__getitem__')


def flatten(nested, _levels=()):
    flat = {}

    for k, v in nested.iteritems():
        levels = _levels + (k,)

        if is_dict(v):
            flat.update(flatten(v, levels))
        else:
            flat['.'.join(levels)] = v

    return flat

