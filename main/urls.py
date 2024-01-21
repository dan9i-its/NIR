
from django.urls import path 
from . import views 
from .views import RegisterView
app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('ssrf', views.ssrf, name='ssrf'),
    path('scans', views.scans, name='scans'),
    path('zap', views.zap, name='zap'),
    path('zap_results/<int:zap_results_id>/', views.zap_results, name='zap_results'),
    path('zap_full_results/<int:scan_full_results_id>/', views.zap_full_results, name='zap_full_results'),
    path('nuclei', views.nuclei, name='nuclei'),
    path('create', views.create, name='create'),
    path('crawl', views.crawl, name='crawl'),
    path('nuclei_resulsts/<int:nuclei_results_id>/', views.nuclei_results, name='nuclei_results'),
    path('crawl_scan/<int:crawl_results_id>/', views.crawl_results, name='crawl_results'),
    path('logout_page', views.logout_page, name='logout_page'),
    path('register', RegisterView.as_view(), name='register'),
    path('generate', views.generate, name='generate'),
    path('get_sessions', views.get_sessions, name='get_sessions'),

    path('scans1', views.scans1, name='scans1'),
    path('ssrf1', views.ssrf1, name='ssrf1'),
    path('zap1', views.zap1, name='zap1'),
    path('zap_results1/<int:zap_results_id>/', views.zap_results1, name='zap_results1'),
    path('zap_full_results1/<int:scan_full_results_id>/', views.zap_full_results1, name='zap_full_results1'),
    path('nuclei1', views.nuclei1, name='nuclei1'),
    path('create1', views.create1, name='create1'),
    path('crawl1', views.crawl1, name='crawl1'),
    path('nuclei_resulsts1/<int:nuclei_results_id>/', views.nuclei_results1, name='nuclei_results1'),
    path('crawl_scan1/<int:crawl_results_id>/', views.crawl_results1, name='crawl_results1'),
    path('logout_page1', views.logout_page1, name='logout_page1'),



    path('scans2', views.scans2, name='scans2'),
    path('zap2', views.zap2, name='zap2'),
    path('zap_results2/<int:zap_results_id>/', views.zap_results2, name='zap_results2'),
    path('zap_full_results2/<int:scan_full_results_id>/', views.zap_full_results2, name='zap_full_results2'),
    path('nuclei2', views.nuclei2, name='nuclei2'),
    path('create2', views.create2, name='create2'),
    path('crawl2', views.crawl2, name='crawl2'),
    path('nuclei_resulsts2/<int:nuclei_results_id>/', views.nuclei_results2, name='nuclei_results2'),
    path('crawl_scan2/<int:crawl_results_id>/', views.crawl_results2, name='crawl_results2'),
    path('logout_page2', views.logout_page2, name='logout_page2'),




    path('scans3', views.scans, name='scans3'),
    path('zap3', views.zap, name='zap3'),
    path('zap_results3/<int:zap_results_id>/', views.zap_results3, name='zap_results3'),
    path('zap_full_results3/<int:scan_full_results_id>/', views.zap_full_results3, name='zap_full_results3'),
    path('nuclei3', views.nuclei3, name='nuclei3'),
    path('create3', views.create3, name='create3'),
    path('crawl3', views.crawl3, name='crawl3'),
    path('nuclei_resulsts3/<int:nuclei_results_id>/', views.nuclei_results3, name='nuclei_results3'),
    path('crawl_scan3/<int:crawl_results_id>/', views.crawl_results3, name='crawl_results3'),
    path('logout_page3', views.logout_page3, name='logout_page3'),



    # path('scans', views.scans, name='scans'),
    # path('zap', views.zap, name='zap'),
    # path('zap_results/<int:zap_results_id>/', views.zap_results, name='zap_results'),
    # path('zap_full_results/<int:scan_full_results_id>/', views.zap_full_results, name='zap_full_results'),
    # path('nuclei', views.nuclei, name='nuclei'),
    # path('create', views.create, name='create'),
    # path('crawl', views.crawl, name='crawl'),
    # path('nuclei_resulsts/<int:nuclei_results_id>/', views.nuclei_results, name='nuclei_results'),
    # path('crawl_scan/<int:crawl_results_id>/', views.crawl_results, name='crawl_results'),
    # path('logout_page', views.logout_page, name='logout_page'),



    # path('scans', views.scans, name='scans'),
    # path('zap', views.zap, name='zap'),
    # path('zap_results/<int:zap_results_id>/', views.zap_results, name='zap_results'),
    # path('zap_full_results/<int:scan_full_results_id>/', views.zap_full_results, name='zap_full_results'),
    # path('nuclei', views.nuclei, name='nuclei'),
    # path('create', views.create, name='create'),
    # path('crawl', views.crawl, name='crawl'),
    # path('nuclei_resulsts/<int:nuclei_results_id>/', views.nuclei_results, name='nuclei_results'),
    # path('crawl_scan/<int:crawl_results_id>/', views.crawl_results, name='crawl_results'),
    # path('logout_page', views.logout_page, name='logout_page'),




    # path('', views.index, name='home'),
    # path('scans', views.scans, name='scans'),
    # path('zap', views.zap, name='zap'),
    # path('zap_results/<int:zap_results_id>/', views.zap_results, name='zap_results'),
    # path('zap_full_results/<int:scan_full_results_id>/', views.zap_full_results, name='zap_full_results'),
    # path('nuclei', views.nuclei, name='nuclei'),
    # path('create', views.create, name='create'),
    # path('crawl', views.crawl, name='crawl'),
    # path('nuclei_resulsts/<int:nuclei_results_id>/', views.nuclei_results, name='nuclei_results'),
    # path('crawl_scan/<int:crawl_results_id>/', views.crawl_results, name='crawl_results'),
    # path('logout_page', views.logout_page, name='logout_page'),
    # path('register', RegisterView.as_view(), name='register'),




    # path('', views.index, name='home'),
    # path('scans', views.scans, name='scans'),
    # path('zap', views.zap, name='zap'),
    # path('zap_results/<int:zap_results_id>/', views.zap_results, name='zap_results'),
    # path('zap_full_results/<int:scan_full_results_id>/', views.zap_full_results, name='zap_full_results'),
    # path('nuclei', views.nuclei, name='nuclei'),
    # path('create', views.create, name='create'),
    # path('crawl', views.crawl, name='crawl'),
    # path('nuclei_resulsts/<int:nuclei_results_id>/', views.nuclei_results, name='nuclei_results'),
    # path('crawl_scan/<int:crawl_results_id>/', views.crawl_results, name='crawl_results'),
    # path('logout_page', views.logout_page, name='logout_page'),
    # path('register', RegisterView.as_view(), name='register'),




    # path('', views.index, name='home'),
    # path('scans', views.scans, name='scans'),
    # path('zap', views.zap, name='zap'),
    # path('zap_results/<int:zap_results_id>/', views.zap_results, name='zap_results'),
    # path('zap_full_results/<int:scan_full_results_id>/', views.zap_full_results, name='zap_full_results'),
    # path('nuclei', views.nuclei, name='nuclei'),
    # path('create', views.create, name='create'),
    # path('crawl', views.crawl, name='crawl'),
    # path('nuclei_resulsts/<int:nuclei_results_id>/', views.nuclei_results, name='nuclei_results'),
    # path('crawl_scan/<int:crawl_results_id>/', views.crawl_results, name='crawl_results'),
    # path('logout_page', views.logout_page, name='logout_page'),
    # path('register', RegisterView.as_view(), name='register'),




    #     path('', views.index, name='home'),
    # path('scans', views.scans, name='scans'),
    # path('zap', views.zap, name='zap'),
    # path('zap_results/<int:zap_results_id>/', views.zap_results, name='zap_results'),
    # path('zap_full_results/<int:scan_full_results_id>/', views.zap_full_results, name='zap_full_results'),
    # path('nuclei', views.nuclei, name='nuclei'),
    # path('create', views.create, name='create'),
    # path('crawl', views.crawl, name='crawl'),
    # path('nuclei_resulsts/<int:nuclei_results_id>/', views.nuclei_results, name='nuclei_results'),
    # path('crawl_scan/<int:crawl_results_id>/', views.crawl_results, name='crawl_results'),
    # path('logout_page', views.logout_page, name='logout_page'),
    # path('register', RegisterView.as_view(), name='register'),
]
