class Solution:

    def encode(self, strs: List[str]) -> str:
        # questions:
        # what is the range of strs length
            # 0 to 99
        # can the string element be length of 0?
        # can the string contains numbers, special char?
            # yes

        # idea:
        # for each str element, s, add len(s) in front of it
        # and add it to the result

        result = ""

        for s in strs:
            length = str(len(s))
            newString = length +  "#"+ s 
            result += newString

        print(result)

        return result


    def decode(self, s: str) -> List[str]:

        # idea:
        # use the first index as the starting point
        # and skip by the value of first index

        # use a index and a while statement
        # like... while index < len(s)

        # how to convert char to string
            # cast it

        # 10#neetcoders4#code
        #  1  4

        # to get neet s[1:5]
        index = 0
        result = []
        while index < len(s):
            whereHashIsFound = index
            while s[whereHashIsFound] != "#":
                whereHashIsFound += 1
            skipBy = int(s[index:whereHashIsFound])
            index += whereHashIsFound - index + 1
            newString = s[index: index + skipBy]
            index += skipBy
            result.append(newString)

        return result
        



        






