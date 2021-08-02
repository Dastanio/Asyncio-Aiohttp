import aiohttp
import asyncio
import time

start = time.time()
all_data = []

async def get_page_data(session,category: str, page_id: int) -> str:
    if page_id:
        url = f"https://ozon.ru/brand/{category}/?page={page_id}"
    else:
        url = f"https://ozon.ru/brand/{category}/"
    
    async with session.get(url, ssl = False) as resp:
        assert resp.status == 200
        print(f'get: url: {url}')
        resp_text = await resp.text()
        all_data.append(resp_text)
        return resp_text

async def load_site_data():
    categories_list = ['playstation-79966341', 'apple-26303000', 'adidas-144082850', 'tefal-18819636']
    async with aiohttp.ClientSession() as session:
        tasks = []

        for cat in categories_list:
            for page_id in range(100):
                task = asyncio.create_task(get_page_data(session, cat, page_id))
                tasks.append(task)

        await asyncio.gather(*tasks)

asyncio.run(load_site_data())

end_time = time.time() - start
print(end_time)