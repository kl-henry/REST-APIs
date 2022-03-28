-- SelectSonnendaten source
drop view SelectSonnendaten ;

CREATE VIEW SelectSonnendaten AS
SELECT
	ort.name_ort as ortsname,
	astrodata.fk_id_ort,
	strftime('%d.%m.%Y', date(astrodata.datum, 'unixepoch')) as Datum,
	strftime('%d.%m.%Y', date(astrodata.sunrise, 'unixepoch')) as Sonnenaufgang,
	strftime('%H-%M-%S', date(astrodata.sunrise, 'unixepoch')) as SonnenaufgangZeit,
	strftime('%d.%m.%Y', date(astrodata.sunset, 'unixepoch')) as Sonnenuntergang
from
	ort,
	astrodata
where
	astrodata.fk_id_ort = ort.id_ort;