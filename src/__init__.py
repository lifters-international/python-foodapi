from typing import Optional, List
from .queries import isApiKeyValid, getAllFood, searchFoodByName, getFoodByCategory, getFoodById

from .utils import fetchGraphQl

from .types import FoodApiError, Food, FoodCategories

class FoodApi():
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_key_valid = False
        
        self.verifyApiKey(True)
        
    def verifyApiKey(self, throwError = False):
        result = fetchGraphQl(isApiKeyValid, { "apiKey": self.api_key })
        
        if result.errors:
            raise FoodApiError(result.errors[0].message)
        
        self.api_key_valid = result.data.isFoodApiKeyValid;
        
        if ( not self.api_key_valid and throwError ):
            raise FoodApiError("Invalid API key")
        
    def getAllFood(self, limit: Optional[int] = None) -> List[Food]: 
        result = fetchGraphQl(getAllFood, { "api_key": self.api_key, "limit": limit })
        
        if ( result.errors ):
            raise FoodApiError( result.errors[0].message )
        
        return result.data.foodApiGetAllFood;
    
    def searchFoodByName(self, name: str, limit: Optional[int] = None) -> List[Food]:
        result = fetchGraphQl(searchFoodByName, { "apiKey": self.api_key, "name": name, "limit": limit })

        if ( result.errors ):
            raise FoodApiError( result.errors[0].message )

        return result.data.foodApiSearchFoodByName;
        
    def getFoodByCategory(self, categories: FoodCategories, limit: Optional[int] = None) -> List[Food]:
        result = fetchGraphQl(getFoodByCategory, { "apiKey": self.api_key, "categories": categories, "limit": limit })

        if ( result.errors ):
            raise FoodApiError( result.errors[0].message )

        return result.data.foodApiSearchFoodByCategory
    
    def getFoodById(self, id: str) -> Food:
        result = fetchGraphQl(getFoodById, { "apiKey": self.api_key, "id": id });

        if ( result.errors ):
            raise FoodApiError( result.errors[0].message )

        return result.data.foodApiGetFoodById