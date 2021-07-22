select 
  * 
from {{ source('inventory', 'products') }}
WHERE weight < 5