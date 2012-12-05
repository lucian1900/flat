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