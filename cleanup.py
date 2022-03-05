import re
import socket
from tqdm import tqdm
pattern = re.compile(r'^(?:https?:\/\/)?(?:[^@\/\n]+@)?([^:\/?\n]+)')

source = open('targets.txt')
dest = open('new_targets.txt', 'w')
log = open('cleanup.log', 'w')
domains = set()
for line in tqdm(source.readlines()):
    domain_match = pattern.match(line)
    if domain_match:
        domain = domain_match.groups()[0]
        if domain not in domains:
            try:
                socket.gethostbyname(domain)
                print(line, end='', file=dest)
                domains.add(domain)
            except:
                print(f'{domain} - couldn\'t resolve', file=log)
        else:
            print(f'{domain} - duplicate', file=log)
source.close()
dest.close()
log.close()