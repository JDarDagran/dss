select c.name as country_name, SUM(sp.attendees_count) as attendees_count from {{ ref('countries') }} c
join {{ source('dss', 'session_performance' )}} sp on c.speaker_id = sp.speaker_id
GROUP BY c.name