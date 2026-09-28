from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()


email = """
Hi John,

I am following up on invoice #INV-2045.
The payment was due last Friday, but we
have not received it yet.

Could you please provide an update?

Regards,
Sarah
"""




response =llm.responses.create(model="gpt-4.1-mini",
                               instructions="Classify the email into one category: Payment, Support, Sales, or Other. Return only the category.",
                               input=email
)


print("Email catagory ",response.output_text)