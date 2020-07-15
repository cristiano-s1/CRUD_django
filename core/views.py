from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto


class IndexView(ListView):
    models = Produto  # Trazer produtos do banco
    template_name = 'index.html'
    queryset = Produto.objects.all()  # queryset é consulta, objects.all( aqui inserir busca )
    context_object_name = 'produtos'  # Qual o nome que ira usar para recuperar os dados no template


# Cadastrar
class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')
# reverse_lazy -> Verifica a views da nossa rota e redirecionar para ela
# success_url -> Para onde vai ser redirecionado em caso de sucesso


# Atualizar
class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


# Deletar
class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')