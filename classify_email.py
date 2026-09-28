import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()


client = AsyncOpenAI(timeout=30.0)


MAX_CONCURRENT_REQUESTS = 5

CATEGORIES = ["Payment", "Support", "Sales", "Other"]


async def classify_each_email(email, semaphore):

    async with semaphore:
        email_id = email["id"]
        subject = email["subject"]
        body = email["body"]

        print(f"Classifying {email_id} : {subject}")

        try:
            response = await client.responses.create(model="gpt-4.1-mini",instructions=(
                    "You are an email classification assistant. "
                    "Classify the email into exactly one of these "
                    "categories: Payment, Support, Sales, Other. "
                    "Return only the category name, with no explanation."),
                    input=f"Subject: {subject} \n Email : {body} ")
            category = response.output_text.strip()

            if category not in CATEGORIES:
                raise ValueError(f"Unexpected category returned {category}")

            return{
                 "id": email_id,
                "subject": subject,
                "category": category,
                "status": "Success",
                "error": ""
            }
        except Exception as error:
            print(f"Error processing {email_id}: {error}")

            return {
                "id": email_id,
                "subject": subject,
                "category": "",
                "status": "Failed",
                "error": str(error)
            }



async def email_classifier(emails):
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    tasks = [classify_each_email(email,semaphore) for email in emails]

    results = await asyncio.gather(*tasks)

    return results 

