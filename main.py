
from linkedlist import LinkedList


mylist = LinkedList()
mylist.add( "Hello" )
mylist.add( "There" )
mylist.add( "Cruel" )
mylist.add( "World" )

print( mylist.toList() )
mylist.reverse()
print( mylist.toList() )



