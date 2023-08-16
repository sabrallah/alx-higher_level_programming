-- Lists all shows without the genre Comedy
-- Lists all shows without the genre Comedy
SELECT tv_shows.title 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id != 5
ORDER BY tv_shows.title ASC;
