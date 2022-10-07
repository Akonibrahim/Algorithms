def solve(matrix):
    length = len(matrix)
    hash_map = {}
    half = length / 2 if length % 2 == 0 else length // 2
    final_set = [0]
    for row in matrix:
        for ele in set(row):
            if ele not in hash_map:
                hash_map[ele] = 1
            else:
                hash_map[ele] += 1
                if hash_map[ele] == half and ele not in final_set:
                    final_set.append(ele)
                elif ele in final_set:
                    final_set.remove(ele)

    print(sum([int(i) for i in final_set]))

matrix = [
    ["2","3","4","5", "2"],
    ["1","-1","2","0", "1"],
    ["-5","-6","1","2", "5"],
    ["-1","8","-8","-4", "-4"],
    ["7","7","7","7", "7"],
]
solve(matrix)

