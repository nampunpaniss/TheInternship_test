def getAcronym(sentence):
    split_s = sentence.split(' ')
    acr = []
    for word in split_s:
        if word[0].isupper():
            acr.append(word[0])
    return ''.join(acr)

def sortData(data):
    data.sort()
    data.sort(key=len, reverse=True)
    return data

def main():
    while True:
        try: 
            number_inp = int(input('please enter your number : '))
            break
        except ValueError :
            print("please input only integer")
            continue
    acr_list = []
    for i in range(number_inp):
        sentence_inp = input('please enter your word : ')
        sentence_inp = sentence_inp.strip()
        acr_list.append(getAcronym(sentence_inp))
    sorted_acr_list = sortData(acr_list)
    for word in sorted_acr_list:
        print(word)

if __name__ == "__main__":
    main()