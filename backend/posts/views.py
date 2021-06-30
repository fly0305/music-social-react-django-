from django.shortcuts import render
from django.http import JsonResponse
#Auth dependencies
from rest_framework.decorators import api_view, permission_classes #for authenticated routes
from rest_framework.permissions import IsAuthenticated #for authenticated routes
from django.views.decorators.csrf import csrf_exempt #for authenticated routes
# API dependencies
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework import status
import json #Useful for POST and PUT requests
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps 
Users = apps.get_model('users', 'CustomUser')

# Create your views here.

# // @router  GET api/posts 
#             POST /posts
# // @desc    Get all posts
              # Create a post
# // @access  Private
@api_view(["GET", "POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all() # Get all posts
        serializer = PostSerializer(posts, many=True)
        # PROCESSING DATA IN WHICH FRONTEND CAN READ
        data = serializer.data
        for item in data:
            item["added_by"] = Users.objects.get(id=item["added_by"]).username
        return JsonResponse({'posts': data }, safe=False, status=status.HTTP_200_OK)
    else:
        pass
        # Put POST request logic here ! DO NOT FORGET

# // @router  GET /posts/:id
# // @desc    Get one post by ID
# // @access  Private
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_one_post(request, post_id):
    try:
        user = request.user
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        data = serializer.data
        data["added_by"] = Users.objects.get(id=data["added_by"]).username
        return JsonResponse({'posts': data }, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': "Sorry, this post doesn't exist. "}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# // @router  DELETE /posts/:id
# // @desc    Delete a post
# // @access  Private

# // @router  PUT /posts/like/:id
# // @desc    Like a post
# // @access  Private

# // @router  PUT /posts/unlike/:id
# // @desc    Unlike a post
# // @access  Private

# // @router  Posting COMMENTS - POST /posts/comment/:post_id
# // @desc    Comment on a post
# // @access  Private

# // @router  DELETE /posts/comment/:postid/:comment_id
# // @desc    Comment on a post
# // @access  Private
