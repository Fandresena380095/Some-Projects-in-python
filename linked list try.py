class Node:
    def __init__(self,element,new_element):
        self.element = element
        self.new_element = new_element


class linked_list:
    def __init__(self,root):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def __str__(self):
        this_node = self.root
        while this_node is not None:
            print(this_node ,end='=>')
            this_node = this_node.new_element
        print("None")


r = linked_list(2)
r.add(5)
print(r)



        
