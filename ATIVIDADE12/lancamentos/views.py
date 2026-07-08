from django.shortcuts import render
from django.http import Http404

# Create your views here.

lista = [
    {
        'id': 1,
        'data_lancamento': '20 JUL',
        'titulo': 'the vampire diaries',
        'plataforma': 'netflix',
        'descrição': 'Quatro meses após o trágico acidente de carro que matou seus pais, a adolescente Elena Gilbert (Nina Dobrev) e seu irmão mais novo, Jeremy, tentam lidar com o luto e reconstruir suas vidas na pacata cidade de Mystic Falls, Virgínia. O ano letivo começa e Elena se sente instantaneamente atraída por Stefan Salvatore (Paul Wesley), um misterioso e charmoso aluno novo que esconde um segredo milenar: ele é um vampiro secular que tenta viver pacificamente entre os humanos.'
        
    },

    {
        'id': 2,
        'data_lancamento': '30 AGO',
        'titulo': 'The originals',
        'plataforma': 'netflix',
        'descrição': 'Derivada do sucesso The Vampire Diaries, esta série épica acompanha Klaus Mikaelson (Joseph Morgan), o híbrido original de vampiro e lobisomem, em seu retorno a Nova Orleans — a cidade vibrante e perigosa que ele e sua família ajudaram a construir séculos atrás. Atraído de volta por pistas sobre uma conspiração de bruxas contra ele, Klaus descobre que seu antigo protegido, o carismático e implacável Marcel Gerard (Charles Michael Davis), agora detém o controle absoluto sobre os vampiros, humanos e bruxas locais.'
    },

    {
        'id': 3,
        'data_lancamento': '15 MAR',
        'titulo': 'Supernatural',
        'plataforma': 'netflix',
        'descrição': 'Procurando um novo começo, Josh (Patrick Wilson) e Renai Lambert (Rose Byrne) se mudam com seus filhos para uma casa maior. O plano de uma vida tranquila é interrompido de forma drástica quando o primogênito, Dalton, sofre um misterioso acidente no sótão e entra em um coma inexplicável que desafia os médicos. Conforme os meses passam, fenômenos perturbadores e aparições aterrorizantes começam a assombrar a residência, convencendo a família de que o novo lar é amaldiçoado. Desesperados, eles decidem se mudar novamente, apenas para descobrir a verdade mais terrível de todas: o problema nunca foi a casa, mas sim o próprio menino. Dalton possui o raro dom da projeção astral e sua consciência está presa no "Além" (The Further), uma dimensão sombria de almas perdidas.'
    },
    {
        'id': 4,
        'data_lancamento': '18 ABR',
        'titulo': 'se não fosse você',
        'plataforma': 'netflix',
        'descrição': 'Baseado no aclamado romance de Colleen Hoover, o filme acompanha a complexa relação entre Morgan Grant e sua filha adolescente, Clara. Morgan engravidou aos 18 anos e abriu mão de seus sonhos para se dedicar à família, enquanto Clara tenta encontrar sua independência. A vida das duas vira de cabeça para baixo quando um acidente de carro trágico tira a vida de Chris (o marido de Morgan) e de Jenny (irmã de Morgan).'
    },

    {
        'id': 5,
        'data_lancamento': '23 DEZ',
        'titulo': 'Scooby doo na ilha dos zoombies',
        'plataforma': 'netflix',
        'descrição': 'O maior mistério da Mistério S.A. começa quando as máscaras caem. Após um longo período de separação, Fred, Velma, Daphne, Salsicha e Scooby-Doo se reúnem para salvar o programa de TV de Daphne com um furo jornalístico imbatível: encontrar um fantasma real. '
    }    

]

def lancamentos(request):
    contexto = {'lista':lista}
    return render(request, 'lancamentos/lista_lancamentos.html', contexto)

def detalhes(request, id):
    serie_encontrada = None

    for item in lista:
        if item['id'] == id:
            serie_encontrada = item
            break

    if not serie_encontrada:
        raise Http404("Série não encontrada")

    contexto = {'serie': serie_encontrada}
    return render(request, 'lancamentos/detalhes.html', contexto)


