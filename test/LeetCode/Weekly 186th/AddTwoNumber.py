#1hour 
#leetcode 테스트 케이스를 만드는과정이 번거로워 시간이 많이 걸렸다.
#또한 생각을 정리하지 않고 짜서 그런지 로직을 좀 어렵게 생각했다.
#더 좋은 방법이 있을지 생각하면서 짜자

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    cur = head
    while cur != None:
        print(cur.val)
        cur = cur.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curL1 = l1
        curL2 = l2
        l3 = ListNode(0)
        curL3 = l3
        add = 0
        while curL1 != None or curL2 != None or add != 0:
            num1 = curL1.val if curL1 != None else 0
            num2 = curL2.val if curL2 != None else 0
            sum = num1+num2+add
            num3 = sum%10
            #print('{} {} {}'.format(num1,num2,num3))
            add = int(sum/10)
            newNode = ListNode(num3)
            curL3.next = newNode
            curL3 = curL3.next
            if curL1 != None:
                curL1 = curL1.next
            if curL2 != None:
                curL2 = curL2.next
        return l3.next
            
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(9)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
# l2.next.next.next = ListNode(1)

l1 = ListNode(1)
l2 = ListNode(9)
l2.next = ListNode(9)

sol = Solution()
sol.addTwoNumbers(l1,l2)