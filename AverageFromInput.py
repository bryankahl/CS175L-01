#CS175L
#Bryan Kahl
#03/02/2023

def main():
    numberfile = open('numbers.txt', 'r')

    content = numberfile.readlines()



    total = 0



    n = 0
    for number in content:
        n += 1
        print("I read in", n, " number(s) Current number is: ",str(n), end= '' )
        print(' number(s) Current number is:' , float(number), end='')
        total += float(number)
        print(' Total is: ',total)

    average = total/n
    print("Average is: ",average)

main()




