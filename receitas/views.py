from django.shortcuts import render
from datetime import datetime
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(req):
    return render(req, 'filho.html')

def controle(req):
    lista = [1, 2, 6, 'teste', 10]
    hoje = datetime.now()
    return render(req, 'controle.html', {
        'variavel': lista,
        'agora': hoje
    })

from django.shortcuts import redirect, render
from .forms import models
from .forms import PostForm
from .models import Post

@login_required(login_url='/contas/login')
def criar_post(request:HttpRequest):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if (form.is_valid):
            post:Post = form.save(commit = False)
            post.autor = request.user
            post.save()
            return redirect("postar")
    else:
        form = PostForm()

    return render(request, "postar.html", {"form": form})


def inicio(req):
    posts = models.Post.objects.filter(aprovado = False).all()
    return render(req, "inicio.html", {"posts": posts})
