select (CASE  WHEN count(1) BETWEEN 20 and 9223372036854775807 THEN sum(CASE kind WHEN 'caught' THEN 1 ELSE 0 END)*100/count(1) ELSE 0 END) as caught, 
  (CASE  WHEN count(1) BETWEEN 20 and 9223372036854775807 THEN sum(CASE kind WHEN 'bowled' THEN 1 ELSE 0 END)*100/count(1) ELSE 0 END) as bowled, 
  (CASE  WHEN count(1) BETWEEN 20 and 9223372036854775807 THEN sum(CASE kind WHEN 'lbw' THEN 1 ELSE 0 END)*100/count(1) ELSE 0 END) as lbw, 
  (CASE  WHEN count(1) BETWEEN 20 and 9223372036854775807 THEN sum(CASE kind WHEN 'run out' THEN 1 ELSE 0 END)*100/count(1) ELSE 0 END) as run_out, 
  (CASE  WHEN count(1) BETWEEN 20 and 9223372036854775807 THEN sum(CASE kind WHEN 'retired hurt' THEN 1 ELSE 0 END)*100/count(1) ELSE 0 END) as retired_hurt, 
  (CASE  WHEN count(1) BETWEEN 20 and 9223372036854775807 THEN sum(CASE kind WHEN 'stumped' THEN 1 ELSE 0 END)*100/count(1) ELSE 0 END) as stumped, 
  (CASE  WHEN count(1) BETWEEN 20 and 9223372036854775807 THEN sum(CASE kind WHEN 'caught and bowled' THEN 1 ELSE 0 END)*100/count(1) ELSE 0 END) as c_b, 
  (CASE  WHEN count(1) BETWEEN 20 and 9223372036854775807 THEN sum(CASE kind WHEN 'hit wicket' THEN 1 ELSE 0 END)*100/count(1) ELSE 0 END) as hit_wicket, 
  (CASE  WHEN count(1) BETWEEN 20 and 9223372036854775807 THEN sum(CASE kind WHEN 'obstructing the field' THEN 1 ELSE 0 END)*100/count(1) ELSE 0 END) as otf, count(1), player from wickets group by player order by -bowled limit 10;