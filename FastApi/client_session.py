import httpx

class RequestClient:
    client: httpx.AsyncClient

    async def __ainit__(self):
        self.client = httpx.AsyncClient()

    async def __adel__(self):
        await self.client.aclose()

request_client = RequestClient()