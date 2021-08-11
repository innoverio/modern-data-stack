{{
  config(
    materialized='table',
    properties={
      "format": "'PARQUET'",
      "partitioning": "ARRAY['bucket(id, 2)']",
    }
  )
}}
select 
  * 
from {{ source('inventory', 'products') }}
WHERE weight < 5