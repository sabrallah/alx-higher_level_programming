-- Lists all genres from hbtn_0d_tvshows_rate by their rating
-- Uses two joins to link tv_genres to tv_show_ratings via tv_show_genres
-- Sums the rates for each genre to calculate overall rating
-- Groups by genre name to aggregate ratings per genre  
-- Orders genres by their calculated rating in descending order

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
