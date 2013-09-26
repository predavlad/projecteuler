import time
import socket
from sys import argv
from multiprocessing import Pool, cpu_count

start_time = time.time()


def check_domain(domain):
    try:
        rez = socket.gethostbyname(domain)
        if rez == domain:
            return {domain: 0}
        else:
            return {domain: 1}
    except:
        return {domain: 0}


def generate_domains(names, tlds):
    domains = []
    for name in names:
        for tld in tlds:
            domains.append(name + '.' + tld)
    return domains


if __name__ == '__main__':

    # domains = list(open("domains.txt").read().split("\n"))
    script, names, tlds = argv
    names = names.split(',')
    tlds = tlds.split(',')
    #
    domains = generate_domains(names, tlds)
    nr_domains = len(domains)

    processes = 40  # cpu_count() * 2

    pool = Pool(processes=processes)
    rez = pool.map(check_domain, domains)
    print rez

print time.time() - start_time, "seconds"
