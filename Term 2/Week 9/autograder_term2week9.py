import numpy.testing as npt
from time import time
import numpy as np
import math
print("Autograder loaded successfully!")
print("Remember to always restart and run all from the Kernel menu before submitting!")
def question1ia(_globals):
    number_of_tests = 2
    score = 0
    score00, score01, score02, score03 = 0,0,0,0
    score10, score11, score12, score13 = 0,0,0,0
    try:
        assert(list(_globals['list1']) == list(range(13,104,2)))
    except:
        print("list1 does not contain the correct data")
    else:
        print("list1 contains the correct data")
        score00 += 1
    try:
        assert(list(_globals['tuple1']) == list(range(13,104,2)))
    except:
        print("tuple1 does not contain the correct data")
    else:
        print("tuple1 contains the correct data")
        score01 += 1
    try:
        assert(set(_globals['set1']) == set(range(13,104,2)))
    except:
        print("set1 does not contain the correct data")
    else:
        print("set1 contains the correct data")
        score02 += 1
    try:
        assert(set(_globals['fs1']) == set(range(13,104,2)))
    except:
        print("fs1 does not contain the correct data")
    else:
        print("fs1 contains the correct data")
        score03 += 1
    score0 = score00 * score01 * score02 * score03
    try:
        assert(isinstance(_globals['list1'],list))
    except:
        print("\nlist1 is not a list")
    else:
        print("\nlist1 is a list")
        score10 += 1
    try:
        assert(isinstance(_globals['tuple1'],tuple))
    except:
        print("tuple1 is not a tuple")
    else:
        print("tuple1 is a tuple")
        score11 += 1
    try:
        assert(isinstance(_globals['set1'],set))
    except:
        print("set1 is not a set")
    else:
        print("set1 is a set")
        score12 += 1
    try:
        assert(isinstance(_globals['fs1'],frozenset))
    except:
        print("fs1 is not a frozenset")
    else:
        print("fs1 is a frozenset")
        score13 += 1
    score1 = score10 * score11 * score12 * score13
    score = score0+score1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ib(_globals):
    number_of_tests = 2
    score = 0
    score00, score01, score10, score11 = 0, 0, 0, 0
    try:
        assert(_globals['list2'] == _globals['list1'])
    except:
        print("list2 does not contain the same elements as list1")
    else:
        print("list2 contains the same elements as list1")
        score00 += 1
    try:
        assert(_globals['list2'] is _globals['list1'])
    except:
        print("list2 is not the same object as list1, which is incorrect")
    else:
        print("list2 is the same object as list1, which is correct")
        score01 += 1
    score += score00*score01
    try:
        assert(_globals['list3'] == _globals['list1'])
    except:
        print("\nlist3 does not contain the same elements as list1")
    else:
        print("\nlist3 contains the same elements as list1")
        score10 += 1
    try:
        assert(not(_globals['list3'] is _globals['list1']))
    except:
        print("list2 is the same object as list1, which is incorrect")
    else:
        print("list3 is not the same object as list1, which is correct")
        score11 += 1
    score += score10*score11
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ic(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['list1'] == [13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105])
    except:
        print("list1 is not correct")
    else:
        print("list1 is correct")
        score += 1
    try:
        assert(_globals['set1'] == {13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105})
    except:
        print("set1 is not correct")
    else:
        print("set1 is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1id():   
    return 3

def question1ie(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['list1'] == [13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 105])
    except:
        print("list1 is not correct")
    else:
        print("list1 is correct")
        score += 1
    try:
        assert(_globals['set1'] == {13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105})
    except:
        print("set1 is not correct")
    else:
        print("set1 is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1if():   
    return 5

def question1ig(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['list1'] == list(range(1005,1310,5)))
    except:
        print("list1 is not correct")
    else:
        print("list1 is correct")
        score += 1
    try:
        assert(_globals['set1'] == set(range(1005,1310,5)))
    except:
        print("set1 is not correct")
    else:
        print("set1 is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1ih():   
    return 2

def question1iia(_globals):
    number_of_tests = 3
    score = 0
    score10, score11, score20, score21 = 0, 0, 0, 0
    try:
        assert(_globals['list_of_lists1'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("list_of_lists1 does not contain the right values")
    else:
        print("list_of_lists1 contains the right values")
        score += 1
    try:
        assert(_globals['list_of_lists2'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("\nlist_of_lists2 does not contain the right values")
    else:
        print("\nlist_of_lists2 contains the right values")
        score10 += 1
    try:
        assert(_globals['list_of_lists2'] is _globals['list_of_lists1'])
    except:
        print("list_of_lists2 is not the same object as list_of_lists1, which is incorrect")
    else:
        print("list_of_lists2 is the same object as list_of_lists1, which is correct")
        score11 += 1
    score += score10*score11
    try:
        assert(_globals['list_of_lists3'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("\nlist_of_lists3 does not contain the right values")
    else:
        print("\nlist_of_lists3 contains the right values")
        score20 += 1
    try:
        assert(not(_globals['list_of_lists3'] is _globals['list_of_lists1']))
    except:
        print("list_of_lists2 is the same object as list_of_lists1, which is incorrect")
    else:
        print("list_of_lists3 is not the same object as list_of_lists1, which is correct")
        score21 += 1
    score += score20*score21
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iib():   
    return 1

def question1iic(_globals):
    number_of_tests = 4
    score = 0
    score10, score11 = 0, 0  
    try:
        assert(_globals['list_of_lists1'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("list_of_lists1 does not contain the right values")
    else:
        print("list_of_lists1 contains the right values")
        score += 1
    try:
        assert(_globals['list_of_lists4'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("\nlist_of_lists4 does not contain the right values")
    else:
        print("\nlist_of_lists4 contains the right values")
        score += 1
    try:
        assert(not(_globals['list_of_lists4'] is _globals['list_of_lists1']))
    except:
        print("\nlist_of_lists4 is the same object as list_of_lists1, which is incorrect")
    else:
        print("\nlist_of_lists4 is not the same object as list_of_lists1, which is correct")
        score += 1
    try:
        assert(
            not(
                (_globals['list_of_lists4'][0] is _globals['list_of_lists1'][0]) or
                (_globals['list_of_lists4'][1] is _globals['list_of_lists1'][1]) or
                (_globals['list_of_lists4'][2] is _globals['list_of_lists1'][2])
            )
        )
    except:
        print("\nlist_of_lists4 is not a deep copy: its rows are not all separate objects from those of list_of_lists1")
    else:
        print("\nlist_of_lists4 is a deep copy: its rows are separate objects from those of list_of_lists1")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iid(_globals):
    number_of_tests = 4
    score = 0
    score10, score11 = 0, 0
    try:
        assert(_globals['list_of_lists1'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("list_of_lists1 does not contain the right values")
    else:
        print("list_of_lists1 contains the right values")
        score += 1
    try:
        assert(_globals['list_of_lists5'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("\nlist_of_lists5 does not contain the right values")
    else:
        print("\nlist_of_lists5 contains the right values")
        score += 1
    try:
        assert(not(_globals['list_of_lists5'] is _globals['list_of_lists1']))
    except:
        print("\nlist_of_lists5 is the same object as list_of_lists1, which is incorrect")
    else:
        print("\nlist_of_lists5 is not the same object as list_of_lists1, which is correct")
        score += 1
    try:
        assert(
            not(
                (_globals['list_of_lists5'][0] is _globals['list_of_lists1'][0]) or
                (_globals['list_of_lists5'][1] is _globals['list_of_lists1'][1]) or
                    (_globals['list_of_lists5'][2] is _globals['list_of_lists1'][2])
            )
        )
    except:
        print("\nlist_of_lists5 is not a deep copy: its rows are not all separate objects from those of list_of_lists1")
    else:
        print("\nlist_of_lists5 is a deep copy: its rows are separate objects from those of list_of_lists1")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2ia(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['radius_list'] == [2400000.0, 6100000.0, 6300000.0, 3400000.0, 69000000.0, 57000000.0, 25000000.0, 25000000.0])
    except:
        print("radius_list is not correct")
    else:
        print("radius_list is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2ib(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['mass_set'] == {6e+24, 5.6e+26, 3.3e+23, 4.9e+24, 1.9e+27, 6.4e+23, 1e+26, 8.7e+25})
    except:
        print("mass_set is not correct")
    else:
        print("mass_set is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2ic(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['name_set'] == {'mars', 'venus', 'saturn', 'uranus', 'mercury', 'neptune', 'jupiter', 'earth'})
    except:
        print("name_set is not correct")
    else:
        print("name_set is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2id(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['ev_dict'] == {'mercury': 4300.0, 'venus': 10000.0, 'earth': 11000.0, 'mars': 5000.0, 'jupiter': 60000.0, 'saturn': 36000.0, 'uranus': 22000.0, 'neptune': 24000.0})
    except:
        print("ev_dict is not correct")
    else:
        print("ev_dict is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2iia(_globals):
    number_of_tests = 4
    score = 0
    try:
        assert(isinstance(_globals['xylene_isomers'],dict))
    except:
        print("xylene_isomers seems not to be a dictionary")
    else:
        print("xylene_isomers is a dictionary")
        score += 1
    try:
        assert(list(_globals['xylene_isomers'].values()) == ['orthoxylene', 'metaxylene', 'paraxylene'])
    except:
        print("\nxylene_isomers does not have the right values")
    else:
        print("\nxylene_isomers has the right values")
        score += 1
    try:
        assert(
            isinstance(list(_globals['xylene_isomers'].keys())[0], tuple) and
            isinstance(list(_globals['xylene_isomers'].keys())[1], tuple) and
            isinstance(list(_globals['xylene_isomers'].keys())[2], tuple)
        )
    except:
        print("\nFor your keys, you don't seem to be using tuples, which we think is the best choice.")
    else:
        print("\nFor your keys, you seem to be using tuples, which we think is the best choice.")
        score += 1
    try:
        assert(
            (list(_globals['xylene_isomers'].keys())[0] == (1, 2)) and
            (list(_globals['xylene_isomers'].keys())[1] == (1, 3)) and
            (list(_globals['xylene_isomers'].keys())[2] == (1, 4))
        )
    except:
        print("\nYour keys don't seem to have the correct values.")
    else:
        print("\nYour keys have the correct values.")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2iib():   
    return {1,2,3,4,6,9}
        
def question2iic():   
    return {1,2,3,4,5,6,7,8,9,10}

def question3(_globals):
    number_of_tests = 4
    score = 0
    try:
        assert(_globals['power_set']({0, 1}) == {frozenset(), frozenset({1}), frozenset({0}), frozenset({0, 1})})
    except:
        print("power_set({0, 1}) does not return the correct value")
    else:
        print("power_set({0, 1}) returns the correct value")
        score += 1
    try:
        assert(_globals['power_set']({'a','b','c','d'}) == {frozenset({'d', 'c'}), frozenset({'b'}), frozenset({'a', 'd', 'b'}), frozenset({'a', 'b'}), frozenset({'d', 'c', 'b'}), frozenset({'d'}), frozenset({'a', 'd', 'c'}), frozenset({'d', 'b'}), frozenset({'a', 'd', 'c', 'b'}), frozenset({'c'}), frozenset(), frozenset({'a', 'c'}), frozenset({'c', 'b'}), frozenset({'a'}), frozenset({'a', 'd'}), frozenset({'a', 'c', 'b'})})
    except:
        print("power_set({'a','b','c','d'}) does not return the correct value")
    else:
        print("power_set({'a','b','c','d'}) returns the correct value")
        score += 1
    try:
        assert(_globals['power_set']({7}) == {frozenset(), frozenset({7})})
    except:
        print("power_set({7}) does not return the correct value")
    else:
        print("power_set({7}) returns the correct value")
        score += 1
    try:
        assert(_globals['power_set']({}) == {frozenset()})
    except:
        print("power_set({}) does not return the correct value")
    else:
        print("power_set({}) returns the correct value")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4a(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['xylene_isomers_string'] == "{(1, 2): 'orthoxylene', (1, 3): 'metaxylene', (1, 4): 'paraxylene'}")
    except:
        print("xylene_isomers_string is not correct")
    else:
        print("xylene_isomers_string is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4c(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['xylene_isomers_string2'] == "{(1, 2): 'orthoxylene', (1, 3): 'metaxylene', (1, 4): 'paraxylene'}")
    except:
        print("xylene_isomers_string2 is not correct")
    else:
        print("xylene_isomers_string2 is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4d(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['xylene_isomers2'] == {(1, 2): 'orthoxylene', (1, 3): 'metaxylene', (1, 4): 'paraxylene'})
    except:
        print("xylene_isomers2 is not correct")
    else:
        print("xylene_isomers2 is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4f(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['xylene_isomers3'] == {(1, 2): 'orthoxylene', (1, 3): 'metaxylene', (1, 4): 'paraxylene'})
    except:
        print("xylene_isomers3 is not correct")
    else:
        print("xylene_isomers3 is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4g(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['new_cos'] == math.cos)
    except:
        print("new_cos is not correct")
    else:
        print("new_cos is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4h(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['new_power_set']({0, 1}) == {frozenset(), frozenset({1}), frozenset({0}), frozenset({0, 1})})
    except:
        print("new_power_set({0, 1}) does not return the correct value")
    else:
        print("new_power_set({0, 1}) returns the correct value")
        score += 1
    try:
        assert(_globals['new_power_set']({'a','b','c','d'}) == {frozenset({'d', 'c'}), frozenset({'b'}), frozenset({'a', 'd', 'b'}), frozenset({'a', 'b'}), frozenset({'d', 'c', 'b'}), frozenset({'d'}), frozenset({'a', 'd', 'c'}), frozenset({'d', 'b'}), frozenset({'a', 'd', 'c', 'b'}), frozenset({'c'}), frozenset(), frozenset({'a', 'c'}), frozenset({'c', 'b'}), frozenset({'a'}), frozenset({'a', 'd'}), frozenset({'a', 'c', 'b'})})
    except:
        print("new_power_set({'a','b','c','d'}) does not return the correct value")
    else:
        print("new_power_set({'a','b','c','d'}) returns the correct value")
        score += 1
    try:
        assert(_globals['new_power_set']({7}) == {frozenset(), frozenset({7})})
    except:
        print("new_power_set({7}) does not return the correct value")
    else:
        print("new_power_set({7}) returns the correct value")
        score += 1
    try:
        assert(_globals['new_power_set']({}) == {frozenset()})
    except:
        print("new_power_set({}) does not return the correct value")
    else:
        print("new_power_set({}) returns the correct value")
        score += 1
    if score == 4:
        print('Test passed!')
        return 1
    else: 
        raise AssertionError('Test failed overall!')
        
def question5ia(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['expr1'].contents == ('power', 3, 'x'))
    except:
        print("expr1 is not correct")
    else:
        print("expr1 is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question5ib(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['expr1subs'].contents == ('power', 3, 6))
    except:
        print("expr1subs is not correct")
    else:
        print("expr1subs is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question5ic(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['val1']== 729)
    except:
        print("val1 is not correct")
    else:
        print("val1 is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question5iia(_globals):
    number_of_tests = 1
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    try:
        assert(_globals['expr1'].contents == (5,))
    except:
        print("expr1 is not correct")
    else:
        print("expr1 is correct")
        score0 += 1
    try:
        assert(_globals['expr2'].contents == (3,))
    except:
        print("expr2 is not correct")
    else:
        print("expr2 is correct")
        score1 += 1
    try:
        assert(_globals['expr3'].contents == ('x',))
    except:
        print("expr3 is not correct")
    else:
        print("expr3 is correct")
        score2 += 1
    try:
        assert(_globals['expr4'].contents == ('y',))
    except:
        print("expr4 is not correct")
    else:
        print("expr4 is correct")
        score3 += 1
    score = score0*score1*score2*score3
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question5iib(_globals):
    number_of_tests = 3
    score = 0
    try:
        assert(_globals['expr5'].prefixForm() == 'power(3, x)')
    except:
        print("expr5 is not correct")
    else:
        print("expr5 is correct")
        score += 1
    try:
        assert(_globals['expr6'].prefixForm() == 'times(5, power(3, x))')
    except:
        print("expr6 is not correct")
    else:
        print("expr6 is correct")
        score += 1
    try:
        assert(_globals['expr7'].prefixForm() == 'subtract(times(5, power(3, x)), y)')
    except:
        print("expr7 is not correct")
    else:
        print("expr7 is correct")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question5iiia(_globals):
    number_of_tests = 4
    score = 0
    try:
        ExpressionTree = _globals['ExpressionTree']
    except:
        print("ExpressionTree doesn't seem to be set up correctly")
    else:
        print("ExpressionTree is set up correctly")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr5 = ExpressionTree('power', expr2, expr3)
        assert(expr5.infixForm() == '(3) ** (x)')
    except:
        print("expr5.infixForm() does not seem to return the correct output")
    else:
        print("expr5.infixForm() returns the correct output")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        assert(expr6.infixForm() == '(5) * ((3) ** (x))')
    except:
        print("expr6.infixForm() does not seem to return the correct output")
    else:
        print("expr6.infixForm() returns the correct output")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr4 = ExpressionTree('y')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        expr7 = ExpressionTree('subtract', expr6, expr4)
        assert(expr7.infixForm() == '((5) * ((3) ** (x))) - (y)')
    except:
        print("expr7.infixForm() does not seem to return the correct output")
    else:
        print("expr7.infixForm() returns the correct output")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question5iiib(_globals):
    number_of_tests = 4
    score = 0
    try:
        ExpressionTree = _globals['ExpressionTree']
    except:
        print("ExpressionTree doesn't seem to be set up correctly")
    else:
        print("ExpressionTree is set up correctly")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr5 = ExpressionTree('power', expr2, expr3)
        assert(expr5.subs('x',6).infixForm() == '(3) ** (6)')
    except:
        print("\nexpr5.subs('x',6).infixForm() does not seem to return the correct output")
    else:
        print("\nexpr5.subs('x',6).infixForm() returns the correct output")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        assert(expr6.subs('x',6).infixForm() == '(5) * ((3) ** (6))')
    except:
        print("\nexpr6.subs('x',6).infixForm() does not seem to return the correct output")
    else:
        print("\nexpr6.subs('x',6).infixForm() returns the correct output")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr4 = ExpressionTree('y')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        expr7 = ExpressionTree('subtract', expr6, expr4)
        assert(expr7.subs('x',6).subs('y',40).infixForm() == '((5) * ((3) ** (6))) - (40)')
    except:
        print("\nexpr7.subs('x',6).subs('y',40).infixForm() does not seem to return the correct output")
    else:
        print("\nexpr7.subs('x',6).subs('y',40).infixForm() returns the correct output")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question5iiib(_globals):
    number_of_tests = 4
    score = 0
    try:
        ExpressionTree = _globals['ExpressionTree']
    except:
        print("ExpressionTree doesn't seem to be set up correctly")
    else:
        print("ExpressionTree is set up correctly")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr5 = ExpressionTree('power', expr2, expr3)
        assert(expr5.subs('x',6).infixForm() == '(3) ** (6)')
    except:
        print("\nexpr5.subs('x',6).infixForm() does not seem to return the correct output")
    else:
        print("\nexpr5.subs('x',6).infixForm() returns the correct output")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        assert(expr6.subs('x',6).infixForm() == '(5) * ((3) ** (6))')
    except:
        print("\nexpr6.subs('x',6).infixForm() does not seem to return the correct output")
    else:
        print("\nexpr6.subs('x',6).infixForm() returns the correct output")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr4 = ExpressionTree('y')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        expr7 = ExpressionTree('subtract', expr6, expr4)
        assert(expr7.subs('x',6).subs('y',40).infixForm() == '((5) * ((3) ** (6))) - (40)')
    except:
        print("\nexpr7.subs('x',6).subs('y',40).infixForm() does not seem to return the correct output")
    else:
        print("\nexpr7.subs('x',6).subs('y',40).infixForm() returns the correct output")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question5iiic(_globals):
    number_of_tests = 4
    score = 0
    try:
        ExpressionTree = _globals['ExpressionTree']
    except:
        print("ExpressionTree doesn't seem to be set up correctly")
    else:
        print("ExpressionTree is set up correctly")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr5 = ExpressionTree('power', expr2, expr3)
        assert(expr5.subs('x',6).evaluate() == 729)
    except:
        print("\nexpr5.subs('x',6).evaluate() does not seem to return the correct output")
    else:
        print("\nexpr5.subs('x',6).evaluate() returns the correct output")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        assert(expr6.subs('x',6).evaluate() == 3645)
    except:
        print("expr6.subs('x',6).evaluate() does not seem to return the correct output")
    else:
        print("expr6.subs('x',6).evaluate() returns the correct output")
        score += 1
    try:
        ExpressionTree = _globals['ExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr4 = ExpressionTree('y')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        expr7 = ExpressionTree('subtract', expr6, expr4)
        assert(expr7.subs('x',6).subs('y',40).evaluate() == 3605)
    except:
        print("expr7.subs('x',6).subs('y',40).evaluate() does not seem to return the correct output")
    else:
        print("expr7.subs('x',6).subs('y',40).evaluate() returns the correct output")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question5iiid(_globals):
    number_of_tests = 3
    score = 0
    try:
        ExpressionTree = _globals['NewExpressionTree']
    except:
        print("NewExpressionTree doesn't seem to be set up correctly")
    else:
        print("NewExpressionTree is set up correctly")
        score += 1
    try:
        ExpressionTree = _globals['NewExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr4 = ExpressionTree('y')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        expr7 = ExpressionTree('subtract', expr6, expr4)
        assert(expr7.subs('x',6).subs('y',40).infixForm() == '((5) * ((3) ** (6))) - (40)')
    except:
        print("\nThe subs and infixForm methods do not seem to be working for this class.")
    else:
        print("\nThe subs and infixForm methods seems to be working for this class.")
        score += 1
    try:
        ExpressionTree = _globals['NewExpressionTree']
        expr1 = ExpressionTree(5)
        expr2 = ExpressionTree(3)
        expr3 = ExpressionTree('x')
        expr5 = ExpressionTree('power', expr2, expr3)
        expr6 = ExpressionTree('times', expr1, expr5)
        expr7 = ExpressionTree('subtract', expr6, expr4)
        assert(expr7.subs('x',6).subs('y',40).evaluate() == 3605)
    except:
        print("\nThe evaluate method does not seem to be working for this class.")
    else:
        print("\nThe evaluate method seems to be working for this class.")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')