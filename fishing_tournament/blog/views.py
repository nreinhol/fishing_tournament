from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from . import data
from . import data_utils
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-date_posted']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['fish_type', 'fish_length', 'img']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['fish_type', 'fish_length', 'img']
    success_url = '/posts'
    template_name = 'blog/post_form_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def dashboard(request):
    RankingList = data.RankingList(request)
    context = {
        'UserDataContainer': data.get_user_data_container(request),
        'Usernames': RankingList.usernames,
        'Scores': RankingList.scores,
    }
    return render(request, 'blog/dashboard.html', context)


@login_required
def dashboard_2020(request):
    year = 2020
    RankingList = data.RankingList(request, year)
    context = {
        'UserDataContainer': data.get_user_data_container(request, year),
        'Usernames': RankingList.usernames,
        'Scores': RankingList.scores,
        'Winner': RankingList.winner,
        'WinnerScore': RankingList.winner_score,
        'AllFishes': data_utils.get_len_of_all_posts_of_year(request, year)
    }
    return render(request, 'blog/dashboard_2020.html', context)

@login_required
def dashboard_2021(request):
    year = 2021
    RankingList = data.RankingList(request, year)
    context = {
        'UserDataContainer': data.get_user_data_container(request, year),
        'Usernames': RankingList.usernames,
        'Scores': RankingList.scores,
        'Winner': RankingList.winner,
        'WinnerScore': RankingList.winner_score,
        'AllFishes': data_utils.get_len_of_all_posts_of_year(request, year)
    }
    return render(request, 'blog/dashboard_2021.html', context)


@login_required
def dashboard_2022(request):
    year = 2022
    RankingList = data.RankingList(request, year)
    context = {
        'UserDataContainer': data.get_user_data_container(request, year),
        'Usernames': RankingList.usernames,
        'Scores': RankingList.scores,
        'Winner': RankingList.winner,
        'WinnerScore': RankingList.winner_score,
        'AllFishes': data_utils.get_len_of_all_posts_of_year(request, year)
    }
    return render(request, 'blog/dashboard_2022.html', context)


@login_required
def dashboard_2023(request):
    year = 2023
    RankingList = data.RankingList(request, year)
    context = {
        'UserDataContainer': data.get_user_data_container(request, year),
        'Usernames': RankingList.usernames,
        'Scores': RankingList.scores,
        'Winner': RankingList.winner,
        'WinnerScore': RankingList.winner_score,
        'AllFishes': data_utils.get_len_of_all_posts_of_year(request, year)
    }
    return render(request, 'blog/dashboard_2023.html', context)


@login_required
def table(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/table.html', context)


@login_required
def rules(request):
    return render(request, 'blog/rules.html')


@login_required
def statistic(request):
    RankingList = data.RankingList(request)
    context = {
        'LongestFishes': data.Statistics(request).longest_fishes,
        'TotalAmountFishType': data.Statistics(request).total_amount_fish_type,
        'MonthlyDistribution': data.Statistics(request).monthly_distribution,
        'DateLength': data.Statistics(request).date_length
    }
    return render(request, 'blog/statistic.html', context)
