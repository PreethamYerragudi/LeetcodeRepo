# Problem 811: Subdomain Visit Count
# Difficulty: Medium
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)
        for cpdomain in cpdomains:
            seperated = cpdomain.split(" ")
            num, domain = int(seperated[0]), seperated[1]
            i = domain.find('.')
            while i != -1:
                count[domain] += num
                domain = domain[i+1:]
                i = domain.rfind('.')
            count[domain] += num
        ans = []
        for domain, value in count.items():
            ans.append(str(value) + " " + domain)
        return ans