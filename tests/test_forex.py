#%% code imports
import pytest
from ..function_app.services.forex import utils as u

#%% define tests
class TestFxOandaCalculator():

    @pytest.mark.parametrize('start, end, pair, output',
                            [(1, 1, 'random_pair', 1),
                             (1.4530, 1.4550, 'USD_CHF', 20),
                             (1.4550, 1.4525, 'EUR_USD', -25)])
    def test_calculate_pips(self, oanda_calc, start, end, pair, output):
        if pair == 'random_pair':
            with pytest.raises(AssertionError):
                _ = oanda_calc.calculate_pips(start, end, pair)
        else:
            result = oanda_calc.calculate_pips(start, end, pair)
            assert result == output
    
    @pytest.mark.parametrize('price, pips, pair, output',
                            [(1, 1, 'random_pair', 1),
                             (1.4530, 20, 'USD_CHF', 1.4550)])
    def test_calculate_price(self, oanda_calc, price, pips, pair, output):
        if pair == 'random_pair':
            with pytest.raises(AssertionError):
                _ = oanda_calc.calculate_price(price, pips, pair)
        else:
            result = oanda_calc.calculate_price(price, pips, pair)
            assert result == output
    
    @pytest.mark.parametrize('price, units, pair, output',
                            [(1, 10000, 'random_pair', 1),
                             (1, 1, 'EUR_USD', 1),
                             (1.4550, 100000, 'USD_CHF', 6.873),
                             (1.5467, 100000, 'EUR_USD', 10),])
    def test_pip_value(self, oanda_calc, price, units, pair, output):
        if (pair == 'random_pair' and units == 10000) or \
           (pair == 'EUR_USD' and units == 1):
            with pytest.raises(AssertionError):
                _ = oanda_calc.pip_value(price, units, pair)
        else:
            result = oanda_calc.pip_value(price, units, pair)
            assert result == output
    
    @pytest.mark.parametrize('price, units, pair, output',
                            [(1, 1, 'random_pair', 1),
                             (0.91263, 1000, 'USD_CHF', 40),
                             (0.71593, 1000, 'AUD_USD', 35.8)])
    def test_requested_margin(self, oanda_calc, price, units, pair, output):
        if pair == 'random_pair':
            with pytest.raises(AssertionError):
                _ = oanda_calc.requested_margin(price, units, pair)
        else:
            result = oanda_calc.requested_margin(price, units, pair)
            assert result == output
    
