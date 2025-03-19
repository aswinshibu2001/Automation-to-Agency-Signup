from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableLambda
from transformers import pipeline
import config

class Automation:
    def __init__(self,filename):
        self.model = ChatGroq(model="mistral-saba-24b")

        with open(filename, "r", encoding="utf-8") as f:
            self.website_content = f.read()

        self.prompt = PromptTemplate(
            input_variables=[self.website_content],
            template="""
            Analyze the following website content and classify it.

            Content: {website_content}

            Look for similar keywords: Services, Web Design, Web Development, SEO Agency, Ads Agency, Digital, Marketing , Agency, Website Creation,
            brands,web,design,Boosts creativity,Reduces costs.

            ***The website content may not mention all the keywords. Use logic and find keywords similar to the above.****

            **if the above keywords or similar keywords are found then it can be a digital marketing agency**

            ***Provide the answer in the following JSON format:***
            ```json
            {{
            "classification": "Yes" or "No"
            }}
        """
        )

        self.classifier = pipeline("zero-shot-classification",model="facebook/bart-large-mnli")


    def prediction(self):
        # chain = LLMChain(llm=self.model, prompt=self.prompt)
        chain = self.prompt | self.model 
        # response = chain.run(self.website_content[:5000])
        response = chain.invoke(self.website_content[:5000])

        sequence_to_classify = response.content
        candidate_labels = ['Yes','No']
        output = self.classifier(sequence_to_classify, candidate_labels)

        print(response.content)
        print(output['scores'])

        return output['scores']
        

