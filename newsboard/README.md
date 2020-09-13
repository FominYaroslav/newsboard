# Text analyzer
Web-application with list of news.

# To start:
 To start, project requires docker-compose to be installed on you PC.
 1. Download files from repository
 2. Run: docker-compose up -d --build
 3. Do migration in DB: run docker-compose exec web python manage.py migrate --noinput
 4. Create user: docker-compose exec web python manage.py createsuperuser
 5. Open in browser "localhost:8000
 
# API endpoints
 - GET "/news" - view list of all news
 - POST "/news" - create news
 - GET "/news/[news_id]" view news by id
 - PUT, DELETE "/news/[news_id]" - update/delete  news by id (only for author of news)
 - POST "/news/[news_id]/upvote" - upvote for news by id (only for authorized)
 - GET "/news/[news_id]/comments" view comments for news by id of news
 - POST "/news/[news_id]/comments" create comments for news by id of news (only for authorized)
 - GET "/comment/[comment_id]" view comment by id of comment
 - PUT, DELETE "/comment/[comment_id]" update/delete comment by id (only for author of comment)



