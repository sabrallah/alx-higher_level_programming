-- Lists all shows and their ratings from the database hbtn_0d_tvshows
-- Uses an INNER JOIN to match tv_shows and tv_show_ratings
-- Orders results alphabetically by show title

SELECT 
   tv_shows.title,
   tv_show_ratings.rating
FROM
   tv_shows
   INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
ORDER BY
   tv_shows.title;
