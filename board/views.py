from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings

from .models import Article


class ListView(LoginRequiredMixin, TemplateView):
    login_url = settings.LOGIN_URL
    template_name = 'articleList.html'

    def get(self, request, *args, **kwargs):
        request.session['is_logined'] = True
        queryset = Article.objects.all()
        data = {
            'articles': queryset,
            'listNum': 1
        }
        return self.render_to_response(data)


@method_decorator(csrf_exempt, name='dispatch')
class DetailAndDeleteView(LoginRequiredMixin, TemplateView):
    template_name = 'articleDetail.html'
    article_id = 'article_id'
    queryset = Article.objects.all()

    def searchObj(self):
        key = self.kwargs.get(self.article_id)
        return self.queryset.filter(id=key).first()

    def get(self, request, *args, **kwargs):
        article = self.searchObj()
        if not article:
            return Http404('not defined data | 데이터가 없습니다.')
        data = {
            'article': article
        }
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        target = self.searchObj()
        target.delete()
        return HttpResponseRedirect('/article/delete')


@method_decorator(csrf_exempt, name='dispatch')
class CreateUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'articleCreateUpdate.html'
    article_id = 'article_id'
    queryset = Article.objects.all()

    def searchObj(self):
        queryset = self.queryset
        key = self.kwargs.get(self.article_id)
        return queryset.filter(id=key).first()

    def get(self, request, *args, **kwargs):
        request.session.get('is_logined')
        article = self.searchObj()
        data = {
            'article': article
        }
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        postAction = request.POST.get('action')
        postData = {key: request.POST.get(key)
                    for key in ('title', 'content', 'author')}
        for key in postData:
            if not postData[key]:
                raise Http404('not defined  {}'.format(key))

        if postAction == 'create':
            article = Article.objects.create(**postData)
        elif postAction == 'update':
            article = self.searchObj()
            for key, value in postData.items():
                setattr(article, key, value)
            article.save()
        else:
            raise Http404('알 수 없는 요청')

        return HttpResponseRedirect('/article/')


class DeleteCompView(LoginRequiredMixin, TemplateView):
    template_name = 'deleteBoard.html'
