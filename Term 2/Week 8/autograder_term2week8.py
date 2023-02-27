import numpy.testing as npt
from time import time
import numpy as np
print("Autograder loaded successfully!")
print("Remember to always restart and run all from the Kernel menu before submitting!")
def fn1(data, already_sorted):
    global cc
    next_item = data[already_sorted]
    insertion_index = already_sorted-1
    cc += 1
    while next_item < data[insertion_index] and insertion_index > -1:
        cc += 1
        insertion_index -= 1    
    if insertion_index == -1:
        cc -= 1
    data[insertion_index+2:already_sorted+1] = \
    data[insertion_index+1:already_sorted]
    data[insertion_index+1] = next_item
def fn2(data):
    for already_sorted in range(1,len(data)):
        fn1(data, already_sorted)
def fn3(left_buffer, right_buffer, data):
    global cc
    left_index = right_index = main_index = 0
    while left_index < len(left_buffer) and right_index < len(right_buffer):
        cc += 1
        if left_buffer[left_index] < right_buffer[right_index]:
            data[main_index] = left_buffer[left_index]
            left_index += 1
        else:
            data[main_index] = right_buffer[right_index]
            right_index += 1
        main_index += 1
    if left_index < len(left_buffer):
        data[main_index:] = left_buffer[left_index:]
    else:
        data[main_index:] = right_buffer[right_index:]
def fn4(data):
    ndata = len(data)
    if ndata > 1:
        half_length = ndata//2
        left_half = data[0:half_length]
        right_half = data[half_length:ndata]
        fn4(left_half)
        fn4(right_half)
        fn3(left_half,right_half,data)
def question1ia(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == _globals['masterList'])
    except:
        print("data does not consist of the correct list")
    else:
        print("data consists of the correct list")
        score += 1
    try:
        assert(not (_globals['data'] is _globals['masterList']))
    except:
        print("data seems to be the same object as masterList; did you use the copy function?")
    else:
        print("data is a separate object from masterList, which is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ib(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ic(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    try:
        assert(_globals['comparison_count'] == 120)
    except:
        print("comparison_count is not correct")
    else:
        print("comparison_count is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1id():   
    return 1

def question1ie(_globals):
    number_of_tests = 2
    score = 0
    score00, score01 = 0, 0
    score10, score11 = 0, 0
    try:
        assert([_globals['bubble_sort_simple_max'](n) for n in range(1,21)] == [n*(n-1)//2 for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_simple_max seems not to return the correct numbers")
    else:
        print("The lambda-expression bubble_sort_simple_max seems to return the correct numbers")
        score00 += 1
    try:
        assert([isinstance(_globals['bubble_sort_simple_max'](n), int) for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_simple_max seems not to return ints")
    else:
        print("The lambda-expression bubble_sort_simple_max seems to return ints")
        score01 += 1
    score += score00*score01
    try:
        assert([_globals['bubble_sort_simple_min'](n) for n in range(1,21)] == [n*(n-1)//2 for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_simple_min seems not to return the correct numbers")
    else:
        print("The lambda-expression bubble_sort_simple_min seems to return the correct numbers")
        score10 += 1
    try:
        assert([isinstance(_globals['bubble_sort_simple_min'](n), int) for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_simple_min seems not to return ints")
    else:
        print("The lambda-expression bubble_sort_simple_min seems to return ints")
        score11 += 1
    score += score10*score11
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1if():   
    return 1

def question1iia(_globals):
    number_of_tests = 3
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['bubble_sort_enhanced'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("bubble_sort_enhanced does not seem to sort lists correctly")
    else:
        print("bubble_sort_enhanced seems to sort lists correctly")
        score += 1
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['bubble_sort_enhanced'](test_data)
        assert(_globals['comparison_count'] < 190)
    except:
        print("Your function seems to be requiring too many comparisons; is the tracking of orderedness working?")
    else:
        if _globals['comparison_count'] == 187:
            print("Your function requires exactly the same number of comparisons as ours")
        elif _globals['comparison_count'] > 187:
            print("Your function seems to require slightly more comparisons than ours; can it be further improved?")
        else:
            print("Your function seems to require fewer comparisons than ours; very well done if so! It's worth double-checking that you're counting them all, though.")
        score += 1
    try:
        assert(len(_globals['bubble_sort_enhanced'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iib(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    try:
        assert(_globals['comparison_count'] <= 120)
    except:
        print("Your function seems to be requiring too many comparisons; is the tracking of orderedness working?")
    else:
        if _globals['comparison_count'] == 120:
            print("Your function requires exactly the same number of comparisons as ours")
        else:
            print("Your function seems to require fewer comparisons than ours; very well done if so! It's worth double-checking that you're counting them all, though.")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iic():   
    return 3

def question1iid(_globals):
    number_of_tests = 2
    score = 0
    score00, score01 = 0, 0
    score10, score11 = 0, 0
    try:
        assert([_globals['bubble_sort_enhanced_max'](n) for n in range(1,21)] == [n*(n-1)//2 for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_enhanced_max seems not to return the correct numbers")
    else:
        print("The lambda-expression bubble_sort_enhanced_max seems to return the correct numbers")
        score00 += 1
    try:
        assert([isinstance(_globals['bubble_sort_enhanced_max'](n), int) for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_enhanced_max seems not to return ints")
    else:
        print("The lambda-expression bubble_sort_enhanced_max seems to return ints")
        score01 += 1
    score += score00*score01
    try:
        assert([_globals['bubble_sort_enhanced_min'](n) for n in range(1,21)] == [n-1 for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_enhanced_min seems not to return the correct numbers")
    else:
        print("The lambda-expression bubble_sort_enhanced_min seems to return the correct numbers")
        score10 += 1
    try:
        assert([isinstance(_globals['bubble_sort_enhanced_min'](n), int) for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_enhanced_min seems not to return ints")
    else:
        print("The lambda-expression bubble_sort_enhanced_min seems to return ints")
        score11 += 1
    score += score10*score11
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1iie():   
    return 2
        
def question2a(_globals):
    number_of_tests = 2
    score = 0
    try:
        test_data = [5, 12, 13, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['insertion_pass'](test_data, 3)
        assert(test_data == [5, 8, 12, 13, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18])
    except:
        print("insertion_pass does not seem to be working correctly")
    else:
        print("insertion_pass seems be working correctly")
        score += 1
    try:
        assert(len(_globals['insertion_pass'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2b(_globals):
    number_of_tests = 2
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['insertion_sort'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("insertion_sort does not seem to sort lists correctly")
    else:
        print("insertion_sort seems to sort lists correctly")
        score += 1
    try:
        assert(len(_globals['insertion_sort'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2c(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2d():   
    return 120

def question2e(_globals):
    number_of_tests = 1
    score = 0
    global cc
    try:
        cc = 0
        data = _globals['insertion_sort_length16_worstcase']
        fn2(data)
        assert(cc == 120)
    except:
        print("We think this is incorrect, and that it doesn't require the maximum number of comparisons; can you check again?")
    else:
        print("We agree: this seems to be a good 'worst case'")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
    
def question2f():   
    return 15

def question2g(_globals):
    number_of_tests = 1
    score = 0
    global cc
    try:
        cc = 0
        data = _globals['insertion_sort_length16_bestcase']
        fn2(data)
        print(cc)
        assert(cc == 15)
    except:
        print("We think this is incorrect, and that it requires more than the minimum number of comparisons; can you check again?")
    else:
        print("We agree: this seems to be a good 'best case'")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2hfunc(_globals):
    number_of_tests = 3
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['insertion_sort'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("insertion_sort does not seem to sort lists correctly")
    else:
        print("insertion_sort seems to sort lists correctly")
        score += 1
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['insertion_sort'](test_data)
        assert(_globals['comparison_count'] < 190)
    except:
        print("Your function seems to be requiring too many comparisons")
    else:
        if _globals['comparison_count'] == 118:
            print("Your function requires exactly the same number of comparisons as ours")
        elif _globals['comparison_count'] > 118:
            print("Your function seems to require slightly more comparisons than ours; can it be further improved?")
        else:
            print("Your function seems to require fewer comparisons than ours; very well done if so! It's worth double-checking that you're counting them all, though.")
        score += 1
    try:
        assert(len(_globals['insertion_sort'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2htest(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    try:
        assert(_globals['comparison_count'] < 120)
    except:
        print("Your function seems to be requiring too many comparisons")
    else:
        if _globals['comparison_count'] == 83:
            print("Your function requires exactly the same number of comparisons as ours")
        elif globals['comparison_count'] > 83:
            print("Your function seems to require slightly more comparisons than ours; can it be further improved?")
        else:
            print("Your function seems to require fewer comparisons than ours; very well done if so! It's worth double-checking that you're counting them all, though.")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2j():   
    return 4

def question3ia(_globals):
    number_of_tests = 2
    score = 0
    try:
        left_buffer = [2,5,9,12]
        right_buffer = [1,4,7,8]
        data = [0,0,0,0,0,0,0,0]
        _globals['merge'](left_buffer,right_buffer,data)
        assert(data == [1,2,4,5,7,8,9,12])
    except:
        print("merge does not seem to be working correctly")
    else:
        print("merge seems to be working correctly")
        score += 1
    try:
        assert(len(_globals['merge'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3ib():   
    return 8

def question3ic():   
    return 15

def question3iia(_globals):
    number_of_tests = 2
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['merge_sort'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("merge_sort does not seem to sort lists correctly")
    else:
        print("merge_sort seems to sort lists correctly")
        score += 1
    try:
        assert(len(_globals['merge_sort'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3iib():   
    return 32

def question3iic():   
    return 49

def question3iid(_globals):
    number_of_tests = 1
    score = 0
    score0, score1 = 0, 0
    try:
        assert([_globals['merge_sort_min'](m) for m in range(1,5)] == [m*2**(m-1) for m in range(1,5)])
    except:
        print("The lambda-expression merge_sort_min seems not to return the correct numbers")
    else:
        print("The lambda-expression merge_sort_min seems to return the correct numbers")
        score0 += 1
    try:
        assert([isinstance(_globals['merge_sort_min'](m), int) for m in range(1,5)])
    except:
        print("The lambda-expression merge_sort_min seems not to return ints")
    else:
        print("The lambda-expression merge_sort_min seems to return ints")
        score1 += 1
    score += score0*score1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3iie(_globals):
    number_of_tests = 1
    score = 0
    score0, score1 = 0, 0
    try:
        assert([_globals['merge_sort_max'](m) for m in range(1,5)] == [(m-1)*2**m+1 for m in range(1,5)])
    except:
        print("The lambda-expression merge_sort_max seems not to return the correct numbers")
    else:
        print("The lambda-expression merge_sort_max seems to return the correct numbers")
        score0 += 1
    try:
        assert([isinstance(_globals['merge_sort_max'](m), int) for m in range(1,5)])
    except:
        print("The lambda-expression merge_sort_max seems not to return ints")
    else:
        print("The lambda-expression merge_sort_max seems to return ints")
        score1 += 1
    score += score0*score1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iif():   
    return 2

def question3iiiafunc(_globals):
    number_of_tests = 3
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['merge_sort'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("merge_sort does not seem to sort lists correctly")
    else:
        print("merge_sort seems to sort lists correctly")
        score += 1
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['merge_sort'](test_data)
        assert(_globals['comparison_count'] == 66)
    except:
        print("Your comparison count is different from ours; can you check?")
    else:
        print("Your function requires exactly the same number of comparisons as ours")
        score += 1
    try:
        assert(len(_globals['merge_sort'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iiiatest(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    try:
        assert(_globals['comparison_count'] == 47)
    except:
        print("Your comparison count is different from ours; can you check?")
    else:
        print("Your function requires exactly the same number of comparisons as ours")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iiib(_globals):
    number_of_tests = 1
    score = 0
    global cc
    try:
        cc = 0
        data = _globals['merge_sort_length16_bestcase']
        fn4(data)
        assert(cc == 32)
    except:
        print("We think this is incorrect, and that it requires more than the minimum number of comparisons; can you check again?")
    else:
        print("We agree: this seems to be a good 'best case'")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')      
        
def question3iiic(_globals):
    number_of_tests = 1
    score = 0
    global cc
    try:
        cc = 0
        data = _globals['merge_sort_length16_worstcase']
        fn4(data)
        assert(cc == 49)
    except:
        print("We think this is incorrect, and that it requires more than the minimum number of comparisons; can you check again?")
    else:
        print("We agree: this seems to be a good 'worst case'")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!') 
        
