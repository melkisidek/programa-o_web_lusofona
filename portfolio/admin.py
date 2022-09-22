from django.contrib import admin

from .models import Post, Pessoa



from .models import Licenciatura

from .models import Cadeira

from .models import Tfc

from .models import Aluno

from .models import Professor

admin.site.register(Post)

admin.site.register(Pessoa)

admin.site.register(Licenciatura)
admin.site.register(Cadeira)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Tfc)