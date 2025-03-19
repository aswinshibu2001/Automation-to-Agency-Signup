import asyncio
from crawl4ai import *
from chain import Automation
import save_csv
import mail

'''
https://www.digitalsilk.com/
https://www.baunfire.com/
https://fourbynorth.com/
https://www.langchain.com/langchain
https://huggingface.co/
 '''

async def main():

    url="https://huggingface.co/"
    email='aswinshibu2024gcsj@gmail.com' 

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
        )
       
        f=open('markdown4.txt','w',encoding="utf-8")
        f.write(result.markdown)
        f.close()
        automate=Automation('markdown4.txt')

        response = automate.prediction()
        print("########################################")
    
        if response[0]>response[1]:
            status="accepted"
        else:
            status="rejected"

        save_csv.write_csv(email,url,status)

        # mail.send_email(email,url,data["status"],data["reason"])

if __name__ == "__main__":
    asyncio.run(main())