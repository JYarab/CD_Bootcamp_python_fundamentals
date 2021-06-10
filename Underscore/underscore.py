class Underscore:
    def map(self, iterable, callback):
        # your code here
        newList = []
        for x in iterable:
            newList.append(callback(x))
        return newList

    def find(self, iterable, callback):
        # your code here
        for x in iterable:
            if callback(iterable[x]):
                return iterable[x]

    def filter(self, iterable, callback):
        # your code
        newList = []
        for x in iterable:
            if callback(x) == True:
                newList.append(x)
        return newList
                
    def reject(self, iterable, callback):
        # your code
        newList = []
        for x in iterable:
            if callback(x) == False:
                newList.append(x)
        return newList

# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
timesTwo = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 2)
match = _.find([1, 2, 3, 4, 5, 6], lambda x: x == 4)
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

print(timesTwo)
print(match)
print(evens)
print(odds)