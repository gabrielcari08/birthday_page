from django.shortcuts import render


def home_view(request):
    cards = [
        {
            'image': '/media/cards/1.jpeg',
            'text': 'Te amo!!! Te deseo un muy feliz cumpleaños'
        },
        {
            'image': '/media/cards/2.jpeg',
            'text': 'Gracias por todos esos momentos que vivimos, por nunca haberme dejado solo y estar en las buenas y en las malas. ❤️'
        },
        {
            'image': '/media/cards/3.jpeg',
            'text': 'Felices 18!!. Ahora estás más vieja, pero para mi seguís siendo una nenita chiquita con las cosas que haces y por tu forma de ser que tanto me encanta. 🥹'
        },
        {
            'image': '/media/cards/4.jpeg',
            'text': 'La ciencia dice que la materia no se crea ni se destruye, solo se transforma. Yo digo que mi amor por vos no para de crecer, lo que desafía completamente esas leyes. Sos la única persona por la que puedo salir mientras veo un partido de River, vos sabes muy bien que eso no lo hago ni loco, te das cuenta lo importante que sos?'
        },
        {
            'image': '/media/cards/5.jpeg',
            'text': 'Escribiría mil versos sobre el brillo de tus ojos y la paz que me da tu sonrisa. También escribiría un ensayo sobre cómo logras aguantar mis chistes malos sin salir corriendo.'
        },
        {
            'image': '/media/cards/6.jpeg',
            'text': 'Si el amor fuera un viaje, con vos me iría hasta el fin del mundo. Claro que, conociendo nuestro sentido de la orientación, probablemente nos perderíamos a las tres cuadras y terminaríamos buscando un lugar para comer sambui o panchos, je'
        },
        {
            'image': '/media/cards/7.jpeg',
            'text': 'Gracias de vuelta por todo lo que pasamos, por todas esas sonrisas que me sacás sin importar el humor. Por todas esas mañanas, tardes y noches donde salíamos sin tener un plan pero terminaban siendo los mejores días, espero podamos seguir teniendo muchas más experiencias lindas. Espero que seas feliz toda tu vida, te lo mereces por lo genial que sos!'
        },
        {
            'image': '/media/cards/8.jpeg',
            'text': 'En fin, sos el arte que no necesita museos y la risa que no necesita chistes. Podría ponerme súper profundo y decirte que sos el aire que respiro, pero prefiero decirte que sos la única persona con la que no me importa compartir comida o gaseosa Y eso, mi amor, es el nivel más alto de amor que un ser humano puede ofrecer (?). Felices 18 te amoOoOoooOO ❤️'
        },
    ]
    
    return render(request, 'home.html', {'cards': cards})
