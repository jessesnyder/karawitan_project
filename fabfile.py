from fabric.api import local


def prepare_deployment():
    local('python manage.py test')
    local('git add -p && git commit')
