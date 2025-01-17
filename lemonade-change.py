from typing import List
def lemonadeChange(bills:List[int])-> bool:
    bal=bills[0]

    for ele in bills[1:]:
        if ele !=5 and ele <=bal:
            bal -=ele
        else:
            return False
    return True


print(lemonadeChange(bills=[5,5,5,10,20]))
