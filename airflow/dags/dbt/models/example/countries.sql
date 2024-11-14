
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with countries as (
    select 1 as speaker_id, 'Poland' as name
    union all
    select 2 as speaker_id, 'Germany' as name
    union all
    select 3 as speaker_id, 'France' as name
    union all
    select 4 as speaker_id, 'Spain' as name
)
select * from countries