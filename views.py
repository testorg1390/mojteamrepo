# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from site_posts.models import Site_Posts
from permanent_data import *
from site_comment.models import Comment
from account_profile.models import Account_Profile
from site_ad.models import Site_Ad
import datetime
import uuid
# from site_category.models import Category

class index(View):
    def get(self,request):
        request.breadcrumbs("صفحه اصلی",request.path_info)
        lod = static_data()
        all_post = Site_Posts.objects.all()

        # ///////////////////////Paginator////////////////////////////////////////
        paginator = Paginator(all_post,5)
        page_number = paginator.num_pages
        page = request.GET.get('page')
        try:
            data_limit = paginator.page(page)
        except PageNotAnInteger:
            data_limit = paginator.page(1)
        except EmptyPage:
            data_limit = paginator.page(paginator.num_pages)

        post_comment_count = []
        for it in data_limit:
            post_comment_count.append({'id':it.id,'nazar_count':Comment.objects.filter(post_id=it.id).count()})

        print("all_post={}".format(all_post))
        print("post_comment_count={}".format(post_comment_count))
        ref_id = ''
        if request.user.is_authenticated:
            try:
                ref_id = Account_Profile.objects.get(account=request.user.id).ref_id
            except:
                pass

        ads = Site_Ad.objects.filter(status=1,engheza__lte=datetime.datetime.now())
        # print(ads[0].file)
        return render(request,'home.html',{'all_post':data_limit,'nazar_count':post_comment_count,'page_number':range(1,page_number+1),'ref':ref_id,'all_cat':lod.all_cat(),'all_menue':lod.all_menue(),'all_candidate':lod.post_candidate(),'last_posts':lod.last_post(),'ads':ads})

class about_me(View):
    def get(self,request):
        return render(request,'about_me.html')