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

        Look for similar keywords: Services, Web Design, Web Development, SEO Agency, Ads Agency, Digital, Marketing , Agency, Website Creation,
        brands,web,design,Boosts creativity,Reduces costs.

        ***The website content may not mention all the keywords. Use logic and find keywords similar to the above.****

        **if the above keywords or similar keywords are found then it can be a digital marketing agency**
       
       format the output as a json object with two field as  ***(status  "accepted" :  |"rejected") and (reason : )***
       give reason.
       ***Ensure proper json format with opening and closing brackets***
        ***Dont give explanation. Just display only the json object.***

        
      
        Website Content:
        {website_content}

        Final Answer:
        """
        )
    def prediction(self):
        chain = LLMChain(llm=self.model, prompt=self.prompt)
        response = chain.run(self.website_content[:5000])
        return response

