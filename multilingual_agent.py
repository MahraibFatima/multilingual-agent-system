from agents import Agent, Runner
import asyncio

# Define language-specific agents
spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You only speak Spanish. Respond to the user in Spanish.",
)

english_agent = Agent(
    name="English Agent",
    instructions="You only speak English. Respond to the user in English.",
)

italian_agent = Agent(
    name="Italian Agent",
    instructions="You only speak Italian. Respond to the user in Italian.",
)

german_agent = Agent(
    name="German Agent",
    instructions="You only speak German. Respond to the user in German.",
)

french_agent = Agent(
    name="French Agent",
    instructions="You only speak French. Respond to the user in French.",
)

# Triage agent routes to the correct language agent
triage_agent = Agent(
    name="Triage Agent",
    instructions="Detect the language of the input and hand off to the appropriate agent. "
                "Options: Spanish, English, Italian, German, or French.",
    handoffs=[spanish_agent, english_agent, italian_agent, german_agent, french_agent],
)

async def main():
    # Test with different language inputs
    test_inputs = [
        "Hola, ¿cómo estás?",  # Spanish
        "Hello, how are you?",  # English
        "Ciao, come stai?",     # Italian
        "Hallo, wie geht's?",   # German
        "Bonjour, comment ça va?",  # French
    ]

    for input_text in test_inputs:
        print(f"\nInput: '{input_text}'")
        result = await Runner.run(triage_agent, input=input_text)
        print(f"Response: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
