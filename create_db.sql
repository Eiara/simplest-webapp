CREATE DATABASE greeting;
\connect greeting
CREATE TABLE content (
  id integer primary key,
  value text not null
);

insert into content values (1, 'hello database');
