#/]: # ( ------------------------------------------------------------------ {c)
#/]: # ( COPYRIGHT 2022 Dwij Bavisi <dwijbavisi@gmail.com>                  {c)
#/]: # ( Licensed under:                                                    {c)
#/]: # (     Taciturn Coder's `License to Hack` License                     {c)
#/]: # (     TC's L2H 1.0                                                   {c)
#/]: # ( A copy of the License may be obtained from:                        {c)
#/]: # (     https://TaciturnCoder.github.io/TCsL2H/legalcode/1.0           {c)
#/]: # ( See the License for the permissions and limitations.               {c)
#/]: # ( ------------------------------------------------------------------ {c)

# # Palindrome Number
# Shrutajnana (version:1, patch:0, draft:0)

# Original problem available at: https://leetcode.com/problems/palindrome-number/

# ---
# ## Problem statement
# Available here: [Problem.md](../Problem.md)

# ## Version 1.0.0
# Time complexity | Space complexity | Notes |
# | --- | --- | --- |
# | O(n^2) | O(n) | Using strings |

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)

        return s == s[::-1]
