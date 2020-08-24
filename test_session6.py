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


def test_annotation():
    q1=session6.pokerstar.__annotations__
    assert q1 == {'no_of_card': 'int',
    'no_of_player': 'int',
    'return': 'winner of the game',
    'sequence_cardsA': 'list',
    'sequence_cardsB': 'list'}


def test_created_cards():
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


def test_number_of_card():
    q1=session6.pokerstar(7,2,['acehearts','queenclubs','6hearts','4spades'],['kinghearts','kingspades','9daimonds','8spades'])
    assert q1=='please enter correct number of card'


def test_number_of_player():
    q1=session6.pokerstar(5,3,['acehearts','queenclubs','6hearts','4spades'],['kinghearts','kingspades','9daimonds','8spades'])
    assert q1=='please enter correct number of players'


def test_winner_in_three_pair_card():
    q1=session6.pokerstar(3,2,['acehearts','queenclubs','6hearts'],['kinghearts','kingspades','9daimonds'])
    assert q1=='Player B is winner'


def test_winner_in_four_pair_card():
    q1=session6.pokerstar(4,2,['acehearts','queenclubs','6hearts','4spades'],['kinghearts','kingspades','9daimonds','8spades'])
    assert q1=='Player B is winner'


def test_winner_in_five_pair_card():
    q1=session6.pokerstar(5,2,['acehearts','queenclubs','6hearts','4spades','2diamonds'],['kinghearts','kingspades','9daimonds','8spades','4hearts'])
    assert q1=='Player B is winner'


def test_lenth_of_created_cards():
    q1=session6.poker(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'],['spades', 'clubs', 'hearts', 'diamonds'])
    assert len(q1)==52


def test_length_of_sequence_players():
    q1=session6.pokerstar(4,2,['acehearts','queenclubs','6hearts','4spades'],['kinghearts','kingspades','9daimonds'])
    assert q1=='please enter the same length for sequence of cards for both players'


def create_cards_using_lambda():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    final = zip((lambda x: x+x+x+x)(cards), (lambda y:y+y+y+y+y+y+y+y+y+y+y+y+y)(suits))
    list(final) is not None


def test_A_winner_in_three_pair_card():
    q1=session6.pokerstar(3,2,['kinghearts','kingspades','9daimonds'],['acehearts','queenclubs','6hearts'])
    assert q1=='Player A is winner'


def test_A_winner_in_five_pair_card():
    q1=session6.pokerstar(5,2,['kinghearts','kingspades','9daimonds','8spades','4hearts'],['acehearts','queenclubs','6hearts','4spades','2diamonds'])
    assert q1=='Player A is winner'


def test_A_winner_in_four_pair_card():
    q1=session6.pokerstar(4,2,['kinghearts','kingspades','9daimonds','8spades'],['acehearts','queenclubs','6hearts','4spades'])
    assert q1=='Player A is winner'






