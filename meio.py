from behave import given, when, then


@given(u'os numeros 10 e 50 e 80')
def primeiro(context):
    context.n1 = 10
    context.n2 = 50
    context.n3 = 80
    context.result = 0


@when(u'verifico, os mesmos')
def segundo(context):
    a1 = context.n1
    a2 = context.n2
    a3 = context.n3
    context.resulta = context.result
    if (a1 > a2):
        if (a1 > a3):
            return context.resulta == a1
    if (a2 > a1):
        if (a2 > a3):
            return context.resulta == a2

    if (a3 > a1):
        if (a3 > a2):
            return context.resulta == a3


@then(u'descubro que o do meio é 50')
def terceiro(context):
    context.resulto = context.resulta
    print('do meio é : '+str(context.resulto))
