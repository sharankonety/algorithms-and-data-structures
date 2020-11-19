# insertion of elements of array to a linked list
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
def create_linked_list(arr,n):
    head = None
    for i in range(0,n):
        head = insert(head,arr[i])
    return head
def insert(head,new_data):
    new_node = Node(new_data)
    if head == None:
        head = new_node
    else: 
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    return head
def display(head):
    while head:
        print(head.data,end="-->")
        head = head.next
    print("/0")
if __name__=='__main__':
    arr1 = [2, 3, 5, 6]
    arr2 = [1, 4, 10]
    n1 = len(arr1)
    n2 = len(arr2)
    ll_1 = create_linked_list(arr1,n1)
    display(ll_1)
    ll_2 = create_linked_list(arr2,n2)
    display(ll_2)
    