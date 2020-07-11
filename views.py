from django.shortcuts import render


#cd into the flash folder on git and run it by the commannd "python manage.py runserver "

# Create your views here.
def home(request):
	return render(request, 'home.html', {})
def about(request):
	return render(request, 'about.html', {})

def add(request):

	from random import randint

	num_1 = randint(0,100)
	num_2 = randint(0, 100)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']


		if not answer:

			color = "warning"
			result = 'Something is wrong'
			motivation = "Not valid input"
			my_answer = "You forgot to fill out the form"


			return render(request, 'add.html', {
				'answer': answer, 
				'my_answer': my_answer,
				'num_1': num_1,
				'num_2': num_2,
				'color': color,
				'result': result,
				'motivation': motivation,

				#this returns straight to the front-end
			})



		if isinstance(answer, str):

			color = "warning"
			result = 'Something is wrong'
			motivation = "Not valid input"
			my_answer = "Doesn't look like you submitted a number:("


			return render(request, 'add.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation,
			})

		
		

		correct_answer = int(old_num_2) + int(old_num_1)

		if int(answer) == correct_answer:
			my_answer =  old_num_1 + "+" + old_num_2 + " equals " + answer
			color = "success"
			result = 'Correct!'
			motivation = "you rock! keep going!!"

			
			
		else:
			my_answer = old_num_1 + "+" + old_num_2 + " does not equal " + answer
			color = "danger"
			result = 'Incorrect'
			motivation = "Aww... try again!"

		

		return render(request, 'add.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation
					

				})


		# this is what passes our values back

	return render(request, 'add.html', {

		'num_1': num_1,
		'num_2': num_2,
#passing all the numerical values to the back and front-end

		})


def subtract(request):
	
	from random import randint

	num_1 = randint(0,100)
	num_2 = randint(0, 100)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']


		if not answer:

			color = "warning"
			result = 'Something is wrong'
			motivation = "Not valid input"
			my_answer = "You forgot to fill out the form"


			return render(request, 'subtract.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation,
			})



		if isinstance(answer, str):

			color = "warning"
			result = 'Something is wrong'
			motivation = "Not valid input"
			my_answer = "Doesn't look like you submitted a number:("


			return render(request, 'subtract.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation,
			})

		
		

		correct_answer = int(old_num_2) - int(old_num_1)

		if int(answer) == correct_answer:
			my_answer =  old_num_1 + "-" + old_num_2 + " equals " + answer
			color = "success"
			result = 'Correct!'
			motivation = "you rock! keep going!!"
	
		else:
			my_answer = old_num_1 + "-" + old_num_2 + " does not equal " + answer
			color = "danger"
			result = 'Incorrect'
			motivation = "Aww... try again!"

		return render(request, 'subtract.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation
			

			})


		# this is what passes our values back

	return render(request, 'subtract.html', {

		'num_1': num_1,
		'num_2': num_2,


		})

def divide(request):

	from random import randint

	num_1 = randint(0,100)
	num_2 = randint(0, 100)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']


		if not answer:

			color = "warning"
			result = 'Something is wrong'
			motivation = "Not valid input"
			my_answer = "You forgot to fill out the form"


			return render(request, 'divide.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation,
			})


		

		if isinstance(answer, str):

			color = "warning"
			result = 'Something is wrong'
			motivation = "Not valid input"
			my_answer = "Doesn't look like you submitted a number:("


			return render(request, 'divide.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation,
			})

		

		correct_answer = int(old_num_2)/int(old_num_1)

		if int(answer) == correct_answer:
			my_answer =  old_num_1 + "/" + old_num_2 + " equals " + answer
			color = "success"
			result = 'Correct!'
			motivation = "you rock! keep going!!"
	
		else:
			my_answer = old_num_1 + "/" + old_num_2 + " does not equal " + answer
			color = "danger"
			result = 'Incorrect'
			motivation = "Aww... try again!"

		return render(request, 'divide.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation
			

			})


	return render(request, 'divide.html', {

		'num_1': num_1,
		'num_2': num_2,


		})

def multiply(request):

	from random import randint

	num_1 = randint(0,100)
	num_2 = randint(0, 100)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']


		if not answer:

			color = "warning"
			result = 'Something is wrong'
			motivation = "Not valid input"
			my_answer = "You forgot to fill out the form"


			return render(request, 'multiply.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation,
			})



		if isinstance(answer, str):

			color = "warning"
			result = 'Something is wrong'
			motivation = "Not valid input"
			my_answer = "Doesn't look like you submitted a number:("


			return render(request, 'multiply.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation,
			})

		


		

		correct_answer = int(old_num_2) * int(old_num_1)

		if int(answer) == correct_answer:
			my_answer =  old_num_1 + "x" + old_num_2 + " equals " + answer
			color = "success"
			result = 'Correct!'
			motivation = "you rock! keep going!!"
	
		else:
			my_answer = old_num_1 + "x" + old_num_2 + " does not equal " + answer
			color = "danger"
			result = 'Incorrect'
			motivation = "Aww... try again!"

		return render(request, 'multiply.html', {
			'answer': answer, 
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			'result': result,
			'motivation': motivation
			

			})


	return render(request, 'multiply.html', {

		'num_1': num_1,
		'num_2': num_2,


		})

