from playToken import PlayToken
from typing import List

class ModelView:
    def update_view(self, arr : List[PlayToken]):

        if len(arr) is not 9:
            raise TypeError("Array must be 9 units long")

        print("---------")
        print("| ", end="")
        for i in range(3):
            print(str(arr[i].name)  + " ", end="")
        print("|")
        print("| ", end="")
        for i in range(3, 6):
            print(str(arr[i].name) + " ", end="")
        print("|")
        print("| ", end="")
        for i in range(6, 9):
            print(str(arr[i].name) + " ", end="")
        print("|")
        print("---------")