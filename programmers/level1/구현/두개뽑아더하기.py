def solution(numbers):
    answer = set()
    for index, i in enumerate(numbers):
        for j in numbers[index+1:]:
            answer.add(i+j)
    return sorted(list(answer))
