from START_asn_1 import myInventory, myProduct
import pytest
import math
import os

def toleranceEquals(a, b, tolerance):
    if math.isclose(a, b, abs_tol=tolerance):
        return True
    else:
        return False
FILE_1 = "Strength_Training.csv"
FILE_2 = "Car_Electronics.csv"
4
#inv_1 = START_asn_1.myInventory("Inv 1", FILE_1)
#inv_2 = START_asn_1.myInventory("Inv 2", FILE_2)
inv_1 = myInventory("Inv 1", FILE_1)
inv_2 = myInventory("Inv 2", FILE_2)

inv_1_item_1 = "Reebok Resistance Tube"
inv_1_item_1_init_rating = 4.4

"""
def test_preTest():
    real_val = 7
    stud_val = SUBMISSION.sampleTestFunction()
    print(stud_val)
    did_pass = toleranceEquals(stud_val, real_val, .01)
    print(did_pass)
    assert did_pass
"""

def test_strengthLength():
    current_dir = os.getcwd()
    os.system(f"ls {current_dir}")
    real_val = 1097
    #inv_1 = START_asn_1.myInventory("Inv 1", FILE_1)
    stud_val = len(inv_1)
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, .01)

def test_strengthSubsetPrices():
    #inv_1 = START_asn_1.myInventory("Inv 1", FILE_1)
    real_val = 1020
    stud_val = inv_1.getPrices(5, 10000)
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(len(stud_val), real_val, .01)

def test_strengthRating1():
    #inv_1 = START_asn_1.myInventory("Inv 1", FILE_1)
    stud_val = inv_1.itemRating(inv_1_item_1)
    real_val = inv_1_item_1_init_rating
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, .01)

def test_carLength():
    #inv_2 = START_asn_1.myInventory("Inv 2", FILE_2)
    real_val = 976
    stud_val = len(inv_2)
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, .01)
