# 4406. 모음이 보이지 않는 사람
"""
불의의 교통사고를 당한 당신은 얼마 후 자신의 인식 속에서 모음이라는 것이 사라진 것을 알게 되었다.

알파벳 소문자 만으로 이루어진 단어를 당신은 어떤 식으로 보게 될까?

알파벳에서 모음은 ‘a’, ‘e’, ‘i’, ‘o’, ‘u’의 다섯가지로 예를 들어 “congratulation”이라는 단어를 당신이 보게 되면 “cngrtltn”으로 인식하게 될 것이다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 길이가 50이하이고 알파벳 소문자만으로 이루어진 단어가 주어진다. 이 단어에 모음이 아닌 문자(자음)이 적어도 하나는 들어있다는 것이 보장된다.

[출력]

테스트 케이스 T에 대한 결과는 “#T ”을 찍고,  각 테스트 케이스마다 주어진 단어를 당신이 어떻게 인식하는지를 출력한다.
"""
voyelles = 'aeiou'

T = int(input())
for t in range(1, T+1):
    word = input()
    remove_v = word
    for v in voyelles:
        remove_v = remove_v.replace(v, "", -1)
    print(f"#{t} {remove_v}")