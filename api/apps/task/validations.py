def validate_max_title(title):
	if len(title) > 70:
		print('debes de salir')
		raise ValueError(str('El título debe de ser menor a 70 caracteres'))

def validate_max_description(description):
	if len(description) > 200:
		raise ValueError(str('El título debe de ser menor a 200 caracteres'))

def validate_completed(completed):
	if completed!=True and completed!=False:
		print('Entro en la validacion del completed')
		raise ValueError(str('El campo "completed" debe de ser "true" or "false"'))