from dotenv import load_dotenv
from mem0 import MemoryClient
import logging
import json


load_dotenv()
username = 'Kasi'
mem0 = MemoryClient()

def add_memory():

    messages_formatted = [
        {   "role": "user",
            "content": "I really like Linkin Park."
        },
        {
            "role": "assistant",
            "content": "That is a good choice."
        },
        {
            "role": "user",
            "content": "I think so too."
        },
        {
            "role": "assistant",
            "content": "What is your favorite song by them?"
        },
    ]

    mem0.add(messages_formatted, user_id="Kasi")

def get_memory_by_query():
    mem0 = MemoryClient()
    query = f"What are {username}'s preferences?"
    search_response = mem0.search(query, filters={"user_id": username})

    # The backend returns a dict package; the actual array sits inside "results"
    results_list = search_response.get("results", [])

    memories = [
        {
            "memory": result.get("memory"),
            "created_at": result.get("created_at")
        }
        for result in results_list
    ]
    
    memories_str = json.dumps(memories, indent=4)
    print(f"Memories:\n{memories_str}")
    return memories_str



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    get_memory_by_query()