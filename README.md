# 📌 Automation-to-Agency-Signup

This is a fully enabled automation to the process of agency signup on the CookiYes platform.
When the client submit the sign up form, an Ai process will evaluate the client website and takes the decision to either accept or reject the client request. Accordingly an automatic notification mail will be sent to the client and their request will be stored for future refernce in a csv file.

The program can be runned using the command `python main.py`

The requirements needed to build this project is specified in the `requirements.txt` file

Install those requirements using `pip install -r requirements.txt`

Instead of submmiting the signup form , here i have manullay given the client email and their website url.
Initially we will get the data from the client website using webscraping methods. Here I have used [Crawl4AI](https://github.com/unclecode/crawl4ai) for getting the scrapped content from the website. Then using an LLM, a decision is made whether the website falls under the specified category. The Large Language Model(LLM) used here is mistral-saba-24b which is loaded and runned using groq api. [Groq](https://groq.com/) offers LLM inference via APIs which allows us to run the models with high efficiency. 
The entire application is built upon [LangChain](https://www.langchain.com/) which is an open source framework for building applications based on large language models (LLMs).

The history is stored in `history.csv`.The notification mail is sent using smtplib library in python.