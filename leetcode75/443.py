from collections import defaultdict

class Solution(object):

    # Beats 8% (runtime)
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        cnt = defaultdict(int)
        prev = chars[0]
        cnt[prev] += 1
        idx = 1

        while idx < len(chars):
            
            cur = chars[idx]
            
            if cur == prev:
                cnt[cur] += 1
                chars.pop(idx)

            else:

                if cnt[prev] > 1:

                    cnt_letters = list(str(cnt[prev]))[::-1]

                    for let in cnt_letters: 
                        chars.insert(idx, let)

                    idx += (len(cnt_letters)+1)

                else :
                    idx += 1

                cnt[cur] += 1
                cnt[prev] = 0
                prev = cur

        last = chars[-1]
        last_cnt = cnt[last]

        if last_cnt > 1:

            cnt_letters = list(str(last_cnt))

            for let in cnt_letters: 
                chars.append(let)

        return len(chars)
                