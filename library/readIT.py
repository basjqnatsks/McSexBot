class readIT:
    def f(self, filename='proxies.txt'):
        
        try:
            userf = open(filename, 'r', encoding="utf-8")
            arr = userf.read().split('\n')

        except:
            userf = open(filename, 'r')
            arr = userf.read().split('\n')
        if arr[len(arr) - 1] == '\n' or arr[len(arr) - 1] == '':
            del arr[-1]
        return arr
    def accounts(self, filename='alts.txt'):
        USERNAMES = []
        PASSWORDS = []
        with open(filename) as f:
            next(f)
            allA = f.readlines()
            for line in allA:
                allA = [x.strip() for x in allA]
        accnt = 0
        for accnt in allA:
            newArr = str(accnt).split(":") #  [myuser, mypass]
            USERNAMES.insert(len(USERNAMES), newArr[0])
            PASSWORDS.insert(len(PASSWORDS), newArr[1])
        return allA