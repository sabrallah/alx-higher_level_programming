-- Select the genre and count the number of shows linked to each genre
SELECT genre, COUNT(*) AS number_of_shows
-- Join the tv_genres and tv_show_genres tables to get the genre information for each show
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Group the results by genre
GROUP BY genre
-- Filter out any genres that don't have any shows linked
HAVING COUNT(*) > 0
-- Sort the results in descending order by the number of shows linked
ORDER BY number_of_shows DESC;
