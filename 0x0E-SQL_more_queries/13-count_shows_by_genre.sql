-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- download (same as 12-no_genre.sql)

-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY COUNT(*) DESC;

