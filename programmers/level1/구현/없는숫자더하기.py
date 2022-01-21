def solution(numbers):
    answer = [1,2,3,4,5,6,7,8,9]
    for number in numbers:
        if(number in answer):
            answer.remove(number)
    return sum(answer)
