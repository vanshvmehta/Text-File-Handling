"""
1. To create a file
2. Append records
3. Display the file and the number of records
4. Search for an employee on code
5. Details of employee having basic sal > 70000
6. Delete an employee on code
7. Update some information
8. Display the file and the number of characters
9. Display the file and the number of words
10. Display the file and the number of lines
11. Count number of uppercase, lowercase, digits and special characters
"""

def create():
    with open('employee.txt', 'x') as f:
        rec1 = '1011,AMIT ARORA,77000,12\n'
        rec2 = '1013,MONA BHARGAV,75000,15\n'
        rec3 = '1014,KOMAL GUPTA,73000,23\n'
        f.writelines([rec1, rec2, rec3])
    print('Records appended')
    print()


def append():
    with open('employee.txt', 'x') as f:
        rec1 = '1011,AMIT ARORA,77000,12\n'
        rec2 = '1013,MONA BHARGAV,75000,15\n'
        rec3 = '1014,KOMAL GUPTA,73000,23\n'
        f.writelines([rec1, rec2, rec3])
    print('Records appended')
    print()


def display():
    with open('employee.txt') as f:
        data = f.read()
        line = data.count('\n') - 1
        print()
        print(data)
        print(line, ' records')
        print()


def search():
    code = input('Enter the code: ')
    with open('employee.txt') as f:
        data = f.readlines()
        for i in data:
            if i[:4] == code:
                print(i)
                break
        else:
            print('No such employee')


def basic():
    with open('employee.txt') as f:
        f.readline()
        data = f.readlines()
        for i in data:
            rec = i.split(',')
            if int(rec[2]) > 70000:
                print(i, end='')
    print()


def delete():
    code = input('Enter the code: ')
    with open('employee.txt') as f:
        data = f.readlines()
        for i in data:
            if i[:4] == code:
                del data[data.index(i)]
                break
        else:
            print('No such employee')

    with open('employee.txt', 'w') as f:
        f.writelines(data)
    print('record deleted')
    print()


def update():
    code = input('Enter the code: ')
    with open('employee.txt') as f:
        data = f.readlines()
        for i in data:
            rec = i.split(',')
            if rec[0] == code:
                rec[2] = str(int(rec[2]) * 1.1)
                data[data.index(i)] = ','.join(rec)
                break
        else:
            print('No such employee')

    with open('employee.txt', 'w') as f:
        f.writelines(data)
    print('record updated')
    print()


def chars():
    with open('soccer.txt') as f:
        data = f.read()
        print(data)
        print(len(data), 'characters\n')


def words():
    with open('employee.txt') as f:
        data = f.read()
        print(data)
        word = data.count(' ') + data.count('\n')
        print(word, 'words\n')


def lines():
    with open('employee.txt') as f:
        data = f.read()
        print(data)
        line = data.count('\n')
        print(line, 'lines\n')


def count():
    with open('employee.txt') as f:
        lo = up = di = sp = 0
        data = f.read()
        for i in data:
            if 'a' < i < 'z':
                lo += 1
            elif 'A' < i < 'Z':
                up += 1
            elif '0' < i < '9':
                di += 1
            else:
                sp += 1
    print('No of uppercase, lowercase, digits and special characters are', up, lo, di, sp, 'resp\n', sep=', ')


print('''
1. To create a file
2. Append records
3. Display the file and the number of records
4. Search for an employee on code
5. Details of employee having basic sal > 70000
6. Delete an employee on code
7. Update some information
8. Display the file and the number of characters
9. Display the file and the number of words
10. Display the file and the number of lines
11. Count number of uppercase, lowercase, digits and special characters
12. Exit the menu
''')
opt = 0
while opt != 12:
    opt = int(input('Enter your option: '))
    if opt == 1:
        create()
    elif opt == 2:
        append()
    elif opt == 3:
        display()
    elif opt == 4:
        search()
    elif opt == 5:
        basic()
    elif opt == 6:
        delete()
    elif opt == 7:
        update()
    elif opt == 8:
        chars()
    elif opt == 9:
        words()
    elif opt == 10:
        lines()
    elif opt == 11:
        count()
