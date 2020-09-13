from rest_framework import generics
from .serializer import UserSerializer, NewsSerializer, CommentSerializer
from newsapp.models import User, News, Comment
from django.http import JsonResponse
from rest_framework import permissions
from .serializer import IsAuthorOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.
class UserView(generics.ListAPIView):
    """
    Returns a list of all users.
    """

    model = User
    serializer_class = UserSerializer
    queryset = User.object.all()


class NewsView(generics.ListCreateAPIView):
    """
    Returns a list of all news.
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = News
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class OneNewsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns one news .
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentView(generics.ListCreateAPIView):
    """
    Returns a list of comments for news.
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        news_id = self.kwargs["pk"]
        queryset = Comment.objects.filter(news=news_id)
        print(f"len queryset {len(queryset)}")
        return queryset

    model = Comment
    serializer_class = CommentSerializer


class OneCommentView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@csrf_exempt
@login_required
@require_http_methods(["POST"])
def upvote(request, pk):
    print("request")
    news = News.objects.get(pk=pk)
    if news.upvoted.filter(username=request.user).exists():  # filter exists?
        return JsonResponse({"status_code": 403, "error": "You have already voted"})
    else:
        news.upvoted.add(request.user.id)
        return JsonResponse({"status_code": 200, "succes": "News upvoted"})


# json response
