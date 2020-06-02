dic = [
{
'name':'Krishna',
'maths':67,
'physics':68,
'chemistry':69
},
{
'name':'Arjun',
'maths':70,
'physics':98,
'chemistry':63
},
{
'name':'Malika',
'maths':52,
'physics':56,
'chemistry':60
}]

number_student = 3

# for i in range(number_student):
#     for key in dic[i]:
#         # print(dic[i][key], end=(''))
        
name = 'Malika'

for j in range(number_student):
        if name == dic[j]['name']:
            total = dic[j]['maths'] + dic[j]['physics'] + dic[j]['chemistry']
            result = total/3
            print(format(result, '.2f'))



