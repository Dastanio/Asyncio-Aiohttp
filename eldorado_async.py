import aiohttp
import asyncio
import time

start = time.time()
all_data = []

async def get_page_data(session, url):

    async with session.get(url, ssl=False) as resp:
        assert resp.status == 200
        print(f'get: url: {url}')
        resp_text = await resp.text()
        all_data.append(resp_text)
        return resp_text

async def load_site_data():

    async with aiohttp.ClientSession(trust_env=True) as session:
        tasks = []
        num = 0

        for page_id in range(1, 184):
            url = f'https://www.eldorado.ru/search/catalog.php?q=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD&offset={str(num)}&utf'
            task = asyncio.create_task(get_page_data(session, url))
            tasks.append(task)

            num += 36

        await asyncio.gather(*tasks)

asyncio.run(load_site_data())

end_time = time.time() - start
print(end_time)