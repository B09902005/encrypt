def make_table(file):
    myfile = open(file, encoding = 'utf-8')
    transform_table = {}
    while (True):
        line = myfile.readline().split(',')
        if (line[0] != '') and (line[0][0] in {'0','1','2','3','4','5','6','7','8','9'}):
            transform_table[int(line[0])] = line[1][0]
            transform_table[line[1][0]] = int(line[0])
            if (int(line[0]) == 9999):
                break
    return transform_table

def message_to_num(message, table):
    ans = 0
    for i in range (len(message)):
        ans *= 10000
        ans += table[message[i]]
    return ans

def answer_to_num(answer):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
    ans = 0
    for i in range (len(answer)):
        ans *= 26
        temp = 0
        for j in range (26):
            if (answer[i] == alphabet[j]):
                temp = j
        ans += temp
    return ans
        
transform_table = make_table("code.txt")
message = input("請輸入你想傳的訊息？")
answer = input("請輸入今天的semantle答案？")
num_message = message_to_num(message, transform_table)
num_answer = answer_to_num(answer)
print("以下是加密過後的訊息：")
print(num_message * num_answer)
