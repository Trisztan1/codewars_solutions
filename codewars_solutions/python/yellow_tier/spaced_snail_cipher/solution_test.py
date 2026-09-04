import pytest
from solution import decode, encode

# --- Test Data Sets ---

cipher_orientation = (
    ("HelloWorld", 10, "oWolHrleld"),
    ("HelloWorld", 20, "oWorHlleld"),
    ("HelloWorld", 30, "orldWHeoll"),
    ("HelloWorld", 40, "ollWHeorld"),
    ("HelloWorld", 50, "dlelrHloWo"),
    ("HelloWorld", 60, "dlellHroWo"),
    ("HelloWorld", 70, "lloeHWdlro"),
    ("HelloWorld", 80, "dlroeHWllo"),
    ("Tis a perfect code", 10, "deoa pc Te sirtcef"),
    ("Tis a perfect code", 20, "edp aoeT cris fect"),
    ("Tis a perfect code", 30, "perf Tieea scdoc t"),
    ("Tis a perfect code", 40, "doc tea sc Tieperf"),
    ("Tis a perfect code", 50, "fectris eT cp aoed"),
    ("Tis a perfect code", 60, "tcef sirc Teoa pde"),
    ("Tis a perfect code", 70, "t codcs aeeiT frep"),
    ("Tis a perfect code", 80, "frepeiT cs aet cod"),
    ("immunoelectrophoretically", 10, "reticonoeahuillpmmelortcy"),
    ("immunoelectrophhetically", 20, "citeraeonolliuhlemmpyctro"),
    ("immunoelectrophhetically", 30, "callyielectoimtenumrrohpo"),
    ("immunoelectrophhetically", 40, "rohpoenumrtoimtieleccally"),
    ("immunoelectrophhetically", 50, "yctrolemmplliuhaeonociter"),
    ("immunoelectrophhetically", 60, "ortcypmmelhuillonoearetic"),
    ("immunoelectrophhetically", 70, "ophorrmunetmiotceleiyllac"),
    ("immunoelectrophhetically", 80, "yllacceleitmiotrmuneophor"),
)

cipher_inward = (
    ("Fluffy Bunny", -10, "B yuyfnnfFlu"),
    ("Groovy", -20, "Gryovo"),
    ("absolute leprosy", -30, "l eteysuprolabso"),
    ("I am Groot", -40, "Gro toma I"),
    ("Nothing Beats a Jet2 Holiday!", -50, "htoNi2teJn ya gH!da oli Beats"),
    ("To be, or not to be?", -60, "or n beo, ?teot b oT"),
    ("Hi Hungry! I'm Dad!", -70, "gnuH raD iyd!mH! I'"),
    ("Galvanized Square Steel", -80, "Galuarevqel aSetSn dezi"),
)

cipher_gaps = (
    ("Supercalifragilisticexpialidocious", 10, "sticeircaxsleSlpuipuiiogarfaicodil"),
    ("Supercalifragilisticexpialidocious", 11, "usoiifragclioaSldcuiirepsltaipxeci"),
    ("Supercalifragilisticexpialidocious", 12, "gilistiacrefSxiuplpiacrealisuoicod"),
    ("Supercalifragilisticexpialidocious", 13, "sticexpiailliidgSoaucrpifeoilacrus"),
    (
        "Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long",
        14,
        "opicsilicovcoslocgrancPnoinolmec auosrmnrtluonoieotstiesl evif-ytrof si ",
    ),
    (
        "Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long",
        15,
        "silicovolcanocciopnoicosPsonirescu imimosartluon fortygnol srettel evif-",
    ),
    (
        "Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long",
        16,
        "covolcanoconiosiilsi sicsi pPfonocersutomyro-cnfimartluoive letgnol sret",
    ),
    (
        "Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long",
        17,
        "lcanoconiosis is ofvoorctiyl-ifsPicnvieepu omlcoesntootrcimartluers long",
    ),
    (
        "Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long",
        18,
        "oconiosis is forty-nfaicvleo vloectiPtlneiersuscm iolpnoooncugsorcimartl",
    ),
    (
        "Pneumonoultramicroscopicsilicovolcanoconiosis is forty-five letters long",
        19,
        "iosis is forty-five lneotctoenrasc lloovPnongceiulmiosncoiuplocsorcimart",
    ),
)

cipher_mix = (
    ("aibohphobia", 32, "aibohpaiboh"),
    ("Squirrel in My Pants", -60, "l inent rasMrP yiuqS"),
    ("Diamond Under Pressure", -21, "nder UP erdrenussomaiD"),
    ("Pop Goes the Weasel!", 67, "saeW eht esle!oG poP"),
    ("ILLEGALLY", -19, "YLLAGELLI"),
    ("Spooky Scary Skeleton!", 74, "ry Skeletona!cS ykoopS"),
    (
        "Hey!! This is a Secret Message! You're not Supposed to Read This",
        -82,
        "Hey!! re not SupT'phuoioThisssY e  ddi!aeR ot se gaasseM terceS ",
    ),
    (
        "Yummy Pen Pineapple Apple Pen and Baby Shark dodo dodo dodo",
        45,
        "elppA elppaen iPPe nn eaYummy Pndo dBoadby Shark dodo dodo ",
    ),
)


# --- Encoding Tests ---


@pytest.mark.parametrize("plaintext, key, expected", cipher_orientation)
def test_encode_orientations(plaintext, key, expected):
    assert encode(plaintext, key) == expected


@pytest.mark.parametrize("plaintext, key, expected", cipher_inward)
def test_encode_outside_in(plaintext, key, expected):
    assert encode(plaintext, key) == expected


@pytest.mark.parametrize("plaintext, key, expected", cipher_gaps)
def test_encode_gap_sizes(plaintext, key, expected):
    assert encode(plaintext, key) == expected


@pytest.mark.parametrize("plaintext, key, expected", cipher_mix)
def test_encode_mix(plaintext, key, expected):
    assert encode(plaintext, key) == expected


# --- Decoding Tests ---


@pytest.mark.parametrize("expected, key, cipher", cipher_orientation)
def test_decode_orientations(expected, key, cipher):
    assert decode(cipher, key) == expected


@pytest.mark.parametrize("expected, key, cipher", cipher_inward)
def test_decode_outside_in(expected, key, cipher):
    assert decode(cipher, key) == expected


@pytest.mark.parametrize("expected, key, cipher", cipher_gaps)
def test_decode_gap_sizes(expected, key, cipher):
    assert decode(cipher, key) == expected


@pytest.mark.parametrize("expected, key, cipher", cipher_mix)
def test_decode_mix(expected, key, cipher):
    assert decode(cipher, key) == expected
