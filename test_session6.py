import pytest , os , session6 , inspect , re , random
from decimal import Decimal
import math
import cmath


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_funcation_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction )
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def check_docstring():
    q = session6.poker_star.__doc__
    assert q!=None


def test_identation():
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"


def test_docstring():
    q1=session6.poker.__doc__
    assert q1 is not None


def check_annotation():
    q1=session6.pokerstar.__annotations__
    assert q1 == {'no_of_card': 'int',
    'no_of_player': 'int',
    'return': 'winner of the game',
    'sequence_cardsA': 'list',
    'sequence_cardsB': 'list'}


