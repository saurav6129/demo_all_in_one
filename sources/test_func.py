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

