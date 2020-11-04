#%% code imports 


#%% main class
class FxOandaCalculator():

    def __init__(self):
        self.pairs = ['EUR_USD', 'USD_JPY', 'GBP_USD', 
                      'USD_CAD', 'USD_CHF', 'AUD_USD', 
                      'NZD_USD']
        self.pair_margin = {'EUR_USD': 3.33, 'USD_JPY': 3.33, 'GBP_USD': 3.33, 
                            'USD_CAD': 3.33, 'USD_CHF': 4, 'AUD_USD': 5, 
                            'NZD_USD': 5}
        self.standard_lot = 100000

    def calculate_pips(self, start: float, end: float, pair: str) -> float:
        '''function to calculate the number of pips between two prices

        parameters
        ----------
        start : float
        end : float
        pair : str

        returns
        -------
        pips : float
            number of pips between the two pirces
        '''
        assert pair in self.pairs, 'unsupported pair'
        if pair == 'USD_JPY':
            pips = (end - start) / 0.01
        else:
            pips = (end - start) / 0.0001
        return round(pips, 1)

    def calculate_price(self, price: float, pips: float, pair: str) -> float:
        '''function to calculate the new price given difference in pips

        parameters
        ----------
        price : float
        pip : float
        pair : str

        returns
        -------
        new_price : float
            price plus the added pips to it
        '''
        assert pair in self.pairs, 'unsupported pair'
        if pair == 'USD_JPY':
            new_price = price + (0.01 * pips)
            rounding = 3
        else:
            new_price = price + (0.0001 * pips)
            rounding = 5
        return round(new_price, rounding)

    def pip_value(self, price: float, units: float, pair: str) -> float:
        '''function to calculate the single pip value based on pair, price and units

        parameters
        ----------
        price : float
        units : float
        pair : str

        returns
        -------
        value : float
            the value in dollars of 1 pip
        '''
        assert pair in self.pairs, 'unsupported pair' 
        assert units/self.standard_lot == round(units/self.standard_lot, 2), 'unexpected lot size'
        delta_unit = 0.0001 if pair != 'USD_JPY' else 0.01
        if pair in ['EUR_USD', 'GBP_USD', 'AUD_USD', 'NZD_USD']:
            value = delta_unit * units
        else:
            value = (delta_unit / price) * units
        return round(value, 3)
    
    def requested_margin(self, price: float, units: float, pair: str) -> float:
        '''function to calculate needed margin based on pair, price and units

        parameters
        ----------
        price : float
        units : float
        pair : str

        returns
        -------
        value : float
            the needed margin for this trade
        '''
        assert pair in self.pairs, 'unsupported pair' 
        assert units/self.standard_lot == round(units/self.standard_lot, 2), 'unexpected lot size'
        margin = self.pair_margin[pair]
        if pair in ['EUR_USD', 'GBP_USD', 'AUD_USD', 'NZD_USD']:
            value = units * price * (margin/100)
        else:
            value = units * (margin/100)
        return round(value, 2)


#%% main section
if __name__ == '__main__':
    pass
