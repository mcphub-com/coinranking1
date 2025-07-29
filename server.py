import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Coinranking/api/coinranking1'

mcp = FastMCP('coinranking1')

@mcp.tool()
def get_coins(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, in which all the prices are calculated. This includes the price, the change and the sparkline. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
              timePeriod: Annotated[Union[str, None], Field(description='By setting the timeperiod the change percentage and sparkline in the response will be calculated accordingly Default value: 24h Allowed values: 3h 24h 7d 30d 3m 1y 3y 5y')] = None,
              symbols: Annotated[Union[list, None], Field(description='Symbols to filter the list on. Array parameters should be suffixed with brackets. Example: ?symbols[]=BTC&symbols[]=ETH.')] = None,
              uuids: Annotated[Union[list, None], Field(description='UUIDs to filter the list on. If you know the UUIDs of the coins you want to fetch, you can use this filter to get the specific coins. Array parameters should be suffixed with brackets. Example: ?uuids[]=razxDUgYGNAdQ&uuids[]=Qwsogvtv82FCd.')] = None,
              tiers: Annotated[Union[list, None], Field(description='We seperate coins into three tiers. With this parameter you can filter coins on the tiers you need. Read more about out our tiers in our methodology Array parameters should be suffixed with brackets. Example: ?tiers[]=1&tiers[]=2.')] = None,
              tags: Annotated[Union[list, None], Field(description='Tags to filter the list on. Allowed values: defi, stablecoin, nft, dex, exchange, staking, dao, meme, privacy Array parameters should be suffixed with brackets. Example: ?tags[]=defi&tags[]=nft.')] = None,
              orderBy: Annotated[Union[str, None], Field(description='Index to order by. All sortings excluding listedAt still take our different tiers of coins into account, read more about it in our methodology. Default value: marketCap Allowed values: price marketCap 24hVolume change listedAt')] = None,
              search: Annotated[Union[str, None], Field(description='Filter the results by searching for coin names or symbols.')] = None,
              orderDirection: Annotated[Union[str, None], Field(description='Applies direction to the orderBy query, which can be in ascending or descending order. Default value: desc Allowed values: desc asc')] = None,
              limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination. Default value: 50 Size range: 0-100 Default: 50')] = None,
              offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination. Default value: 0 Default: 0')] = None) -> dict: 
    '''Get a list of coins. Coins are by default ordered by their rank, which - somewhat simplified - means that they are ordered on marketcap. The response not only returns a list of coins, but also statistics regarding the requested list, such as the volume in the last 24 hours.'''
    url = 'https://coinranking1.p.rapidapi.com/coins'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'timePeriod': timePeriod,
        'symbols': symbols,
        'uuids': uuids,
        'tiers': tiers,
        'tags': tags,
        'orderBy': orderBy,
        'search': search,
        'orderDirection': orderDirection,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coin(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, in which all the prices are calculated. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
             timePeriod: Annotated[Union[str, None], Field(description='Time period where the change and sparkline are based on Default value: 24h Allowed values: 24h 7d 30d')] = None) -> dict: 
    '''Find information about a specific coin.'''
    url = 'https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'timePeriod': timePeriod,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coin_price(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency. This is the currency the price is shown in, which defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
                   timestamp: Annotated[Union[int, float, None], Field(description='Timestamp. Epoch timestamp in seconds. If it is not provided this endpoint will get the latest price Default: 0')] = None) -> dict: 
    '''With the price endpoint the price can be requested for a specific coin on a specific time. The response is just a single price nearest to the requested time, including its timestamp.'''
    url = 'https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/price'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'timestamp': timestamp,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coin_price_history(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, in which all the prices are calculated. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
                           timePeriod: Annotated[Union[str, None], Field(description='Timeperiod where the change and history are based on Default value: 24h Allowed values: 3h 24h 7d 30d 3m 1y 3y 5y')] = None) -> dict: 
    '''Coinranking keeps track of prices on all listed assets. The history endpoint lists prices and their timestamp for the requested time period, useful for making a chart.'''
    url = 'https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'timePeriod': timePeriod,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coin_ohlc_data(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, in which all the prices are calculated. Defaults to US Dollar. Default value: yhjMzLPhuIDl')] = None,
                       interval: Annotated[Union[str, None], Field(description='The interval determines the time period over which each OHLC item is determined. Default value: day Allowed values: minute 5minutes hour 8hours day week month')] = None,
                       limit: Annotated[Union[int, float, None], Field(description='Limit the amount of time periods for which the OHLC data is retrieved. For example, when interval=hour and limit is 10, data will be returned for the last 10 hours. Default value: 50 Size range: 0-100 Default: 0')] = None) -> dict: 
    '''Get OHLC (Open High Low Close) data for the coin throughout time. This endpoint requires the **ultra** plan or higher. **Beta** The OHLC endpoint is currently in beta. This means we might make some changes that could be considered breaking for your application, and we expect to have downtime every now and then while we are still in beta.'''
    url = 'https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/ohlc'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'interval': interval,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coin_exchanges(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, which rate is used to calculate the volume. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
                       search: Annotated[Union[str, None], Field(description='Value to search for within results, i.e. exchange names')] = None,
                       limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination Default value: 50 Size range: 0-100 Default: 50')] = None,
                       offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination Default value: 0 Default: 0')] = None,
                       orderBy: Annotated[Union[str, None], Field(description='Index to order by. Default is 24h volume. Default value: 24hVolume Allowed values: 24hVolume price')] = None,
                       orderDirection: Annotated[Union[str, None], Field(description='Order in ascending or descending order Default value: desc Allowed values: desc asc')] = None) -> dict: 
    '''Find exchanges where a specific coin can be traded. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/exchanges'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'search': search,
        'limit': limit,
        'offset': offset,
        'orderBy': orderBy,
        'orderDirection': orderDirection,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coin_markets(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, which rate is used to calculate the volume. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
                     search: Annotated[Union[str, None], Field(description='Value to search for within results, e.g. exchange names, currency names, or currency symbols')] = None,
                     limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination Default value: 50 Size range: 0-100 Default: 50')] = None,
                     offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination Default value: 0 Default: 0')] = None,
                     orderBy: Annotated[Union[str, None], Field(description='Index to sort on. Default is 24h volume. Default value: 24hVolume Allowed values: 24hVolume price')] = None,
                     orderDirection: Annotated[Union[str, None], Field(description='Order in ascending or descending order Default value: desc Allowed values: desc asc')] = None) -> dict: 
    '''Find markets on different exchanges that trade a specific coin. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/markets'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'search': search,
        'limit': limit,
        'offset': offset,
        'orderBy': orderBy,
        'orderDirection': orderDirection,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coin_supply(uuid: Annotated[str, Field(description='UUID of the coin you want to request the supply for')]) -> dict: 
    '''Get the maximum, total, and circulating supply of a coin.'''
    url = 'https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/supply'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'uuid': uuid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coin_issuance_blockchains(limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination Default value: 50 Size range: 0-100 Default: 50')] = None,
                                  offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination Default value: 0 Default: 0')] = None) -> dict: 
    '''Get the issuance blockchains on which the coin is issued. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/issuance-blockchains'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coin_modifiers(limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination Default value: 50 Size range: 0-100 Default: 50')] = None,
                       offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination Default value: 0 Default: 0')] = None) -> dict: 
    '''Get the modifiers of a coin's supply and their balance. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/modifiers'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_exchanges(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, in which all the prices are calculated. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
                  uuids: Annotated[Union[list, None], Field(description='Exchange UUIDs to filter the exchanges on. Array parameters should be suffixed with brackets. Example: ?uuids[]=-zdvbieRdZ&uuids[]=8FXHCkosV.')] = None,
                  search: Annotated[Union[str, None], Field(description='Value to search for within results, e.g. exchange names.')] = None,
                  limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination. Only usable when no filters are applied Default value: 50 Size range: 0-100 Default: 50')] = None,
                  offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination. Only usable when no filters are applied Default value: 0 Default: 0')] = None,
                  orderBy: Annotated[Union[str, None], Field(description='Order by either 24h volume, number of markets or latest ticker. Ordering can only be done when no filters are applied Default value: 24hVolume Allowed values: 24hVolume numberOfMarkets lastTickerCreatedAt')] = None,
                  orderDirection: Annotated[Union[str, None], Field(description='Applies direction to the orderBy query, which can be in ascending or descending order. Only usable when no filters are applied Default value: desc Allowed values: desc asc')] = None) -> dict: 
    '''Get a list of exchanges. Exchanges are ranked based on their trading volume in the last 24 hours. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/exchanges'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'uuids': uuids,
        'search': search,
        'limit': limit,
        'offset': offset,
        'orderBy': orderBy,
        'orderDirection': orderDirection,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_exchange(uuid: Annotated[str, Field(description='UUID of the exchange you want to request')]) -> dict: 
    '''Find information on a specific exchange listed on coinranking. An exchange is a place where cryptocurrencies are traded. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/exchange/-zdvbieRdZ'
    headers = {'referenceCurrencyUuid': 'yhjMzLPhuIDl', 'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'uuid': uuid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_exchange_coins(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, which rate is used to calculate the volume. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
                       search: Annotated[Union[str, None], Field(description='Filter the results by searching for coin names or symbols.')] = None,
                       limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination Default value: 50 Size range: 0-100 Default: 50')] = None,
                       offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination Default value: 0 Default: 0')] = None,
                       orderBy: Annotated[Union[str, None], Field(description='Index to sort on. Default is 24h volume Default value: 24hVolume Allowed values: 24hVolume price numberOfMarkets')] = None,
                       orderDirection: Annotated[Union[str, None], Field(description='Order in ascending or descending order Default value: desc Allowed values: asc desc')] = None) -> dict: 
    '''Find coins listed on a specific exchange. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/exchange/-zdvbieRdZ/coins'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'search': search,
        'limit': limit,
        'offset': offset,
        'orderBy': orderBy,
        'orderDirection': orderDirection,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_exchange_markets(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, which rate is used to calculate the volume. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
                         search: Annotated[Union[str, None], Field(description='Value to search for within results, e.g. exchange names, currency names, or currency symbols')] = None,
                         limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination Default value: 50 Size range: 0-100 Default: 50')] = None,
                         offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination Default value: 0 Default: 0')] = None,
                         orderBy: Annotated[Union[str, None], Field(description='Index to sort on. Default is 24h volume. Default value: 24hVolume Allowed values: 24hVolume price')] = None,
                         orderDirection: Annotated[Union[str, None], Field(description='Order in ascending or descending order Default value: desc Allowed values: desc asc')] = None) -> dict: 
    '''Find markets on a specific exchange. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/exchange/-zdvbieRdZ/markets'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'search': search,
        'limit': limit,
        'offset': offset,
        'orderBy': orderBy,
        'orderDirection': orderDirection,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_markets(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, in which all the prices are calculated. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
                currencyUuid: Annotated[Union[str, None], Field(description='Filter markets with specific currency as either base or quote. Specifying a currencyUuid will also alter how prices are shown: By default all the markets will show the price of the base in the reference currency (e.g. an ETH/BTC market will show the price of ETH). By specifying a currencyUuid the prices of this currency will always be shown, disregarding whether or not this currency represents the base or the quote in the market (e.g. by specifying BTC as currency, both ETH/BTC as BTC/USD markets will show prices of BTC)')] = None,
                toCurrencyUuid: Annotated[Union[str, None], Field(description='Filter markets with specific currency as either base or quote. The toCurrencyUuid will not alter how the prices will be shown, but will keep the base price. This can be combined with the currencyUuid variable to get specific markets.')] = None,
                baseCurrencyUuid: Annotated[Union[str, None], Field(description='Filter markets with specific currency as base')] = None,
                quoteCurrencyUuid: Annotated[Union[str, None], Field(description='Filter markets with specific currency as quote')] = None,
                search: Annotated[Union[str, None], Field(description='Filter the results by searching for coin names, symbols or exchange names.')] = None,
                limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination. Only usable when no filters are applied Default value: 50 Size range: 0-100 Default: 50')] = None,
                offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination only usable when no filters are applied Default value: 0 Default: 0')] = None,
                orderBy: Annotated[Union[str, None], Field(description='Sort by either 24h volume or price. Only usable when no filters are applied Default value: 24hVolume Allowed values: 24hVolume price')] = None,
                orderDirection: Annotated[Union[str, None], Field(description='Sort in ascending or descending order. Only usable when no filters are applied. Default value: desc Allowed values: desc asc')] = None) -> dict: 
    '''Get a list of markets. Markets are ranked by their volume over the last 24 hours. Use our filters to get a subset of the markets. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/markets'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'currencyUuid': currencyUuid,
        'toCurrencyUuid': toCurrencyUuid,
        'baseCurrencyUuid': baseCurrencyUuid,
        'quoteCurrencyUuid': quoteCurrencyUuid,
        'search': search,
        'limit': limit,
        'offset': offset,
        'orderBy': orderBy,
        'orderDirection': orderDirection,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_market(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='Uuid of reference currency, in which all the prices are calculated. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None) -> dict: 
    '''Find information on a specific market listed on Coinranking. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/market/MP77r-vKf4'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_reference_currencies(types: Annotated[Union[list, None], Field(description='A currency is one of three types: coin (e.g. Bitcoin, Ethereum, etc.), fiat (US Dollar, Euro, Yen, etc.) or a denominator (e.g. Satoshi). Filter the response by providing one or more types Allowed values: coin, fiat, denominator Array parameters should be suffixed with brackets. Example: ?types[]=coin&types[]=fiat.')] = None,
                             search: Annotated[Union[str, None], Field(description='Filter the results by searching for currency names or symbols.')] = None,
                             limit: Annotated[Union[int, float, None], Field(description='Limit. Used for pagination Default value: 20 Size range: 0-100 Default: 50')] = None,
                             offset: Annotated[Union[int, float, None], Field(description='Offset. Used for pagination Default value: 0 Default: 0')] = None) -> dict: 
    '''Get a list of reference currencies, which can be used as reference for coins. The response includes all the essentials for this use-case, such as the symbol (e.g. USD) and - if available - the sign (e.g. $).'''
    url = 'https://coinranking1.p.rapidapi.com/reference-currencies'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'search': search,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_global_stats(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, in which all the prices are calculated. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None) -> dict: 
    '''These global statistics tell about the data available on coinranking.'''
    url = 'https://coinranking1.p.rapidapi.com/stats'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_search_suggestions(referenceCurrencyUuid: Annotated[Union[str, None], Field(description='UUID of reference currency, in which the coin prices are calculated. Defaults to US Dollar Default value: yhjMzLPhuIDl')] = None,
                           query: Annotated[Union[str, None], Field(description='Value to search on')] = None) -> dict: 
    '''Search suggestions are a quick and easy way to find data on coinranking. The endpoint only accepts one parameter; a query. With this query you can find currencies (including fiat), exchanges and markets, by their symbol or name. The response always returns a set of the most prominent coins, exchanges and markets matching your query.'''
    url = 'https://coinranking1.p.rapidapi.com/search-suggestions'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'referenceCurrencyUuid': referenceCurrencyUuid,
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_coins_index() -> dict: 
    '''List of all coins currently available on coinranking, for indexing purposes. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/indexes/coins'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_exchanges_index() -> dict: 
    '''List of all exchanges currently available on Coinranking, for indexing purposes. This endpoint requires the **ultra** plan or higher.'''
    url = 'https://coinranking1.p.rapidapi.com/indexes/exchanges'
    headers = {'x-rapidapi-host': 'coinranking1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
