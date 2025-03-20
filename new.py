# import asyncio
# import aiohttp
# import validators
# from crawl4ai import *
# import sys

# # if sys.platform.startswith('win') and sys.version_info >= (3, 8):
# #     asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
# # async def is_url_accessible(url):
# #     try:
# #         async with aiohttp.ClientSession() as session:
# #             async with session.head(url, allow_redirects=True) as response:
# #                 return response.status == 200
# #     except Exception:
# #         return False
    

# async def main(url):

#     if not validators.url(url):
#         print(f"Invalid URL format: {url}")
#         return
    
#     # Check if URL is accessible
#     # if not await is_url_accessible(url):
#     #     print(f"URL is not accessible: {url}")
#     #     return
    
    
#     async with AsyncWebCrawler() as crawler:
            
#         result = await crawler.arun(url=url,)
            
     
    
#     if result.markdown is not None and len(result.markdown)>100:
#         f=open('markdown.txt','w',encoding="utf-8")
#         f.write(result.markdown)
#         print("content to write.")
#         print(len(result.markdown))
#     else:
#         print("No content to write.")

# url="https://www.langchain.com/lanmap"
# if __name__ == "__main__":
#     asyncio.run(main(url))