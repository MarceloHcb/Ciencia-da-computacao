from linked_list_content import LinkedList

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"Node(value={self.value}, next={self.next})"
    
if __name__ == "__main__":
    my_linked_list = LinkedList()

    my_linked_list.insert_first('A')
    my_linked_list.insert_first('B')
    my_linked_list.insert_first('C')
    my_linked_list.insert_first('D')
    my_linked_list.insert_first('E')
    # print(my_linked_list)
    print(my_linked_list.get_mid_element())