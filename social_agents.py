from agents import Agent, Runner


content_agent = Agent(
    name="Social Media Content Agent",
    instructions="""
You are a social media content generation agent.

You will receive a topic and a selected platform.

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
The selected platform must determine the output.
"""
)


review_agent = Agent(
    name="Content Review Agent",
    instructions="""
You are a social media content review agent.

You will receive the topic, selected platform, and generated content.

Review the content for:
- Relevance to the topic
- Clarity
- Engagement
- Platform suitability
- Relevant hashtags

For Instagram, return an Instagram caption with hashtags.

For LinkedIn, return a complete professional LinkedIn post with paragraphs and hashtags.

For X, return a short concise X post with hashtags.

If the content needs improvement, rewrite it.

Return ONLY the final improved content.
"""
)


async def generate_content(topic, platform):

    prompt = f"""
Topic: {topic}
Selected Platform: {platform}

Generate social media content for this platform.
"""

    result = await Runner.run(content_agent, prompt)

    generated_content = result.final_output

    review_prompt = f"""
Topic: {topic}
Selected Platform: {platform}

Generated Content:
{generated_content}

Review and improve this content according to the selected platform.
"""

    review_result = await Runner.run(
        review_agent,
        review_prompt
    )

    return review_result.final_output