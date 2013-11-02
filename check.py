from __future__ import with_statement  # Required in 2.5
import time
import socket
import json
from sys import argv
from multiprocessing import Pool, cpu_count
import signal
from contextlib import contextmanager


class TimeoutException(Exception):
    pass


start_time = time.time()


def check_domain(domain):
    if not domain:
        return [domain, 0]
    check = 0
    try:
        rez = socket.gethostbyname(domain)
        if rez == domain:
            check = 0
        else:
            check = 1
    except:
        check = 0
    return [domain, check, domain.split('.')[0], domain.split('.')[1]]


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException, "Timed out!"

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def generate_domains(names, tlds):
    domains = []
    for name in names:
        for tld in tlds:
            domains.append(name + tld)
    return domains


def time_limit_check_domain(domain, seconds=0):
    try:
        with time_limit(seconds):
            return check_domain(domain)
    except TimeoutException:
        return [domain, 0, domain.split('.')[0], domain.split('.')[1]]


if __name__ == '__main__':
    # domains = list(open("domains.txt").read().split("\n"))
    script, names, tlds = argv
    names = names.split(',')
    tlds = tlds.split(',')

    domains = generate_domains(names, tlds)

    domains = [domain for domain in domains if len(domain) > 3]

    nr_domains = len(domains)

    processes = 40  # cpu_count() * 2

    pool = Pool(processes=processes)
    rez = pool.map(time_limit_check_domain, domains)
    print json.dumps(list(rez))

# print time.time() - start_time, "seconds"
