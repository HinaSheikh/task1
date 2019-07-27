class CharacterCount:
    def inputchar(self,user_input):
        self.__inputString=None
        if type(user_input)==str:
          self.__inputString=user_input
        else:
            print("input is invalid")
    def countCharacter (self):
        if self.__inputString != None:
            return len(self.__inputString)

c=CharacterCount()
c.inputchar("HELLO")
count=c.countCharacter()
if count!=None:
    print("The no of characters in string :",c.countCharacter())


                
                

