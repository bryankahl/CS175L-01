#CS175L
#Bryan Kahl
#03/06/2023

def main():

    try:
        
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

    except IOError:
        print('Please make sure the file exists')

    except ValueError:
        print('Data in file might contain a string or a non-integer chracter')
    
main()



