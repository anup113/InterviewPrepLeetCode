'''
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Example 2:
Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Example 3:
Input: n = 3
Output: 90
'''


class Solution:
    def countOrders(self, n: int) -> int:
        '''
                        0
                    /       \
                    p1      p2    
                /     \     /   \
                p2      d1      d2
            /    \        \        \
            d1    d2        p2      p1
        /           \         \        \      

        '''
        MOD = 10**9 + 7

        def generate(pickup, delivery):
            if pickup == delivery == 0:
                return 1
            res = 0
            if pickup:  # There are `pickup` number of different open parenthesises
                res = (res + pickup * generate(pickup - 1, delivery) % MOD) % MOD
            if pickup < delivery:
                res = (res + (delivery - pickup) *
                       generate(pickup, delivery - 1) % MOD) % MOD
            return res
        return generate(n, n)
