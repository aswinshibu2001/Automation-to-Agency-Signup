import asyncio
from crawl4ai import *
from chain import Automation
import save_csv
import mail
import validators
from datetime import datetime


'''
https://www.digitalsilk.com/
https://www.baunfire.com/
https://fourbynorth.com/
https://www.langchain.com/langchain
https://huggingface.co/
 '''

async def main(url,email):

    curr_dt = datetime.now()
    if not validators.url(url):
        mail.send_email(email,url,status="rejected")
        print(f"Invalid URL format: {url}")
        return

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun( url=url,)
       
        filename='markdown.txt'
        if result.markdown is not None and len(result.markdown)>100:
            f=open(filename,'w',encoding="utf-8")
            f.write(result.markdown)
            f.close()
        else:
            mail.send_email(email,url,status="rejected")
            print("Bad request. Check url and try again")
            return

        automate=Automation(filename)
        print("########################################")
        output = automate.prediction()
        if output["digital marketing agency"]=='yes' and output['confidence scores'][0]>output['confidence scores'][1] :
            status="accepted"
            print("Your request accepted.Check mail for more information.")
        else:
            status="rejected"
            print("Your request rejected. Check mail for more information.")
        
        save_csv.write_csv(curr_dt,email,url,status)

        mail.send_email(email,url,status)





if __name__ == "__main__":
    while True:
        
        print("\n\tWelcome to CookieYes!!\n")
        print("1.Sign up")
        print("2.Exit")
        ch=int(input())
        if ch==1:
            email=input("\nEmail : ")
            url=input("Url : ")
            print("\n")
            try:
                asyncio.run(main(url,email))
            except Exception as e:
                status="rejected"
                mail.send_email(email,url,status)
                print(f"Unexpected error occured: {e}")
                print("Restarting signup process...\n")
        else:
            
            exit()
