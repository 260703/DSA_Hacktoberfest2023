# this is leetcode solution for the problem number 25. (Merge k Sorted Lists)
# i hope you like this 



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    def reverseLinkedList(head, k):
        prev = None
        curr = head

        for _ in range(k):
            if not curr:
                return None
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def getKthNode(head, k):
        for _ in range(k):
            if not head:
                return None
            head = head.next
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    while head:
        kth_node = getKthNode(head, k)
        if not kth_node:
            break
        next_group_start = kth_node.next
        kth_node.next = None  # Disconnect the group
        prev_group_end.next = reverseLinkedList(head, k)
        head.next = next_group_start
        prev_group_end = head
        head = next_group_start

    return dummy.next

# Helper function to create a linked list from a list
def createLinkedList(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
nums = [1, 2, 3, 4, 5]
k = 3
head = createLinkedList(nums)
print("Original linked list:")
printLinkedList(head)
result = reverseKGroup(head, k)
print("Linked list after reversing in groups of", k)
printLinkedList(result)
