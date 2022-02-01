# DynamicProgramming
DP assignment for ECE414 class

# Problem
The goal is to find the optimal policy for a late student arriving at class as shown in the
diagram below. Since the student arrives late in class he must choose one of the seats in the
right most column (which are all empty). The goal of the student is to sit as far up as front
as possible while reducing the probability of getting sick.

1. There are N empty seats at the far right of the class.
2. The student enters the class from the back of the room.
3. When the student walks by the spot they can choose to either take the seat or move
on to the next seat (the student cannot walk backwards).
4. When at a row the student can observe the seat next to the empty one and asses if it
is empty, has a student with a mask, or has a non masked student.
5. When making a decision the student is not able to see the situation in the next rows
(cannot tell if anyone is sitting in the next row).
6. The student would like to sit as far up as front as possible.
7. If the student is not able to find a spot he will need to exit the class from the front
door which will be very embarrassing.
1


You are tasked with writing a computer program which will guide the student’s behavior.
More specifically you are asked to model the problem as an MDP, and find the optimal policy
using DP. You can make the following assumptions:

1. There is a probability of a student being seated at each neighboring seat ptaken, and
given that a student is seated, that the student is masked pmask.
2. Depending on who the student sits next to (no one, masked, non-masked) there is a
different probability they would get sick (psick−empty, psick−masked, psick−nonmasked respec-
tively) .
3. Your learning ability is linear in the row you decide to sit at. That is you can measure
it by Rlearn ×(N −row), where row is the row you decide to sit at.
4. However, getting sick is bad and should be rewarded negatively with Rsick.
5. If leaving the classroom without sitting you will not get sick, but that should be
rewarded negatively ( Rexit) as well since there is no learning.
