from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from post.forms import CommentForm
from .models import Post, Comment


def post_list(request):
    return render(
        request,
        'post/post_list.html',
        {
            'posts': Post.objects.all()
        }
    )

def comment_create(request, post_pk):
    # 요청 메서드가 POST방식일 때 처리
    if request.method == 'POST':
        # Post인스턴스를 가져오거나 404 Response를 돌려줌
        post = get_object_or_404(Post, pk=post_pk)

        # # request.POST에서 'content'키의 값을 가져옴
        # content = request.POST.get('content')
        # # 'content'키가 없었거나 내용이 입력되지 않았을 경우
        # if not content:
        #     # 400(BadRequest)로 응답을 전송
        #     return HttpResponse('댓글 내용을 입력하세요', status=400)

        # 위 방식 대신,  request.POST를  Form에 Bounding함
        comment_form = CommentForm(request.POST)
        #Form에 맞는 데이터가 바인딩 되어 있는지 검사
        if comment_form.is_valid():
            # 유효성 검사를 통과하면 Comment객체 생성 및 DB저장
            Comment.objects.create(
                post=post,
                # 작성자는 현재 요청의 사용자로 지정
                author=request.user,
                content=comment_form.cleaned_data['content']
        )
        # 정상적으로 Comment가 생성된 후
        # 'post' 네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동
        return redirect('post:post_list')
