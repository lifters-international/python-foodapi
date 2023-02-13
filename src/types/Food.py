from types import SimpleNamespace as NS
from enum import Enum
from typing import Optional

class NutritionUnits(Enum):
    mL = 'mL'
    mcg = 'mcg'
    L = 'L'
    dL = 'dL'
    t = 't'
    tsp = 'tsp'
    tbsp =  'tbsp'
    gill = 'gill'
    cup = 'cup'
    pt = 'pt'
    qt = 'qt'
    gal = 'gal'
    mg = 'mg'
    g = 'g'
    kg = 'kg'
    lb = 'lb'
    oz = 'oz'
    can = 'can'
    percent = '%'
    
class NutritionFactsJson(NS):
    measurment: int
    unit: NutritionUnits
    
class NutritionFacts(NS):
    totalFat: NutritionFactsJson
    
    saturatedFat: NutritionFactsJson
    
    transFat: NutritionFactsJson
    
    cholesterol: NutritionFactsJson
    
    sodium: NutritionFactsJson
    
    totalCarbohydrate: NutritionFactsJson
    
    dietaryFiber: NutritionFactsJson
    
    totalSugars: NutritionFactsJson
    
    addedSugars: NutritionFactsJson
    
    protein: NutritionFactsJson
    
    vitaminD: NutritionFactsJson
    
    calcium: NutritionFactsJson
    
    iron: NutritionFactsJson
    
    potassium: NutritionFactsJson
    
class NutritionFactsInput(NS):
    totalFat: Optional[NutritionFactsJson]
    
    saturatedFat: Optional[NutritionFactsJson]
    
    transFat: Optional[NutritionFactsJson]
    
    cholesterol: Optional[NutritionFactsJson]
    
    sodium: Optional[NutritionFactsJson]
    
    totalCarbohydrate: Optional[NutritionFactsJson]
    
    dietaryFiber: Optional[NutritionFactsJson]
    
    totalSugars: Optional[NutritionFactsJson]
    
    addedSugars: Optional[NutritionFactsJson]
    
    protein: Optional[NutritionFactsJson]
    
    vitaminD: Optional[NutritionFactsJson]
    
    calcium: Optional[NutritionFactsJson]
    
    iron: Optional[NutritionFactsJson]
    
    potassium: Optional[NutritionFactsJson]
    
class Food(NS):
    id: str
    
    name: str
    
    calories: int
    
    servingSize: NutritionFactsJson
    
    nutritionFacts: NutritionFacts
    
    adminCreated: bool
