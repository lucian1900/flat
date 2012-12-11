from flat import NestedDict, unflatten, flatten

def test_nested_dict():
    d = NestedDict()
    d['a']['b']['c'] = 2

    assert d == {'a': {'b': {'c': 2}}}

def test_unflatten():
    assert unflatten({
        'a': 1,
        'data.a': 2,
        'data.data.a': 3,
    }) == {
        'a': 1,
        'data': {
            'a': 2,
            'data': {
                'a': 3,
            }
        }
    }


def test_flatten():
    assert flatten({
        'a': 1,
        'data': {
            'a': 2,
            'data': {
                'a': 3,
            }
        }
    }) == {
        'a': 1,
        'data.a': 2,
        'data.data.a': 3,
    }


def test_roundtrip():
    data = {
        'a.b.c': 3,
    }
    assert data == flatten(unflatten(data))


if __name__ == '__main__':
    # The tests are written primarily to be run by py.test, but this lets one
    # run them without it
    for func in [v for k, v in globals().items() if k.startswith('test_')]:
        func()
