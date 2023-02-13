# Getting Started

> If you have not done so, please create an api account at the following: https://business.lifters.app/food-api


### Install the Node js Lifters FoodApi wrapper
```Python
  pip install @lifters-international/python-foodapi
```

### Once imported you can start using the wrapper like so
```Python
  from FoodApi import FoodApi
  
  foodApi = new FoodApi("{FOOD_API_TOKEN}");
```

### Functions & Uses:
```Python
    foodApi.verifyApiKey( throwError: boolean = false ) # Checks if the api_key provided is valid. And throws error if it is not.
  
    foodApi.getAllFood( limit?: number ) # Returns all food from Lifters Food Database, if a limit is given that limit on Food is returned.
  
   foodApi.searchFoodByName( name: string, limit?: number ) # Returns list of food in database with similar name.
  
   foodApi.getFoodByCategory( categories: FoodCategories, limit?: number ) # Returns list of food in database that meets one or all category.
  
   foodApi.getFoodById( id : string ) #Returns food with the given id.
```

### Important Types:

> FoodCategories:

```PYTHON
class FoodCategories(NS):
    calories: Optional[int]
    
    totalFat: Optional[int]
    
    saturatedFat: Optional[int]
    
    transFat: Optional[int]
    
    cholesterol: Optional[int]
    
    sodium: Optional[int]
    
    totalCarbohydrate: Optional[int]
    
    dietaryFiber: Optional[int]
    
    totalSugars: Optional[int]
    
    addedSugars: Optional[int]
    
    protein: Optional[int]
    
    vitaminD: Optional[int]
    
    calcium: Optional[int]
    
    iron: Optional[int]
    
    potassium: Optional[int]
```


> Food:

```PYTHON
class Food(NS):
    id: str
    
    name: str
    
    calories: int
    
    servingSize: NutritionFactsJson
    
    nutritionFacts: NutritionFacts
    
    adminCreated: bool
```
