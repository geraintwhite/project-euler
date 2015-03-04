import sys

numbers = {
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine',
  '10': 'ten',
  '11': 'eleven',
  '12': 'twelve',
  '13': 'thirteen',
  '15': 'fifteen',
  '18': 'eighteen',
  '20': 'twenty',
  '30': 'thirty',
  '40': 'forty',
  '50': 'fifty',
  '80': 'eighty'
}

def number_word (n):
  n = str(n)
  l = len(n)

  word = ''
  if l > 3:
    word += numbers[n[-4]] + ' thousand '
    word += 'and ' if (n[-2] in numbers or n[-1] in numbers) and not n[-3] in numbers else ''
  if l > 2 and n[-3] in numbers:
    word += numbers[n[-3]] + ' hundred '
    word += 'and ' if n[-2] in numbers or n[-1] in numbers else ''
  if l > 1 and n[-2] in numbers:
    if n[-2] == '1':
      word += numbers[n[-2:]] if n[-2:] in numbers else numbers[n[-1]] + 'teen'
    else:
      word += numbers[n[-2]+'0']+' ' if n[-2]+'0' in numbers else numbers[n[-2]] + 'ty '
    if n[-1] == '0' or n[-2] == '1':
      return word
  word += numbers[n[-1]] if n[-1] in numbers else ''
  return word

# for i in range(1,1001):
#   print(number_word(i))
#print(sum(len(number_word(i).replace(' ', '')) for i in range(1,1001)))

#for i in range(1,10000):
#    print('{} = {}'.format(i, number_word(i)))

i=sys.argv[1]
print('{} = {}'.format(i, number_word(i)))
