##Assignment 4
##Name: Cindy Gao
##Student Number: 10026799



"""
Creates and returns a linked list containing all of the elements
of the Python-style list parameter.  A useful shortcut for testing.
"""
def createList(plist):
   
    linkedList = None
    # goes backwards, adding each element to the beginning
    # of the list.  
    for index in range(len(plist)-1, -1, -1):
        linkedList = insertValueHead(linkedList, plist[index])
    return linkedList

'''
Create an empty linked list
'''
def emptyList():
  return None   #absence of a value -- nothing

'''
Creates a string representation of the values in the linked list such as:
5->6->9->14.
'''
def listString(linkedList):
  ptr = linkedList
  str1 = ''
  while ptr != None:
    str1 += str(ptr['data'])
    ptr = ptr['next']
    if ptr != None:
      str1 += "->"
  str1 = str1
  return str1

'''
Inserts a new node containing the value "value" to the head of the list.
LinkedList is the head of the list to be added to
Value is the data to be stored in the node
'''
def insertValueHead(linkedList, value):
    newnode = {}
    newnode["data"] = value
    #set the next pointer of this new node to the head of the list, linkedList
    #newnode is now the head of the list 
    newnode["next"] = linkedList
    return newnode

"""
Helper method: returns a reference to node n in a list counting from zero).
Parameters: the list and an index n
If there is no node n, returns None.
"""
def nthNode(linkedList, n):
    ptr = linkedList
    count = 0
    if n < 0:
        return None
    while ptr != None and count < n:
        ptr = ptr['next']
        count += 1
    return ptr


#This function is a general function for inserting values in a linked list given an index

def insertNode(alist, index, value):
    
  #case 1:  Adding to the head of the list -- index == 0
    if index == 0:
        new ={"data":value, "next":alist}
        alist = new
        return alist

  #case 2:  Adding elsewhere in the list
    else:
        beforeN = nthNode(alist, index-1)
        if beforeN == None:
            print "the index you have entered is invalid"
        else:
            afterNode = nthNode(alist, index)
            new = {"data":value}
            beforeN['next'] = new
            new["next"] = afterNode
            return alist


##This function switches the head of the linked list with the node at the inputted index

def switch(alist, index):

    ## valid index case
    if nthNode(alist, index)!= None:
        middle = nthNode(alist, index)
        afterMid = nthNode(alist, index+1)
        beforeMid = nthNode(alist, index-1)
        oldHead = alist
        tempHead = alist['next']

        oldHead['next'] = afterMid
        beforeMid['next'] = oldHead
        middle['next'] = tempHead

        alist = middle
        return alist

    ## invalid index case
    else:
        print "you have not entered a valid index"
        return alist


##This function computes the sum of all the even values contained in the linked list.

def sumEvens(linkedList):

    ## base case for when node after the last node is reached
    if linkedList == None:
        return 0

    ## checking if data contained within specified node is even or not
    else:
        if int(linkedList['data'])%2 == 0:
            temp = linkedList['next']
            return int(linkedList['data']) + sumEvens(temp)
        else:
            temp = linkedList['next']
            return sumEvens(temp)
        

def testInsert():
  #test code to ensure that insertNode is working correctly.
  myList = createList([1, 2, 3, 4, 5, 6])
  print "The initial list", listString(myList)
  #insert 0 at the head
  myList = insertNode(myList,0, 0)
  print "Inserted 0 at the start of list: ", listString(myList)
  #insert 7 at the end
  myList = insertNode(myList, 7, 7)
  print "Inserted 7 at the end of list: ", listString(myList)
  myList= insertNode(myList, 3, 2.2)
  print "Inserted 2.2 in the 3rd position ", listString(myList)
  myList = insertNode(myList, 26, 12)   #should generate an error

def testSumEvens():
    #test code to ensure that sumEvens() is working properly
    myList = createList([14, 21, 29, 2, 16, 49, -26])
    print "The sum of the even numbers in the first list is ", sumEvens(myList)
    myList = createList([])
    print "The sum of the even numbers in an empty list is ", sumEvens(myList)
    myList = createList([5, 15, 25])
    print "The sume of the even numbers in the final list is ", sumEvens(myList)


def testSwitch():
    #test code to ensure that switch() is working correctly.
    myList = createList([10, 20, 30, 40, 50, 60])
    print "The initial list", listString(myList)
    myList = switch(myList, 2)
    print "Switching the head and the 30.  Resulting list is ", listString(myList)
    myList = switch(myList, 5)
    print "Switching the head and the 60.  Resuling list is ", listString(myList)
    myList = switch(myList, 29)  #should result in an error


## main function that utilizes the test functions to see whether sumEvens(),
## insertNode(), and switch() works
    
def main():
    testInsert()
    testSwitch()
    testSumEvens()

main()

  
