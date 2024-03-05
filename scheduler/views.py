from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')

class Celula():
  item = None
  proximo = None

  def __init__(self,valor):
      self.item = valor

class Fila:
  inicio = None
  fim = None

  def __init__(self):
    self.inicio = None
    self.fim = None

  def EstaVazia(self):
    return self.inicio == None

  def inserir(self,valor):
    c = Celula(valor)
    if self.EstaVazia():
      self.fim = c
      self.inicio = c
    else:
      self.fim.proximo = c
      self.fim = c

  def remover(self):
    if self.EstaVazia():
      return None
    else:
      aux = self.inicio
      valor = self.inicio.item
      self.inicio = self.inicio.proximo
      return valor, aux


  def imprimir(self):
    aux = self.inicio
    list = []
    while aux != None:
      # print(aux.item)
      list.append(aux.item)
      aux = aux.proximo
      
    return list

def add_client_to_queue(fila,data_client):
    fila.inserir(data_client)
    
def complete_current_customer_service(fila):
    removed_client = fila.remover()
    return removed_client

queue_service = Fila()

def agendar(request):
    print(request.method)
    if request.method == 'POST':
        nome = request.POST['nome']
        servico = request.POST.getlist('servico')
        email = request.POST['email']
        celular = request.POST['celular']
        
        data_client = {
            'name': nome,
            'servico': servico,
            'email': email,
            'celular': celular
        }
        
        add_client_to_queue(queue_service,data_client)
        client_name = data_client['name']
        client_services = data_client['servico']
   
        print('$$$$$$$$$$$$$$$$444')
        print(queue_service.imprimir())
        
        return render(request, 'sucess.html', {'client_name': client_name,'client_services':client_services})
        
        # return render(request, 'scheduler/resultado_agendamento.html', {'clientes': all_clients})
        return HttpResponse('sucesso!')
    else:
        return render(request, 'scheduler.html')

def get_queue(request):
   return render(request, "get_queue.html")

def complete_service(request):
   return render(request, "complete_service.html")
