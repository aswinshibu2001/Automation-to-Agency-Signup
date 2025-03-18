import asyncio
from crawl4ai import *
from chain import Automation
import json
import csv
import re
import os
import mail
'''
https://www.digitalsilk.com/
https://www.baunfire.com/
https://fourbynorth.com/
https://www.langchain.com/langchain
 '''

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.digitalsilk.com/",
        )
        # print(result.markdown)
        f=open('markdown4.txt','w',encoding="utf-8")
        f.write(result.markdown)
        f.close()
        automate=Automation('markdown4.txt')

        response = automate.prediction()
        print("########################################")
        print(response)
        response = response.strip()  # Remove extra spaces/newlines

        # Ensure the response starts with '{' and ends with '}'
        if not response.startswith("{"):
            response = "{" + response
        if not response.endswith("}"):
            response = response + "}"
                
        url="https://www.digitalsilk.com/"
        email='aswinshibu2024gcsj@gmail.com'      
        # Extract JSON object from text
        match = re.search(r'\{.*\}', response, re.DOTALL)  # Finds the JSON part
        if match:
            json_text = match.group(0)  # Extract the JSON string
            data = json.loads(json_text)  # Convert to dictionary
            
            csv_file = "output.csv"
            write_header = not os.path.exists(csv_file) or os.stat(csv_file).st_size == 0
            
            
            with open(csv_file, mode="a", newline="") as file:
                writer = csv.writer(file)
                if write_header:
                    writer.writerow(["Email","url","Status", "Reason"])
                # writer.writerow(["Status", "Reason"])  # Writing header
                writer.writerow([email,url,data["status"], data["reason"]])  # Writing data

            print(f"Data saved to {csv_file}")
        else:
            print("No JSON found in the response")

        mail.send_email(email,data["status"],data["reason"])

if __name__ == "__main__":
    asyncio.run(main())