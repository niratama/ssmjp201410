import re
import yaml

def expand_hosts(hosts):
    new_hosts = []
    for host in hosts:
        m = re.search('\[(\d+)-(\d+)\]', host)
        if m:
            pre = host[:m.start()]
            post = host[m.end():]
            prec = len(m.group(1))
            for n in range(int(m.group(1)), int(m.group(2)) + 1):
                new_hosts.append(pre + ('%%0%dd' % prec % n) + post)
        else:
            new_hosts.append(host)
    return new_hosts

def load_servers(filename):
    config_yaml = open(filename).read()
    config = yaml.load(config_yaml)
    roledefs = config['roles']
    all_hosts = []
    for role in roledefs:
        all_hosts.extend(roledefs[role])
    roledefs['all'] = all_hosts
    return roledefs
