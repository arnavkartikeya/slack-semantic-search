# slack-semantic-search
## About
Searches a dictionary of key-value pairs given a query to find the most semantically similar key using the cosine similarity on the embedded vectors of both queries and keys. Uses the openai api TikToken. 

## Instructions: 
To run, first generate an OpenAI api key, and create a `.env` file in the code directory with the phrase `openai_key = "<generated key>"`. Next run, `pip install -r requirements.txt`, and finally `python main.py`. To edit key-value pairs, change values in the dictionary, making sure the value is stored a single entry in an array of length 1, like the current code has. Type an natural phrase such as "Who is the AS commander", and the code will retrieve the value for the key of `as_commander`. 

