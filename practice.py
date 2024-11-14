import math
#Calculate area of a circle using function
def area_circle(radiuos):
    #return math.pi*radiuos**2
    return math.pi*radiuos*radiuos
#print('Area of The Circle is :',f'{area_circle(5)}:.2f')
print(f'Area of the Circle is: {round(area_circle(5), 2)}')
print(f'Area of the Circle is: {area_circle(5):.2f}')

#Calculate Pwer using function
def power(base,exp):
    return base**exp

req_power=power(3,5)
print(f'3 power 5 is :{power(3,5)}')
print(f'3 power 5 is :{req_power}')

#Conver Celcious to Farenhiet using function
def celciuos_to_farenhiet(celcious):
    return (celcious*9/5)+32
print(f'30 degree celcious equvalent farenhiet is :, {celciuos_to_farenhiet(36)}')
print('30 degree celcious equvalent farenhiet is :',celciuos_to_farenhiet(36))

#Count Vowels in a given string using function
def count_vowels(s):
    count = 0
    for i in s:
        if i in 'aeiou':
            count+=1
    return count
input_string=input('Enter you Desired String :')
print(f'Total Vowels in {input_string} are :{count_vowels(input_string)}')

#Determine Even or Odd using Function

def even_odd(n):
    if n%2==0:
        print('The Number is Even')
    else:
        print('The Number is Odd')
number=int(input('Enter your Desire Number: '))
print(even_odd(number))


