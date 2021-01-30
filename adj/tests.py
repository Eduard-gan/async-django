from asyncio import gather

from aiohttp import ClientSession
from django.test import TestCase

from adj import shared


class QuestionModelTests(TestCase):

    async def test_async_view_by_async_test(self):
        shared.AIOHTTP_SESSION = ClientSession()
        responses = await gather(*[self.async_client.get('/async') for _ in range(3)])
        assert all(x.status_code == 200 for x in responses)

    async def test_sync_view_by_async_test(self):
        responses = await gather(*[self.async_client.get('/') for _ in range(3)])
        assert all(x.status_code == 200 for x in responses)

    def test_sync_view_by_sync_test(self):
        response = self.client.get('/')
        assert response.status_code == 200
