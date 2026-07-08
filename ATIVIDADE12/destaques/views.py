from django.shortcuts import render
from django.http import Http404

# Create your views here.

lista = [
    {
        'id': 1,
        'data_lancamento': '22 NOV',
        'titulo': 'mensagens para isabelle',
        'plataforma': 'netflix',
        'descrição': 'Leo e Isabelle viveram uma história de amor intensa, poética e interrompida abruptamente por um trágico acidente que levou a jovem à UTI, deixando-a em um coma profundo e irreversível segundo os médicos. Incapaz de aceitar a frieza dos diagnósticos e o silêncio do quarto de hospital, Leo descobre que a única forma de não desmoronar é continuar conversando com ela. Todos os dias, no mesmo horário, ele envia longas mensagens de áudio e texto para o celular de Isabelle, narrando sua rotina, relembrando memórias do passado, confessando seus medos mais profundos e reafirmando promessas de um futuro juntos.'
    },

    {
        'id': 2,
        'data_lancamento': '19 FEB',
        'titulo': 'off campus',
        'plataforma': 'netflix',
        'descrição': 'Bem-vindo à Universidade de Briar, onde o hóquei no gelo é uma religião, as festas na república Off-Campus são lendárias e o amor é o jogo mais imprevisível de todos. Acompanhe a jornada dos quatro astros do time de hóquei da faculdade — Garrett, Logan, Dean e Tucker — enquanto eles patinam entre a pressão do esporte profissional, os dramas da vida acadêmica e os romances avassaladores que mudam suas vidas para sempre.'
    },

    {
        'id': 3,
        'data_lancamento': '31 OUT',
        'titulo': 'continência ao amor',
        'plataforma': 'netflix',
        'descrição': 'Cassie é uma jovem musicista progressista que precisa de um plano de saúde urgente para tratar seu diabetes. Luke é um fuzileiro naval conservador com dívidas perigosas do passado. Apesar de viverem em mundos opostas e não se suportarem, os dois decidem forjar um casamento de conveniência para conseguir os benefícios financeiros e médicos oferecidos pelo exército. No entanto, quando Luke é gravemente ferido em combate e precisa voltar para casa, a farsa é posta à prova.'
    },

     {
        'id': 4,
        'data_lancamento': '09 SET',
        'titulo': 'teen wolf',
        'plataforma': 'netflix',
        'descrição': 'Scott McCall (Tyler Posey) é um adolescente comum e socialmente excluído que vive na misteriosa cidade de Beacon Hills e joga no banco de reservas do time de lacrosse da escola. Sua vida muda radicalmente em uma noite fria, quando seu melhor amigo hiperativo, Stiles Stilinski (Dylan OBrien), o arrasta para a floresta para ajudar a polícia a procurar um corpo desaparecido. Separado de Stiles, Scott é atacado e mordido no peito por uma criatura monstruosa na escuridão. No dia seguinte, ele começa a notar mudanças bizarras em seu próprio corpo: sentidos超humanos, cura acelerada, reflexos inacreditáveis e uma agressividade incontrolável.'
    },

     {
        'id': 5,
        'data_lancamento': '12 JUN',
        'titulo': 'mentirosos',
        'plataforma': 'netflix',
        'descrição': 'A rica, aristocrática e aparentemente perfeita família Sinclair tem uma tradição inabalável: passar todas as férias de verão em Beechwood Island, sua deslumbrante ilha particular na Nova Inglaterra. Sob o controle rígido e manipulador do patriarca Harris Sinclair, as aparências de felicidade escondem disputas gananciosas por herança e segredos sombrios. A jovem Cadence Sinclair (Emily Alyn Lind), herdeira da fortuna, vive os melhores momentos de sua vida na ilha ao lado de seus primos Johnny e Mirren, e de Gat, o sobrinho do namorado de sua tia. Juntos, os quatro formam um grupo inseparável apelidado de "Os Mentirosos". No entanto, durante o "verão dos quinze", um misterioso e terrível acidente deixa Cadence gravemente ferida, com amnésia profunda e dores de cabeça crônicas incapacitantes.'
    }
]

def destaques(request):

    contexto = {'lista':lista}
    return render(request, 'destaques/destaques.html', contexto)

def detalhes_destaques(request, id):
    destaques = None

    for item in lista:
        if item['id'] == id:
            destaques = item
            break

    if not destaques:
        raise Http404("destaque não encontrado")

    contexto = {'destaques': destaques}
    return render(request, 'destaques/detalhes_destaques.html', contexto)


