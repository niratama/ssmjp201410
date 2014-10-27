from fabric.api import *
from fabric.contrib.files import *
import cuisine
from config import *
from pit import Pit

env.use_ssh_config = True

env.roledefs.update(load_servers('./servers.yaml'))
env.hosts = expand_hosts(env.hosts)

cuisine.select_package('yum')

@task
def create_user():
    with settings(user='root'):
        cuisine.user_ensure('ssmjp')
        append('/etc/sudoers', 'ssmjp ALL=(ALL) ALL')
        cuisine.ssh_authorize('ssmjp', cuisine.file_local_read('~/.ssh/ssmjp.pub'))
        conf = Pit.get('ssmjp-user', { 'require': { 'password': 'Your password' } })
        cuisine.user_passwd('ssmjp', conf['password'])

@task
def install_packages():
    with settings(user='root'):
        cuisine.package_ensure('nginx')

@task
def restart_nginx():
    with settings(user='ssmjp'):
        sudo('service nginx restart')

@task
def install_nginx_conf():
    with settings(user='ssmjp'):
        put('ssmjp.conf', '/etc/nginx/conf.d/', use_sudo=True)
        with cd('/etc/nginx/conf.d'):
            if exists('default.conf'):
                sudo('mv default.conf default.conf.dist')
