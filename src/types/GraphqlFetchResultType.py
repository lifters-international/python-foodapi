from types import SimpleNamespace as NS
from typing import Optional, List

from GraphqlError import GraphqlError

class GraphqlFetchResult(NS):
    data: any
    errors: Optional[List[GraphqlError]]
