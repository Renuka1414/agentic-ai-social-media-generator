from agents import Agent, Runner


content_agent = Agent(
    name="Social Media Content Agent",
    instructions="""
    You are a social media content generator.

    Create engaging social media content based on the user's topic
    and selected platform.

    If the platform is Instagram:
    - Create an engaging Instagram caption
    - Add relevant hashtags

    If the platform is LinkedIn:
    - Create a professional LinkedIn post
    - Add relevant hashtags

    If the platform is X:
    - Create a short and engaging X (Twitter) post
    - Add relevant hashtags

    Keep the content clear, engaging and suitable for students
    and professionals.
    """
)


def generate_content(topic, platform):

    prompt = f"""
    Topic: {topic}
    Platform: {platform}

    Generate content specifically for the selected platform.
    """

    result = Runner.run_sync(
        content_agent,
        prompt
    )

    return result.final_output