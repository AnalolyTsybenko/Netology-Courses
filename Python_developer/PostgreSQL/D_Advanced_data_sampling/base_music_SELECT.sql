-- количество исполнителей в каждом жанре
SELECT
	name_genre, COUNT(artist_id) AS count_artists
FROM
	genre
JOIN genre_artist USING(genre_id)
GROUP BY name_genre;

-- количество треков, вошедших в альбомы 2019-2020 годов
SELECT
	name_album, year_release, COUNT(name_track) AS count_track
FROM
	album
JOIN track USING(album_id)
WHERE year_release BETWEEN '2019-01-01' AND '2020-12-31'
GROUP BY name_album, year_release;

-- средняя продолжительность треков по каждому альбому
SELECT
	name_album, ROUND(AVG(duration), 2) AS avg_duration_track
FROM
	album
JOIN track USING(album_id)
GROUP BY name_album;

-- все исполнители, которые не выпустили альбомы в 2020 году
SELECT DISTINCT
	name_artist
FROM
	artist
JOIN artist_album USING(artist_id)
JOIN album USING(album_id)
WHERE artist_id NOT IN
	(
		SELECT artist_id
		FROM artist_album
		JOIN album USING(album_id)
		WHERE TO_CHAR(album.year_release, 'YYYY') LIKE '%2020%'
	);

-- названия сборников, в которых присутствует конкретный исполнитель (выберите сами)
SELECT DISTINCT
	name_collection, name_artist
FROM
	collection
JOIN track_collection USING(collection_id)
JOIN track USING(track_id)
JOIN album USING(album_id)
JOIN artist_album USING(album_id)
JOIN artist USING(artist_id)
WHERE name_artist LIKE '%Prodigy';

-- название альбомов, в которых присутствуют исполнители более 1 жанра
SELECT
	name_album, name_artist, COUNT(name_genre) AS count_genre
FROM
	album
JOIN artist_album USING(album_id)
JOIN artist USING(artist_id)
JOIN genre_artist USING(artist_id)
JOIN genre USING(genre_id)
GROUP BY name_album, name_artist
HAVING COUNT(name_genre) > 1;

-- наименование треков, которые не входят в сборники
SELECT
	name_track
FROM
	track
JOIN track_collection USING(track_id)
WHERE track_collection.collection_id IS NUll
GROUP BY name_track;

-- исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
SELECT
	name_artist, duration
FROM
	artist
JOIN artist_album USING(artist_id)
JOIN album USING(album_id)
JOIN track USING(album_id)
WHERE duration =
	(
		SELECT MIN(duration)
		FROM track
	)
GROUP BY name_artist, duration;

-- название альбомов, содержащих наименьшее количество треков
SELECT
	name_album, COUNT(name_track) AS count_track
FROM
	album
JOIN track USING (album_id)
GROUP BY name_album
HAVING COUNT(name_track) =
	(
		SELECT COUNT(name_track) AS count_track_HAV
		FROM album
		JOIN track USING(album_id)
		GROUP BY name_album
		ORDER BY count_track_HAV
		LIMIT 1
	);
