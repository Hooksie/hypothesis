from warnings import filterwarnings

filterwarnings(
    "ignore",
    "Call to '__init__' function with deprecated usage of input argument/s 'retry_on_timeout'",
    category=DeprecationWarning,
)
