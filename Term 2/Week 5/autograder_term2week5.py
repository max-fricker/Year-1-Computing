import numpy.testing as npt
from time import time
import numpy as np
import math
print("Autograder loaded successfully!")
print("Remember to always restart and run all from the Kernel menu before submitting!")
def question1ia(_globals):
    number_of_tests = 3
    score = 0
    score0, score1, score2 = 0, 0, 0
    score00, score01, score10, score11, score20, score21 = 0, 0, 0, 0, 0, 0
    try:
        assert(all([_globals["myrange"][i]==97+i for i in range(6)]))
    except:
        print("myrange does not contain the right numbers")
    else:
        print("myrange contains the right numbers")
        score00 += 1
    try:
        assert(isinstance(_globals["myrange"],range))
    except:
        print("myrange is not a range")
    else:
        print("myrange is a range")
        score01 += 1
    score0 = score00 * score01
    if score0 == 1:
        print('First test passed!\n')
    else:
        print('First test failed!\n')
    try:
        assert(all([_globals["mylist"][i]==97+i for i in range(6)]))
    except:
        print("mylist does not contain the right numbers")
    else:
        print("mylist contains the right numbers")
        score10 += 1
    try:
        assert(isinstance(_globals["mylist"],list))
    except:
        print("mylist is not a list")
    else:
        print("mylist is a list")
        score11 += 1
    score1 = score10 * score11
    if score1 == 1:
        print('Second test passed!\n')
    else:
        print('Second test failed!\n')
    try:
        assert(all([_globals["myarray"][i]==97+i for i in range(6)]))
    except:
        print("myarray does not contain the right numbers")
    else:
        print("myarray contains the right numbers")
        score20 += 1
    try:
        assert(isinstance(_globals["myarray"],np.ndarray))
    except:
        print("myarray is not a numpy array")
    else:
        print("myarray is a numpy array")
        score21 += 1
    score2 = score20 * score21
    if score2 == 1:
        print('Final test passed!\n')
    else:
        print('Final test failed!\n')
        score += 1
    score = score0 + score1 + score2
    if score > 0:
        print("{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ib():   
    return 1

def question1ic(_globals):
    number_of_tests = 3
    score = 0
    score0, score1, score2 = 0, 0, 0
    score00, score01, score10, score11, score20, score21 = 0, 0, 0, 0, 0, 0
    try:
        assert(all([_globals["range_squares"][i]==(97+i)**2 for i in range(6)]))
    except:
        print("range_squares does not contain the right numbers")
    else:
        print("range_squares contains the right numbers")
        score00 += 1
    try:
        assert(isinstance(_globals["range_squares"],list))
    except:
        print("range_squares is not a list")
    else:
        print("range_squares is a list")
        score01 += 1
    score0 = score00 * score01
    if score0 == 1:
        print('First test passed!\n')
    else:
        print('First test failed!\n')
    try:
        assert(all([_globals["list_squares"][i]==(97+i)**2 for i in range(6)]))
    except:
        print("list_squares does not contain the right numbers")
    else:
        print("list_squares contains the right numbers")
        score10 += 1
    try:
        assert(isinstance(_globals["list_squares"],list))
    except:
        print("list_squares is not a list")
    else:
        print("list_squares is a list")
        score11 += 1
    score1 = score10 * score11
    if score1 == 1:
        print('Second test passed!\n')
    else:
        print('Second test failed!\n')
    try:
        assert(all([_globals["array_squares"][i]==(97+i)**2 for i in range(6)]))
    except:
        print("list_squares does not contain the right numbers")
    else:
        print("list_squares contains the right numbers")
        score20 += 1
    try:
        assert(isinstance(_globals["array_squares"],list))
    except:
        print("array_squares is not a list")
    else:
        print("array_squares is a list")
        score21 += 1
    score2 = score20 * score21
    if score2 == 1:
        print('Final test passed!\n')
    else:
        print('Final test failed!\n')
        score += 1
    score = score0 + score1 + score2
    if score > 0:
        print("{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1id():   
    return 1

def question1ie(_globals):
    number_of_tests = 1
    score = 0
    score0, score1 = 0, 0
    try:
        assert(all([_globals["square_array"][i]==(97+i)**2 for i in range(6)]))
    except:
        print("square_array does not contain the right numbers")
    else:
        print("square_array contains the right numbers")
        score0 += 1
    try:
        assert(isinstance(_globals["square_array"],np.ndarray))
    except:
        print("square_array is not a numpy array")
    else:
        print("square_array is a numpy array")
        score1 += 1
    score = score0 * score1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question1iia(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(np.all(_globals["mat1"]==np.fromfunction(lambda x, y: x+y, (3,4))))
    except:
        pass
    else:
        print("Test passed!")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question1iib(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals["squares1"]==[0.0, 1.0, 4.0, 9.0, 1.0, 4.0, 9.0, 16.0, 4.0, 9.0, 16.0, 25.0])
    except:
        pass
    else:
        print("Test passed!")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question1iic(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals["squares2"]==[0.0, 1.0, 4.0, 1.0, 4.0, 9.0, 4.0, 9.0, 16.0, 9.0, 16.0, 25.0])
    except:
        pass
    else:
        print("Test passed!")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question1iid(_globals):
    number_of_tests = 3
    score = 0
    score0, score1, score2 = 0, 0, 0
    try:
        assert(np.all(_globals['mat2']==np.fromfunction(lambda x, y: abs(x-y), (3,4))))
    except:
        print("mat2 is incorrect\n")
    else:
        print("mat2 is correct\n")
        score0 += 1
    try:
        assert(np.all(_globals['mat3']==np.fromfunction(lambda x: x**2, (4,))))
    except:
        print("mat3 is incorrect\n")
    else:
        print("mat3 is correct\n")
        score1 += 1
    try:
        assert(np.all(_globals['mat4']==np.fromfunction(lambda x, y: y**2 - x**2, (4,4))))
    except:
        print("mat4 is incorrect\n")
    else:
        print("mat4 is correct\n")
        score2 += 1
    score = score0 + score1 + score2
    if score > 0:
        print("{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iie():   
    return 2

def question2a(_globals):
    number_of_tests = 4
    score = 0
    try:
        assert(np.isclose(_globals['simpsons_rule1'](math.sin, 0, math.pi/2, 20), 1.00000021))
    except:
        print('Test with positional value of n failed!\n')
    else:
        print('Test with positional value of n passed!\n')
        score += 1
    try:
        assert(np.isclose(_globals['simpsons_rule1'](math.sin, 0, math.pi/2, n=16), 1.00000051))
    except:
        print('Test with keyword value of n failed!\n')
    else:
        print('Test with keyword value of n passed!\n')
        score += 1
    try:
        assert(np.isclose(_globals['simpsons_rule1'](math.sin, 0, math.pi/2), 1.00000339))
    except:
        print('Test with default value of n failed!\n')
    else:
        print('Test with default value of n passed!\n')
        score += 1
    try:
        assert(len(_globals['simpsons_rule1'].__doc__)>0)
    except:
        print('This function does not seem to have a docstring\n')
    else:
        print('This function seems to have a docstring\n')
        score += 1
    if score > 0:
        print("{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2b(_globals):
    number_of_tests = 4
    score = 0
    try:
        assert(np.isclose(_globals["simpsons_rule2"](np.sin, 0, np.pi/2, 20), 1.00000021))
    except:
        print('Test with positional value of n failed!\n')
    else:
        print('Test with positional value of n passed!\n')
        score += 1
    try:
        assert(np.isclose(_globals["simpsons_rule2"](np.sin, 0, np.pi/2, n=16), 1.00000051))
    except:
        print('Test with keyword value of n failed!\n')
    else:
        print('Test with keyword value of n passed!\n')
        score += 1
    try:
        assert(np.isclose(_globals["simpsons_rule2"](np.sin, 0, np.pi/2), 1.00000339))
    except:
        print('Test with default value of n failed!\n')
    else:
        print('Test with default value of n passed!\n')
        score += 1
    try:
        assert(len(_globals['simpsons_rule2'].__doc__)>0)
    except:
        print('This function does not seem to have a docstring\n')
    else:
        print('This function seems to have a docstring\n')
        score += 1
    if score > 0:
        print("{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2c():   
    return 1

def question2d():   
    return 2

def question2e():   
    return 1

def question2f():   
    return 3

def question3a(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.isclose(_globals['sine_map1'](0.3, 1.0, 0.3), 0.6 - 1.0/(2*np.pi) * np.sin(2*np.pi*0.3)))
    except:
        print('Test of sine_map1 failed!\n')
    else:
        print('Test of sine_map1 passed!\n')
        score += 1
    try:
        assert(np.isclose(_globals['sine_map2'](0.3, 1.0, 0.3), 0.6 - 1.0/(2*np.pi) * np.sin(2*np.pi*0.3)))
    except:
        print('Test of sine_map2 failed!\n')
    else:
        print('Test of sine_map2 passed!\n')
        score += 1
    if score > 0:
        print("{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3b():   
    return 1
        
def question3c():   
    return 3

def question3d(_globals):
    number_of_tests = 8
    score = 0
    try:
        assert(np.isclose(_globals["rotation_number1"](0.4, 0.5, 0.4, 100), 0.3974647501883852))
    except:
        print('Test of rotation_number1 with positional value of N failed!\n')
    else:
        print('Test of rotation_number1 with positional value of N passed!\n')
        score += 1
    try:
        assert(np.isclose(_globals["rotation_number1"](0.4, 0.5, 0.4, N=200), 0.3968885492490793))
    except:
        print('Test of rotation_number1 with keyword value of N failed!\n')
    else:
        print('Test of rotation_number1 with keyword value of N passed!\n')
        score += 1
    try:
        assert(np.isclose(_globals["rotation_number1"](0.4, 0.5, 0.4), 0.39710384441275653))
    except:
        print('Test of rotation_number1 with default value of N failed!\n')
    else:
        print('Test of rotation_number1 with default value of N passed!\n')
        score += 1
    try:
        assert(len(_globals['rotation_number1'].__doc__)>0)
    except:
        print('The function rotation_number1 does not seem to have a docstring\n')
    else:
        print('The function rotation_number1 seems to have a docstring\n')
        score += 1
    try:
        assert(np.isclose(_globals["rotation_number2"](0.4, 0.5, 0.4, 100), 0.3974647501883852))
    except:
        print('Test of rotation_number2 with positional value of N failed!\n')
    else:
        print('Test of rotation_number2 with positional value of N passed!\n')
        score += 1
    try:
        assert(np.isclose(_globals["rotation_number2"](0.4, 0.5, 0.4, N=200), 0.3968885492490793))
    except:
        print('Test of rotation_number2 with keyword value of N failed!\n')
    else:
        print('Test of rotation_number2 with keyword value of N passed!\n')
        score += 1
    try:
        assert(np.isclose(_globals["rotation_number2"](0.4, 0.5, 0.4), 0.39710384441275653))
    except:
        print('Test of rotation_number2 with default value of N failed!\n')
    else:
        print('Test of rotation_number2 with default value of N passed!\n')
        score += 1
    try:
        assert(len(_globals['rotation_number2'].__doc__)>0)
    except:
        print('The function rotation_number2 does not seem to have a docstring\n')
    else:
        print('The function rotation_number2 seems to have a docstring\n')
        score += 1
    if score > 0:
        print("{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3e(_globals):
    number_of_tests = 3
    score = 0
    try:
        assert(np.allclose(_globals["rotation_number_list1"]([0.2,0.3,0.4], 0.5, 0.4, 100), [0.18652483708865758, 0.29232934281200235, 0.3974647501883852]))
    except:
        print('Test of rotation_number_list1 with positional value of N failed!\n')
    else:
        print('Test of rotation_number_list1 with positional value of N passed!\n')
        score += 1
    try:
        assert(np.allclose(_globals["rotation_number_list1"]([0.2,0.3,0.4], 0.5, 0.4, N=200), [0.18539904377078986, 0.2928263544305301, 0.3968885492490793]))
    except:
        print('Test of rotation_number_list1 with keyword value of N failed!\n')
    else:
        print('Test of rotation_number_list1 with keyword value of N passed!\n')
        score += 1
    try:
        assert(np.allclose(_globals["rotation_number_list1"]([0.2,0.3,0.4], 0.5, 0.4), [0.1855252200450131, 0.2927373715587223, 0.39710384441275653]))
    except:
        print('Test of rotation_number_list1 with default value of N failed!\n')
    else:
        print('Test of rotation_number_list1 with default value of N passed!\n')
        score += 1
    if score > 0:
        print("{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3h():   
    return 3

def question4ia(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.all(_globals["ints"]==np.arange(2,31)))
    except:
        print("ints does not contain the right numbers")
    else:
        print("ints contains the right numbers")
        score += 1
    try:
        assert(isinstance(_globals["ints"],np.ndarray))
    except:
        print("ints is not a numpy array")
    else:
        print("ints is a numpy array")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question4ib(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.all(_globals["bool1"]==np.array([False, False, False,  True, False, False, False, False,  True,False, False, False, False,  True, False, False, False, False,  True, False, False, False, False,  True, False, False, False, False,  True])))
    except:
        print("bool1 does not contain the right truth values")
    else:
        print("bool1 contains the right truth values")
        score += 1
    try:
        assert(isinstance(_globals["bool1"],np.ndarray))
    except:
        print("bool1 is not a numpy array")
    else:
        print("bool1 is a numpy array")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')  

def question4ic(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.all(_globals["ints2"]==np.array([ 2,  3,  4,  6,  7,  8,  9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29])))
    except:
        print("ints2 does not contain the right numbers")
    else:
        print("ints2 contains the right numbers")
        score += 1
    try:
        assert(isinstance(_globals["ints2"],np.ndarray))
    except:
        print("ints2 is not a numpy array")
    else:
        print("ints2 is a numpy array")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')  

def question4id(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.all(_globals["ints3"]==np.array([ 2,  5,  7, 10, 11, 13, 14, 17, 19, 22, 23, 25, 26, 29])))
    except:
        print("ints3 does not contain the right numbers")
    else:
        print("ints3 contains the right numbers")
        score += 1
    try:
        assert(isinstance(_globals["ints3"],np.ndarray))
    except:
        print("ints3 is not a numpy array")
    else:
        print("ints3 is a numpy array")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')  

def question4ie(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.all(_globals["ints4"]==np.array([ 2,  3,  5,  7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])))
    except:
        print("ints4 does not contain the right numbers")
    else:
        print("ints3 contains the right numbers")
        score += 1
    try:
        assert(isinstance(_globals["ints4"],np.ndarray))
    except:
        print("ints4 is not a numpy array")
    else:
        print("ints4 is a numpy array")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question4if(_globals):
    number_of_tests = 6
    score = 0
    print('Testing with a non-square composite value of n:')
    try:
        assert(np.all(_globals["my_primes2"](30)==np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing with a prime value of n:')
    try:
        assert(np.all(_globals["my_primes2"](31)==np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing with a prime-squared value of n:')
    try:
        assert(np.all(_globals["my_primes2"](49)==np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing edge case n = 2:')
    try:
        assert(np.all(_globals["my_primes2"](2)==np.array([ 2])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing output type (should be a numpy array):')
    try:
        assert(isinstance(_globals["my_primes2"](30),np.ndarray))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing for the presence of a docstring:')
    try:
        assert(len(_globals['my_primes2'].__doc__)>0)
    except:
        print('The function my_primes2 does not seem to have a docstring\n')
    else:
        print('The function my_primes2 seems to have a docstring\n')
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question4iia(_globals):
    number_of_tests = 6
    score = 0
    print('Testing with a non-square composite value of n:')
    try:
        assert(np.all(_globals["my_primes1"](30)==np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing with a prime value of n:')
    try:
        assert(np.all(_globals["my_primes1"](31)==np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing with a prime-squared value of n:')
    try:
        assert(np.all(_globals["my_primes1"](49)==np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing edge case n = 2:')
    try:
        assert(np.all(_globals["my_primes1"](2)==np.array([ 2])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing output type (should be a list):')
    try:
        assert(isinstance(_globals["my_primes1"](30),list))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing for the presence of a docstring:')
    try:
        assert(len(_globals['my_primes1'].__doc__)>0)
    except:
        print('The function my_primes1 does not seem to have a docstring\n')
    else:
        print('The function my_primes1 seems to have a docstring\n')
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question4iib(_globals):
    sieving_array = _globals["sieving_array"]
    try:
        assert(not(np.any(sieving_array[0:2])) and np.all(sieving_array[2:101]))
    except:
        print('sieving_array does not appear to contain the correct values')
        raise AssertionError('Test failed!')
    else:
        print('sieving_array contains the correct values')
        return 1

def question4iic(_globals):
    sieving_array = _globals["sieving_array"]
    try:
        assert(not(np.any(sieving_array[0:2])) and not(np.any(sieving_array[4:101:2])) and np.all(sieving_array[3:101:2]))
    except:
        print('sieving_array does not appear to contain the correct values')
        raise AssertionError('Test failed!')
    else:
        print('sieving_array contains the correct values')
        return 1

def question4iid(_globals):
    sieving_array = _globals["sieving_array"]
    numbers = np.arange(101)[sieving_array]
    try:
        assert(np.all((numbers==2)|(numbers==3)|(numbers%2>0)|(numbers%3>0)))
    except:
        print('sieving_array does not appear to contain the correct values')
        raise AssertionError('Test failed!')
    else:
        print('sieving_array contains the correct values')
        return 1

def question4iie(_globals):
    sieving_array = _globals["sieving_array"]
    numbers = np.arange(101)[sieving_array]
    try:
        assert(np.all((numbers==2)|(numbers==3)|(numbers==5)|(numbers%2>0)|(numbers%3>0)|(numbers%5>0)))
    except:
        print('sieving_array does not appear to contain the correct values')
        raise AssertionError('Test failed!')
    else:
        print('sieving_array contains the correct values')
        return 1

def question4iif(_globals):
    sieving_array = _globals["sieving_array"]
    numbers = np.arange(101)[sieving_array]
    try:
        assert(np.all((numbers==2)|(numbers==3)|(numbers==5)|(numbers==7)|(numbers%2>0)|(numbers%3>0)|(numbers%5>0)|(numbers%7>0)))
    except:
        print('sieving_array does not appear to contain the correct values')
        raise AssertionError('Test failed!')
    else:
        print('sieving_array contains the correct values')
        return 1

def question4iiia(_globals):
    number_of_tests = 6
    score = 0
    print('Testing with a non-square composite value of n:')
    try:
        assert(np.all(_globals["my_primes3"](30)==np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing with a prime value of n:')
    try:
        assert(np.all(_globals["my_primes3"](31)==np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing with a prime-squared value of n:')
    try:
        assert(np.all(_globals["my_primes3"](49)==np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing edge case n = 2:')
    try:
        assert(np.all(_globals["my_primes3"](2)==np.array([ 2])))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing output type (should be a numpy array):')
    try:
        assert(isinstance(_globals["my_primes3"](30),np.ndarray))
    except:
        print('Test failed!\n')
    else:
        print('Test passed!\n')
        score += 1
    print('Testing for the presence of a docstring:')
    try:
        assert(len(_globals['my_primes3'].__doc__)>0)
    except:
        print('The function my_primes3 does not seem to have a docstring\n')
    else:
        print('The function my_primes3 seems to have a docstring\n')
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 
        
def question4iiib(_globals):
    number_of_tests = 3
    score = 0
    start = time()
    _globals["my_primes1"](10**6)
    time1 = time()-start
    start = time()
    _globals["my_primes2"](10**6)
    time2 = time()-start
    start = time()
    _globals["my_primes3"](10**6)
    time3 = time()-start
    try:
        assert(time1<10)
    except:
        print('The my_primes1 function takes more than ten seconds for n=10**6; this can probably be improved.')
    else:
        print('The my_primes1 function takes less than ten seconds for n=10**6; well done.')
        score += 1
    try:
        assert(time2<1)
    except:
        print('The my_primes2 function takes more than one second for n=10**6; this can probably be improved.')
    else:
        print('The my_primes2 function takes less than one second for n=10**6; well done.')
        score += 1
    try:
        assert(time3<0.05)
    except:
        print('The my_primes3 function takes more than 0.05s for n=10**6; this can probably be improved.')
    else:
        print('The my_primes3 function takes less than 0.05s for n=10**6; well done.')
        score += 1    
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 