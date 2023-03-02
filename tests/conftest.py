import pytest
from dotenv import load_dotenv

from tests.test_demo_web_shop import SHOP_URL
from tests.utils.base_session import BaseSession

load_dotenv()


@pytest.fixture(scope="session")
def demoshop():
    return BaseSession(SHOP_URL)



