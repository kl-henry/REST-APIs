-- SelectSonnendaten source
drop view SelectSonnendaten;

CREATE VIEW SelectSonnendaten AS
SELECT
	ort.name_ort as ortsname,
	astrodata.fk_id_ort,
	strftime('%d.%m.%Y', date(astrodata.datum, 'unixepoch')) as Datum,
	astrodata.sunrise_date as Sonnenaufgang,
	astrodata.sunrise_time as SonnenaufgangZeit,
	astrodata.sunset_date as Sonnenuntergang,
	astrodata.sunset_time  as SonnenuntergangZeit,
	astrodata.datum 
from
	ort,
	astrodata
where
	astrodata.fk_id_ort = ort.id_ort
	order by astrodata.datum asc;