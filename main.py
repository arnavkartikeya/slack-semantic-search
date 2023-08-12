# imports
import pandas as pd
import tiktoken
import openai
import numpy as np
import os 
import dotenv

from dotenv import load_dotenv
from openai.embeddings_utils import get_embedding

embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  
max_tokens = 8000  

load_dotenv()

openai.api_key = os.getenv("openai_key")

#testing dictionary, must be an array with a single entry for the value in the key, value pair
dictionary = {"creating war room" : ['wiki page link'], 'as home page' : ['wiki for as home page'], 'as dashboard' : ['dashboard'], 'as_commanders': ['Kumar']}

def append_embeddings_to_dict(dictionary):
  embeds = dictionary
  for keys in embeds:
    embeds[keys].append(get_embedding(keys , engine=embedding_model))
  return embeds

def vector_similarity(x, y):
    return np.dot(np.array(x), np.array(y))

def retrieve_command(dictionary, query):
  query_embed = get_embedding(query, engine=embedding_model)
  sims = [] 
  for keys in dictionary:
    sims.append((keys, vector_similarity(query_embed, dictionary[keys][1])))
  sims.sort(key=lambda x: x[1], reverse=True)
  return sims

#currently only answers with the appropriate value pair, commented section attempts to answer with natural language using gpt
def answer_query(query, dictionary): 
    # COMPLETIONS_MODEL = "text-davinci-003"
    # COMPLETIONS_API_PARAMS = {
    #   # We use temperature of 0.0 because it gives the most predictable, factual answer.
    #   "temperature": 0.0,
    #   "max_tokens": 500,
    #   "model": COMPLETIONS_MODEL,
    # }
    # sims = retrieve_command(dictionary, query)
    # key = sims[0][0]
    # ans = dictionary[key][0]
    # section = key + ": " + ans
    # prompt = """Answer the question as truthfully as possible using the provided context. \n\nContext:\n"""
    # prompt = prompt + "".join(section) + "\n\n Q: " + query + "\n A:"
    # print(prompt)
    # response = openai.Completion.create(
    #           prompt=prompt,
    #           **COMPLETIONS_API_PARAMS
    #       )
    # return response["choices"][0]["text"].strip(" \n")
    sims = retrieve_command(dictionary, query)
    return dictionary[sims[0][0]][0]

query = input("enter a query: ")
embeds = append_embeddings_to_dict(dictionary)
print(answer_query(query, embeds)) 