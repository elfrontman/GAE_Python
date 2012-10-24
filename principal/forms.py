from util import djangoforms
from principal.models import *

class newProyecto(djangoforms.ModelForm):
	class Meta:
		model = Proyecto