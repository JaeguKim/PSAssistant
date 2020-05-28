class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        for i in range(len(favoriteCompanies)):
            isSubset = False
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                set1 = set(favoriteCompanies[i])
                set2 = set(favoriteCompanies[j])
                if set1.issubset(set2):
                    isSubset = True
            if isSubset == False:
                res.append(i)
        return res