
'''
CRAFTED BY - SANJAY T
AIM - TO MAKE A COMMAND-LINE BASED TODO APPLICATION
'''

import sys #SYSTEM LIBRARY FOR COLLECTING COMMAND LINE ARGUMENTS
from datetime import date #DATETIME LIBRARY FOR FETCHING THE ACTIVE DATE FROM THE SYSTEM

# HELP STRING
def help():
    help_string = 'Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics'
    print(help_string)

# DISPLAYING REPORT
def report():
    today = date.today()
    d1 = today.strftime('%Y-%m-%d')
    pending = open('todo.txt','r').readlines()
    done = open('done.txt','r').readlines()

    print(d1 + ' Pending : ' + str(len(pending)) + ' Completed : ' + str(len(done)))

# TODO LISTING
def todo_list():
    pending_file_ip = open('todo.txt','r')
    pending = pending_file_ip.readlines()
    l = len(pending)
    if l == 0:
        print('There are no pending todos!')
        return
    temp = l
    for i in range(0,l):
        print(r'[{}] {}'.format(temp,pending[i].strip('\n')))   
        temp -= 1
    
# ADDING NEW TODOS
def add(content):
    pending_file_ip = open('todo.txt','r')
    pending = pending_file_ip.readlines()
    gen =[]
    gen.append(content + '\n')
    for p in pending:
        gen.append(p)
    pending_file_ip = open('todo.txt','w')
    pending_file_ip.truncate(0)
    for p in gen:
        pending_file_ip.write(p)
    print('Added todo: \"' + content + '\"')
    
# DELETING A TODO
def delete(id):
    pending_file_ip = open('todo.txt','r')
    pending = pending_file_ip.readlines()
    if len(pending) == 0:
        print(r'Error: todo #{} does not exist. Nothing deleted.'.format(id))
        return(1)

    if (int(id) > len(pending)) or int(id)==0:
        print(r'Error: todo #{} does not exist. Nothing deleted.'.format(id))
        return(1)
    else:
        pending.remove(pending[len(pending)-int(id)])
        pending_file_ip = open('todo.txt','w')
        pending_file_ip.truncate(0)
        pending_file_ip.writelines(pending)

# MARKING A TODO AS DONE 
def done(id):
    today = date.today()
    d1 = today.strftime('%Y-%m-%d')
    pending_file_ip = open('todo.txt','r')
    pending = pending_file_ip.readlines()
    if (int(id) > len(pending)) or int(id)==0:
        print(r'Error: todo #{} does not exist.'.format(id))
        return
    else:
        completed_list = open('done.txt','r').readlines()
        completed_file = open('done.txt','w')
        completed_file.truncate(0)
        completed_file.write('x ' + d1 + ' ' +pending[int(id)-1])
        for c in completed_list:
            completed_file.write(c)
        delete(id)
        print(r'Marked todo #{} as done.'.format(id))

# MAIN MODULE
if __name__ == "__main__":

    argument_length = len(sys.argv) #Getting the length of the argument list
    file1, file2 = open('todo.txt','a'), open('done.txt','a') #Initialising the files in append mode for avoiding data loss.

    if argument_length == 1:
        help()           
        
    elif argument_length == 2:
        arg = sys.argv[1]
        if arg == 'help':
            help()
        if arg == 'report':
            report()
        if arg == 'ls':
            todo_list() 
        if arg == 'add':
            print('Error: Missing todo string. Nothing added!')
        if arg == 'del':
            print('Error: Missing NUMBER for deleting todo.')
        if arg == 'done':
            print('Error: Missing NUMBER for marking todo as done.')

    elif argument_length == 3:
        command = sys.argv[1]
        ip = sys.argv[2]
        if command == 'add':
            add(ip)
        if command == 'del':
            if delete(ip) != 1:
                print('Deleted todo #'+ip)
        if command == 'done':
            done(ip)    