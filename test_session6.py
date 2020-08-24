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


def test_identation():
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"


def check_annotation():
    q=session6.poker_star.__annotations__
    assert q=={'no_of_card': 'int',
    'no_of_player': 'int',
    'return': 'winner of the game',
    'sequence_cardsA': 'list',
    'sequence_cardsB': 'list'}


def check_docstrings():
    q=session6.poker_star.__doc__
    assert q!=None


def check_created_cards():
    q=session6.poker(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'],['spades', 'clubs', 'hearts', 'diamonds'])
    q==['2spades',
    '2clubs',
    '2hearts',
    '2diamonds',
    '3spades',
    '3clubs',
    '3hearts',
    '3diamonds',
    '4spades',
    '4clubs',
    '4hearts',
    '4diamonds',
    '5spades',
    '5clubs',
    '5hearts',
    '5diamonds',
    '6spades',
    '6clubs',
    '6hearts',
    '6diamonds',
    '7spades',
    '7clubs',
    '7hearts',
    '7diamonds',
    '8spades',
    '8clubs',
    '8hearts',
    '8diamonds',
    '9spades',
    '9clubs',
    '9hearts',
    '9diamonds',
    '10spades',
    '10clubs',
    '10hearts',
    '10diamonds',
    'jackspades',
    'jackclubs',
    'jackhearts',
    'jackdiamonds',
    'queenspades',
    'queenclubs',
    'queenhearts',
    'queendiamonds',
    'kingspades',
    'kingclubs',
    'kinghearts',
    'kingdiamonds',
    'acespades',
    'aceclubs',
    'acehearts',
    'acediamonds']

