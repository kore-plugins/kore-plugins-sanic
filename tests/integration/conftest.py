import pytest

from kore import config_factory, container_factory


@pytest.fixture(scope='session')
def sanic_config():
    return {
        'instance_path': '/',
        'root_path': './',
        'DEBUG': True,
        'SECRET_KEY': 'verysecretkey',
    }


@pytest.fixture(scope='session')
def config(sanic_config):
    return config_factory.create('dict', **{'sanic': sanic_config})


@pytest.fixture
def container(config):
    initial = {
        'config': config,
    }
    return container_factory.create(**initial)


@pytest.fixture
def application(container):
    return container('kore.components.sanic.application')
