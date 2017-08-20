from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/$', views.usersignup, name="signup"),
	url(r'^login/$', views.userlogin, name="login"),
	url(r'^logout/$', views.userlogout, name="logout"),
	url(r'^placeholder/$', views.placeholder, name="placeholder"),
	url(r'^create/bean/$', views.doing_gods_work_bean, name="bean"),
	url(r'^create/powder/$', views.doing_gods_work_powder, name="powder"),
	url(r'^create/roast/$', views.doing_gods_work_roast, name="roast"),
	url(r'^create/syrup/$', views.doing_gods_work_syrup, name="syrup"),
	url(r'^create/coffee/$', views.create_coffee, name="coffee"),
	url(r'^list/$', views.coffee_list, name="list"),
	url(r'^coffee/detail/(?P<coffee_id>\d+)/$', views.coffee_detail, name="detail"),
	url(r'^update/bean/(?P<bean_id>\d+)/$', views.updating_gods_work_bean, name="update_bean"),
	url(r'^update/powder/(?P<powder_id>\d+)/$', views.updating_gods_work_powder, name="update_powder"),
	url(r'^update/roast/(?P<roast_id>\d+)/$', views.updating_gods_work_roast, name="update_roast"),
	url(r'^update/syrup/(?P<syrup_id>\d+)/$', views.updating_gods_work_syrup, name="update_syrup"),
	url(r'^delete/coffee/(?P<coffee_id>\d+)/$', views.the_ol_mallet, name="delete_coffee"),
	url(r'^delete/bean/(?P<bean_id>\d+)/$', views.bean_delete, name="delete_bean"),






	]