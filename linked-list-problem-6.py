"""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(head1, head2): 
    # Initialize the result
    result = None
    # Check if the first list is empty
    if head1 == None:
        # Return the second list
        return head2
    # Check if the second list is empty
    if head2 == None:
        # Return the first list
        return head1
    # Check if the first list value is smaller
    if head1.val < head2.val:
        # Update the result
        result = head1
        # Update the result next
        result.next = merge_sorted_lists(head1.next, head2)
    # Otherwise
    else:
        # Update the result
        result = head2
        # Update the result next
        result.next = merge_sorted_lists(head1, head2.next)
    # Return the result
    return result

# Create linked list 1: 1 -> 3 -> 5
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

# Create linked list 2: 2 -> 4 -> 6
l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

# Merge the linked lists
merged = merge_sorted_lists(l1, l2)

# Traverse and print the merged linked list
current = merged
while current:
    print(current.val)
    current = current.next

    