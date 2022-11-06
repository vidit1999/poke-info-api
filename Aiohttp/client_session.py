import aiohttp

class RequestSessions:
    poke_session: aiohttp.ClientSession

    async def __ainit__(self):
        self.poke_session = aiohttp.ClientSession()

    async def __adel__(self):
        await self.poke_session.close()

request_sessions = RequestSessions()
