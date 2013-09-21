import time

start_time = time.time()


############# 2.4 seconds
def is_pandigital(nr, n):
    nr = str(nr)
    beg = nr[0:n]
    end = nr[-n:]
    for i in map(str, range(1, n + 1)):
        if i not in beg or i not in end:
            return False
    return True


######### 4.2
# def is_pandigital(nr, n):
#     nr = str(nr)
#     beg = set(nr[0:n])
#     end = set(nr[-n:])
#     return beg == end and beg == set(map(str, range(1, n + 1)))


##### 3 seconds
# def is_pandigital(nr, n):
#     digits = ''.join(map(str, range(1, n + 1)))
#     nr = str(nr)
#     for i in digits:
#         if str(i) not in nr[0:n]:
#             return False
#         if str(i) not in nr[-n:]:
#             return False
#     return True

###### 6 seconds
# def adapt_nr(nr):
#     nr = [int(i) for i in list(nr)]
#     nr.sort()
#     return nr
#
#
# def is_pandigital(nr, n):
#     nr = str(nr)
#     if len(nr) < n:
#         return False
#     chk = list(range(1, n + 1))
#     if adapt_nr(nr[0:n]) != chk: return False
#     if adapt_nr(nr[-n:]) != chk: return False
#     return True

########## 10 seconds
# def adapt_nr(nr):
#     nr = [int(i) for i in list(nr)]
#     nr.sort()
#     return ''.join([str(i) for i in nr])
#
#
# def is_pandigital(nr, n):
#     nr = str(nr);
#     if len(nr) < n: return False
#     chk = ''.join(str(i) for i in list(range(1, n + 1)))
#     if adapt_nr(nr[0:n]) != chk: return False
#     if adapt_nr(nr[-n:]) != chk: return False
#     return True

assert is_pandigital(1423, 4)
assert not is_pandigital(1423, 5)
assert is_pandigital(14235554123, 4)
assert not is_pandigital(14235552222, 4)  # !important
assert not is_pandigital(1444, 4)
assert is_pandigital(123564987, 9)
assert not is_pandigital(9999912399999, 3)

# this loop is strictly for benchmarking is_pandigital
pandigitals = [i for i in range(100000, 999999) if is_pandigital(i, 6)]

print 'Found: ', len(pandigitals), ' numbers'
print pandigitals

print time.time() - start_time, "seconds"
