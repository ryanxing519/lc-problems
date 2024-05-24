from collections import Counter

class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:

        word_scores = {}
        word_letters = {}
        for word in words:
            word_score = 0
            for c in word:
                word_score += score[ord(c) - ord("a")]
            word_scores[word] = word_score
            word_letters[word] = Counter(word)

        letter_cnt = Counter(letters)

        def solve(index, cur_letters, points):
            if index == len(words):
                return points

            can_use = True
            for c in word_letters[words[index]]:
                if word_letters[words[index]][c] > cur_letters[c]:
                    can_use = False

            use = 0
            if can_use:
                for c in word_letters[words[index]]:
                    cur_letters[c] -= word_letters[words[index]][c]
                solve(index + 1, cur_letters, points + word_scores[word])
                for c in word_letters[words[index]]:
                    cur_letters[c] += word_letters[words[index]][c]

            skip = solve(index + 1, cur_letters, points)
            return max(use, skip)

        return solve(0, letter_cnt, 0)
