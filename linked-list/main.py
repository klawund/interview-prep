class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

# traverse

def print_linked_list(head):
    current = head
    
    while current is not None:
        print(current.val)
        current = current.next

# print_linked_list(a)

def print_linked_list_recursively(head):
    if head is None:
        return

    print(head.val)
    print_linked_list_recursively(head.next)

def linked_list_values(head):
    values = []
    current = head

    while current is not None:
        values.append(current.val)
        current = current.next

    return values

# print_linked_list_recursively(a)

def linked_list_values_recursively(head):
    values = []
    fill_values(head, values)
    return values
    
def fill_values(current, values):
    if current is None:
        return
    
    values.append(current.val)
    fill_values(current.next, values)

# print(linked_list_values_recursively(a))

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

one.next = two
two.next = three
three.next = four

# sum

def sum_list(head):
    sum = 0
    current = head

    while current is not None:
        sum += current.val
        current = current.next

    return sum

# print(sum_list(one))

def sum_list_recursively(head):
    if head is None:
        return 0
    
    return head.val + sum_list_recursively(head.next)

# print(sum_list_recursively(one))

# find

def find(head, target):
    current = head

    while current is not None:
        if current.val == target:
            return True
        current = current.next
    
    return False

# print(find(a, 'C'))
# print(find(a, 'G'))

def find_recursively(head, target):
    if head is None:
        return False
    
    if head.val == target:
        return True
    return find_recursively(head.next, target)

# print(find_recursively(a, 'C'))
# print(find_recursively(a, 'G'))

# get_at_index

def get_at_index(head, index):
    current = head
    count = 0

    while current is not None:
        if count == index:
            return current.val

        count += 1
        current = current.next
    
    return None

# print(get_at_index(a, 2))

def get_at_index_recursively(head, target_index):
    if head is None:
        return None

    if target_index == 0:
        return head.val
    
    return get_at_index_recursively(head.next, target_index - 1)

# print(get_at_index_recursively(a, 2))

# reverse

def reverse(head):
    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        
        prev = current
        current = next

    return prev

# print(reverse(one).val)

def reverse_recursively(head, prev = None):
    if head is None:
        return prev
    
    next = head.next
    head.next = prev

    return reverse_recursively(next, head)

# print(reverse(one).val)

# zipper

def zipper(head1, head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0

    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next

        tail = tail.next
        count += 1

    if current1 is not None:
        tail.next = current1
    elif current2 is not None:
        tail.next = current2

    return head1

# print(print_linked_list(zipper(a, one)))

def zipper_recursively(head1, head2):
    if head1 is None and head2 is None:
        return None
    
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
    
    next1 = head1.next
    next2 = head2.next

    head1.next = head2
    head2.next = zipper_recursively(next1, next2)

    return head1

# print(print_linked_list(zipper_recursively(a, one)))
