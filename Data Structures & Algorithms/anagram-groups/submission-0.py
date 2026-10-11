class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is the string sorted
        # value is an array of strings 
        hm = {}

        for str in strs:
            key = "".join(sorted(str))

            if key in hm.keys():
                hm[key].append(str)

            else:
                hm[key] = [str]

        

        result = list(hm.values())

        return result

