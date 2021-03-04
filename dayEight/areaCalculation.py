#Wall paint 
#1 can of paint = 5 square meters
import math

def paint_calc(height,width,cover):
    #18.2 to 19: math.cell
    number_of_cans = math.cell((height*width)/cover)
    print(f"You will need {number_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h,width=test_w,cover=coverage)
