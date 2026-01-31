from django.shortcuts import render, redirect

from .models import Topic, Entry
from forms import TopicForm

def index(request):
    """ 学习笔记主页 """
    return render(request, 'learning/index.html')

def topics(request):
    """ 显示所有主题 """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning/topics.html', context)

def topic(request, topic_id):
    """ 显示单个主题及所有的条目 """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning/topic.html', context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning:topics')
    
    context = {'form': form}
    return render(request, 'learning/new_topic.html', context)
