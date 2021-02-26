def main():
    i = 0
    answer_list =  listgenerator(12)
    point = 0
    while True:
        question = input('please input your question : ')
        question_split = question.split(" ")
        try:
            question_split = [int(i) for i in question_split]
        except :
            print("Error : you have to input 12 numbers from 0-9 or check your white space")
            continue
        if len(question) != 23:
            if any(num >=10 for num in question_split):
                print('Error : you can input only numbers from 0-9')
            print("Error : wrong size of input")
        elif len(question_split) != 12 :
            if any(num >=10 for num in question_split):
                print('Error : you can input only numbers from 0-9')
            print("Error : you have to input 12 numbers from 0-9")
        else:
            show_list(answer_list)
            break
    while i < 5:
        try:
            i += 1
            inp = int(input('please input your number : '))
            if inp >= 10 or inp < 0:
                i -= 1
                print("Error : you can input only number from 0-9")
                continue
            elif inp in answer_list[:]:
                i -= 1
                print("Error : you already used this number")
                continue
        except ValueError:
            i -= 1
            print("Error : you can input only number")
            continue
        count = question_split.count(inp)
        if count == 0:
            answer_list.append(inp)
        else:
            point += count
            for x in range(12):
                if question_split[x] == inp:
                    answer_list[x] =inp
        show_list(answer_list)
    print(point)

def show_list(list):
    for x in list:
        print(x, end = ' ')
    print('')

def listgenerator(n):
    lists = ["_"] * n
    return lists

if __name__ == "__main__":
    main()