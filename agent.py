from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, ChatContext
from livekit.plugins import (
    noise_cancellation,
    openai
)
from livekit.plugins import google
from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from tools import getweather, searchweb, sendemail
from mem0 import AsyncMemoryClient
import os
import json
import logging
load_dotenv()

username="Kasi"
class Assistant(Agent):
    def __init__(self, chat_ctx=None) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTION,
            llm=google.beta.realtime.RealtimeModel(
                 voice="Charon"
             
            ),
            tools=[
                getweather,
                searchweb,
                sendemail
            ],
            chat_ctx=chat_ctx

        )
        


async def entrypoint(ctx: agents.JobContext):

    initial_ctx = ChatContext()

    async def shutdown_hook(chat_ctx: ChatContext, mem0: AsyncMemoryClient, memory_str: str):
        logging.info("Shutting down, saving chat context to memory...")

        messages_formatted = [
        ]

        logging.info(f"Chat context messages: {chat_ctx.items}")

        for item in chat_ctx.items:
            content_str = ''.join(item.content) if isinstance(item.content, list) else str(item.content)

            if memory_str and memory_str in content_str:
                continue

            if item.role in ['user', 'assistant']:
                messages_formatted.append({
                    "role": item.role,
                    "content": content_str.strip()
                })

        logging.info(f"Formatted messages to add to memory: {messages_formatted}")
        await mem0.add(messages_formatted,filters={"user_id": "Kasi"})
        logging.info("Chat context saved to memory.")


    session = AgentSession(
        
    )

    

    mem0 = AsyncMemoryClient()
    query = f"What are {username}'s preferences?"
    # Force Python to await the async coroutine
    search_response = await mem0.search(query, filters={"user_id": username})

    # Now this will successfully execute without throwing an AttributeError
    results_list = search_response.get("results", [])


    memories = [
        {
            "memory": result.get("memory"),
            "created_at": result.get("created_at")
        }
        for result in results_list
    ]
    
    memory_str = json.dumps(memories)
    logging.info(f"Memories: {memory_str}")
    initial_ctx.add_message(
        role="assistant",
        content=f"The user's name is {username}, and this is relvant context about him: {memory_str}."
    )

    # mcp_server = MCPServerSse(
    #     params={"url": os.environ.get("N8N_MCP_SERVER_URL")},
    #     cache_tools_list=True,
    #     name="SSE MCP Server"
    # )

    # agent = await MCPToolsIntegration.create_agent_with_tools(
    #     agent_class=Assistant, agent_kwargs={"chat_ctx": initial_ctx},
    #     mcp_servers=[mcp_server]
    # )

    await session.start(
        room=ctx.room,
        agent=Assistant(chat_ctx=initial_ctx),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            video_enabled=True,
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_INSTRUCTION,
    )

    ctx.add_shutdown_callback(lambda: shutdown_hook(session._agent.chat_ctx, mem0, memory_str))

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))