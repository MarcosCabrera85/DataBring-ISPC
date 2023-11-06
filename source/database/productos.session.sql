CREATE TABLE productos(
    id int PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(90),
    marca VARCHAR(90),
    precio VARCHAR(90),
    ciudad VARCHAR(90)
);

CREATE TABLE ciudad (
    id int PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50)
);
