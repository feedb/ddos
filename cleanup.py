import re
import socket
from tqdm import tqdm
pattern = re.compile(r'^(?:https?:\/\/)?(?:[^@\/\n]+@)?([^:\/?\n]+)')

source = open('targets.txt')
dest = open('new_targets.txt', 'w')
for line in tqdm(source.readlines()):
    domain_match = pattern.match(line)
    if domain_match:
        domain = domain_match.groups()[0]
        try:
            socket.gethostbyname(domain)
            print(line, end='', file=dest)
        except:
            pass
source.close()
dest.close()