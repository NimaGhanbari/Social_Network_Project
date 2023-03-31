from django.shortcuts import render,get_object_or_404
from .models import Post, Post_File , Comment
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostsSerializer,PostSerSerializer,CommentSerializer,ParCommentSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized = PostsSerializer(
            posts, many=True, context={'request': request})
        return Response(serialized.data)


class PostForMe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.filter(user=request.user)
        serialized = PostsSerializer(
            posts, many=True, context={'request': request})
        return Response(serialized.data)

#برای اضافه کردن پست به کار میرود
class AddPostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        title = request.data.get('title')
        avatar = request.data.get('avatar')
        caption = request.data.get('caption')
        is_active = request.data.get('is_active')
        is_public = request.data.get('is_public')
        if request.data.get('is_active') == None:
            is_active = True
        if request.data.get('is_public') == None:
            is_public = True
        
        post = Post.objects.create(title=title, user=request.user,
                                   caption=caption, is_active=is_active, is_public=is_public)
        post.save()
        return Response({'title': 'The post was successfully registered'})

#برای اضافه کردن پست به کار میرود
class PostSerView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        post = Post.objects.get(pk=pk,user=request.user)
        serialized = PostsSerializer(post, context={'request': request})
        return Response(serialized.data)
        
    
    def post(self,request):
        serialized = PostSerSerializer(data=request.data)
        if serialized.is_valid(raise_exception=True):
            serialized.save(user=request.user)
            return Response({'detail':'succesfully'})
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self,request,pk):
        post = get_object_or_404(Post,pk=pk,user=request.user)
        serializer = PostsSerializer(post,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,pk):
        post = get_object_or_404(Post,pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'title':'not found'},status=status.HTTP_404_NOT_FOUND)
        #comments = post.comments.filter(is_approved=True)
        comments = Comment.objects.filter(post=post,is_approved=True)
        serialized = CommentSerializer(comments,many=True, context={'request': request})
        return Response(serialized.data)
    
    def post(self,request,pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'title':'not found'},status=status.HTTP_404_NOT_FOUND)
        serialized = CommentSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save(post=post, user=request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


class CommentReply(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,pk_post,pk_comment):
        post = get_object_or_404(Post,pk=pk_post)
        comment = get_object_or_404(Comment,pk=pk_comment,post=post)
        serialized = ParCommentSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save(parentComment= comment,user=request.user)
            return Response({'title':'mission accomplished.'},status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    