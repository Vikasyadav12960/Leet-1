class Solution:
    def toHex(self, num: int) -> str:
        
        if num == 0:
            return "0"

        hexa_dcml = "0123456789abcdef"

        if num < 0:
            num = num & 0xffffffff

        answer = ""

        while num > 0:
            digit = num&15

            answer = hexa_dcml[digit] + answer

            num = num >> 4


        return answer




          
