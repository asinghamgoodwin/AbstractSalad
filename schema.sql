--drop table if exists Ingredient, Category, Salad;

create table Ingredient (
    ingredient_id  integer primary key autoincrement not null,
    name    text,
    person  text,
    category_id     integer,
    salad_id        integer
);

create table Category(
    category_id integer primary key autoincrement not null,
    name    text
);


create table Salad(
    salad_id integer primary key autoincrement not null,
    name    text
);

insert into Category (name) values
    ('Greens'),
    ('Veggies'),
    ('Protein'),
    ('Dressing'),
    ('Other');
