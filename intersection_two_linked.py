# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(list):

       #Initializing values
       prev = None
       curr = list.head
       nex = curr.getNextNode()
  
       #looping
       while curr:
           #reversing the link
           curr.setNextNode(prev)     

           #moving to next node      
           prev = curr
           curr = nex
           if nex:
               nex = nex.getNextNode()

       #initializing head
       list.head = prev
    
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #reverse both linked lists,
        a_reversed = reverseList(headA)
        b_reversed = reverseList(headB)
        
        node_val = null
        
        #compare list values, if value doesn't match return null
        while a_reversed.next != None or b_reversed.next != None
            #if values match, go to the next one
            if a_reversed.val == b_reversed.val:
                node_val = a_reversed.val
                a_reversed = a_reversed.next  #move to the next item
                b_reversed = b_reversed.next  #move to the next item
                
            if a_reversed.val != b_reversed.val:
                break
        
        return node_val
       
    
        
