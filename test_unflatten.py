from unflatten import unflatten, NestedDict


def test_nested_dict():
    d = NestedDict()
    d['a']['b']['c'] = 2

    assert d == {'a': {'b': {'c': 2}}}

def test_basic():
    assert unflatten({
        'a': 1,
        'data.a': 2,
        'data.data.a': 3
    }) == {
        'a': 1,
        'data': {
            'a': 2,
            'data': {
                'a': 3,
            }
        }
    }