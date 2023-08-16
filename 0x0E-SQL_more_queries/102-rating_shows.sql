-- Lists all shows from the hbtn_0d_tvshows_rate database
-- Joins the tv_shows and tv_show_ratings tables to match the show IDs
-- Calculates the sum of the rates for each show to get its overall rating 
-- Groups the results by show title to aggregate the ratings per show
-- Orders the shows by their calculated rating in descending order

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id  
GROUP BY tv_shows.title
ORDER BY rating DESC;
