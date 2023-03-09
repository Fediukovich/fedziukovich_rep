from http import HTTPStatus

from aiohttp import ClientSession, ClientResponse


class QiwiWallet(object):

    BASE_URL: str = 'https://edge.qiwi.com'
    HEADERS: dict = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    def __init__(self, token: str) -> None:
        if not isinstance(token, str):
            raise ValueError('argument `token` must be string')
        self.__token = token

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value: str):
        if not isinstance(value, str):
            raise ValueError('argument `token` must be string')
        self.__token = value

    @staticmethod
    def create_session(func):
        async def wrapper(*args, **kwargs):
            async with ClientSession(
                base_url=QiwiWallet.BASE_URL,
                headers=QiwiWallet.HEADERS
            ) as session:
                return await func(*args, **kwargs, session=session)
        return wrapper

    @create_session
    async def _get(self, url: str, session: ClientSession = None, **kwargs) -> ClientResponse:
        session.headers.update(
            {'Authorization': f'Bearer {self.token}'}
        )
        async with session.get(url=url, params=kwargs) as response:
            return response

    async def profile(
            self,
            auth_info: bool = None,
            contract_info: bool = None,
            user_info: bool = None
    ) -> dict:
        response = await self._get(
            url='/person-profile/v1/profile/current',
            params={
                'authInfoEnabled': True if auth_info is None else False,
                'contractInfoEnabled': True if contract_info is None else False,
                'userInfoEnabled': True if user_info is None else False,
            }
        )
        if response.status == HTTPStatus.OK:
            return await response.json()