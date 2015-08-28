# http://www.dalkescientific.com/writings/NBN/parsing_with_ply.html

def assert_raises(exc, f, *args):
    try:
        f(*args)
    except exc:
        pass
    else:
        raise AssertionError("Expected %r" % (exc,))

def test_element_counts():
    assert element_counts("CH3COOH") == {"C": 2, "H": 4, "O": 2}
    assert element_counts("Ne") == {"Ne": 1}
    assert element_counts("") == {}
    assert element_counts("NaCl") == {"Na": 1, "Cl": 1}
    assert_raises(TypeError, element_counts, "Blah")
    assert_raises(TypeError, element_counts, "10")
    assert_raises(TypeError, element_counts, "1C")

def test_atom_count():
    assert atom_count("He") == 1
    assert atom_count("H2") == 2
    assert atom_count("H2SO4") == 7
    assert atom_count("CH3COOH") == 8
    assert atom_count("NaCl") == 2
    assert atom_count("C60H60") == 120
    assert_raises(TypeError, atom_count, "SeZYou")
    assert_raises(TypeError, element_counts, "10")
    assert_raises(TypeError, element_counts, "1C")

def test():
    test_atom_count()
    test_element_counts()

if __name__ == "__main__":
    test()
    print "All tests passed."
