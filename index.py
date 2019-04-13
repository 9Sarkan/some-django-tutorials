def reverseNumber(number):
    n = 0
    mod = number % 10
    modd = number // 10
    n = mod * 10 + modd


def is_primary(number):
    k = 0
    if number == 1:
        return False
    elif number > 1:
        for i in range(2, number//2):
            if number % i == 0:
                k += 1
        if k > 2:
            return False
        return True


def Q310NUmber():
    lst = []
    for i in range(10):
        lst.append(int(input('number %s : ' % i)))

    maxx = lst[0]
    minn = lst[0]
    total = 0
    for i in lst:
        if i > max:
            maxx = i
        if i < min:
            minn = i
        total += i
    print('Max : {0}\n\rMin : {1}\n\rTotal : {3}\n\rAverage : {4}'.format(maxx, minn, total, total / 10))


def Q4Zeros(number):
    if number >= 100000:
        return 0
    count = 0
    while number > 0:
        count += (number % 10 > 0 ? 0 : 1)
        number /= 10
    return count
