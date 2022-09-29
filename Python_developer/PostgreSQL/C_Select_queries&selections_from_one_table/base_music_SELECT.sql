-- название и год выхода альбомов, вышедших в 2018 году
SELECT
	name_album,
	year_release
FROM
	album
WHERE TO_CHAR(year_release, 'YYYY') = '2018'
;

-- название и продолжительность самого длительного трека
SELECT
	name_track,
	duration
FROM
	track
WHERE duration = (SELECT MAX(duration) FROM track)
;

-- название треков, продолжительность которых не менее 3,5 минуты
SELECT
	name_track,
	duration
FROM
	track
WHERE duration > 3.5
ORDER BY duration
;

-- названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT
	name_collection,
	year_release
FROM
	collection
WHERE year_release BETWEEN '2018-01-01' AND '2020-12-31'
;

-- исполнители, чье имя состоит из 1 слова
SELECT
	name_artist
FROM
	artist
WHERE name_artist NOT LIKE '% %'
;

-- название треков, которые содержат слово "мой"/"my"
SELECT
	name_track
FROM
	track
WHERE name_track ~* '.*мой.*' OR name_track ~* '.*my.*'
;
