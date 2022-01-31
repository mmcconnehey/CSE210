class Base:

    def __init__(self):
        self._helper()
    
    def _helper(self):
        print('Helper function')

    #__ sets the function to private
    def __helper2(self):
        print('Helper 2 function')

x = Base()

print('Trying to call subfunction')

x._helper()

print('Trying to call private function')

#x.__helper2()


#access private functions by using _Base before calling the private function
x._Base__helper2()