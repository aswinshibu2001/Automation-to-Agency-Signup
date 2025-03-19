import asyncio
from crawl4ai import *
from chain import Automation
import save_csv
import mail
from datetime import datetime


'''
https://www.digitalsilk.com/
https://www.baunfire.com/
https://fourbynorth.com/
https://www.langchain.com/langchain
https://huggingface.co/
 '''

async def main():

    url="https://www.digitalsilk.com/"
    email="masterofkings2023@gmail.com" 
    curr_dt = datetime.now()
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
        )
       
        f=open('markdown.txt','w',encoding="utf-8")
        f.write(result.markdown)
        f.close()
        automate=Automation('markdown.txt')
        print("########################################")
        output = automate.prediction()
        if output["digital marketing agency"]=='yes' and output['confidence scores'][0]>output['confidence scores'][1] :
            status="accepted"
        else:
            status="rejected"
        print(status)
        save_csv.write_csv(curr_dt,email,url,status)

        # mail.send_email(email,url,status)
        
if __name__ == "__main__":
    asyncio.run(main())