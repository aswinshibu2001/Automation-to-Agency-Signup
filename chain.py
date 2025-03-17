from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import config

class Automation:
    def __init__(self,filename):
        self.model = ChatGroq(model="llama3-8b-8192")

        with open(filename, "r", encoding="utf-8") as f:
            self.website_content = f.read()

        self.prompt = PromptTemplate(
            input_variables=[self.website_content],
            template="""
        Analyze the following website content and determine if it belongs to a Digital Marketing Agency.

        Look for these keywords: Services, Web Design, Web Development, SEO Agency, Ads Agency, Digital Marketing Agency, Agency, Website Creation.

        If ALL keywords appear multiple times then classify it as **"Digital Marketing Agency"**.
        Otherwise classify it as **"Not a Digital Marketing Agency"**.
        No explanations.

        Website Content:
        {website_content}

        Final Answer:
        """
        )
    def prediction(self):
        chain = LLMChain(llm=self.model, prompt=self.prompt)
        response = chain.run(self.website_content[:1000])
        return response

