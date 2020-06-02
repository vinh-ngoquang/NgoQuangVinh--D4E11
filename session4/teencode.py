dic = {'hc': 'hoc',
'ng': 'ngoc',
'pt': 'phat trien',
'ns': 'noi',
'lm': 'lam',
'stt': 'so thu tu'
}
while True:

    code = input('\nEnter your teencode: ')
    if code in dic:  #kiem tra gia tri co trong dic hay k
        print('It mean: ', dic[code])
    else:
        print('Not found, do you want to contribute this work:')
        ans = input('Y/N: ')
        if ans == 'yes':
            dic[code] =  input('Update: ')
            for key in dic:      #chi in value
                print(dic[key], end='\t')
        else: 
            print('Stop')
            break
