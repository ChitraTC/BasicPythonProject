class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, " -> ", end='')
            temp = temp.next_node
        print("")

    def insert_at_head(self, data):
        new_node = Node(data)  #create a new node and put the data=4
        new_node.next_node = self.head #New node should have address of previous node which is available in self.head
        self.head = new_node #self.head should have adrees of new node



if __name__ == '__main__':
    llist = LinkedList()
    # print(llist.head)
    llist.head = Node(1)
    print(llist.head) #address of first node
    print(llist.head.next_node)# address of next node
    print(llist.head.data)     # data

    # second=Node(2)
    # third=Node(3)
    # llist.head.next_node=second
    # second.next_node=third
    # llist.printList()
    #
    #
    # llist.insert_at_head(4)
    # llist.printList()

