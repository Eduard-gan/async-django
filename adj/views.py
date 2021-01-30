from time import sleep

from django.http import HttpResponse
from adj import shared


async def async_index(request):
    print("ASYNC MAKING REQUEST TO SOME REMOTE SERVER")
    async with shared.AIOHTTP_SESSION.get('https://ya.ru') as resp:
        print(resp.status, resp._session)
        await resp.text()
    print("ASYNC OK")
    return HttpResponse("Hello, async Django!")


def index(request):
    print("GOING TO SLEEP")
    sleep(5)
    print("OK")
    return HttpResponse("Hello, sync Django!")
