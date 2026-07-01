class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #step 1 ingest the dict with the key and its sorted value 
        #fir club the similar value pair to a list and thats it right ?
        #
        group = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in group:
                group[key]= [word]
            else:
                group[key].append(word)
        ans = []
        for value in group.values():
            ans.append(value)


        return ans