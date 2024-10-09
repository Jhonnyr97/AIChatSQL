from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from cat.mad_hatter.decorators import tool, hook
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import subprocess

@tool
def database(tool_input, cat):
    """This plugin needs tool_input (human message) to return the result from the database data in human natural
    language"""
    db = connect(cat)
    chain = create_sql_query_chain(cat._llm, db)

    system = """Double check the user's {dialect} query for common mistakes, including:
    - Using NOT IN with NULL values
    - Using UNION when UNION ALL should have been used
    - Using BETWEEN for exclusive ranges
    - Data type mismatch in predicates
    - Properly quoting identifiers
    - Using the correct number of arguments for functions
    - Casting to the correct data type
    - Using the proper columns for joins
    
    If there are any of the above mistakes, rewrite the query.
    If there are no mistakes, just reproduce the original query with no further commentary.
    
    Output the final SQL query only."""
    prompt = ChatPromptTemplate.from_messages(
        [("system", system), ("human", "{query}")]
    ).partial(dialect=db.dialect)

    validation_chain = prompt | cat._llm | StrOutputParser()

    full_chain = {"query": chain } | validation_chain

    query = full_chain.invoke(
        {
            "question": tool_input
        }
    )
    return str(db.run(query))


@hook(priority=0)
def before_cat_bootstrap(cat) -> None:
    check_pkg_config();
    check_libmysqlclient();
    check_mysqlclient_module();


def check_pkg_config():
    subprocess.check_call(["apt-get", "-y", "update"])
    subprocess.check_call(["apt-get", "-y", "install", "pkg-config"])


def check_libmysqlclient():
    try:
        subprocess.check_call(["pkg-config", "--exists", "default-libmysqlclient"])
    except subprocess.CalledProcessError:
        print("Installing default-libmysqlclient-dev")
        subprocess.check_call(["apt-get", "-y", "install", "default-libmysqlclient-dev"])


def check_mysqlclient_module():
    try:
        import mysqlclient
    except ImportError:
        print("Installing mysqlclient")
        subprocess.check_call(["pip", "install", "mysqlclient"])


def connect(cat):
    settings = cat.mad_hatter.plugins["aichatsql"].load_settings()
    if settings["data_source"] == "sqlite":
        uri = f"sqlite:///cat/plugins/sqlite_db/{settings['host']}"
    elif settings["data_source"] == "postgresql":
        uri = f"postgresql+psycopg2://{settings['username']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"
    else:
        uri = f"mysql://{settings['username']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"

    db = SQLDatabase.from_uri(uri,
                                    include_tables=settings["allowed_tables"].split(", "),
                                    )

    return db
