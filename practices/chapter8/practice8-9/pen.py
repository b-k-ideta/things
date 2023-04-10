class Pen:

    def __init__(self,color="黒",ink=10):
        self.__color = color
        self.__ink = ink

    def __str__(self):
        return f"ペンの色は{self.__color}です。インク残量は{self.__ink}。"
    
    def draw(self,msg=""):
        if self.__ink == 0:
            print("インク切れ")
            return
        else:
            print(f"ペンの色は{self.__color}です。{msg}")
            self.__ink -= 1
            return

