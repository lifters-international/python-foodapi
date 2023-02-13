import requests

from .urls import *

from ..types import GraphqlFetchResult

def fetchGraphQl( query: str, variables: any ): 
    response = requests.post( getApiUrl(), json={ query, variables } )
    
    return GraphqlFetchResult(response.json())
