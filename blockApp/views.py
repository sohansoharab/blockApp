from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from blockApp.forms import UserForm, UserProfileInfoForm
from django.contrib import messages


# Create your views here.


class person():
	def __init__(self):
		self.name = str()
		self.age = int()

	def set_name(self, name):
		self.name = name
		print(f"Name set to {name}")


def index(request):

	ismail = person()
	ismail.set_name("ISMAIL")

	say = "hello madafaka"
	return render(request, 'blockApp/index.html', {
		'say': ismail
		})
 

def register(request):

	register = False

	if request.method == ['POST']:
		user_form = UserForm(request.POST)
		profile_form = UserProfileInfoForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			registered = True

			messages.add_message(request, messages.SUCCESS, 'Successfully registered')

			return HttpResponseRedirect(reverse('index'))


		elif user_form.cleaned_data['password'] != user_form.cleaned_data['confirm_password']:
			user_form.add_error('confirm_password', 'password do not match')

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request, 'blockApp/register.html', {
		'user_form': user_form,
		'profile_form': profile_form,
		'messages': messages,
		'registered': registered
		})