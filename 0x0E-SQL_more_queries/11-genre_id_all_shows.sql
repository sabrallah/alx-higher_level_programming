-- Select the title and genre_id columns from the tv_shows and tv_show_genres tables
SELECT tv_shows.title, tv_show_genres.genre_id
-- Use a LEFT JOIN to combine the tv_shows and tv_show_genres tables
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Order the results by title and genre_id in ascending order
ORDER BY tv_shows.title, tv_show_genres.genre_id;
