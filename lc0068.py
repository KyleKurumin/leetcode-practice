import math
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        temp = []
        total = 0
        while words:
            first_length = len(words[0])

            addition = first_length + 1 if total > 0 else first_length

            if total + addition <= maxWidth:
                w = words.pop(0)
                temp.append(w)
                total += addition
            else:
                alpha_length = sum(len(w) for w in temp)
                space_nums = maxWidth - alpha_length
                if len(temp) >= 2:
                    spaces = [math.floor(space_nums / (len(temp) - 1))] * len(temp)
                    spaces[0] = 0
                    total_space = sum(spaces)
                    i = 1
                    while total_space < space_nums:
                        spaces[i] += 1
                        total_space += 1
                        i += 1
                    o = ''
                    for i in range(len(spaces)):
                        o += ' ' * spaces[i] + temp[i]
                else:
                    o = temp[0] + ' ' * (maxWidth - len(temp[0]))

                output.append(o)
                temp = []
                total = 0

        if len(temp) > 0:
            last_line = ' '.join(temp)
            remains = maxWidth - len(last_line)
            last_line += ' ' * remains
            output.append(last_line)
        return output