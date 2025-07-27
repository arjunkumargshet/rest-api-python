
import pytest
from config.settings import Settings
from helpers.api_helpers import UserAPI
from helpers.ssh_helpers import SSHClient

@pytest.fixture(scope="session")
def settings():
    return Settings()

@pytest.fixture
def user_api(settings):
    return UserAPI(base_url=settings.base_url)

@pytest.fixture
def ssh_client(settings):
    client = SSHClient(host=settings.ssh_host, user=settings.ssh_user, password=settings.ssh_password)
    yield client
    client.close()
