#Complexity
#    time: O(N * S + N logN) ~ O(N logN)
#    space: O(N * S) ~ O(N)
#    where N = # votes and S = length of a word in the votes array
#    max(S) is 26 chars so it would be constant O(1)

from typing import List

def rankTeam(votes:List[str])-> str:
    out={}
    for vote in votes:
        for key, value in enumerate(vote):
            if value not in out:
                out[value]=[0]*len(vote)
            out[value][key]+=1
    ranked=''.join(sorted(out.keys(), key=lambda x:out[x], reverse=True))
    #return ranked[:3]
    return ranked, out
#print(rankTeam(votes= ["WXYZ","XYZW"]))
votes = [
    ["Beta", "Alpha", "Gamma"],
    ["Beta", "Alpha", "Gamma"],
    ["Gamma", "Alpha", "Beta"],
    ["Alpha", "Gamma", "Beta"],
    ["Alpha", "Gamma", "Beta"]
]

votes1=["ABC","ACB","ABC","ACB","ACB"]

print(rankTeam(votes = votes))
