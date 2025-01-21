def counter(l):
    words={}
    for word in l:
        if word in words:
            words[word]+=1
        else:
            words[word]=1
    for k in words:
        print(f'{k} : {words[k]}')

def main():
    s = input().split()
    counter(s)
main()