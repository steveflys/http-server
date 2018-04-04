from . import server
import pytest
from multiprocessing import Process


@pytest.fixture(scope='module', autouse=True)
def server_setup():
    instance = server.create_server()

    process = Process(target=instance.serve_forever)

    yield process.start()

    process.terminate()
