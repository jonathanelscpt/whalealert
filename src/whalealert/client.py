from typing import Dict, Union, Optional
from urllib.parse import urljoin

from whalealert.exceptions import handle_error_response
from whalealert.session import WhaleAlertAPISession
from whalealert.enums import Plan
from requests import RequestException


class BaseAPI(object):

    def __init__(
            self, api_key: str, version: str = "v1", timeout: int = 5
    ):
        """
        Instantiate a new API client.

        Args:
            version (str): API version to use. This should remain 'v1'.
            api_key (str): api key for authenticated APIs.
        """
        self._base_url = 'https://api.whale-alert.io/'
        self.version = version
        self.timeout = timeout
        self._session = WhaleAlertAPISession()
        if api_key:
            self._session.init_auth(api_key)

    @property
    def url(self):
        return urljoin(self._base_url, self.version)

    def _request(self, endpoint: str, params: Dict = None, data: Dict = None):
        data = data or {}
        params = params or {}
        url = f'{self.url}/{endpoint}'
        resp = self._session.request("GET", url=url, params=params, json=data)
        try:
            resp.raise_for_status()
        except RequestException:
            handle_error_response(resp)
        return resp.json()


class WhaleAlert(BaseAPI):
    """
    Whale Alert's API allows you to retrieve live and historical transaction data from major blockchains.
    Currently supported are Bitcoin, Ethereum, Ripple, NEO, EOS, Stellar and Tron.
    More blockchains will be added in the future. Please read our terms and conditions before using the API.
    """

    def __init__(self, api_key: str, version: str, plan: Optional[Union[Plan, str]] = None):
        plan = plan or Plan.FREE
        self.plan = plan if isinstance(plan, Plan) else Plan(plan)
        self.default_min_value = 100000 if self.plan == Plan.PERSONAL else 5000000
        super().__init__(api_key, version)

    def status(self):
        """
        Shows the current status of Whale Alert.
        Response lists all currently tracked blockchains, currencies and the current status for each blockchain.
        If Whale Alert is currently receiving data from a blockchain the status will be listed as "connected".
        :return:
        """
        return self._request("/status")

    def transaction(self, blockchain: str, hash: str):  # noqa
        """
        Returns the transaction from a specific blockchain by hash.
        Blockchain inputs are: bitcoin, ethereum, ripple, neo, eos, tron and stellar.
        If a transaction consists of multiple OUTs, it is split into multiple transactions,
        provided the corresponding OUT is of high enough value (>=$10 USD).

        :param blockchain: The blockchain to search for the specific hash (lowercase)
        :param hash: The hash of the transaction to return
        :return:
        """
        return self._request(f"/transaction/{blockchain}/{hash}")

    def transactions(self, start: int, end: int = None, cursor: str = None, min_value: Optional[int] = None,
                     limit: int = 100, currency: str = None):
        """
        Returns transactions with timestamp after a set start time (excluding) in order in which they were added
        to our database. This timestamp is the execution time of the transaction on its respective blockchain.
        Some transactions might be reported with a small delay.

        Use the cursor with the same start time when retrieving transactions in multiple or continuous requests
        (when retrieving the newest transactions or when the number of retrieved transactions is higher than
        the limit per result set).

        Low value transactions (<$10 USD) are periodically grouped per blockchain and per
        FROM and TO address owner to reduce data size.

        :param start: (Required) Unix timestamp for retrieving transactions from timestamp (exclusive).
        Retrieves transactions based on their execution time on the blockchain.
        :param end: Unix timestamp for retrieving transactions until timestamp (inclusive).
        :param cursor: Pagination key from the previous response. Recommended when retrieving transactions in intervals.
        :param min_value: Minimum USD value of transactions returned (value at time of transaction).
        Allowed minimum value varies per plan ($500k for Free, $100k for Personal).
        :param limit: Maximum number of results returned. Default 100, max 100.
        :param currency:
        :return: Returns transactions for a specific currency code. Returns all currencies by default.
        """
        min_value = min_value or self.default_min_value
        params = {
            k: v for k, v
            in {'end': end, 'cursor': cursor, 'min_value': min_value, 'limit': limit, 'currency': currency}.items()
            if v
        }
        params.update({'start': start})
        return self._request("/transactions", params=params)
