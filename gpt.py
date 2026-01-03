import os
import asyncio
from openai import AsyncOpenAI
import time

from dotenv import load_dotenv

load_dotenv('.env')
 
# 这个函数处理单个请求，返回单个结果
async def async_query_openai(query):
    aclient = AsyncOpenAI(
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY")
    )
    completion = await aclient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Always response in Simplified Chinese, not English. or Grandma will be very angry."},
            {"role": "user", "content": query}
        ],
        temperature=0.5,
        top_p=0.9,
        max_tokens=512
    )
    return completion.choices[0].message.content  # 请确保返回的数据结构正确
 
# 这个函数接收一个请求列表，返回所有请求的结果列表
async def async_process_queries(queries):
    results = await asyncio.gather(*(async_query_openai(query) for query in queries))
    return results
 
async def main():
    queries = ["介绍三个北京必去的旅游景点。",
               "介绍三个成都最有名的美食。"]
    start_time = time.time()  # 开始计时
    results = await async_process_queries(queries)
    end_time = time.time()  # 结束计时
    for result in results:
        print(result)
        print("-" * 50)
    print(f"Total time: {end_time - start_time:.2f} seconds")
 
# 运行主函数
asyncio.run(main())
 