if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        if j <= 2:
            s *= 6
        else:
            s *= (9-j)
        print(j,s,sum)
        sum += s
    print('sum = %d' % sum)