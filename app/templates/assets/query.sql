with eventCnt(rateder , event , cnt, rn) as
	(
		select
			rateder , event , cnt,
			row_number() over(partition by rateder order by cnt desc) rn
		from
			(
				select distinct
					rateder,
					event,
					count(1) over(partition by rateder, event) cnt
				from reaction
				where 1=1
					and datetime(event_datetime) between DATETIME('now', '-7 day') and DATETIME('now')
			)
	)
    select
	a.rateder,
	a.toplamoy,
	b.event as oy1_tip,
	b.cnt as oy1_sayi,
	c.event as oy2_tip,
	c.cnt as oy2_sayi,
	d.event as oy3_tip,
	d.cnt as oy3_sayi,
	e.event as oy4_tip,
	e.cnt as oy4_sayi,
	f.event as oy5_tip,
	f.cnt as oy5_sayi
from
	(
		select
			r.rateder,
			count(1) toplamOy
		from reaction r
		where 1=1
			and datetime(event_datetime) between DATETIME('now', '-7 day') and DATETIME('now')
		group by rateder
		order by count(1) desc
		limit 5
	) a
	left join eventCnt b on a.rateder = b.rateder and b.rn=1
	left join eventCnt c on a.rateder = c.rateder and c.rn=2
	left join eventCnt d on a.rateder = d.rateder and d.rn=3
	left join eventCnt e on a.rateder = e.rateder and e.rn=4
	left join eventCnt f on a.rateder = f.rateder and f.rn=5