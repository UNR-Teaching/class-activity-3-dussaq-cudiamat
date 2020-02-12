from playToken import PlayToken

class ModelView:
    def update_view(self, arr):
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


model = ModelView()
model.update_view([PlayToken.E, PlayToken.E, PlayToken.X, PlayToken.E, PlayToken.E, PlayToken.O, PlayToken.E, PlayToken.E, PlayToken.X])