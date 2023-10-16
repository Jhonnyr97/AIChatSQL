# AIChatSQL

AIChatSQL is a powerful tool that translates natural language queries into SQL and delivers meaningful responses in natural language. It seamlessly integrates with your database, offering an efficient way to interact with your data.

## Features

- **Natural Language Queries**: Easily communicate with your database using everyday language.

- **SQL Translation**: AIChatSQL translates your natural language queries into SQL commands for efficient data retrieval.

- **Database Integration**: Utilize your database directly to access and manage your data.

- **The Cheshire Cat Integration**: AIChatSQL is a dedicated plugin for The Cheshire Cat, a framework for building custom AIs on top of any language model. Visit the [Cheshire Cat repository](https://github.com/cheshire-cat-ai/core) for more details.

## Getting Started

1. Install AIChatSQL.
2. Set up your database connection.
3. Start using natural language queries to interact with your data.

## Usage

Here's a simple example of how to use AIChatSQL to retrieve data from your database:

```python
from aichatsql import AIChatSQL

# Initialize AIChatSQL
chatbot = AIChatSQL()

# Send a natural language query
result = chatbot.query("Retrieve all customers who made a purchase in the last month.")

# Access the result in natural language
print(result)
```
# Dependencies
The Cheshire Cat: AIChatSQL is designed to work exclusively with The Cheshire Cat framework.

Contact
For questions or support, please contact our team at oneill.jhon97@gmail.com

Happy querying with AIChatSQL!
