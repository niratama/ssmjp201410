from fabric.api import *
from fabric.contrib.files import *
from config import *

env.use_ssh_config = True

env.roledefs.update(load_servers('./servers.yaml'))
env.hosts = expand_hosts(env.hosts)

@task
def hostname():
      run('hostname')

@task
def upload_page():
    if not exists('/home/ssmjp/html'):
        run('mkdir /home/ssmjp/html')
    put('sample_html/*', '/home/ssmjp/html/')

@task
def download_logs():
    get('/var/log/nginx/access.log')

@task
def reboot_nginx():
    sudo('service nginx restart')

@task
def test():
    print 'test %s' % env.host
