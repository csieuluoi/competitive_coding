import math

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#     def __len__(self):
#         return self.length
#     def push(self, val):
#         new_node = ListNode(val)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length+=1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         c = 0
#         r = l1.val + l2.val + c
#         c = r//10
#         d = r - c*10
#         current = ListNode(d, None)
#         result = current
#         l1 = l1.next
#         l2 = l2.next
#         if l1!= None and l2 != None:

#             while ((l1.next is not None) & (l2.next is not None)):
#                 # print("hello")
#                 r = l1.val + l2.val + c
#                 c = r//10
#                 d = r - c*10
#                 current.next = ListNode(d)
#                 current = current.next

#                 l1 = l1.next
#                 l2 = l2.next
#             r = l1.val + l2.val + c
#             c = r//10
#             d = r - c*10
#             current.next = ListNode(d)
#             current = current.next
#             l1 = l1.next
#             l2 = l2.next
#         if l1 == None and l2!= None:
#             while (l2.next is not None):
#                 r = l2.val + c
#                 c = r//10
#                 d = r - c*10

#                 current.next = ListNode(d)
#                 current = current.next
#                 l2 = l2.next
#             r = l2.val + c
#             c = r//10
#             d = r - c*10
#             current.next = ListNode(d)
#             current = current.next
#             l2 = l2.next
#         elif l2 == None and l1 != None:
#             while (l1.next is not None):
#                 r = l1.val + c
#                 c = r//10
#                 d = r - c*10
#                 current.next = ListNode(d)
#                 current = current.next
#                 l1 = l1.next
#             r = l1.val + c
#             c = r//10
#             d = r - c*10
#             current.next = ListNode(d)
#             current = current.next
#             l1 = l1.next
#         if c == 1:
#             current.next = ListNode(c)

#         return result

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        r = l1.val + l2.val + c
        c = r//10
        d = r - c*10
        current = ListNode(d, None)
        result = current
        l1 = l1.next
        l2 = l2.next
        

        while ((l1 is not None) & (l2 is not None)):
            r = l1.val + l2.val + c
            c = r//10
            d = r - c*10
            current.next = ListNode(d)
            current = current.next

            l1 = l1.next
            l2 = l2.next

        if l1 == None and l2!= None:
            while (l2 is not None):
                r = l2.val + c
                c = r//10
                d = r - c*10

                current.next = ListNode(d)
                current = current.next
                l2 = l2.next

        elif l2 == None and l1 != None:
            while (l1 is not None):
                r = l1.val + c
                c = r//10
                d = r - c*10
                current.next = ListNode(d)
                current = current.next
                l1 = l1.next

        if c == 1:
            current.next = ListNode(c)

        return result

if __name__ == "__main__":
    l1=  ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    while result is not None:
        print(result.val)
        result = result.next
