-- Select the name column from the tv_genres table
-- Select the name column from the tv_genres table
SELECT tv_genres.name
-- Left join the tv_show_genres table on the genre_id column
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Left join the tv_shows table on the show_id column
LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
-- Filter the results to only include genres not linked to the show Dexter
WHERE tv_shows.title != 'Dexter' OR tv_shows.title IS NULL
-- Group the results by the genre name
GROUP BY tv_genres.name
-- Order the results in ascending order by the genre name
ORDER BY tv_genres.name;
