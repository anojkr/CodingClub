

'''
    //BuildInDataType in python
    1. Number [Int, Float, Long, Double]
    2. Char
    3. String
    4. List
    5. Dict
    6. Set
    7. Tuple
    8. Other (Boolean, None)


    //Operation Permitted on BuildInDataType

    1. Number : +, -, *, Pow(**),
        import math
        math.pi
        math.sqrt(9) => 3

    2. String
        Note: String is immutable in python
        str = "ANOJKUMAR"
        print(str[0])  -> A
        print(str[-1]) -> R
        Slicing -> str[1:3] -> "NO"
        Repetition ->  ARE*3 -> AREAREARE
        S.replace('NO', 'xyz) -> AxyzJKUMAR
        S.split("abc,xyz,mvp") -> [abc, xyz , mvp]
        S.upper("anoj") -> ANOJ
        S.lower("ANOJ") -> anoj
        Formatting
            print('User age={} and  Name={}'.format(10, "Anoj"))


    3. List

        L  =  [1, 'C', "Spam" , 3.14]
        Number of item in  list: len(L) -> 3
        Slicing: L[0:-1] ->  [1, 'C', "Spam"]
        Concat:  L + ["12A", "GB12", 544] -> [1, 'C', "Spam" , 3.14, "12A", "GB12", 544]
        Add item to list to end: L.append()
        Delete item from list from index: L.pop(2)
        Sort list: L.sort()
        Reverse Sort: L.reverse()
        Nesting: [[1,2,3], [4,5,6],[7,8,9]] -> M[1][2]-> 6

    4. Dict
        D.values() -> ['HarrPotter', 'Cricket', 'Winner']
        D.items() -> [('Book', 'HarrPotter'), ('Sport', 'Cricket'), (1, 'Winner')]
        D.keys() -> ['Book', 'Sport', 1]
        D.get(1) -> Winner
        D.get(2) -> None

    5. Set
        X = set('spam') -> {'a', 'p', 's', 'm'}
        Y = {'h', 'a', 'm'} -> {'a', 'h', 'm'}
        X & Y  -> {'a', 'm'}
        X | Y  -> {'a', 'p', 's', 'h', 'm'}
        X – Y -> {'p', 's'}
        {x ** 2 for x in [1, 2, 3, 4]} {16, 1, 4, 9}
'''

