from django.db import migrations, models # models tem as ferramenta para trabalhar com as tabelas...

class CoursesManager(models.Manager):
	# usar search()
	def search(self, query):
		# return self.get_queryset().all()
		# busca com logico E. por padrão vírgula ',' é E
		# return elf.get_queryset().filter(
		#	name__icontains=query, description__icontains=query)
		# busca OU
		return self.get_queryset().filter(
			models.Q(name__icontains=query) | \
			models.Q(description__icontains=query))

# Create your models here.
class Courses(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição', blank=True)
	start_date = models.DateField(
		'Data de Início', null=True, blank=True
	)
	image = models.ImageField(
		upload_to='courses/images', verbose_name='Imagem',
		null=True, blank=True
	)
	created_at = models.DateTimeField(
		'Criando em', auto_now_add=True
	)
	update_at = models.DateTimeField('Atualizando em', auto_now=True)
	# padrão do banco para usar search()
	objects = CoursesManager()

	# classe retornar string
	def __str__(self):
		return self.name

	# classe Meta serve p modificar nomes para plurar(criei no plural)
	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		#ordenar
		ordering = ['name']