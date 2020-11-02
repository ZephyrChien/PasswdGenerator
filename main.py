import sys
import getopt
import random

USAGE="main.py -n -l <length>"

def get_args(argv):
    flag_l=random.randint(12,16)
    flag_n=False
    try:
        opts,args = getopt.getopt(argv,"nl:")
    except getopt.GetoptError:
        print(USAGE)
        sys.exit(2)
    else:
        if len(args):
            print(USAGE)
            sys.exit(2)

    for opt,val in opts:
        if opt == "-n":
            flag_n=True
        elif opt == "-l":
            flag_l=int(val)
        else:
            print(USAGE)
            sys.exit(2)
    return flag_n,flag_l

def generate_passwd(flag_n,flag_l):
    c=[]
    if flag_n:
        seed="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        seed="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    for i in range(flag_l):
        c.append(random.choice(seed))
    return "".join(c)

if __name__ == "__main__":
    n,l = get_args(sys.argv[1:])
    passwd = generate_passwd(n,l)
    print(passwd)
