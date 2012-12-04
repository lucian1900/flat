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
        for part in parts[:-1]:
            level = level[part]

        level[parts[-1]] = v

    return nested.to_dict()