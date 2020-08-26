import calculator
import pytest
 
def test_addition():
    assert calculator.addition(10,5)==15
    assert calculator.addition(10,3)==13
    assert calculator.addition(10,100)==110
    print("testing build trigger ")
    print("testing again.")
    
def test_subtraction():
    assert calculator.subtraction(10,3)==7
    assert calculator.subtraction(30,10)==20
    assert calculator.subtraction(25,10)==15
    print("checking auto trigger function again.")
    
def test_multiply():
    assert calculator.mul(10,3)==30
    assert calculator.mul(30,10)==300
    assert calculator.mul(25,10)==250
    print("Finished")

def test_division():
    assert calculator.div(100,10)==10
    assert calculator.div(30,10)==3
    assert calculator.div(25,5)==5
    print("checking auto trigger function again.")



