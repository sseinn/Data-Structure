1. text file 불러오기

```
with open('test.txt') as f:
    data = [line.strip() for line in f]
print(data)
```

```

2. import 한 text file에는 string과 integer이 섞여 있는데 이는 하나의 list에 담겨있다.

list에 있는 integer과 string을 구분해서 integer은 integer만 string은 string만 담긴 list로 만들고 싶다.

https://stackoverflow.com/questions/14776980/splitting-list-that-contains-strings-and-integers

intData = [x for x in data if isinstance(x, int)]
print(intData)
strData = [x for x in data if isinstance(x, str)]
print(strData)


이렇게 하니

- 실행 결과
```
['567', '0', '3432', '-', '--', 'p', '+', 'p', 'c', '5', '6', '8', '*', 'l', '4', '/', '++', '+', 'p', 'q']
[]
['567', '0', '3432', '-', '--', 'p', '+', 'p', 'c', '5', '6', '8', '*', 'l', '4', '/', '++', '+', 'p', 'q']
```

전부 str로 분류됨



2-2. text file의 데이터는 전부 str. 숫자도 str. str 숫자를 어떻게 int로 바꿀까?

https://stackoverflow.com/questions/67642596/how-to-convert-string-elements-in-a-list-into-integers

```
with open('test.txt') as f:
    data = [line.strip() for line in f]

print(data)

list_with_numers = [int(x) if x.isdigit() else x for x in data]

print(list_with_numers)
```

- 실행 결과
```
['567', '0', '3432', '-', '--', 'p', '+', 'p', 'c', '5', '6', '8', '*', 'l', '4', '/', '++', '+', 'p', 'q']
[567, 0, 3432, '-', '--', 'p', '+', 'p', 'c', 5, 6, 8, '*', 'l', 4, '/', '++', '+', 'p', 'q']
```

str형 int를 int형으로 바꾸는 걸 성공


3. import한 txt file에 str은 연산자와 명령 전부 str로 저장되어 있다.

숫자 리스트 / 연산자 리스트 / 명령 리스트로 나눠야한다.

3-2. 숫자 리스트 / 연산자 + 명령 리스트로 나누었다.

https://stackoverflow.com/questions/14776980/splitting-list-that-contains-strings-and-integers

```
>>> myList = [ 4,'a', 'b', 'c', 1, 'd', 3]
>>> myIntList = [x for x in myList if isinstance(x, int)]
>>> myIntList
[4, 1, 3]
>>> myStrList = [x for x in myList if isinstance(x, str)]
>>> myStrList
['a', 'b', 'c', 'd']
```

위 코드를 사용해 만듦

```
with open('test.txt') as f:
    data = [line.strip() for line in f]

print(data)

list_with_numbers = [int(x) if x.isdigit() else x for x in data]

print(list_with_numbers)
print()

operandList = [x for x in list_with_numbers if isinstance(x, int)]
print(operandList)

strlist = [x for x in list_with_numbers if isinstance(x, str)]
print(strlist)
```

- 실행 결과

```
['567', '0', '3432', '-', '--', 'p', '+', 'p', 'c', '5', '6', '8', '*', 'l', '4', '/', '++', '+', 'p', 'q']
[567, 0, 3432, '-', '--', 'p', '+', 'p', 'c', 5, 6, 8, '*', 'l', 4, '/', '++', '+', 'p', 'q']

[567, 0, 3432, 5, 6, 8, 4]
['-', '--', 'p', '+', 'p', 'c', '*', 'l', '/', '++', '+', 'p', 'q'] 
```


3-3. 연산자 + 문자 리스트를 연산자 리스트 / 명령 리스트로 나누고 싶음

-> 연산자 리스트 / 명령 리스트로 나눌 필요 없음!!



사용하는 명령 : p, q, l, c

4. 연산자 기능 만들기


사용하는 연산자 : +, -, *, /, %, ++, --

