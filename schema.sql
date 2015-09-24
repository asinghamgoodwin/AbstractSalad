--drop table if exists Ingredient, Category, Salad;

create table Ingredient (
    ingredient_id  integer primary key autoincrement not null,
    ingredient    text,
    person  text,
    category     text,
    salad        text
);

create table Category(
    id integer primary key autoincrement not null,
    category    text
);


create table Salad(
    id integer primary key autoincrement not null,
    salad    text
);

insert into Category (category) values
    ('Greens'),
    ('Veggies'),
    ('Protein'),
    ('Dressing'),
    ('Other');
