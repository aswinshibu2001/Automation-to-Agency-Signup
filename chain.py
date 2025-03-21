from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableLambda
import config
import re
import json

class Automation:
    def __init__(self,filename):
        self.model = ChatGroq(model="gemma2-9b-it") #mistral-saba-24b
        self.count=0
        with open(filename, "r", encoding="utf-8") as f:
            self.website_content = f.read()

        self.prompt = PromptTemplate(
            input_variables=[self.website_content],
            template="""You are a classification model. Your task is to analyze the given website content {website_content} and determine if it belongs to a **Digital Marketing Agency**.  

            ### **Classification Logic**
            - Look for keywords related to digital marketing such as:
            * Services, Web Design, Web Development, SEO Agency, Ads Agency, Digital, Marketing, Agency, Website Creation, brands, web, design, Boosts creativity, Reduces costs.
            - You may also detect similar keywords that imply digital marketing services.

            ### **Strict JSON Output Format**  
            ONLY return a valid JSON object in the format below. **No explanations, no additional text—just the JSON.**

            
            {{
            "Digital Marketing Agency": "Yes" or "No",
            "Confidence Scores": [score1, score2]  // First score → Digital Marketing, Second score → Not Digital Marketing
            }}

        Example Outputs

        For a Digital Marketing Agency, return:
        {{
        "Digital Marketing Agency": "Yes",
        "Confidence Scores": [99.00, 1.00]
        
        }}

        For Not a Digital Marketing Agency, return:
        {{
        "Digital Marketing Agency": "No",
        "Confidence Scores": [1.00, 99.00]
        }}

       """ )

        
    def prediction(self):
       
        chain = self.prompt | self.model 
        response = chain.invoke(self.website_content[:5000])
    
        match = re.search(r'\{.*\}', response.content.lower(), re.DOTALL)  
        # print(response.content) # for debugging
        if match:
            json_text = match.group(0)  
            data = json.loads(json_text) 
           
        else:
            raise ValueError(" Could not extract JSON.")
            
        # print(data) 
        return data
        