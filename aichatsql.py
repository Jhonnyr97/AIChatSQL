from langchain.utilities import SQLDatabase
from cat.mad_hatter.decorators import tool, hook
from langchain_experimental.sql import SQLDatabaseChain

@tool
def get_data_from_database(tool_input, cat):
    """This plugin needs tool_input (human message) to return the result from the database data in human natural
    language"""

    db = connect(cat)
    db_chain = SQLDatabaseChain.from_llm(cat._llm, db, verbose=True)

    return str(db_chain.run(tool_input))


def connect(cat):
    settings = cat.mad_hatter.plugins["AIChatSQL"].load_settings()
    if settings["data_source"] == "sqlite":
        uri = f"sqlite:///cat/plugins/connect_database/{settings['host']}"
    elif settings["data_source"] == "postgresql":
        uri = f"postgresql+psycopg2://{settings['username']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"
    else:
        uri = f"mysql://{settings['username']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"

    return SQLDatabase.from_uri(uri,
                                include_tables=settings["allowed_tables"].split(", "),
                                sample_rows_in_table_info=2
    )
