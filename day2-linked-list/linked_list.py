class SinglyLinkedList:

    class ListNode:
        value: object
        next: object

        def __init__(self, value, next):
            self.value = value
            self.next = next

        def has_next(self):
            return not self.next is None
        
        def __str__(self):
            return f"[{self.value}]"

    first: ListNode
    len: int

    def __init__(self, first_value: object):
        self.first = self.ListNode(value=first_value, next=None)
        self.len = 1

    def add(self, value, index=None):
        if index is None: index = self.len

        try:
            prev_node = self._get_node_at_index(index)
        except IndexError as e:
            print(e)
            return 1
        
        after_node = None

        if prev_node.has_next():
            after_node = prev_node.next
            
        new_node = self.ListNode(value=value, next=after_node)
        prev_node.next = new_node

        self.len += 1

    def remove(self, index):
        if index == 0:
            self.first = self.first.next
            return 0
        
        if index >= self.len:
            raise IndexError(f"Index out of bounds: {index}")
        
        prev_node = self._get_node_at_index(index=index)
        curr_node = self._get_node_at_index(index=index+1)

        prev_node.next = curr_node.next
        self.len -= 1

        return curr_node


    def _get_node_at_index(self, index) -> ListNode:
        # Traverse through list until index is found
        #   Throw error if index is outside of length of list 
        if index > self.len:
            raise IndexError(f"Linked List does not have {index} elements.")
        
        curr_node = self.first
        curr_index = 0

        while curr_index < index-1:
            curr_node = curr_node.next
            curr_index += 1
            
        return curr_node
    
    def __len__(self):
        return self.len

    def __str__(self):
        ret = ""

        curr_node = self.first
        while curr_node.has_next():
            ret += f"{curr_node.__str__()}->"
            curr_node = curr_node.next
        ret += f"{curr_node.__str__()}"

        return ret
    
if __name__ == "__main__":
    llist = SinglyLinkedList(5)

    llist.add(4)

    llist.add(3)

    print(llist)

    llist.add(2)

    llist.remove(1)

    print(llist)