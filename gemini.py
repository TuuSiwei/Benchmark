import os
import asyncio
import aiohttp
import json

from dotenv import load_dotenv

load_dotenv('.env')

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

# 异步调用生成内容
async def fetch_content(session, prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    headers = {
        "x-goog-api-key": api_key,
        "Content-Type": "application/json"
    }
    # 请求体
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }
    try:
        # 使用 aiohttp 发起 POST 请求
        async with session.post(url, headers=headers, json=data) as response:
            response_data = await response.json()
            # 打印完整响应内容以检查结构
            # print(json.dumps(response_data, indent=2))  # 打印响应的JSON结构
            # 修正字段提取
            candidates = response_data.get("candidates", [])
            if candidates:
                content = candidates[0].get("content", {})
                parts = content.get("parts", [])
                if parts:
                    return parts[0].get("text", "No response text")
            return "No response text"
    except Exception as e:
        return f"Error: {e}"

# 并发请求处理多个内容生成
async def generate_content_concurrently(prompts):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_content(session, prompt) for prompt in prompts]
        results = await asyncio.gather(*tasks)
        return results

# 示例多个请求
prompts = [
    "Explain how AI works in a few words",
    "What is the future of quantum computing?",
]

# 执行并发请求
loop = asyncio.get_event_loop()
results = loop.run_until_complete(generate_content_concurrently(prompts))

# 打印结果
for result in results:
    print("==========")
    print(result)
