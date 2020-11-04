#%% code imports
import pytest
from ..function_app.services.forex import utils as u

#%% define fixtures
@pytest.fixture
def dummy_fixture():
    return [1,2,3]

@pytest.fixture
def oanda_calc():
    calc = u.FxOandaCalculator()
    return calc