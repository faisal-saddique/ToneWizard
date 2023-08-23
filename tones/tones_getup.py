from langchain.schema import HumanMessage, SystemMessage

def message_generator(query: str, role: list):
    role = role.lower()

    messages = [
        SystemMessage(
            content=f"You are a helpful assistant that changes the tone of the provided text based on the given tone. You don't have any other work than to just change the tone of the text to adapt it to the requested tone. Don't add anything extra to the original text than what's given to you. If the user asks a direct question or requests something, in that case too, your job is to just convert the tone of that question or request, NEVER answer them. Never answer other than the role you have been strictly assigned. Please convert the tone of the given text to {' and '.join(role)} tone.\n\nText:\n{query}"
        )
    ]
    return messages