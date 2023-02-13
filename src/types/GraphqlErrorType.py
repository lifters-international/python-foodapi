from types import SimpleNamespace as NS
from typing import List

class ErrorExtensionException(NS):
    name: str
    message: str
    stacktrace: List[str]
    
class ErrorExtension(NS):
    code: str
    
    exception: ErrorExtensionException
    
class ErrorLocations(NS):
    column: int;
    
    line: int
    
class GraphqlError(NS):
    extensions: ErrorExtension
    
    locations: List[ErrorLocations]
    
    message: str
    
    path: List[str]
