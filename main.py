import asyncio
from crawl4ai import *
from chain import Automation


'''
https://www.digitalsilk.com/
https://www.baunfire.com/
https://fourbynorth.com/
https://www.langchain.com/langchain
 '''

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.langchain.com/langchain",
        )
        # print(result.markdown)
        f=open('markdown4.txt','w',encoding="utf-8")
        f.write(result.markdown)
        f.close()
        automate=Automation('markdown4.txt')

        response = automate.prediction()
        print(response)

if __name__ == "__main__":
    asyncio.run(main())