class Solution:

    def encode(self, strs: List[str]) -> str:
        # add len # in front of each word
        result = ""

        for s in strs:
            result += (str(len(s)) + "#" + s)
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        pointer = 0
        result = []

        while pointer < len(s):
            # pop the len
            lengthPointer = pointer
            while s[lengthPointer] != "#":
                lengthPointer += 1
            length = s[pointer: lengthPointer]
            pointer = lengthPointer + 1

            # run a while loop till the end of the word
            result.append(s[pointer: pointer + int(length)])

            # update pointer
            pointer += int(length)

        return result

























