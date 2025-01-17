#You are given two integer arrays persons and times. 
# In an election, the ith vote was cast for persons[i] at time times[i].

#For each query at a time t, 
# find the person that was leading the election at time t. 
# Votes cast at time t will count towards our query. 
# In the case of a tie, the most recent vote (among tied candidates) wins.

#Implement the TopVotedCandidate class:

#TopVotedCandidate(int[] persons, int[] times)
#  Initializes the object with the persons and times arrays.
#int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.

#Time Complexity:
# Initialization: O(n)
#Q  Queries: O(m log n), where m is the number of queries.
# Space Complexity: O(n)

from collections import defaultdict
import bisect

class TopVotedCandidate:
    def __init__(self, persons, times) -> None:
        self.persons=persons
        self.times=times
        self.leaders=[]
        votes=defaultdict(int)
        votes1={}
        leader=-1

        for i in range(len(self.persons)):
            votes[self.persons[i]] +=1
            if self.persons[i] not in votes1:
                votes1[self.persons[i]]=1
            else:
                votes1[self.persons[i]] +=1
            if leader==-1 or votes[self.persons[i]]>=votes[leader]:
                leader=self.persons[i]
                #print(leader)
            self.leaders.append(leader)
        
        #print(votes)
        #print(votes1)
        #print(self.leaders)

    def q1 (self,t:int):
        return self.leaders[bisect.bisect_right(self.times,t)-1]
    def q(self, t:int):
        left, right=0, len(self.times)-1
        while left < right:
            mid= (left+right+1)//2
            if self.times[mid]<=t:
                left=mid
            else:
                right =mid -1
        return self.leaders[left]


tvc=TopVotedCandidate(persons=[0, 1, 1, 0, 0, 1, 0],times= [0, 5, 10, 15, 20, 25, 30])
print(tvc.q(3))
print(tvc.q(12))
print(tvc.q(25))
print(tvc.q(15))
print(tvc.q(24))
print(tvc.q(8))