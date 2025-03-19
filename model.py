from transformers import pipeline
import asyncio
from crawl4ai import *
# microsoft/deberta-v3-large-mnli
classifier = pipeline("zero-shot-classification",model="facebook/bart-large-mnli")

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.langchain.com/langchain",
        )
        # print(result.markdown)
        filename='markdown5.txt'
        f=open(filename,'w',encoding="utf-8")
        f.write(result.markdown)
        f.close()
      
        
        with open(filename,'r',encoding="utf-8") as f:
            website_content = f.read()

        sequence_to_classify = website_content
        candidate_labels = ['Digital Marketing Agency','Not a Digital Marketing Agency']
        output = classifier(sequence_to_classify, candidate_labels)

        print(output['scores'])

        

if __name__ == "__main__":
    asyncio.run(main())


