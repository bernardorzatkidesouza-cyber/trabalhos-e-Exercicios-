/*criar nova etrutura de bd revenda*/
1)criar tabelas

create table marca(
codigo serial not null,
nome varchar(50) not null,
primary key(codigo));

create table modelo(
codigo serial not null,
nome varchar(50) not null,
primary key(codigo));

create table automovel(
codigo serial not null,
placa varchar(10) not null,
codmarca int not null,
codmodelo int not null,
ano int not null,
cor varchar(20) not null,
combustivel varchar(20) not null,
valor numeric(10,2) not null,
foreign key(codmarca) references marca(codigo),
foreign key(codmodelo) references modelo(codigo));
2)inserts
insert into marca(nome) values ('Toyota');
insert into marca(nome) values ('Honda');
insert into marca(nome) values ('Ford');
insert into marca(nome) values ('Chevrolet');
insert into marca(nome) values ('Volkswagen');
insert into marca(nome) values ('Hyundai');
insert into marca(nome) values ('Nissan');
insert into marca(nome) values ('Fiat');
insert into marca(nome) values ('Renault');
insert into marca(nome) values ('Jeep');

select*from marca;

insert into modelo(nome) values ('Corolla');
insert into modelo(nome) values ('Civic');
insert into modelo(nome) values ('Focus');
insert into modelo(nome) values ('Cruze');
insert into modelo(nome) values ('Golf');
insert into modelo(nome) values ('HB20');
insert into modelo(nome) values ('Sentra');
insert into modelo(nome) values ('Argo');
insert into modelo(nome) values ('Kwid');
insert into modelo(nome) values ('Compass');

select*from modelo;

INSERT INTO automovel (placa, codmarca, codmodelo, ano, cor, combustivel, valor) VALUES 
('ABC1A23', 1, 1, 2020, 'Prata', 'Gasolina', 95000.00),
('BCD2B34', 2, 2, 2019, 'Preto', 'Flex', 87000.00),
('CDE3C45', 3, 3, 2018, 'Branco', 'Gasolina', 78000.00),
('DEF4D56', 4, 4, 2021, 'Vermelho', 'Flex', 92000.00),
('EFG5E67', 5, 5, 2022, 'Cinza', 'Gasolina', 105000.00),
('FGH6F78', 6, 6, 2023, 'Azul', 'Flex', 88000.00),
('GHI7G89', 7, 7, 2020, 'Prata', 'Gasolina', 89000.00),
('HIJ8H90', 8, 8, 2021, 'Branco', 'Flex', 65000.00),
('IJK9I01', 9, 9, 2022, 'Amarelo', 'Gasolina', 59000.00),
('JKL0J12', 10, 10, 2023, 'Verde', 'Diesel', 155000.00);

select * from automovel;

3)fazer alteraçoes no banco de dados(update)
a)alterar o valo do altomovel com placa'EFG5E67' para valor 120000

update automovel set valor=120000
where placa='EFG5E67';

b) alterar a cor do automóvel com placa 'IJK9I01' (para cor Branco).

update automovel set cor='Branco'
where placa='IJK9I01';

4)
pesquisa simples(select)

a)listar todas as marcas cadastradas
select*from marca;

b)listar nome de todos os modelos cadastrados
select nome from modelo;

c)listar todos os veiculos da cor 'Prata'
select codigo,placa,ano,cor,valor from automovel where cor='Prata';

d)listar todos os automoveis do combustivel 'Gaasolina'
select*from automovel
where combustivel='Gasolina';

e)listar todos os altomoveis do combustivel 'Diesel' com valor acima de 80000
select*from automovel where combustivel='Diesel' and valor>=80000;

5)pesquisas em multiplas tabelas(join)
a)mostrar os automoveis com suas respectivas marcas(INNER)

select automovel.placa,marca.nome,automovel.valor
from automovel
inner join marca on autmovel.codmarca=marca.codigo;

b)mostrar os automoveis com seus respectivos modelos(INNER)

select automovel.palca,modelo.nome,automovel.valor
from automovel
inner join modelo on automovel.codmodelo=modelo.codigo;

c)inserir novos registros na tabela marca e modelo

insert into marca(nome) values ('Peugeot');
insert into marca(nome) values ('BYD');

insert into modelo(nome) values('Palio');
insert into modelo(nome) values('Ranger');

d)mostrar as marcas que não possuem automoveis cadastrados(left join)

select marca.nome,automovel.placa,automovel.valor
from marca
left join automovel on  automovel.codmarca=marca.codigo
where automovel.codmarca is null;

e)mostrar todas as marcas que possuem ou não possuem automoveis cadastrados

select marca.nome,automovel.placa,automovel.placa,automovel.valor
from marca
left join automovel on automovel.codmarca=marca.codigo;

g)mostrar todos os modelos que possuem ou não possuem automovel cadastrado(left join)

select modelo.nome,automovel.placa,automovel.valor
from modelo
left join automovel on automovel.codmodelo=modelo.codigo;

h) mostrar todos os modelos que possuem ou nao possuem automoveis cadastrados

select modelo.nome,automovel.placa,automovel.valor
from modelo
right join automovel on automovel.codmodelo=modelo.codigo;

i) mostrar os automoveis com suas respectivas marcas e modelos 

select marca.nome,modelo.nome,automovel.placa,automovel.valor
from automovel
inner join marca on automovel.codmarca=marca.codigo
inner join modelo on automovel.codmodelo=modelo.codigo;

j)mostrar os automoveis com suas respectivas marcas e modelos  fabricados no ano de 2020

select marca.nome,modelo.nome,automovel.placa,automovel.valor
from automovel
inner join marca on automovel.codmarca=marca.codigo
inner join modelo on automovel.codmodelo=modelo.codigo
where automovel.ano=2020;

k)mostrar soma total de valores dos automoveis agrupados por marca
select marca.nome,SUM(automovel.valor)
from automovel
inner join marca on automovel.codmarca=marca.codigo
group by marca.nome;

l)mostrar soma total de valores dos automoveis agrupados por modelo
select modelo.nome,SUM(automovel.valor)
from automovel
inner join modelo on automovel.codmodelo=modelo.codigo
group by modelo.nome;
