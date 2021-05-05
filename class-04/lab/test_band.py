import json
import pytest
import yaml

from pythonic_garage_band.band import Band, Musician, Guitarist, Bassist, Drummer


def test_guitarist_str():
    joan = Guitarist("Joan Jett")
    actual = str(joan)
    expected = "My name is Joan Jett and I play guitar"
    assert actual == expected


def test_guitarist_repr():
    joan = Guitarist("Joan Jett")
    actual = repr(joan)
    expected = "Guitarist instance. Name = Joan Jett"
    assert actual == expected


def test_drummer_str():
    sheila = Drummer("Sheila E.")
    actual = str(sheila)
    expected = "My name is Sheila E. and I play drums"
    assert actual == expected


def test_drummer_repr():
    sheila = Drummer("Sheila E.")
    actual = repr(sheila)
    expected = "Drummer instance. Name = Sheila E."
    assert actual == expected


def test_bassist_str():
    meshell = Bassist("Meshell Ndegeocello")
    actual = str(meshell)
    expected = "My name is Meshell Ndegeocello and I play bass"
    assert actual == expected


def test_bassist_repr():
    meshell = Bassist("Meshell Ndegeocello")
    actual = repr(meshell)
    expected = "Bassist instance. Name = Meshell Ndegeocello"
    assert actual == expected


def test_band_name():
    nirvana = Band("Nirvana", [])

    assert nirvana.name == "Nirvana"


def test_guitarist():
    jimi = Guitarist("Jimi Hendrix")
    assert jimi.name == "Jimi Hendrix"
    assert jimi.get_instrument() == "guitar"


def test_bassist():
    flea = Bassist("Flea")
    assert flea.name == "Flea"
    assert flea.get_instrument() == "bass"


def test_drummer():
    ginger = Drummer("Ginger Baker")
    assert ginger.name == "Ginger Baker"
    assert ginger.get_instrument() == "drums"


def test_instruments(one_band):
    instruments = ["guitar", "bass", "drums"]
    for i, member in enumerate(one_band.members):
        # NOTE: see stretch goal where zip used
        assert member.get_instrument() == instruments[i]


def test_individual_solos(one_band):
    for member in one_band.members:
        if member.get_instrument() == "guitar":
            assert member.play_solo() == "face melting guitar solo"
        elif member.get_instrument() == "bass":
            assert member.play_solo() == "bom bom buh bom"
        elif member.get_instrument() == "drums":
            assert member.play_solo() == "rattle boom crash"


def test_band_members(one_band):

    assert len(one_band.members) == 3

    assert isinstance(one_band.members[0], Musician)
    assert isinstance(one_band.members[0], Guitarist)
    assert one_band.members[0].name == "Kurt Cobain"

    assert isinstance(one_band.members[1], Musician)
    assert isinstance(one_band.members[1], Bassist)
    assert one_band.members[1].name == "Krist Novoselic"

    assert isinstance(one_band.members[2], Musician)
    assert isinstance(one_band.members[2], Drummer)
    assert one_band.members[2].name == "Dave Grohl"


def test_play_solos_for_whole_band(one_band):
    solos = one_band.play_solos()
    assert len(solos) == 3
    assert solos[0] == "face melting guitar solo"
    assert solos[1] == "bom bom buh bom"
    assert solos[2] == "rattle boom crash"


def test_to_list():
    assert Band.to_list() == []
    Band("The Nobodies", [])
    assert len(Band.to_list()) == 1


#######################
# Fixtures
#######################


@pytest.fixture
def nirvana_data():
    return {
        "name": "Nirvana",
        "members": [
            {"name": "Kurt Cobain", "instrument": "Guitar"},
            {"name": "Krist Novoselic", "instrument": "Bass"},
            {"name": "Dave Grohl", "instrument": "Drums"},
        ],
    }


@pytest.fixture
def one_band():
    some_band = Band(
        "Nirvana",
        [Guitarist("Kurt Cobain"), Bassist("Krist Novoselic"), Drummer("Dave Grohl"),],
    )
    return some_band


@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    Band.instances = []


#######################
# Stretch
#######################


@pytest.mark.skip("stretch")
def test_from_file():
    with open("assets/bands.json") as f:
        bands = json.loads(f.read())

    assert len(bands) == 1

    nirvana_data = bands[0]

    nirvana = Band(nirvana_data["name"], nirvana_data["members"])

    assert nirvana.name == "Nirvana"


@pytest.mark.skip("stretch")
def test_from_yaml():
    bands = yaml.safe_load(open("assets/bands.yml"))

    assert bands[0]["name"] == "Nirvana"

    assert bands[1]["name"] == "The Pixies"


@pytest.mark.skip("stretch")
def test_abstract_musician():
    with pytest.raises(TypeError):
        unacceptably_vague_musician = Musician()
