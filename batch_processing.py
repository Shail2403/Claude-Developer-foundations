import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)


#PREPARE AND CREATE YOUR BATCH
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

message_batch = client.messages.batches.create(
    requests=[

        Request(
            custom_id="review-001",
            params=MessageCreateParamsNonStreaming(
                model=cMN,
                max_tokens=100,
                system="You are a customer sentiment analysis assistant.",
                messages=[
                    {
                        "role": "user",
                        "content": """
                            Analyze the following customer review.

                            Review:
                            "The marketing campaign exceeded our expectations. Website traffic increased by 42 percent and conversions improved significantly."

                            Return:
                            - Sentiment
                            - Confidence
                            - One-sentence summary
                        """
                    }
                ]
            )
        ),

        Request(
            custom_id="review-002",
            params=MessageCreateParamsNonStreaming(
                model=cMN,
                max_tokens=100,
                system="You are a customer sentiment analysis assistant.",
                messages=[
                    {
                        "role": "user",
                        "content": """
                            Analyze the following customer review.

                            Review:
                            "We were disappointed with the campaign results. Lead quality was poor and communication could have been much better."

                            Return:
                            - Sentiment
                            - Confidence
                            - One-sentence summary
                        """
                    }
                ]
            )
        ),

        Request(
            custom_id="review-003",
            params=MessageCreateParamsNonStreaming(
                model=cMN,
                max_tokens=100,
                system="You are a customer sentiment analysis assistant.",
                messages=[
                    {
                        "role": "user",
                        "content": """
                            Analyze the following customer review.

                            Review:
                            "The campaign delivered decent results. Although ROI was acceptable, we would like more detailed monthly reports."

                            Return:
                            - Sentiment
                            - Confidence
                            - One-sentence summary
                        """
                    }
                ]
            )
        )

    ]
)

print(message_batch)

# storing the message batch ID for later use and polling the batch for results
message_batch_id = message_batch.id


#POLLING THE BATCH FOR RESULTS
import time

while True:
    message_batch = client.messages.batches.retrieve(message_batch_id)
    if message_batch.processing_status == "ended":
        for result in client.messages.batches.results(
            message_batch_id,
        ):
            match result.result.type:
                case "succeeded":
                    print(f"Success! {result.custom_id}")
                case "errored":
                    if result.result.error.error.type == "invalid_request_error":
                        # Request body must be fixed before re-sending request
                        print(f"Validation error {result.custom_id}")
                    else:
                        # Request can be retried directly
                        print(f"Server error {result.custom_id}")
                case "expired":
                    print(f"Request expired {result.custom_id}")
        break
    else:
        print(f"Batch processing status: {message_batch.processing_status}")
        time.sleep(60)  # Wait for 60 seconds before polling again