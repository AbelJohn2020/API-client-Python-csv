import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    ''' Manages the clients lifecycle '''
    pass


@clients.command()
@click.option(  '-u', 
                '--username',
                type=str,
                prompt=True,
                help='The client username is: ')
@click.option(  '-p', 
                '--password',
                type=str,
                prompt=True,
                help='The client password is: ')
@click.option(  '-n', 
                '--name',
                type=str,
                prompt=True,
                help='The client name is: ')
@click.option(  '-c', 
                '--company',
                type=str,
                prompt=True,
                help='The client company is: ')
@click.option(  '-y', 
                '--city',
                type=str,
                prompt=True,
                help='The client city is: ')
@click.option(  '-e', 
                '--email',
                type=str,
                prompt=True,
                help='The client email is: ')
@click.option(  '-n', 
                '--position',
                type=str,
                prompt=True,
                help='The client position is: ')
@click.option(  '-a', 
                '--age',
                type=str,
                prompt=True,
                help='The client age is: ')
@click.pass_context
def create(ctx, username, password, name, company, city, email, position, age):
    ''' Create a new client '''
    client=Client(username, password, name, company, city, email, position, age)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def read(ctx):
    ''' List all clients '''
    client_services = ClientService(ctx.obj['clients_table'])

    clients_list = client_services.read_clients()

    click.echo(' ID                                     |   USERNAME    |   PASSWORD    |   NAME        |   COMPANY     |   CITY    |   EMAIL   |   POSITION    |   AGE ')
    click.echo('*' * 156)

    for client in clients_list:
        click.echo('{uid}   |   {username}  |  {password}  |   {name}  |   {company}  |   {city}  |   {email} |   {position}  |   {age}'.format(
            uid=client['uid'],
            username=client['username'],
            password=client['password'],
            name=client['name'],
            company=client['company'],
            city=client['city'],
            email=client['email'],
            position=client['position'],
            age=client['age'],
        ))


@clients.command()
@click.argument('client_uid', 
                    type=str)
@click.pass_context
def update(ctx, client_uid):
    ''' Updates a client '''
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.read_clients()

    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.username = click.prompt('New username', type=str, default=client.username)
    client.password = click.prompt('New password', type=str, default=client.password)
    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.city = click.prompt('New city', type=str, default=client.city)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)
    client.age = click.prompt('New age', type=str, default=client.age)

    return client


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    ''' Deletes a client '''
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.read_clients()

    client = [ client for client in client_list if client['uid'] == client_uid]

    if client:
        client_service.delete_client(Client(**client[0]))
        click.echo('Client deleted')
    else:
        click.echo('Client not found')

#PEP8 - CODIGO LEGIBLE Y ENTENDIBLE POR OTROS PROGRAMADORES / PEP257 - GENERAR BUENA DOCUMENTACION EN NUESTRO CODIGO /PEP20 - IMPORT THIS
all = clients