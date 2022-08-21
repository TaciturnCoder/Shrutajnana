#/]: # ( ------------------------------------------------------------------ {c)
#/]: # ( COPYRIGHT 2022 Dwij Bavisi <dwijbavisi@gmail.com>                  {c)
#/]: # ( Licensed under:                                                    {c)
#/]: # (     Taciturn Coder's `License to Hack` License                     {c)
#/]: # (     TC's L2H 1.0                                                   {c)
#/]: # ( A copy of the License may be obtained from:                        {c)
#/]: # (     https://TaciturnCoder.github.io/TCsL2H/legalcode/1.0           {c)
#/]: # ( See the License for the permissions and limitations.               {c)
#/]: # ( ------------------------------------------------------------------ {c)

# Round E 2022 Coloring Game
# Shrutajnana (version:1, patch:1, draft:0)

# Original problem available at: https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba856a#problem

# ---
# ## Problem statement
# Read: [Problem.md](../Problem.md) for problem statement.

# ## Version 1.0.0
# | Time complexity | Space complexity | Implementation notes |
# | --- | --- | --- |
# | O(1) | O(1) | Math |

# ---
# ## Solutions
# Read: [ReadMe.md](../ReadMe.md) for solutions in more programming languages, if any available.

def ceil (x):
    f = int(x)
    return f if f == x else f + 1

for _ in range(int(input())):
    N = int(input())

    print("Case #{}:".format(_ + 1), end=" ")
    print(ceil(N / 5))
