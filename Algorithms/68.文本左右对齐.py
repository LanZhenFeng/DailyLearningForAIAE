#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#


# @lc code=start
class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 模拟
        # 时间复杂度 O(m)，其中 m 是数组 words 中所有字符串的长度之和。
        # 空间复杂度 O(m)
        pre_lens = [0]
        for word in words:
            pre_lens.append(pre_lens[-1] + len(word) + 1)
        print(pre_lens)
        ans = []
        left = 0
        for i in range(1, len(pre_lens)):
            if pre_lens[i] - pre_lens[left] - 1 > maxWidth:
                cur_len = pre_lens[i - 1] - pre_lens[left] - 1
                rest_len = maxWidth - cur_len
                cur_words = words[left:i - 1]
                len_words = i - 1 - left
                cur_str = cur_words[0]

                if len_words >= 2:
                    space_list = [1] * (len_words - 1)
                    for j in range(rest_len):
                        space_list[j % len(space_list)] += 1
                    for k in range(1, len_words):
                        cur_str = (" " * space_list[k - 1]).join(
                            [cur_str, cur_words[k]])
                else:
                    cur_str += (" " * rest_len)
                ans.append(cur_str)
                left = i - 1
        cur_str = " ".join(words[left:])
        rest_len = maxWidth - len(cur_str)
        cur_str += (" " * rest_len)
        ans.append(cur_str)
        return ans

        # TODO 优化


# @lc code=end
