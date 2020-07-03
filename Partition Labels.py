def partitionLabels(S):
    # last dictionary to store last indexof character in the dictionary
    last = {}

    for index, char in enumerate(S):
        last[char] = index

    start = 0
    end = 0

    answer = []

    for index, char in enumerate(S):
        end = max(end, last[char])

        if (index == end):
            answer.append(index - start + 1)
            start = index + 1

    return answer

S = "ababcbacadefegdehijhklij"

print(partitionLabels(S))