with open("urls.txt", 'w') as f:
    for i in range(1, 11):
        f.write('https://realpython.com/python-gil/#:~:text=The%20'
                'Python%20Global%20Interpreter%20Lock,in%20CPU%2Dbound%'
                '20and%20multi%2Dthreaded%20code' + '\n')