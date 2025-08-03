# initialze data to be stored in files, pickles, shelves.

#records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 3000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 32, 'pay': 1500, 'job': 'camgirl'}
tom = {'name': 'Tom',       'age': 56, 'pay': 0, 'job': None}

#database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=> ', db[key])
        