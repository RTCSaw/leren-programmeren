# def liters(tijd):
#     return tijd // 2

# solution('abc', 'bc') // returns true
# solution('abc', 'd') // returns false

def solution(string, ending):
    return string[-len(ending):] == ending

