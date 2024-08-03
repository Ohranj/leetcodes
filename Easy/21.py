# Merge Two Sorted Lists

# 0 none / 0, 1 / 0, 2 -> 0 none / 0, 1 / 1, 2

def mergeTwoLists(self, list1, list2):
    if not list1: return list2;
    if not list2: return list1;

    newList = ListNode(0);
    pointer = newList;

    while list1 and list2:
        if list1.val < list2.val:
            # List1 is mem locs
            pointer.next = list1;
            list1 = list1.next;
        else:
            # List2 is mem locs
            pointer.next = list2;
            list2 = list2.next;
        # Update mem loc
        pointer = pointer.next;
    
    if list1: pointer.next = list1;
    if list2: pointer.next = list2;
    
    return newList.next;        