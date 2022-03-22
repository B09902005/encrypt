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

def num_to_message(num_message, table):
    ans = ""
    while (num_message != 0):
        ans = table[num_message%10000] + ans
        num_message = num_message // 10000
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
num_message = int(input("請輸入你想解密的訊息？"))
answer = input("請輸入今天的semantle答案？")
num_answer = answer_to_num(answer)
if (num_message % num_answer != 0):
    print("訊息或答案錯誤")
else:
    num_real_message = num_message // num_answer
    real_message = num_to_message(num_real_message, transform_table)
    print("以下是解密過後的訊息：")
    print(real_message)
