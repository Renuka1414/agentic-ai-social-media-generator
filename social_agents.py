import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def generate_content(topic, platform):

    prompt = f"""
You are a social media content generation and review agent.

Topic: {topic}
Selected Platform: {platform}

Create content specifically for the selected platform.

For Instagram:
- Write an engaging Instagram caption.
- Use a friendly tone.
- Use emojis when appropriate.
- Include relevant hashtags.

For LinkedIn:
- Write a complete professional LinkedIn post.
- Start with an engaging opening.
- Explain the topic clearly in 2-3 short paragraphs.
- Use a professional but simple tone.
- End with relevant hashtags.

For X:
- Write a short and concise X post.
- Keep it engaging and brief.
- Include a few relevant hashtags.

Do not use the same format for all platforms.
Return ONLY the final content.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
